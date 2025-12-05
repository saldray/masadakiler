Perfect — here’s a **starter cheat sheet for Jed** so you can jump right in after installing it on Fedora:

---

## 💾 File Management
- **Open file:** `Ctrl-x Ctrl-f`  
- **Save file:** `Ctrl-x Ctrl-s`  
- **Save as (new name):** `Ctrl-x Ctrl-w`  
- **Exit Jed:** `Ctrl-x Ctrl-c`

---

## ✏️ Editing Basics
- **Undo:** `Ctrl-x u`  
- **Cut (kill line):** `Ctrl-k`  
- **Paste (yank):** `Ctrl-y`  
- **Mark region:** `Ctrl-@` (set mark), then move cursor  
- **Cut region:** `Ctrl-w`  
- **Copy region:** `Alt-w`

---

## 🔍 Searching
- **Incremental search forward:** `Ctrl-s`  
- **Incremental search backward:** `Ctrl-r`  
- **Repeat last search:** `Ctrl-s` again

---

## 🪟 Windows & Buffers
- **Split window horizontally:** `Ctrl-x 2`  
- **Close split:** `Ctrl-x 1`  
- **Switch window:** `Ctrl-x o`  
- **Switch buffer:** `Ctrl-x b`

---

## 📜 Navigation
- **Beginning of line:** `Ctrl-a`  
- **End of line:** `Ctrl-e`  
- **Next page:** `Ctrl-v`  
- **Previous page:** `Alt-v`  
- **Go to line:** `Alt-g`

---

## ✅ Quick Workflow Example
1. Start Jed:  
   ```bash
   jed myfile.txt
   ```
2. Edit your text.  
3. Save with `Ctrl-x Ctrl-s`.  
4. Split screen with `Ctrl-x 2` if you want multiple views.  
5. Exit with `Ctrl-x Ctrl-c`.

---

Jed feels like a “mini Emacs” but with menus and syntax highlighting, so it’s beginner-friendly yet powerful.  

👉 Do you want me to also show you how to **enable Emacs keybinding mode in Jed** so it behaves almost exactly like GNU Emacs but stays lightweight?

---

Great — let’s set up **Jed to behave like Emacs** so you get familiar keybindings but keep Jed’s lightweight feel.

---

## ⚙️ Enable Emacs Mode in Jed
Jed supports multiple emulation modes (Emacs, EDT, WordStar, Brief). By default it often starts in Emacs mode, but you can force it explicitly.

### 1. Start Jed in Emacs Mode
Run:
```bash
jed -emacs filename.txt
```
This ensures Jed uses Emacs-style keybindings for that session.

---

### 2. Permanent Emacs Mode (via Config)
You can set Jed to always start in Emacs mode by editing its **init file**:

- Create or edit `~/.jedrc` (Jed’s config file).
- Add:
  ```text
  emacs_mode();
  ```
- Save and restart Jed. Now every time you launch Jed, it will default to Emacs keybindings.

---

## 🖥️ Keybinding Cheat Sheet (Emacs Mode in Jed)

- **Save file:** `Ctrl-x Ctrl-s`  
- **Exit Jed:** `Ctrl-x Ctrl-c`  
- **Open file:** `Ctrl-x Ctrl-f`  
- **Search forward:** `Ctrl-s`  
- **Search backward:** `Ctrl-r`  
- **Split window:** `Ctrl-x 2`  
- **Close split:** `Ctrl-x 1`  
- **Switch window:** `Ctrl-x o`  
- **Undo:** `Ctrl-x u`  
- **Cut line:** `Ctrl-k`  
- **Paste (yank):** `Ctrl-y`

---

✅ **Summary:**  
- Run Jed with `jed -emacs` for Emacs mode.  
- Add `emacs_mode();` to `~/.jedrc` for permanent Emacs behavior.  
- You’ll get familiar Emacs shortcuts without the heavy GNU Emacs runtime.

---

Would you like me to also show you how to **customize Jed’s tab width and indentation** in `~/.jedrc`, so it matches the 4‑space style you asked about earlier for uEmacs?

---



































