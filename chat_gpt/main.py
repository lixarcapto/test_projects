


from btpy.Btpy import Btpy

def main():
    us_input = input()
    r = Btpy.request_open_ai(
        f"{us_input}",
        200
    )
    print(r)

main()