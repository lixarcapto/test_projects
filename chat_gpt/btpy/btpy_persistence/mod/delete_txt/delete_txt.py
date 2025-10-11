


import os


def delete_txt(filename:str)->None:
    """
    Deletes the specified text file.
    @ by Gemini
    """
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