# Package Sorting Function

## Description
This project contains a simple Python function that decides how a package should be handled based on its size and weight.

---

## Rules

### Bulky
A package is bulky if:
- The total volume (width × height × length) is 1,000,000 cm³ or more, or
- Any single dimension is 150 cm or more

### Heavy
A package is heavy if:
- The weight is 20 kg or more

---

## Package Types

| Type | Meaning |
|-----|--------|
| STANDARD | Not bulky and not heavy |
| SPECIAL | Bulky or heavy |
| REJECTED | Bulky and heavy |

---

## Function

```python
def sort(width, height, length, mass):


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
