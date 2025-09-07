

from persistence.Persistence import Persistence

def main():
    dict_ = Persistence\
        .read_profession_dict()
    print(dict_)

main()