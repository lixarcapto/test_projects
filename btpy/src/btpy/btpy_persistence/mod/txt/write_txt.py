

import os


def write_txt(file_path:str, text:str)->None:
    """
    Assigns the given text to the specified 
    text file.
    """
    try:
        if not os.path.exists(file_path):
            # If the file doesn't exist, 
            # create it
            with open(file_path, 'w') as file:
                file.write("")
        # Open the file in append mode
        with open(file_path, 'w') as file:
            # Write the given text to the file
            file.write(text)
        print(f"Text written successfully \
              to {file_path}")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error writing text: {e}")