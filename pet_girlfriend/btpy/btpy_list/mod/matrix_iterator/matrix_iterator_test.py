


from .MatrixIterator import MatrixIterator

def matrix_iterator_test():
    print("--> matrix_iterator_test")
    
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ]
    it = MatrixIterator(matrix)
    for i in range(6):
        it.next()
    print(it.get() == 1)
    for i in range(12):
        it.next()
    print(it.get() == 1)

    print("")
