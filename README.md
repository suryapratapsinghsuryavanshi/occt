# OCCT (Online Compiler Collection Tool)

**OCCT** is a powerful CLI utility that allows you to execute code snippets in various programming and scripting languages using cloud-based compilers. Get native execution and output without the need for local installations of compilers or interpreters.

---

## 📦 Usage

Run directly via `npx` without installation:

```bash
npx occt [options] <command>

```

### ⚙️ Options

| Flag | Long Flag | Description |
| --- | --- | --- |
| **`-c`** | `--compile` | Compile code (Auto-detects OS & Language) and saves the binary. |
| **`-o`** | `--output` | Specify a custom name for the compiled output file (requires `-c`). |
| **`-i`** | `--interpreted` | Run interpreted code (Python, Node.js, etc.) and view output. |
| **`-a`** | `--args` | Treat all subsequent values as command-line arguments for the script. |
| **`-d`** | `--debug` | Print debug information. |
| **`-v`** | `--version` | Display version information. |
| **`-h`** | `--help` | Display help information. |
|  | `--clear` | Clear the terminal window before running (Default: `true`). |
|  | `--no-clear` | Do not clear the terminal window. |

---

## 💻 Examples

### 1. Interpreted Languages (Python, JS, etc.)

Run scripts instantly without local runtime setup.

**Basic Run:**

```bash
npx occt -i ./test.py

```

**Run with Arguments:**
Pass arguments to your script using the `-a` flag.

```bash
npx occt -i ./test.py --args arg1 arg2

```

> **Output:**
> ```text
> OCCT v0.0.1 Learn more, innovate more!!
> / Uploading file and processing...
> ---
> <YOUR_CODE_OUTPUT>
> ---
> 
> ```
> 
> 

### 2. Compiled Languages (C, C++, etc.)

Compile source code and automatically download the executable to your machine.

**Compile & Download:**

```bash
npx occt -c ./test.c

```

**Compile with Custom Output Name:**

```bash
npx occt -c ./test.c -o my_program

```

> **Output:**
> ```text
> OCCT v0.0.1 Learn more, innovate more!!
> Compiled file: my_program
> # Automatically downloaded to your system. You can run it directly.
> 
> ```
> 
> 

---

## 🌐 API Usage (cURL)

You can also use `cURL` to interact with OCCT directly without Node.js.

**Execute a Script:**

```bash
curl -F "file=@./script.py" https://occt.in/

```

**Compile and Save:**

```bash
# Windows
curl.exe -F "file=@./main.c" https://occt.in/ -o output.exe

# Linux/macOS
curl -F "file=@./main.c" https://occt.in/ -o output

```

---

*Thank you for using OCCT!*