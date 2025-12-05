Here’s a **cheat sheet of the fundamental tmux keys** you’ll use all the time. By default, tmux uses **`Ctrl-b`** as its prefix (like Emacs uses `Ctrl-x`). You press `Ctrl-b` first, then the command key.

---

### 🔑 Session & Window Management
- **Start tmux:**  
  ```bash
  tmux
  ```
- **Detach from session:** `Ctrl-b d`  
- **List sessions:** `tmux ls`  
- **Attach to session:**  
  ```bash
  tmux attach -t <session_name>
  ```
- **New window:** `Ctrl-b c`  
- **Switch window:** `Ctrl-b n` (next), `Ctrl-b p` (previous)  
- **Rename window:** `Ctrl-b ,`  
- **Close window:** `Ctrl-b &`

---

### 🪟 Pane (Split Screen) Management
- **Split vertically:** `Ctrl-b %`  
- **Split horizontally:** `Ctrl-b "`  
- **Switch pane:** `Ctrl-b o` (cycle), or `Ctrl-b` + arrow keys  
- **Resize pane:** `Ctrl-b` + `Ctrl-arrow`  
- **Kill pane:** `Ctrl-b x`

---

### 📜 Scrolling & Copy Mode
- **Enter copy mode:** `Ctrl-b [`  
- **Scroll with arrows or PgUp/PgDn**  
- **Search:** `/pattern`  
- **Exit copy mode:** `q`

---

### ⚙️ Misc Essentials
- **Show shortcuts help:** `Ctrl-b ?`  
- **Reload config:** `Ctrl-b :` then type `source-file ~/.tmux.conf`  
- **Command prompt:** `Ctrl-b :`  

---

### ✅ Quick Workflow Example
1. Start tmux: `tmux`  
2. Split vertically: `Ctrl-b %`  
3. Split horizontally: `Ctrl-b "`  
4. Move between panes: `Ctrl-b` + arrow keys  
5. Detach: `Ctrl-b d`  
6. Reattach later: `tmux attach`

---

Would you like me to also create a **visual diagram of tmux keybindings** (like a keyboard map) so you can memorize them faster?

---

Got it 👍 — let’s focus specifically on **pane management in tmux**, since that’s the heart of working with split screens.

---

## 🪟 Creating Panes
- **Split vertically:** `Ctrl-b %`  
- **Split horizontally:** `Ctrl-b "`  
- **Open a new pane with a command:** `Ctrl-b :` then type  
  ```bash
  split-window -h
  split-window -v
  ```

---

## 🔄 Navigating Between Panes
- **Cycle through panes:** `Ctrl-b o`  
- **Move with arrow keys:** `Ctrl-b` + ← ↑ → ↓  
- **Choose pane by number:** `Ctrl-b q` (shows numbers, press the number to jump)

---

## 📐 Resizing Panes
- **Resize with arrow keys:** `Ctrl-b` + `Ctrl-←/↑/→/↓`  
- **Manual resize:** `Ctrl-b :` then type  
  ```bash
  resize-pane -L 10   # shrink left by 10 cells
  resize-pane -R 10   # grow right by 10 cells
  resize-pane -U 5    # shrink up by 5 cells
  resize-pane -D 5    # grow down by 5 cells
  ```

---

## ❌ Closing Panes
- **Kill current pane:** `Ctrl-b x`  
- **Kill all other panes:** `Ctrl-b !` (forces current pane into a new window, closing others)

---

## 🧭 Advanced Pane Tricks
- **Swap panes:** `Ctrl-b {` (swap with previous), `Ctrl-b }` (swap with next)  
- **Convert pane into window:** `Ctrl-b !`  
- **Synchronize input across panes:** `Ctrl-b :` then type  
  ```bash
  setw synchronize-panes on
  ```
  (Now typing in one pane mirrors to all. Turn off with `off`.)

---

### ✅ Quick Workflow Example
1. Start tmux: `tmux`  
2. Split vertically: `Ctrl-b %`  
3. Split horizontally: `Ctrl-b "`  
4. Navigate with `Ctrl-b` + arrows  
5. Resize with `Ctrl-b` + `Ctrl-arrow`  
6. Kill a pane with `Ctrl-b x`

---

Would you like me to also make a **visual ASCII diagram** showing how panes look and how the navigation keys map to them? That way you can memorize pane management faster.

---

Ah, you’ve got two panes open in **tmux** and want one of them to temporarily cover the whole screen. That’s a common workflow trick — here’s how you do it:

---

## 🔎 Zooming a Pane
- **Shortcut:** `Ctrl-b z`  
- This toggles *zoom mode* for the current pane.  
- The pane expands to fill the entire tmux window, hiding the others.  
- Press `Ctrl-b z` again to restore the split view.

---

## 🛠️ Alternative: Break Pane into Window
- **Shortcut:** `Ctrl-b !`  
- This moves the current pane into its own window, effectively giving it full screen.  
- You can switch back to the original window with `Ctrl-b p` (previous) or `Ctrl-b n` (next).

---

## ✅ Quick Example
1. You have two panes: left and right.  
2. Focus on the right pane.  
3. Press `Ctrl-b z` → right pane fills the screen.  
4. Press `Ctrl-b z` again → both panes are visible again.  

---

So the fastest way is **`Ctrl-b z`** for a temporary zoom, or **`Ctrl-b !`** if you want to permanently give that pane its own full window.  

Would you like me to also show you a **workflow tip combining zoom with synchronized panes**, so you can edit the same file across multiple panes but zoom in when needed?

---

Here’s how you can **close all tmux sessions** cleanly:

---

## 🛠️ From Outside tmux
Run this in your shell:
```bash
tmux kill-server
```
- This command kills the entire tmux server.  
- All sessions, windows, and panes are terminated at once.  
- It’s the fastest way to close everything.

---

## 🛠️ From Inside tmux
If you’re already inside a tmux session:
1. Press `Ctrl-b :` to open the command prompt.  
2. Type:
   ```
   kill-server
   ```
3. Press Enter → all sessions close immediately.

---

## 🛠️ Close Individual Sessions
If you don’t want to nuke everything:
- List sessions:
  ```bash
  tmux ls
  ```
- Kill one session:
  ```bash
  tmux kill-session -t <session_name>
  ```

---

### ✅ Recommendation
- Use `tmux kill-server` if you want to **close all sessions at once**.  
- Use `tmux kill-session -t <name>` if you want to **close selectively**.  

---

Would you like me to also show you a **safe workflow tip** so you don’t accidentally kill important sessions when you only meant to close one?



