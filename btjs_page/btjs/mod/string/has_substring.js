


/*
Verifica si existe un sustin dentro 
de otro String ignorando las mayúsculas
*/
export function has_substring(STRING, 
        SUBSTRING) {
    return STRING.toLowerCase()
        .includes(SUBSTRING.toLowerCase());
}