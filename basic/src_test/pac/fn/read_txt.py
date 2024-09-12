


from ..out_deps import os

"""
Loads the entire text from a text file as a string.
ARGS:
* file_path (str): The path to the text file.
RETURN:
* str: The entire text content of the file.
@ by Gemini
"""
def read_txt(file_path:str)->str:
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(\
                f"File not found: {file_path}")
        # Read the file contents
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error loading text from \
              file: {e}")
        return None