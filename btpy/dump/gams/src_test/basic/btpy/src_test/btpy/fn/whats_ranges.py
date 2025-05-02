


from .in_range import*

def whats_ranges(ranges_named:dict, 
            number:int)->list[str]:
        range_keys_arr:list = []
        result:bool = False
        for k in ranges_named:
            result = in_range(
                number,
                ranges_named[k])
            if(result):
                range_keys_arr.append(k)
        return range_keys_arr