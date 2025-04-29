

/*
Función que ajusta un valor en el 
rango límite enviado.
*/
export function set_in_range(VALUE, 
        RANGE_ARR) {
    if (VALUE > RANGE_ARR[1]) {
      return RANGE_ARR[1];
    }
    if (VALUE < RANGE_ARR[0]) {
      return RANGE_ARR[0];
    }
    return VALUE;
}