


from ..out_deps import os

"""
Deletes the specified text file.
ARGS:
* filename (str): The path to the text 
file to be deleted.
RETURN:
* bool: True if the file was deleted 
successfully, False otherwise.
@ by Gemini
"""
def delete_txt(filename:str)->None:
    try:
        # Check if the file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '\
                {filename}' does not exist.")
        # Remove the file
        os.remove(filename)
        return True
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False