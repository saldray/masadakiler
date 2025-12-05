Linus Torvalds’ **uEmacs/PK** (the tiny Emacs‑like editor he maintained) is deliberately minimal. One of its design choices is that it **does not support line numbers** in the way GNU Emacs or Vim do. There’s no built‑in command or mode to toggle line numbers in uEmacs — the editor simply wasn’t designed with that feature.

---

## 🔎 Why No Line Numbers?
- uEmacs was written to be extremely small and fast.  
- Linus explicitly avoided “bloat” features like syntax highlighting, Unicode, or line numbers.  
- The status line only shows buffer name, modification state, and position (line/column counts internally).

---

## 🛠️ Workarounds
If you want line numbers while using uEmacs, you have a few options outside the editor itself:

### 1. Use `nl` or `cat -n` before editing
Show numbered lines in the terminal:
```bash
nl file.txt | less
cat -n file.txt | less
```

### 2. Use `grep -n` for quick navigation
Search with line numbers:
```bash
grep -n "pattern" file.txt
```

### 3. Use external tools while editing
- Keep another terminal open with `tail -n +100 file.txt` to jump to line 100.  
- Use `wc -l file.txt` to count lines.  

### 4. Patch uEmacs
Since uEmacs is open source (C code), you can modify `display.c` to add line numbers in the status line or at the start of each line. Some forks have added this feature, but Linus’ original version does not.

---

## ✅ Summary
- **uEmacs does not support line numbers.**  
- Use external tools (`nl`, `cat -n`, `grep -n`) to see line numbers.  
- Or patch the source code if you want them inside the editor.  

---

👉 Would you like me to show you a **small C code patch** that adds line numbers to uEmacs’ display, so you can recompile it with that feature?
