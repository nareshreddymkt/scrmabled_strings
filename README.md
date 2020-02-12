# Scrambled Word Count 
    The Program is used to Count the Scrambled Words in a file which contains Text lines.
     - developed and validated at  PYTHON 3.7.4

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
        scrmabled_strings.py --dictionary "files/dictionary_words" --input "files/search_string"
        
        sample output:
            Case #1: 4

For running test Cases(Inside the project directory):
    command: python -m unittest test_scrmables_strings.py
    
    sample output:
        Case #1: 4
        .No two words in the dictionary are the same.
        .Each word in the dictionary is between 2 and 105 letters long, inclusive.
        .The sum of lengths of all words in the dictionary does not exceed 105.
        .
        ----------------------------------------------------------------------
        Ran 4 tests in 0.004s
        
        
DOCKER pipeline:

step 1. Get the docker image for Scrambled application from below link,
		
        docker pull nareshreddymkt/python-scrambled-wc

step 2. run a container for the above docker image.
		
        docker run -v "<dictionary_words file path>":/code/files/dictionary_words1 -v "<search file path>":/code/files/search_string1  -it nareshreddymkt/python-scrambled-wc
        
        
Note: To support CICD with docker, integrate github or git with jenkins/open stack using webhooks.


Simplify the above steps with small shell script.

run ./scrmabled_strings.sh  <dictionary_words file path>   <search file path>
