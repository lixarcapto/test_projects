


from btpy_lib.btpy.src.btpy.Btpy import Btpy

def has_between(text, init, end)->bool:
    r = Btpy.get_between(text, 
            init, end)
    if(not r == text):
        return True
    return False