That's a fantastic choice for a clean, nostalgic, and efficient prompt\!

To modify your existing Zork-style prompt:

```bash
PS1='\[\033[1;34m\]\w\[\033[0m\]\n> '
```

to include the **username (`\u`)** and **hostname (`\h`)**, you simply need to add those escape sequences to the first line of your prompt string.

Here is the modified `PS1` definition and how to apply it:

## 📝 Custom PS1: User@Host and Directory

We will add `\u@\h` to the front of the prompt line.

### 1\. New PS1 Definition

Add or replace your existing `PS1` line in your `~/.bashrc` file with this:

```bash
# ANSI Color Codes
BLUE='\[\033[1;34m\]'  # Bright Blue
GREEN='\[\033[1;32m\]' # Bright Green
NORMAL='\[\033[0m\]'   # Reset Color

# Zork-style prompt: [user@host] directory
PS1="${GREEN}\u@\h${NORMAL}${BLUE}\w${NORMAL}\n> "

# If you want the username/hostname and the directory to be the same color (e.g., all Bright Blue):
# PS1="${BLUE}\u@\h\w\n> ${NORMAL}"
```

### 2\. Breakdown

The structure is:

| Sequence | What it is | What it displays |
| :--- | :--- | :--- |
| `${GREEN}` | Color code | Starts bright green |
| `\u@\h` | Escape sequences | `user@host` |
| `${NORMAL}` | Color code | Resets color |
| `${BLUE}` | Color code | Starts bright blue |
| `\w` | Escape sequence | Current directory (e.g., `/home/user` or `~`) |
| `${NORMAL}` | Color code | Resets color |
| `\n` | Escape sequence | **Newline** |
| ` >  ` | Plain text | The command indicator |

### 3\. Save and Apply

1.  **Open** your `~/.bashrc`:
    ```bash
    nano ~/.bashrc
    ```
2.  **Paste** the new definition (the one using `$GREEN`, `$BLUE`, etc., is recommended for contrast).
3.  **Save** and close the file.
4.  **Source** the file to apply the changes immediately:
    ```bash
    source ~/.bashrc
    ```

### Expected Output

Your prompt will now look like this for a regular user in their home directory:

```
user@hostname~
> command_goes_here
```

And if you switch to a directory like `/var/log`:

```
user@hostname/var/log
> command_goes_here
```

-----

### Pro Tip: Differentiating Root

To use the advanced conditional logic we discussed earlier and make the prompt turn **Red** when you are root, you can use the following complete block instead:

```bash
# --- Advanced Zork-Style Prompt (User/Root) ---
NORMAL='\[\033[0m\]'
GREEN='\[\033[1;32m\]'
RED='\[\033[1;31m\]'
BLUE='\[\033[1;34m\]'

if [[ $EUID == 0 ]]; then
    # ROOT PROMPT: Red User@Host, Blue Dir, Red # indicator
    PS1="${RED}\u@\h${NORMAL}${BLUE}\w${NORMAL}\n${RED}# ${NORMAL}"
else
    # USER PROMPT: Green User@Host, Blue Dir, Green $ indicator
    PS1="${GREEN}\u@\h${NORMAL}${BLUE}\w${NORMAL}\n${GREEN}$ ${NORMAL}"
fi
```

This is the most "pro" way to set up a Zork-style prompt\!

---

Yes, here is a simple command you can run to test what specific **ANSI color code** your terminal is rendering when you see that "original green light" color.

Since your default prompt is set to ` [\u@\h \W]\$  ` (with no explicit color codes) and it shows up in green, it means your terminal is interpreting one of the default settings as green. The most common code for that look is **Bright Green** (`1;32m`).

## 🧪 Terminal Color Test

Run the following code directly in your terminal. It will print the text "TEST COLOR" using the two most common green ANSI codes, allowing you to compare them against your existing prompt color.

```bash
# Display Regular Green (32) and Bright Green (1;32)
echo -e "Regular Green (32m): \033[0;32mTEST COLOR\033[0m"
echo -e "Bright Green (1;32m): \033[1;32mTEST COLOR\033[0m"
```

