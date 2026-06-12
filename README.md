# TABIND Scrabble Project

## Overview
A Python program that finds all valid words that can be formed using the letters
in "tabind", where each letter can only be used once.

## Problem Statement
Given the letter combination **"tabind"**, find all valid dictionary words
that can be formed using those letters, with each letter used at most once.
Display the results as an alphabetical list.

## Approach
The program uses Python's `Counter` from the `collections` module to compare
letter frequencies between the input letters and each word in the dictionary.
A word is valid if it does not require more of any letter than is available in "tabind".

## Repository Structure
├── tabind_scrabble.py     # Main program
└── scrabble_results.txt   # Output file with all found words

## Setup

### Prerequisites
- Python 3.x (no third-party packages required)
- Download the SOWPODS Scrabble dictionary:
```bash
curl -o sowpods.txt https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt
```

### Clone the repository
```bash
git clone https://github.com/RossJiao/scrabble-project.git
cd scrabble-project
```

## Run
```bash
python3 tabind_scrabble.py
```

## Results
- Dictionary size: 178,691 words (SOWPODS official Scrabble dictionary)
- Total valid words found: 49
- Words are displayed and saved in alphabetical order

## Limitations
- Results depend on the SOWPODS dictionary, which is the international Scrabble word list
- The dictionary file must be downloaded separately before running the program
