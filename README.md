#OVERVIEW
This Python script provides a dictionary lookup function that fetches word definitions from a JSON file. It allows users to input a word and retrieve its meaning while handling various cases such as capitalization, misspellings, and abbreviations.

#FEATURES
Converts user input to lowercase to match dictionary entries.
Handles proper nouns by checking title case variations.
Supports uppercase words for acronyms like "USA" or "NATO."
Uses difflib.get_close_matches to suggest the closest word if an exact match is not found.
Requests user confirmation when suggesting words to correct misspellings.
Prints definitions either as a list (for multiple meanings) or as a single string.

#HOW TO USE
Run the script:
python main_script.py
Enter a word when prompted.
The script will display the definition or suggest a correction if necessary.

#EXAPLE
Input:
enter word you want to find: texas
Output:
A state in the southern United States

#NOTES
If no exact match or close match is found, the script asks the user to check the spelling.
The script assumes data.json is properly formatted as a dictionary with words as keys and definitions as values.

#FUTURE IMPROVEMENTS
Add error handling for missing or corrupted data.json.
Implement a graphical user interface (GUI) for easier interaction.
Extend functionality to allow multiple word searches at once.
