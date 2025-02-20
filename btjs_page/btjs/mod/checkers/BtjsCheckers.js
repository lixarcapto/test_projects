

//CHECKERS -----------------------------------

import { in_range } 
  from "./in_range.js";
import { is_null_return } 
  from "./is_null_return.js";
import { is_byte127 } 
  from "./is_byte_256.js";
import { is_byte256 } 
  from "./is_byte_256.js";
import { is_RGB } 
  from "./is_rgb.js";
import { is_RGBA } 
  from "./is_rgb.js";
import { is_point_2d } 
  from "./is_point.js";
import { is_point_3d } 
  from "./is_point.js";
import { is_object_js } 
  from "./is_object_js.js";

export class BtjsCheckers {

    //CHECKERS -----------------------------
    
        /*
        This function checks if the elements 
        of the passed array are all equal.
        */
        static are_all_same(array) {
          return are_all_same(array);
        }
    
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
        is a return error such as -1, undefined,
        none, void string, void dict, or void
        array
        */
        static is_null_return(data) {
          return is_null_return(data);
        }
    
        static is_byte127(data) {
          return is_byte127(data);
        }
    
        static is_byte256(data) {
          return is_byte256(data);
        }
        
        static is_RGB(data) {
          return is_RGB(data);
        }
    
        static is_RGBA(data) {
          return is_RGBA(data);
        }
    
        static is_float(data) {
          return data % 1 !== 0;
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

        

}