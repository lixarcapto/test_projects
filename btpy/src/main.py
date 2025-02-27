

from btpy.Btpy import Btpy

def main():
    print("init...")
    r = []
    name_full = ""
    for i in range(20):
        name_full = Btpy.random_full_name(
            "spanish"
        )
        r.append(name_full)

    print(r)

main() 