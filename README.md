# Package Sorting Function

## Overview
This project implements a Python function that determines how packages should be dispatched in an automated warehouse system based on their size and mass.

---

## Sorting Rules

### Bulky
A package is considered **bulky** if:
- Its volume (width × height × length) is **≥ 1,000,000 cm³**, OR
- Any single dimension is **≥ 150 cm**

### Heavy
A package is considered **heavy** if:
- Its mass is **≥ 20 kg**

---

## Stack Categories

| Stack | Description |
|------|------------|
| STANDARD | Package is neither bulky nor heavy |
| SPECIAL | Package is bulky OR heavy |
| REJECTED | Package is both bulky AND heavy |

---

## Function Signature

```python
def sort(width, height, length, mass) -> str

