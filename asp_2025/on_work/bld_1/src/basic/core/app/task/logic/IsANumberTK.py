


class IsANumberTK:

    def inner(self, letter):
        numbersArray = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9"
        ]
        for e in numbersArray:
            if(e == letter):
                return True
        return False
