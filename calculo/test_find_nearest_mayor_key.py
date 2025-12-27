


from find_nearest_mayor_key import*

def main():
    probability_death_dict = {
        0:0,
        40:0.3,
        60:1,
        70:30,
        80:70,
        100:96
    }
    r = find_nearest_mayor_key(
        probability_death_dict, 27
    )
    print(r)

main()