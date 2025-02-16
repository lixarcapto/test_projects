


export function find_substring(cadena, 
    substring) {
  // Encuentra el índice de la primera 
  // aparición del substring
  const indiceInicio = cadena.indexOf(
    substring);

  // Si se encontró el substring, 
  // calcula el índice final
  if (indiceInicio !== -1) {
    const indiceFinal = indiceInicio 
      + substring.length - 1;
    return { inicio: indiceInicio, 
      final: indiceFinal };
  } else {
    return null;
  }
}