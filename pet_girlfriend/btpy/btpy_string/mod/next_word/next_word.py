

"""
    Funcion que busca la siguiente palabra al
    string enviado en el texto. GEMINI autor.
"""
# return string
def next_word(text: str, 
        searched_string: str):
    """
    Finds the next word after a given multi-word string in a string.
    Parameters:
        text (str): The input text string.
        multiword_target (str): The multi-word string to search for the next word after.
    Returns:
        str: The next word after the multiword target, or an empty string if not found.
    """
    words = text.split()
    try:
        # Convert multiword target to a list of words
        target_words = searched_string.split()
        # Find the index of the first word of the multiword target
        start_index = words.index(target_words[0])
        # Check if the multiword target spans multiple words
        if len(target_words) > 1:
            # Check if the last word of the multiword target is in the list
            if target_words[-1] in words[start_index:]:
                # Find the index of the last word of the multiword target
                end_index = words.index(target_words[-1])
                # Check if there's a word after the multiword target
                if end_index < len(words) - 1:
                    return words[end_index + 1]
                else:
                    return ""
            else:
                return ""
        else:
            # If the multiword target is a single word, just return the next word
            if start_index < len(words) - 1:
                return words[start_index + 1]
            else:
                return ""
    except ValueError:
        return ""