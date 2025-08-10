# OCCT

> Online Compiler Collection Tool is a CLI tool that allows you to run code snippets in various programming/scripting languages using online compilers, without the need for local installations of compilers or interpreters you can get native execution and output of your code.

## Usage by `npx` 💻
```bash
>>> occt -h

  Online Compiler Collection Tool

  Usage:
    npx occt [--options] <command>

  Options:
    -c, --compile       Pass flag for Compiled Code output file. [Auto Detect OS and Programming, and save output file]
    -o, --output        Pass flag only used with -c flag, for output file coustome name.
    -i, --interpreted   Pass flag for interprate Code output only.
    -a, --args          After this flag all value consider as command line arguments.
    -d, --debug         Print debug information if needed.
    -v, --version       Print version information.
    -h, --help          Print the help information.
    --clear             Clear the terminal window. (default: true)
    --no-clear          Don't clear the terminal window.

  Commands:
    help              Print the help information.

  Example:
    npx occt -c ./main.cpp -o main
    npx occt -i ./app.js

>>> 
```
- Passing an script language file for run.
```bash
npx occt -i ./test.py # -i for interpreter

# Output:
OCCT  v0.0.1 Learn more, inovate more!!
Online Compiler Collection Tool
    
/ Uploading file and processing...
---
<YOUR_CODE_OUTPUT>
---
```

- Passing an script language file with arguments.
```bash
npx occt -i ./test.py --args arg1 arg2 # -a/--args for passing arguments

# Output:
OCCT  v0.0.1 Learn more, inovate more!!
Online Compiler Collection Tool
    
/ Uploading file and processing...
---
<YOUR_CODE_OUTPUT>
---
```

- Passing an compiled language file for compile.
```bash
npx occt -c ./test.c # -c for compiler

# Output:
OCCT  v0.0.1 Learn more, inovate more!!
Online Compiler Collection Tool
    
Compiled file: <YOUR_COMPILED_FILE>
# automatilcy download the file to your system you can run directly.
```

- Passing an compiled language file with arguments.
```bash
npx occt -c ./test.c --args arg1 arg2 # -a/--args for passing arguments

# Output:
OCCT  v0.0.1 Learn more, inovate more!!
Online Compiler Collection Tool
    
Compiled file: <YOUR_COMPILED_FILE>
# automatilcy download to your system you can run directly.
```

- Passing an compiled language file to compile with custom output file name.
```bash
npx occt -c ./test.c -o check # -o/--output for custom output file name

# Output:
OCCT  v0.0.1 Learn more, inovate more!!
Online Compiler Collection Tool
    
Compiled file: <YOUR_COMPILED_FILE_WITH_CUSTOM_NAME>
# automatilcy download to your system you can run directly.
```

<hr>

Thank You :)
