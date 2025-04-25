


export function min_in_dict(JSOBJECT) {
    let valorMinimo = Infinity; 
    let claveValorMinimo = null;
    for (const clave in JSOBJECT) {
      if (JSOBJECT.hasOwnProperty(clave) 
    && typeof JSOBJECT[clave] === 'number') {
        if (JSOBJECT[clave] < valorMinimo) {
          valorMinimo = JSOBJECT[clave];
          claveValorMinimo = clave;
        }
      }
    }
  
    return claveValorMinimo;
}