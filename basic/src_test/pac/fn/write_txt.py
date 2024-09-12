

from ..out_deps import os

"""
Assigns the given text to the specified 
text file.
ARGS:
* file_path (str): The path to the text 
file.
* text (str): The text to be written to 
the file.
@ by gemini
"""
def write_txt(file_path:str, text:str)->None:
    try:
        if not os.path.exists(file_path):
            # If the file doesn't exist, 
            # create it
            with open(file_path, 'w') as file:
                file.write("")
        # Open the file in append mode
        with open(file_path, 'a') as file:
            # Write the given text to the file
            file.write(text)
        print(f"Text written successfully \
              to {file_path}")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error writing text: {e}")