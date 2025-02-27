

import { BtjsRandom } 
  from "../random/BtjsRandom.js";

// STRING -------------------------------

import { replace_substring } 
    from "./replace_substring.js";
import { delete_substring } 
  from "./delete_substring.js";
import { has_substring } 
  from "./has_substring.js";
import { capitalize } 
  from "./capitalize.js";
import { find_substring } 
  from "./find_substring.js";

export class BtjsString extends BtjsRandom {

    //------------------------------------
    // STRING ------------------------------

    /*
    Verifica si existe un sustin dentro 
    de otro String ignorando las mayúsculas
    */
    static has_substring(STRING, 
        SUBSTRING) {
      return has_substring(STRING, 
        SUBSTRING)
  }

  /*
  Elimina un String de un String enviado
  */
  static delete_substring(STRING, 
        SUBSTRING) {
      return delete_substring(STRING, 
        SUBSTRING)
  }

    static replace_substring(cadena, 
            substring, interval) {
        replace_substring(cadena, 
            substring, interval)
    }

    static capitalize(STRING) {
      return capitalize(STRING)
    }

    static find_substring(cadena, 
           substring) {
        return find_substring(cadena, 
          substring)
    }

}