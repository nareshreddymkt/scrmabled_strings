# Scrambled Word Count 
    The Program is used to Count the Scrambled Words in a file which contains Text lines.
     - developed and validated at  PYTHON 3.7.4

Included files in the Current Repo/Project:
1. Readme file --> README.md
2. Source file --> scrmabled_strings.py 
3. Test Cases file --> test_scrmables_strings.py
4. Docker config file --> Dockerfile
5. project run file --> scrmabled-strings.sh

Docker image is available at : nareshreddymkt/python-scrambled-wc
url : https://hub.docker.com/r/nareshreddymkt/python-scrambled-wc/tags


Program Execution Steps(with PYTHON Oly):
1. clone the Project into the Local system
2. go inside the project directory where the ReadMe/Source file is available.
3. run the following command:
    command: scrmabled_strings.py --dictionary "dictionary words file path" --input "search string file path"
    
    Sample run:
        scrmabled_strings.py --dictionary "files/dictionary_words" --input "files/search_string"

Program Execution Steps(with Docker and shell):
1. clone the Project into the Local system
2. go inside the project directory where the ReadMe/Source file is available.
3. run the following command:
    command:  ./scrmabled-strings.sh  "<dictionary_words file path>"  "<search_file_path>"

	    Sample run:
	    	./scrmabled-strings.sh /mnt/dictionary_words.txt  /mnt/search_file.txt
       		 
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
		
        docker run -v "<dictionary_words file path>":/code/files/dictionary_words -v "<search file path>":/code/files/search_string  -it nareshreddymkt/python-scrambled-wc
	
	where 
		<dictionary_words file path> ==> the file path which contain all the dictionary words.
		<search file path>	     ==> the file path which contain all the Scrambled word lines.
	
        
        
Note: To support CICD with docker, Need integrate github or git with jenkins/open stack using webhooks.


Simplifed the above steps with small shell script.

run ./scrmabled-strings.sh  "<dictionary_words file path>"  "<search_file_path>"

	ex: ./scrmabled-strings.sh /mnt/dictionary_words.txt  /mnt/search_file.txt
	
	sample output:
		Case #1: 4
		Case #2: 4
