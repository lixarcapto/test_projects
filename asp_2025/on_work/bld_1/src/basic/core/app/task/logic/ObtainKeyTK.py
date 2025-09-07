


class ObtainKeyTK:

    def inner(self, map, vint):
        n = 0
        for e in map.keys():
            if(n == vint):
                return e
            n += 1
        return ""
