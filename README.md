# 🌳 Invert Binary Tree (Iterative Solution)

A non-recursive solution for inverting a binary tree using an iterative BFS approach.
Implemented in Python 3.13.7, fully tested, and Docker-ready for quick verification.

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
| 5 | [-2] | [-2] |
| 6 | [-1, -2, -3] | [-1, -3, -2] |

**Constraints:**  
- The number of nodes is in the range `[0, 100]`  
- `-100 <= Node.val <= 100`

---
## 🧪 Quick Verification (No API Required)

This project does not expose an HTTP API.
All logic is verified through unit tests — runable via Docker or locally.

⸻

### ✅ Option A. Run in Docker (Recommended)

1️⃣ Run tests (pytest)
```bash
docker run --rm docker.io/carollin/invert-binary-tree-iterative:py3.13.7
```
This image automatically runs **pytest** and prints test results like:
```bash
============================= test session starts ==============================
platform linux -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0 -- /usr/local/bin/python3.13
cachedir: .pytest_cache
rootdir: /app
collecting ... collected 6 items

test/test_invert_tree.py::test_invert_tree_iterative[inp0-expected0] PASSED [ 16%]
test/test_invert_tree.py::test_invert_tree_iterative[inp1-expected1] PASSED [ 33%]
test/test_invert_tree.py::test_invert_tree_iterative[inp2-expected2] PASSED [ 50%]
test/test_invert_tree.py::test_invert_tree_iterative[inp3-expected3] PASSED [ 66%]
test/test_invert_tree.py::test_invert_tree_iterative[inp4-expected4] PASSED [ 83%]
test/test_invert_tree.py::test_invert_tree_iterative[inp5-expected5] PASSED [100%]

============================== 6 passed in 0.01s ===============================
```

2️⃣ Run main program (interactive mode)
```bash
docker run --rm -it docker.io/carollin/invert-binary-tree-iterative:py3.13.7 run
```

### 💻 Option B. Run Locally (No Docker)
⚠️ Make sure Python 3 is installed on your machine before running the following commands.
0️⃣ Set up virtual environment and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
1️⃣ Run tests (pytest)
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
2️⃣ Run main program
```bash
python source/main.py
```

---

## 📂 File Structure
```
source/  → main logic (invert binary tree)
test/    → unit tests
.venv/   → virtual environment (ignored)
```

---
### Author: Carol Lin

