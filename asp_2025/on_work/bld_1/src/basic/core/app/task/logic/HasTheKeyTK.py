


class HasTheKeyTK:

    def inner(self, map, key):
        for e in map.keys():
            if(e == key):
                return True
        return False
