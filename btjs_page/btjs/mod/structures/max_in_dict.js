


export function max_in_dict(JSOBJECT) {
    let maximoValor = -Infinity;
    let claveMaximoValor = null;
    for (let k in JSOBJECT) {
      if (JSOBJECT.hasOwnProperty(k) 
        && typeof JSOBJECT[k] === 'number') {
        if (JSOBJECT[k] > maximoValor) {
          maximoValor = JSOBJECT[k];
          claveMaximoValor = k;
        }
      }
    }
  
    return claveMaximoValor;
}