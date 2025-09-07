

from model.mod.genes.choose_probability import*

def random_probability_float(
        probability:int|float) -> float:
    r = random.uniform(
        0, 100)
    if(r < probability):
        return True 
    return False

def main():
    r = ""
    for i in range(20):
        print(random_probability_float(30))
    print(r)

main()