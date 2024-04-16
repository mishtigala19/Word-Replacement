# Author: Mishti Gala
# Email: mishtikalpes@umass.edu
# Date: 1st November 2023

# Define a function called replace_word.
def replace_word():
    
    # Initialize a string variable with a sample text.
    str = "Hi! I am Mishti."
    
    # Prompt the user to enter the word to be replaced and store it in the 'word_to_replace' variable.
    word_to_replace = input("Enter the word to replace: ")
    
    # Prompt the user to enter the word to replace with and store it in the 'word_replacement' variable.
    word_replacement = input("Enter the word replacement: ")
    
    # Use the 'replace' method to replace occurrences of 'word_to_replace' with 'word_replacement' in the 'str' variable.
    # Then, print the modified string
    print(str.replace(word_to_replace, word_replacement))

# Call the 'replace_word' function to execute the code.
replace_word()
