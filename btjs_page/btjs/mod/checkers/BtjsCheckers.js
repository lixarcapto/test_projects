

//CHECKERS -----------------------------------

import { in_range } 
  from "./mod/in_range.js";
import { is_null_return } 
  from "./mod/is_null_return.js";
import { is_byte_127 }
  from "./mod/is_byte_127.js";
import { is_byte_256 } 
  from "./mod/is_byte_256.js";
import { is_RGB } 
  from "./mod/is_rgb.js";
import { is_RGBA } 
  from "./mod/is_rgb.js";
import { is_point_2d } 
  from "./mod/is_point.js";
import { is_point_3d } 
  from "./mod/is_point.js";
import { is_object_js } 
  from "./mod/is_object_js.js";
import { is_number } 
  from "./mod/is_number.js";
import { is_range } 
  from "./mod/is_range.js";
import { is_float } 
  from "./mod/is_float.js";
import { is_json } 
  from "./mod/is_json.js";

export class BtjsCheckers {

    //CHECKERS -----------------------------

    
    /*
    Function to identify if the input 
    number is contained within the 
    sending range.
    */
    static in_range(number, range_arr) {
      return in_range(number, range_arr);
    }
    
    /*
    Function that tests whether a value
    is a return error such undefined,
    none, void string, void dict, or void
    array
    */
    static is_null_return(data) {
      return is_null_return(data);
    }
    
    static is_byte127(data) {
      return is_byte_127(data);
    }
    
    static is_byte256(data) {
      return is_byte_256(data);
    }
        
    static is_RGB(data) {
      return is_RGB(data);
    }
    
    static is_RGBA(data) {
      return is_RGBA(data);
    }
    
    /*
    Function that returns true if the 
    data sent is of decimal (float) type
    */
    // return bool
    static is_float(DATA) {
      return is_float(DATA)
    }
    
    static is_array(data) {
      return Array.isArray(data)
    }
    
    static is_integer(data) {
      return Number.isInteger(data)
    }
    
    static is_string(data) {
      return typeof valor === 'string';
    }
    
    static is_object_js(data) {
      return is_object_js(data);
    }
    
    static is_function(data) {
      return typeof data == "function";
    }
    
    static is_map(data) {
      return data instanceof Map;
    }
    
    /*
    Función que verifica  el dato 
    enviado es un punto 2D
    */
    static is_point_2d(data) {
      return is_point_2d(data);
    }
    
    /*
    Función que verifica  el dato 
    enviado es un punto 3D
    */
    static is_point_3d(data) {
       return is_point_3d(data);
    }

    /*
    This function is used to verify if 
    the data sent is of numeric type, 
    returning true if it is.
    */
    // return bool
    static is_number(DATA) {
      return is_number(DATA)
    }

    /*
    Function that returns true if the 
    data sent is of range array type. 
    */
    // return bool
    static is_range(RANGE_ARRAY) {
      return is_range(RANGE_ARRAY)
    }

    /*
    Function that returns true if the 
    data sent is a json string
    */
    // return bool
    static is_json(ANY) {
      return is_json(ANY)
    }

    static is_set(ANY) {
      return ANY instanceof Set;
    }

}