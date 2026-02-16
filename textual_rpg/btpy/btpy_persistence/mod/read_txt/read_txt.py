

import os
import unicodedata

def read_txt(file_path: str) -> str:
    """
    Loads the entire text from a text file as a string, removing accents.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        # Read the file contents
        with open(file_path, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
            file_content = file.read()
        # Remove accents
        normalized_text = unicodedata.normalize('NFKD', file_content)
        text_without_accents = ''.join([c for c in normalized_text if not unicodedata.combining(c)])
        return text_without_accents
    except Exception as e:
        # Handle any exceptions that occur
        print(f"Error loading text from file: {e}")
        return None