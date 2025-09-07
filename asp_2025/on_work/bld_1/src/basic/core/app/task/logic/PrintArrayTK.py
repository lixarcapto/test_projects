



class PrintArrayTK:

    def inner(self, array):
        n = 0
        text = "array(" + str(len(array)) + "):\n"
        for e in array:
            text += "  array[" + str(n) + "] = " + e + "\n"
            n += 1
        print(text)
