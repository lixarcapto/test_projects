



def write_as_list(LIST:list[str],
        TITLE:str, SYMBOL:str = ">")\
        ->str:
    txt = TITLE + ":\n"
    for e in LIST:
        txt += f"  {SYMBOL} {e}\n"
    return txt