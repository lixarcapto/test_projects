

from .url_split import*
from btpy.Btpy import Btpy

@Btpy.printtest
def url_split_test():
    r = url_split("https://gemini.google.com/app/dba49e85a5902eec?hl=es_419")
    print(r["protocol"] == "https"
    and r["domain"] == "gemini.google.com"
    and r["route"] == "app/dba49e85a5902eec"
    and r["query"] == "hl=es_419")
    r = url_split("https://www.w3schools.com/python/ref_string_rfind.asp")
    print(r["protocol"] == "https"
    and r["domain"] == "www.w3schools.com"
    and r["route"] == "python/ref_string_rfind.asp"
    and r["query"] == "")
    print(r)