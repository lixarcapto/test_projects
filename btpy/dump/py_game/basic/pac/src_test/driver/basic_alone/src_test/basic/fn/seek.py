

"""
Function that returns an element of 
the array if the sent function returns 
true. If the element does not exist, 
it returns a value of none.
EXAMPLES: 
"""
def seek(function, array:list) ->list:
    for i in range(len(array)):
        if(function(array[i])):
            return array[i]
    return None