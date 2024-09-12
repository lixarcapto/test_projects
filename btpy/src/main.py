

from btpy.Btpy import Btpy



def main():
    r = "None"
    #--------------------------------
        
    

    date = Btpy.DateEspecial()
    date.set_english_date("1789/09/12")
    r = date.write_narrative()

    #------------------------------
    print(r)

main()