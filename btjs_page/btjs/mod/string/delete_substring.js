


/*
Elimina un String de un String enviado
*/
export function delete_substring(STRING, 
        SUBSTRING) {
    let regex = new RegExp(SUBSTRING, 'gi'); 
    // 'g' para global, 
    // 'i' para ignorar mayúsculas/minúsculas
    return STRING.replace(regex, '');
}