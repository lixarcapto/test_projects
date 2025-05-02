

"""
function that replaces an element of the 
sent array with the new element, looking 
for an element that returns true in the 
sent function.
"""
def update(function, array:list, element)\
        ->list:
    for i in range(len(array)):
        if(function(array[i])):
            array[i] = element
            break
    return array