

import { BtjsString } 
    from "../string/BtjsString.js";

// STRUCTURES -------------------------------

import { clean_voids } 
  from "./clean_voids.js";
import { count } from "./count.js";
import { create_array } 
  from "./create_array.js";
import { find_value } 
  from "./find_value.js";
import { fit_list } 
  from "./fit_list.js";
import { join_jsobject } 
  from "./join_jsobject.js";
import { map2 } from "./map2.js";
import { repeat_each as repeat_each } 
  from "./repeat_reach.js";
import { min_in_dict } 
  from "./min_in_dict.js";
import { max_in_dict } 
  from "./max_in_dict.js";
import { find_closest_lower_array } 
  from "./find_closest_lower.js";
import { find_closest_highest_array } 
  from "./find_closest_lower.js";
import { has_all } 
  from "./has_all.js";
import { has_some } 
  from "./has_some.js";

export class BtjsStructures extends BtjsString {

    //------------------------------------
    // Array bucles ------------------------

    /*
    Funcion que convierte dos arrays en 
    un objeto javascript usando como claves
    el primer array y como valores el 
    segundo.
    */
    static array_to_jsobject(key_arr, values_arr) {
        return array_to_jsobject(key_arr, 
          values_arr);
      }
  
      /*
      Función que itera sobre los elementos 
      del array enviado buscando si todos los 
      elementos del array retornan true a la 
      función enviada.
      */
      static has_all(ARRAY, CHECK_FUNCTION) {
        return has_all(ARRAY, CHECK_FUNCTION);
      }
  
      /*
      Función que itera sobre los 
      elementos del array enviado 
      buscando si alguno de los 
      elementos del array retornan 
      true a la función enviada.
      Se diferencia de has_all en que este
      se detiene al encontrar el valor
      indicado.
      */
      static has_some(ARRAY, 
        CHECK_FUNCTION) {
          return has_some(ARRAY, 
            CHECK_FUNCTION)
      }
  
  
      /*
      Función que crea un nuevo array
      eliminando todos los valores 
      None y void
      */
      static clean_voids(ARRAY) {
        return clean_voids(ARRAY);
      }
  
      /*
      Funcion que cuenta el numero de 
      verificaciones con una funcion 
      checker enviada en un array o jsobject.
      Envia un lambda con esta estructura:
          (e)=>{return e == condicion};
      */
      static count(STRUCTURE, CHECKER) { 
        return count(STRUCTURE, CHECKER);
      }
  
      static create_array(SIZE, 
        DATA = null) {
          return create_array(SIZE, DATA);
      }
  
  
      static repeat_each(SECONDS, CALLBACK) {
        return repeat_each(SECONDS, CALLBACK)
      }
  
      static jsobject_to_map(jsobject) {
        return new Map(
          Object.entries(jsobject));
      }
  
      static map_to_jsobject(map) {
        return map.fromEntries()
      }
  
      static find_value(jsobject) {
        return find_value(jsobject)
      }
  
      static true_percentage(BOOL_ARRAY) {
        return true_percentage(BOOL_ARRAY)
      }
  
      static fit_list(ARRAY, SIZE, 
        DEFAULT_VALUE = null) {
          return fit_list(ARRAY, SIZE, 
            DEFAULT_VALUE);
      }
  
      static join_jsobject(jsobject_1, 
            jsobject_2) {
          return join_jsobject(jsobject_1, 
            jsobject_2);
      }
  
      static join_map(map1, map2) {
        return new Map([...map1, ...map2]);
      }
  
      static sort_from_smallest(ARRAY) {
        let array = ARRAY
        array.sort((a, b) => a - b);
        return array
      }
  
      static sort_from_largest(ARRAY) {
        let array = ARRAY
        array.sort((a, b) => b - a);
        return array
      }
  
      /*
      Funcion que aplica un map a una 
      estructura que puede ser un array, 
      un map o un objeto javascript.
      */
      static map2(DATA, FUNCTION) {
        return map2(DATA, FUNCTION);
      }
  
      static min_in_dict(JSOBJECT) {
        return min_in_dict(JSOBJECT)
      }
  
      static max_in_dict(JSOBJECT) {
        return max_in_dict(JSOBJECT)
      }
  
      static find_closest_highest_array(
        ARRAY, NUMBER) {
          return find_closest_highest_array(
            ARRAY, NUMBER)
      }
  
      static find_closest_lower_array(
        ARRAY, NUMBER) {
          return find_closest_lower_array(
            ARRAY, NUMBER)
      }
  

}