import string # Part of Python's standard library, used for efficient punctuation removal.

def spell_check():
    # Initialize a counter for correctly spelled words
    correctly_spelled_words_count = 0
    
    # Use a set for dictionary words for efficient membership testing (fast lookups) [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts [1]; Hints and Guidance]
    dictionary_words = set()
    
    dictionary_file_name = "dictionary.txt"
    mystery_file_name = "mystery-text.txt"

    # --- 1. Load the dictionary words ---
    # File Processing (B2.5.1): Open and read the dictionary file [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts].
    try:
        with open(dictionary_file_name, 'r', encoding='utf-8') as dict_file:
            # Loop through each line in the dictionary file [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts]
            for line in dict_file:
                # String Manipulation (B2.1.2): Normalize dictionary words by stripping whitespace and converting to lowercase [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts [2, 3]].
                word = line.strip().lower()
                if word: # Add only non-empty words to the set
                    dictionary_words.add(word)
    except FileNotFoundError:
        # Exception Handling (B2.1.3): Handle cases where the dictionary file does not exist [Programming Challenges: Data, Control, and Algorithms, Challenge 1: Temperature Tracker - Key Concepts [4]].
        print(f"Error: The dictionary file '{dictionary_file_name}' was not found. Please ensure it is in the correct directory.")
        return 0 # Return 0 if the dictionary cannot be loaded
    except Exception as e:
        print(f"An unexpected error occurred while reading the dictionary file: {e}")
        return 0

    # --- 2. Process the mystery text ---
    try:
        with open(mystery_file_name, 'r', encoding='utf-8') as mystery_file:
            # Loop through each line in the mystery text file [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts]
            for line in mystery_file:
                # String Manipulation (B2.1.2): Split the line into individual words [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts [2, 3]].
                # `str.split()` without arguments handles various whitespace characters as delimiters.
                words_in_line = line.split()
                
                # Iterate through each extracted word
                for word in words_in_line:
                    # String Manipulation (B2.1.2): Normalize the word.
                    # This involves removing punctuation and converting to lowercase [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts [2, 3]].
                    # The `str.translate` method with `string.punctuation` (from Python's standard `string` module)
                    # is an efficient and comprehensive way to remove all common punctuation.
                    # This method of punctuation removal aligns with the guidance of "removing common punctuation marks"
                    # and using "replace()" or "direct character removal loops" [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts; Hints and Guidance],
                    # by offering a robust way to achieve the specified task of punctuation removal, similar to how other
                    # standard libraries (`math`, `random`) are presented as useful [Oxford.pdf, 398, 399].
                    word_without_punctuation = word.translate(str.maketrans('', '', string.punctuation))
                    
                    # Convert the word to lowercase [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts [2, 3]].
                    normalized_word = word_without_punctuation.lower()
                    
                    # Debugging Techniques (B2.1.4): Uncomment the line below during development to see normalized words [Programming Challenges: Data, Control, and Algorithms, Challenge 2: Spell Checker - Key Concepts [5]].
                    # print(f"Original: '{word}', Normalized: '{normalized_word}'")
                    
                    # Check if the normalized word exists in the dictionary (membership testing)
                    if normalized_word in dictionary_words:
                        correctly_spelled_words_count += 1
                        
    except FileNotFoundError:
        # Exception Handling (B2.1.3): Handle cases where the mystery text file does not exist [Programming Challenges: Data, Control, and Algorithms, Challenge 1: Temperature Tracker - Key Concepts [4]].
        print(f"Error: The mystery text file '{mystery_file_name}' was not found. Please ensure it is in the correct directory.")
        # Return the count of words processed before the error (could be 0 if file not found initially)
        return correctly_spelled_words_count 
    except Exception as e:
        print(f"An unexpected error occurred while reading the mystery text file: {e}")
        return correctly_spelled_words_count

    # --- 3. Return the total count of correctly spelled words ---
    return correctly_spelled_words_count

# --- Example Usage (for testing the function) ---
# To test this program, create two text files in the same directory as your Python script:
#
# 1. 'dictionary.txt' - each line should contain a valid word. For example:
#    hello
#    world
#    python
#    programming
#    challenge
#    solution
#    test
#    computer
#    science
#    teacher
#    student
#    project
#
# 2. 'mystery-text.txt' - containing text to be spell-checked. For example:
#    Hello, world! This is a Python programming challenge solution.
#    Python programming is fun. Word, word.
#    Computer Science is a fascinating project.
#    My teacher said this is a test.
#
# After creating the files, uncomment the lines below to run the function:

# result = spell_check()
# print(f"\nNumber of correctly spelled words: 