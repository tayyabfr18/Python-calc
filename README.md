# 🧮 Simple Calculator with Execution Time & Complexity Analysis

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 👤 Student Information
* **Name:** Muhammad Tayyab
* **Student ID:** `24SP-014-CS`
* **Course:** Algorithms & Programming / Data Structures & Analysis

---

## 📌 Project Overview
This repository contains a Python-based **Simple Calculator** implementation that goes beyond basic arithmetic. In addition to performing calculations, it dynamically measures **real-world execution time** using high-precision timers and provides analytical breakdowns of **Time Complexity** (Big-O notation) and **Space Complexity** for each mathematical operation.

---

## ⚙️ Features & Operations Supported
1. **Basic Arithmetic:** Addition, Subtraction, Multiplication, Division.
2. **Advanced Operations:** Exponentiation (Power), Square Root, and Factorial calculation.
3. **Performance Metrics:** Measures precise execution time down to microseconds using Python's `time` module.
4. **Complexity Logging:** Explicitly details the algorithmic Big-O performance characteristics of each function.

---

## 📊 Complexity Analysis Summary

| Operation | Mathematical Symbol | Time Complexity | Space Complexity | Notes / Description |
| :--- | :---: | :---: | :---: | :--- |
| **Addition / Subtraction** | `+`, `-` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | Constant time primitive arithmetic. |
| **Multiplication / Division** | `*`, `/` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | Handled natively by hardware/Python float types. |
| **Exponentiation** | `a ** b` | $\mathcal{O}(\log b)$ | $\mathcal{O}(1)$ | Optimized binary exponentiation. |
| **Square Root** | `sqrt(x)` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | Uses math library's optimized floating-point routines. |
| **Factorial** | `n!` | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ (Recursive) | Linear growth relative to input size $n$. |

---

## 💻 How to Run
Run the script directly via your terminal:
```bash
python implementation.py
