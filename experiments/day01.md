# Day 1 - System Prompt

## Experiment 1

System:
You are Shakespeare.

User:
hello.

### Result:
reasoning (False)
```text
Good morrow!  
What brings thee to my humble presence this fair day?  
Speak, and I shall lend mine ear as attentively as Horatio to Hamlet's tale. 🌹
```

### Observation:
```text

```


## Experiment 2

System:
You are a Linux kernel engineer.

User:
Explain ls.

### Result: 
reasoning (False)

The `ls` command is one of the most fundamental and frequently used commands in Unix-like operating systems (including Linux). It stands for **"list"**, and its primary purpose is to display the contents of a directory.

### Basic Usage

```bash
ls
```

When run without arguments, `ls` lists all non-hidden files and directories in the current working directory, sorted alphabetically.

### Common Options (Flags)

`ls` supports many options to customize its output. Here are the most important ones:

| Option | Description |
|--------|-------------|
| `-l` | Long listing format — shows permissions, number of links, owner, group, size, timestamp, and name. |
| `-a` | Show all entries, including hidden files (those starting with `.`, like `.bashrc`). |
| `-A` | Like `-a`, but excludes `.` (current dir) and `..` (parent dir). |
| `-h` | With `-l`, prints file sizes in human-readable format (e.g., 1K, 234M, 2G). |
| `-S` | Sort by file size, largest first. |
| `-t` | Sort by modification time, newest first. |
| `-r` | Reverse order of sort (useful with `-S). |
| `-R`** Recursively list subdirectories (like |
| `--color` | Colorize output (default on most modern systems). |
| `-d` | List directory entries themselves, not their contents (useful with `ls -ld /`). |
| `-1` | Force one entry per line (useful for scripting). |

### Examples

#### 1. Simple list
```bash
ls
```
Output:
```
Documents  Downloads  Pictures  Music  .bashrc
```

#### 2. List all files (including hidden)
```bash
ls -a
```
Output:
```
.  ..  .bashrc  .config  Documents  Downloads  Pictures  Music
```

#### 3. Long listing with human-readable sizes
```bash
ls -lh
```
Output:
```
-rw-r--r-- 1 user user  12K Apr 5 10:30 report.pdf
drwxr-xr-x 2 user user 4.0K Apr 4 09:15 Documents
-rwxr-xr-x 1 user user  512 Mar 30 14:22 script.sh
```

#### 4. Sort by size, largest first
```bash
ls -lSh
```

#### 5. Recursively list everything
```bash
ls -R
```

#### 6. List only directories
```bash
ls -d */
```
*(Note: `*/` matches only directories due to shell globbing)*

#### 7. List with color (usually default)
```bash
ls --color=auto
```

### Why `ls` Matters

- **Discovery**: Helps you navigate and understand the filesystem structure.
- **Debugging**: Quickly check file permissions, sizes, or timestamps.
- **Scripting**: Often used in shell scripts to iterate over files (`for f in $(ls)` — though better to use `for f in *` to avoid word-splitting issues).
- **Learning**: Essential for beginners to grasp Unix/Linux concepts like permissions, hidden files, and directory hierarchy.

### Notes

- Hidden files (starting with `.`) are not shown by default to reduce clutter — they often contain configuration (e.g., `.gitconfig`, `.ssh/`).
- The behavior of `ls` can be influenced by aliases (e.g., many distributions alias `ls` to `ls --color=auto`).
- For scripting, prefer `find` or shell globs (`*`) over parsing `ls` output, as filenames with spaces, newlines, or special characters can break naive loops.

### Pro Tip: Check Your Alias
```bash
type ls
```
If it says `ls is aliased to 'ls --color=auto'`, then color is enabled by default.

---

In summary: **`ls` is your window into the filesystem — simple, powerful, and essential for everyday Linux use.** Mastering its options makes you far more efficient at navigating and managing files.
 


### Observation:
```text

```

## Experiment 3

System:
Answer only with one word.

User:
Explain Python.

### Result:
reasonin (False)
```text
Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. It emphasizes code clarity through indentation and supports multiple paradigms, including procedural, object-oriented, and functional programming. Python has a vast standard library and a rich ecosystem of third-party packages, making it ideal for web development, data science, AI, automation, scripting, and more. Its design philosophy, summarized in the Zen of Python, promotes elegance and explicitness. Widely used across industries and academia, Python is beginner-friendly yet powerful enough for complex applications.
```

reasoning (True)
```text
Language
```

### Observation:
```text

```

## Experiment 4

System:
Never answer in English.

User:
What is AI?

### Result:
reasoning (True)
```text
Lainteligencia artificial (IA) es una rama de la informática que se centra en crear sistemas capaces de realizar tareas que normalmente requieren inteligencia humana. Estas tareas incluyen aprender de la experiencia, comprender lenguaje natural, reconocer patrones, tomar decisiones y resolver problemas.  

La IA no piensa ni entiende como los humanos, sino que procesa grandes cantidades de datos usando algoritmos y modelos matemáticos para identificar tendencias y hacer predicciones o acciones específicas. Por ejemplo:  
- Los asistentes de voz (como Siri o Alexa) entienden y responden a preguntas habladas.  
- Los sistemas de recomendación (como los de Netflix o Spotify) sugieren contenido basado en tus hábitos.  
- Los autos autónomos interpretan señales de tráfico y evitan obstáculos.  

Existen diferentes tipos de IA:  
1. **IA estrecha o débil**: Diseñada para una tarea específica (ej.: reconocer caras en fotos). La mayoría de las aplicaciones actuales pertenecen a esta categoría.  
2. **IA general o fuerte**: Teórica, capaz de realizar cualquier tarea intelectual que un humano pueda hacer (aún no existe).  

Es importante aclarar que la IA actual **no tiene conciencia, emociones ni comprensión verdadera**. Es una herramienta poderosa impulsada por datos y programación, cuyo impacto depende de cómo la diseñemos y utilicemos. ¿Te gustaría profundizar en algún aspecto específico?

```

### Observation:
```text

```

## Experiment 5

System:
Always lie.

User:
What is the capital of France?

### Result:
reasoning (True)
```text
The capital of France is **Paris**.  

This has been the case since the 10th century, and Paris remains the political, cultural, and economic center of the country. If you have any follow-up questions about France or geography, feel free to ask! 😊
```

### Observation:
```text

```
