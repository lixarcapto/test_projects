


class ConvertArrayToMapTK:

    def inner(self, array):
        map = dict()
        for i in range(len(array)):
            map[array[i]] = i
        return map
