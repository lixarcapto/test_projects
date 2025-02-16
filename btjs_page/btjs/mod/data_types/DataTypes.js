

import { BtjsConverters } 
    from "../converters/BtjsConverters.js";
// DATA TYPES -------------------------------
import { LimitNumber } 
  from "./LimitNumber.js";
import { IteratorMatrix2D } 
  from "./IteratorMatrix2D.js";

export class DataTypes extends BtjsConverters {

    /*
        Iterador para navegar atraves de 
        matrizes de datos de dos dimensiones.
        Las principales funcione son:
        * get: obtiene el actual elemento.
        * set: modifica el actual elemento.
        * next: avansa al siguiente elemento.
        */
        static IteratorMatrix2D(matrix2d) {
          new IteratorMatrix2D(matrix2d)
        }

        static LimitNumber(range_arr, 
                number = -1) {
              return new LimitNumber(range_arr, 
                number)
            }

}