


class IndexFromArrayTK:

    def inner(self, array, value):
        for i in range(len(array)):
            if(value == array[i]):
                return i
