# Overview

This Python script provides an interactive dictionary lookup function that fetches word definitions from a JSON file. It allows users to input a word and retrieve its meaning while handling various cases such as capitalization, misspellings, and abbreviations.

# Features

1. Converts user input to lowercase to match dictionary entries.
2. Handles proper nouns by checking title case variations.
3. Supports uppercase words for acronyms like "USA" or "NATO."
4. Uses difflib.get_close_matches to suggest the closest word if an exact match is not found.
5. Requests user confirmation when suggesting words to correct misspellings.
6. Prints definitions either as a list (for multiple meanings) or as a single string.

# How to use

1. Run the script:
2. python main_script.py
3. Enter a word when prompted.
4. The script will display the definition or suggest a correction if necessary.

# Example

Input:

~ enter word you want to find: texas

Output:

~ A state in the southern United States

# Notes

If no exact match or close match is found, the script asks the user to check the spelling.

The script assumes data.json is properly formatted as a dictionary with words as keys and definitions as values.

# Future Improvements

1. Add error handling for missing or corrupted data.json.
2. Implement a GUI or web application for easier interaction.
3. Extend functionality to allow multiple word searches at once.
