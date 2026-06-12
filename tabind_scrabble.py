import os
from collections import Counter

# Project Objective - Simulation
# The objective of this project is to develop a program that takes the letter
# combination "tabind" only once and creates an alphabetical list of all the words,
# from a Scrabble dictionary that can be found with those letters.

def load_dictionary(filepath):
    """Load words from the system dictionary file"""
    with open(filepath, 'r') as f:
       words = set(word.strip().lower() for word in f if word.strip().isalpha() and len(word.strip()) >= 2)
    return words

def find_words(letters, word_list):
    """
    Find all words that can be made from the given letters.
    Each letter in 'letters' can only be used once.
    """
    letter_counts = Counter(letters)
    valid_words = []

    for word in word_list:
        word_counts = Counter(word)
        can_form = all(word_counts[char] <= letter_counts[char] for char in word_counts)
        if can_form:
            valid_words.append(word)

    return sorted(valid_words)

def main():
    letters = "tabind"
    dictionary_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sowpods.txt")

    print("TABIND Scrabble Project")
    print(f"Letters: {letters}")
    print("-" * 40)

    # Load dictionary
    word_list = load_dictionary(dictionary_path)
    print(f"Dictionary loaded: {len(word_list)} words")

    # Find all possible words
    results = find_words(letters, word_list)

    # Display results
    print(f"\nFound {len(results)} words that can be made from '{letters}':")
    print("-" * 40)
    for i, word in enumerate(results, 1):
        print(f"{i:3}. {word}")

    # Save results to file
    output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scrabble_results.txt")
    with open(output_file, 'w') as f:
        f.write("TABIND Scrabble Results\n")
        f.write(f"Letters used: {letters} (each letter can be used only once)\n")
        f.write(f"Total words found: {len(results)}\n")
        f.write("-" * 40 + "\n")
        for word in results:
            f.write(f"{word}\n")

    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()