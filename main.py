import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")
history = []
reasoning = False

def send_to_ai():
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = json.dumps({
        "model": "nvidia/nemotron-3-super-120b-a12b:free",
        "messages": history,
        "reasoning": {"enabled": reasoning}
    })
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=data
        )
        response.raise_for_status()
        data = response.json()
        return extract_data(data)
    
    except requests.exceptions.Timeout:
        return "Request timed out."

    except requests.exceptions.ConnectionError:
        return "No internet connection."

    except requests.exceptions.HTTPError:
        return f"HTTP Error: {response.status_code}"

    except KeyError:
        return "Unexpected response format."
    
    except Exception as e:
        return f"Unexpected Error: {e}"
    
def extract_data(response):
    message = response["choices"]
    message = message[0]["message"]["content"]
    add_to_history("assistant", message)
    model = response["model"]
    input_tokens = response["usage"]["prompt_tokens"]
    output_tokens = response["usage"]["completion_tokens"]
    total_tokens = response["usage"]["total_tokens"]
    data = {"message": message, "model": model, "input_tokens": input_tokens, "output_tokens": output_tokens, "total_tokens": total_tokens}
    return data

def add_to_history(role, message):
    message = {"role": role,
               "content": message}
    history.append(message)

def show_history():
    print(json.dumps(history, indent=2))

def clear_history():
    global history
    history = []
    print("History Cleared!")

def set_system_prompt():
    accept = input("Changing the system prompt will clear the conversation.\nContinue? (y/n): ")
    if accept.lower()=="y":
        clear_history()
    message = input("Enter New System Prompt: ")
    add_to_history("system", message)

def prompt_test():
    result = []
    global history
    try:
        
        with open("test_case.json", "r") as input:
            input = json.load(input)
            experimnt_num = 1
            for i in input:
                history = []
                system_prompt = i[0]
                history.append(system_prompt)
                history.append(i[1])
                answer = send_to_ai()
                if isinstance(answer, dict):
                    result.append(history)
                    print(f"Experiment {experimnt_num} Done")
                else:
                    print(f"Experiment {experimnt_num} Failed: {answer}")
                experimnt_num += 1

        with open("test_result.json", "w") as output:
            result = json.dumps(result)
            output.write(result)
            print("\nTest Results Are Saved in \"test_result.json\"")

    except Exception as e:
        print(f"ERROR: {e}")

def context_info():
    context_len = 0
    user_messages = 0
    assistant_messages = 0
    for i in history:
        if i["role"] == "assistant":
            assistant_messages+=1
        if i["role"] == "user":
            user_messages+=1
        context_len += (len(i["content"]))
    print("-------------------------------------------------------------------",
          f"\nContext Length: {context_len}\nUser Messages: {user_messages}\nAssistant Messages: {assistant_messages}",
          "\n-------------------------------------------------------------------")

def chat():
    print("HINT: Type \"exit\" for ending conversation.\"clear\" for clearing history.\"system\" for setting system prompt.")
    while True:
        user_input = input("USER: ")
        if user_input.lower()=="exit":
            print("CHAT ENDED")
            return
        elif user_input.lower()=="clear":
            clear_history()
            continue
        elif user_input.lower()=="system":
            set_system_prompt()
            continue
        add_to_history("user", user_input)
        data = send_to_ai()
        if isinstance(data, dict):
            print(f"AI: {data["message"]}\n",
                "\n-------------------------------------------------------------------",
                f"\n Model: {data["model"]}\n Input Token Cost:{data["input_tokens"]}  "
                f"Output Token Cost:{data["output_tokens"]}  Total Tokens:{data["total_tokens"]}"
                "\n-------------------------------------------------------------------\n")
        else:
            print(data)

while True:
    menu = f"\nPROMPT PLAYGROUND LAB 🔬\n1- Start Chat\n2- System Prompt\n3- Show History\n4- Prompt Test" \
           f"\n5- Context Info\n6- Reasoning ({reasoning})\n0- Exit\nChoose a Number: "
    option = input(menu)
    print()
    match option:
        case "1":
            chat()
        case "2":
            set_system_prompt()
        case "3":
            show_history()
        case "4":
            prompt_test()
        case "5":
            context_info()
        case "6":
            reasoning = not reasoning
        case "0":
            print("Program Closed")
            break
        case _:
            print("Invalid Input!")
