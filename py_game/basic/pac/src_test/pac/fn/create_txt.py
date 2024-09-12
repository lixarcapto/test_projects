


from ..out_deps import os

"""
Creates a new text file with the specified 
filename and optional content.
ARGS:
* filename (str): The desired filename 
for the new text file.
* content (str, optional): The initial 
content to be written in the file. 
Defaults to an empty string.
Returns:
* bool: True if the file was created 
successfully, False otherwise.
@ by Gemini
"""
def create_txt(filename:str, 
        content:str="")->None:
    try:
        # Check if the file already exists
        if os.path.exists(filename):
            raise FileExistsError(f"File '\
                {filename}' already exists.")
        # Open the file in write mode ('w')
        with open(filename, 'w') as file:
            # Write the specified content 
            # to the file
            file.write(content)
        return True
    except FileExistsError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error creating file: {e}")
        return False