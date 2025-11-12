Kate is a **text editor**, not a full Integrated Development Environment (IDE) like KDevelop. It does not natively compile or run C++ code. However, you can use one of two methods to easily compile and run your code within Kate:

1.  **Use the built-in Terminal:** This is the simplest and most common method.
2.  **Configure the Build & Run or External Tools Plugin:** This provides a dedicated button or keyboard shortcut for one-click action.

-----

## 1\. Using the Built-in Terminal (Recommended)

Kate includes an **embedded terminal** (Konsole) that allows you to execute shell commands directly within the editor window.

### Prerequisites

You must have the **G++ compiler** installed on your system. On most Linux distributions, you can install it via the package manager (e.g., `sudo apt install g++` or `sudo dnf install gcc-c++`).

### Step-by-Step Guide

1.  **Write and Save Your Code:**

      * Open a new file in Kate and write your C++ code (e.g., a simple "Hello World").
      * **Save** the file with a `.cpp` extension (e.g., `hello.cpp`).
      * **Note:** The executable file will be created in the same directory as this source file.

2.  **Open the Terminal Tool View:**

      * Look for the **Terminal** tab or button, typically at the bottom or left side of the Kate window.
      * Click it to open the embedded terminal. It should automatically open to the directory where your C++ file is saved.

3.  **Compile the Code:**

      * Use the **`g++`** command in the terminal to compile your source file. This command creates an executable file.
      * **Syntax:**
        ```bash
        g++ <source_file_name>.cpp -o <executable_name>
        ```
      * **Example for `hello.cpp`:**
        ```bash
        g++ hello.cpp -o hello
        ```
      * If the compilation is successful, no output will be shown, and a new executable file named `hello` will appear in your directory. If there are errors, they will be displayed in the terminal.

4.  **Run the Program:**

      * Execute the compiled program using the `./` prefix:
      * **Example:**
        ```bash
        ./hello
        ```
      * The output of your program (e.g., "Hello World\!") will be displayed directly in the embedded terminal.

-----

## 2\. Using the External Tools Plugin (For Automation)

If you want a single keyboard shortcut or button to perform the compile and run steps, you can configure an **External Tool** in Kate.

### Step-by-Step Guide

1.  **Enable the Plugin:**

      * Go to **Settings** -\> **Configure Kate...** -\> **Plugins**.
      * Ensure the **External Tools** plugin is checked and enabled.

2.  **Configure a New Tool:**

      * Go to **Tools** -\> **External Tools** -\> **Configure...** (or **Settings** -\> **Configure Kate...** -\> **External Tools**).
      * Click the **Add** button, then select **Add Tool...**
      * Fill out the settings for the tool:

| Setting | Value | Description |
| :--- | :--- | :--- |
| **Name** | `Compile & Run C++` (or similar) | A descriptive name for the menu. |
| **Command** | `konsole` | Opens the KDE terminal for execution. |
| **Arguments** | `--noclose -e sh -c 'g++ "%{Document:FilePath}" -o "%{Document:FileBaseName}" && "./%{Document:FileBaseName}"'` | This complex string performs two actions: it **compiles** (`g++`) and then **runs** (`./`) the executable. |
| **Working Directory** | `%{Document:Path}` | Ensures the command runs in the same folder as your file. |
| **Show Output** | `In new Konsole window` | Recommended to see the program output and keep the window open. |
| **Save All** | `Checked` | Ensures your latest code changes are compiled. |

3.  **Save and Run:**
      * Click **OK** to save the tool.
      * You can now run your C++ file by going to **Tools** -\> **External Tools** -\> **Compile & Run C++** (or whatever you named it).

**Note:** The variables like `%{Document:FilePath}` and `%{Document:FileBaseName}` are powerful placeholders that Kate replaces with the actual path and filename of the currently open document.
