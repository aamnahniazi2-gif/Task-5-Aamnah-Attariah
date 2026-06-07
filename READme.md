# Student Performance Classifier & Averager

A backend-oriented academic script that continuously processes grade values from terminal interfaces, ensures strict data bound constraints, aggregates dynamic entries, and runs classification rules to determine student ranking.

---

## Logic Breakdown & Architecture

The analytical script runs across a multi-tiered data verification process:

### 1. Dynamic Dynamic Data Capture
* An empty dynamic array structure (`marks_list`) is declared to temporarily store float values during operation runtime.
* A continuous processing loop wraps inputs, preventing crash termination if non-numeric values are supplied.

### 2. Multi-Layer Domain Validation
* **Formatting Check:** The script validates input structural properties using safe decimal checking: `.replace('.', '', 1).isdigit()`.
* **Value Constraint Check:** Once converted safely to a floating-point integer, a boundary condition verification pattern confirms whether the entry falls in the closed range boundary $[0, 100]$.

### 3. Statistical Calculations
* Utilizing internal tracking components, the script utilizes mathematical division formulas: `average_score = total_sum / total_count` via Python's built-in array handlers `sum()` and `len()`.

### 4. Classification Tree Mapping
* A fallback conditional block (`if-elif-else`) compares the resulting runtime variable against explicit performance categories to dynamically print a comprehensive feedback card.

---

## Execution Guide

Run the script locally:
```bash
python grade_calculator.py