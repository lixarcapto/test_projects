

from random_name import*

def main():
    #
    r = random_name(
        "name_female_data.xlsx",
        "name_male_data.xlsx",
        "female", 
        "nordic"
        )
    print(r)
    #
    r = random_name(
        "name_female_data.xlsx",
        "name_male_data.xlsx",
        "female"
        )
    print(r)
    #
    r = random_name(
        "name_female_data.xlsx",
        "name_male_data.xlsx",
        "male"
        )
    print(r)
    #
    r = random_name(
        "name_female_data.xlsx",
        "name_male_data.xlsx"
        )
    print(r)

main()