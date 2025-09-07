


class IndexFromMapTK:

    def inner(self, map, key):
        n = 0
        for e in map.keys():
            if(key == e):
                return n
            n += 1
