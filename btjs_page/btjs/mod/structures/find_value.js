



export function find_value(JSOBJECT, VALUE) {
    for (const k in JSOBJECT) {
      if (JSOBJECT[k] === VALUE) {
        return k;
      }
    }
    return null; 
}