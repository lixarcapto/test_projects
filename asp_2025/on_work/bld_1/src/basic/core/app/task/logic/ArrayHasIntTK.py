


class ArrayHasIntTK:

    def inner(self, array, vint):
        for i in range(len(array)):
            if(vint == array[i]):
                return True
        return False
