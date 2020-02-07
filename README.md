# Scrambled Word Count 
The Program is used to Count the Scrambled Words in a file which contains Text lines.

Included files in the Current Repo/Project:
1. Readme file --> README.md
2. Source file --> scrmabled_strings.py 
3. Test Cases file --> test_scrmables_strings.py



Program Execution Steps:
1. clone the Project into the Local system
2. go inside the project directory where the ReadMe/Source file is available.
3. run the following command:
    command: scrmabled_strings.py --dictionary "dictionary words file path" --input "search string file path"
    
    Sample run:
        scrmabled_strings.py --dictionary "dictionary_words.txt" --input "search_string_file.txt"
        
        sample output:
            Case #1: 4

For running test Cases(Inside the project directory):
    command: python -m unittest
    
    sample output:
        Case #1: 4
        .No two words in the dictionary are the same.
        .Each word in the dictionary is between 2 and 105 letters long, inclusive.
        .The sum of lengths of all words in the dictionary does not exceed 105.
        .
        ----------------------------------------------------------------------
        Ran 4 tests in 0.004s

