

import random

def random_phone(country:str)->str:
    country_codes = {
        "MX": 56
    }
    capital_codes = {
        "MX": 55
    }
    # identificar codigo nacional
    national = country_codes[country]
    capital = capital_codes[country]
    # identificar codigo de area

    # aleatorizar numeros usuario
    user_number = ""
    for i in range(7):
        user_number += str(
            random.randint(0, 7))
    # fusionar
    number = f"+{national}{capital}{user_number}"
    return number

NATIONAL_CODES_DICT = {
    "CA": "+1",
    "US": "+1",
    "Islas Vírgenes de los Estados Unidos": "+1-340",
    "Islas Marianas del Norte": "+1-670",
    "Guam": "+1-671",
    "Samoa Americana": "+1-684",
    "Puerto Rico": ["+1-787", "+1-939"],
    "Bermudas": "+1-441",
    "Groenlandia": "+299",
    "San Pedro y Miquelón": "+508",
    "México": "+52",
    "Bahamas": "+1-242",
    "Barbados": "+1-246",
    "Anguila": "+1-264",
    "Antigua y Barbuda": "+1-268",
    "Islas Vírgenes Británicas": "+1-284",
    "Islas Caimán": "+1-345",
    "Granada": "+1-473",
    "Islas Turcas y Caicos": "+1-649",
    "Montserrat": "+1-664",
    "San Martín": "+1-721",
    "Santa Lucía": "+1-758",
    "Dominica": "+1-767",
    "San Vicente y las Granadinas": "+1-784",
    "República Dominicana": ["+1-809", "+1-829", "+1-849"],
    "Trinidad y Tobago": "+1-868",
    "San Cristóbal y Nieves": "+1-869",
    "Jamaica": ["+1-876", "+1-658"],
    "Aruba": "+297",
    "Haití": "+509",
    "Cuba": "+53",
    "Guadalupe": "+590",
    "San Bartolomé": "+590",
    "Martinica": "+596",
    "Curazao": "+599",
    "Bonaire": "+599",
    "San Eustaquio": "+599",
    "Saba": "+599"
}

