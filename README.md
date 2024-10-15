# **commandPrinter**

## **Description**

**commandPrinter** is a Python-based utility that allows you to execute system commands and print their output directly to the console or a file. It is a lightweight tool designed to **simplify command execution** by combining **command-line inputs and output handling** in a single interface. The tool is useful for developers, system administrators, and users who need to automate repetitive commands and manage their output efficiently.

---

## **Features**

- **Execute system commands** from within a Python environment.
- **Print command output** directly to the console.
- **Save output to a file** for logging purposes.
- **Cross-platform support**: Works on Windows, macOS, and Linux.
- Minimal dependencies and **simple CLI usage**.

---

## **Installation**

### **1. Clone the Repository:**

```bash
git clone https://github.com/SulaimanS11/commandPrinter.git
cd commandPrinter
```
### **2. Install Dependencies:**

Ensure you have Python 3.x installed on your system. Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

---

## **Usage**

### **Command Line Usage:**

You can run the tool using the following syntax:
```bash
python commandPrinter.py <command> [--output <output_file>]
```

### **Options:**

| **Option**           | **Description**                                   | **Example**                                      |
|----------------------|----------------------------------------------------|-------------------------------------------------|
| `<command>`      | The system command you want to execute.                           | `python commandPrinter.py "ls -l"`                   |
| `--output`           | Optional: Path to save the command output to a file.          | `--output output.txt`              

---

## **Examples:**
1. Execute a simple command and print the output:

```bash
python commandPrinter.py "echo Hello, World!"
```

2. Save the output of a command to a file:

```bash
python commandPrinter.py "ls -l" --output output.txt
```

3. Run a system command and display the output directly in the console:

```bash
python commandPrinter.py "ping google.com"
```

---

## **How It Works**

1. **System Command Execution:**
    The tool uses the subprocess module to execute system commands safely and capture their output.

2. **Printing Output:**
    If no `--output` argument is provided, the tool prints the output directly to the console.

3. **Saving Output:**
    If the `--output` argument is used, the command’s output is saved to the specified file.

---

## **Supported Platforms**

- Windows
- macOS
- Linux

---

## **Limitation**

1. **Command Errors:** If a command fails, the error message will be printed to the console.
2. **Command Compatibility:** Some commands may not work across all platforms (e.g., ls works on macOS/Linux but not Windows).
3. **Output Handling:** Only plain text output is supported. Redirected or binary outputs may require additional handling.

---

## **Contributing**

Contributions are welcome! If you'd like to improve the project or add new features:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Submit a pull request.**

---

## **Acknowledgments**

- Built with **Python**.
- Uses the `subprocess` module for executing commands.

---

## **Contact**

If you encounter any issues, have questions, or would like to suggest improvements, feel free to reach out or open an issue on the [GitHub Issues](https://github.com/SulaimanS11/commandPrinter/issues) page.

You can also contact me directly:

- **GitHub:** [SulaimanS11](https://github.com/SulaimanS11)
- **Email:** [sult2271@mylaurier.ca](mailto:sult2271@mylaurier.ca)
- **LinkedIn:** [Mir Sulaiman Sultan](https://www.linkedin.com/in/mirssultan/)

---

## **Changelog**
**v1.0.0**

- Initial release with:
  * Basic command execution functionality.
  * Support for saving output to a file.
  * Cross-platform compatibility.

---

## **Future Improvements**

- Add support for parallel command execution.
- Implement logging options for easier debugging.
- Add error handling enhancements for more complex commands.
- Create a GUI version for non-technical users.

