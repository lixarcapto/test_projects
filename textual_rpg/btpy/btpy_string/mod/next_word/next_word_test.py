


from .next_word import*

def next_word_test():
    print("next_word_test")
    r = next_word(
        "el gato esta jugando", 
        "esta")
    print(r == "jugando")
    r = next_word(
        "el gato esta jugando", 
        "el")
    print(r == "gato")