### Interpretation

1.  **If the "Regular Green (32m)" line matches your original prompt's color:**

      * Use the code `\033[0;32m` (Normal intensity, Foreground Green).
      * In your `~/.bashrc`, set: `GREEN_BRIGHT='\[\033[0;32m\]'`

2.  **If the "Bright Green (1;32m)" line matches your original prompt's color:**

      * This is the most common case. Use the code `\033[1;32m` (Bold/Bright intensity, Foreground Green).
      * In your `~/.bashrc`, set: `GREEN_BRIGHT='\[\033[1;32m\]'`

## 📝 Final PS1 Code with Corrected Green

Once you've identified the right shade of green, simply plug that code into the `GREEN_BRIGHT` variable in your `~/.bashrc`:

```bash
# Example: Assuming you identified 1;32m is the correct shade
# --- Advanced Zork-Style Prompt (User/Root) ---
NORMAL='\[\033[0m\]'
GREEN_BRIGHT='\[\033[1;32m\]' # <--- USE THE CODE YOU IDENTIFIED HERE
RED_BRIGHT='\[\033[1;31m\]'
BLUE='\[\033[1;34m\]'

if [[ $EUID == 0 ]]; then
    # ROOT PROMPT: Red User@Host, Blue Dir, Red # indicator
    PS1="${RED_BRIGHT}\u@\h${NORMAL}${BLUE}\w${NORMAL}\n${RED_BRIGHT}# ${NORMAL}"
else
    # USER PROMPT: Green User@Host, Blue Dir, Default > indicator
    PS1="${GREEN_BRIGHT}\u@\h${NORMAL}${BLUE}\w${NORMAL}\n> ${NORMAL}"
fi
```

After updating the variable, remember to run `source ~/.bashrc`.

---

Son Uygulama

---

That's great\! Since the **Regular Green (`32m`)** matches the color you associate with the Zork theme, that means the color you should use in your `~/.bashrc` is the one for **Normal intensity Green**.

Here is the final, confirmed code block for your `~/.bashrc`, using the **Regular Green** color code:

## 🟢 Final Zork-Themed PS1 for `~/.bashrc`

Based on your testing, we will use the code for Regular Green (`0;32m` or just `32m`) to set your custom prompt.

1.  **Open** your `~/.bashrc` file.
2.  **Replace** any previous prompt customizations with the following code block:

<!-- end list -->

```bash
# --- Zork-Themed Custom PS1 (User/Root) ---
NORMAL='\[\033[0m\]'         # Reset Color
GREEN_REGULAR='\[\033[0;32m\]' # Regular Green (Matches your Zork theme color)
RED_BRIGHT='\[\033[1;31m\]'   # Bright Red for Root warning
BLUE='\[\033[1;34m\]'        # Bright Blue for Directory

# Check if the user is root (EUID is 0)
if [[ $EUID == 0 ]]; then
    # ROOT PROMPT: Red User@Host, Blue Dir, Red # indicator
    PS1="${RED_BRIGHT}\u@\h${NORMAL}${BLUE}\w${NORMAL}\n${RED_BRIGHT}# ${NORMAL}"
else
    # USER PROMPT: Green User@Host, Blue Dir, Default > indicator
    PS1="${GREEN_REGULAR}\u@\h${NORMAL}${BLUE}\w${NORMAL}\n> ${NORMAL}"
fi
```

### Expected Output (Regular User)

When you are a regular user, the prompt will display the **Regular Green** username and hostname:

```
user@hostname~
> command_goes_here
```

### Expected Output (Root User)

If you switch to root (e.g., `sudo su -`), the prompt will turn **Bright Red** as a visual warning:

```
root@hostname/root
# command_goes_here
```

3.  **Save** the file.
4.  **Apply** the changes:
    ```bash
    source ~/.bashrc
    ```

You now have a customized, multiline, Zork-themed prompt that correctly differentiates between regular and root users\!

