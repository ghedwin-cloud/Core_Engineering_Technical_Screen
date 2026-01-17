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

## Installation

git clone <your-repo-url>
cd package-sorter

## Install Dependencies

pip install -r requirements.txt

## Run the program from bash

python

from sorter.sort import sort

print(sort(50, 50, 50, 10))     # STANDARD
print(sort(150, 20, 20, 5))     # SPECIAL
print(sort(100, 100, 100, 20))  # REJECTED

## Running Test from bash

pytest
