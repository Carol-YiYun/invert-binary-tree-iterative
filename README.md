# 🌳 Invert Binary Tree (Iterative Solution)

Non-recursive solution for inverting a binary tree.

---

## 📘 Overview
Given the root of a binary tree, invert it and return the root.  
This implementation uses **an iterative BFS approach**.

---

## 🧠 Examples

| Example | Input | Output |
|----------|--------|---------|
| 1 | [5, 3, 8, 1, 7, 2, 6] | [5, 8, 3, 6, 2, 7, 1] |
| 2 | [6, 8, 9] | [6, 9, 8] |
| 3 | [5, 3, 8, 1, 7, 2, 6, 100, 3, -1] | [5, 8, 3, 6, 2, 7, 1, null, null, null, null, null, -1, 3, 100] |
| 4 | [] | [] |

**Constraints:**  
- The number of nodes is in the range `[0, 100]`  
- `-100 <= Node.val <= 100`

---

## ⚙️ How to Run

### 🧩 1. Clone this repo
```bash
git clone https://github.com/Carol-YiYun/invert-binary-tree-iterative.git
cd invert-binary-tree-iterative
```

### 🧪 2. Run the program
```bash
python source/main.py
```

### ✅ 3. Run tests
```bash
pytest
```

## 📂 File Structure
```
source/  → main logic (invert binary tree)
test/    → unit tests
.venv/   → virtual environment (ignored)
```

Author: Carol Lin
GitHub: https://github.com/Carol-YiYun/invert-binary-tree-iterative

