


from ..out_deps import os

"""
Clears the contents of a text file.
ARGS:
* file_path (str): The path to the text file.
* by Gemini
"""
def clear_txt(file_path:str)->None:
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError( \
                f"File not found: {file_path}")
        # Open the file in write mode and write an empty string
        with open(file_path, 'w') as file:
            file.write("")
        print(f"Text cleared successfully \
              from {file_path}")
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error clearing text: {e}")