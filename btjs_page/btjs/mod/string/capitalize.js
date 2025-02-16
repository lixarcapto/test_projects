



export function capitalize(STRING) {
    // Dividimos el texto en un 
    // array de palabras
    let words = STRING.split(' ');
    // Iteramos sobre cada palabra y 
    // capitalizamos la primera letra
    let capitalized_words = words.map(
        word => {
      return word.charAt(0).toUpperCase() 
        + word.slice(1);
    });
    // Unimos las palabras capitalizadas 
    // en una nueva cadena
    return capitalized_words.join(' ');
}