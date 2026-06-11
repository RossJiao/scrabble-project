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
- macOS (uses built-in system dictionary at `/usr/share/dict/words`)

### Clone the repository
```bash
git clone https://github.com/RossJiao/scrabble-project.git
cd scrabble-project
```

## Run
```bash
python3 tabind_scrabble.py
```

## Sample Output
TABIND Scrabble Project
Letters: tabind
Dictionary loaded: 234454 words
Found 84 words that can be made from 'tabind':

ab
ad
aid
and
ant
...
tind

Results saved to: scrabble_results.txt
## Results
- Dictionary size: 234,454 words
- Total valid words found: 84
- Words are displayed and saved in alphabetical order

## Limitations
- Uses macOS system dictionary (`/usr/share/dict/words`) instead of an official Scrabble dictionary
- System dictionary may include words not valid in Scrabble, and may exclude some valid Scrabble words
