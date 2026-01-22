


from ..is_function.is_function import*

def is_checker_function(FUNCTION:callable)\
        -> bool:
    if(not is_function(FUNCTION)):
        return False
    if(not type(FUNCTION(1)) == bool):
        return False
    return True