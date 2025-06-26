# 📝 Python File Handling Tasks – Assignment A4

This assignment includes two Python tasks focused on practicing file handling using reading, writing, appending, and exception handling techniques.

## 🧠 Task 1: Read from a File with Error Handling

### 📋 Problem Statement:
- Open a file named `sample.txt`
- Read and display the **first two lines**
- Handle the case when the file does **not exist**

### 💡 Key Concepts Used:
- `open()` in read (`"r"`) mode
- `readline()` to read lines individually
- `try-except` block to handle `FileNotFoundError`

### ✅ Sample Output:
```bash
Line 1: Welcome to Task 1.
Line 2: This is line two of the sample file.
```

### ⚠️ If file not found:
```bash
The File 'sample.txt' was not found
```

## 🧠 Task 2: Write, Append, and Read from a File in a Loop

### 📋 Problem Statement:
- Take input from the user and **write** it to `output.txt`
- Ask for additional text and **append** it to the same file
- Read and display the **final file content**
- Repeat the process until the user chooses to exit

### 💡 Key Concepts Used:
- `open()` with `"w"` mode to write (overwrite)
- `open()` with `"a"` mode to append
- `open()` with `"r"` mode to read
- `while True` loop for repeated execution
- `break` to exit based on user choice

### ✅ Sample Run:

```bash
Enter text to write to the file: Hello World
Data Successfully Written To The File

Enter Additional Text To Append: This is a second line
Data Successfully Appended.

Final Output Of File:
Hello World
This is a second line

Do You Want To Continue? (Y/n): y
```

## 🛠 Requirements

- Python 3.x
- No external modules required (uses built-in file handling)

## ▶️ How to Run

Use the terminal to run each script:

```bash
python task1.py
python task2.py
```
