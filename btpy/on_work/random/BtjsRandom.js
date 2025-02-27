

import { BtjsMath } 
  from "../math/BtjsMath.js";
// RANDOM ----------------------------------

import { random_string } 
  from "./random_string.js";
import { random_bool } 
  from "./random_bool.js";
import { random_probability } 
  from "./random_probability.js";
import { random_rgb } 
  from "./random_rgb.js";
import { random_element } 
  from "./random_element.js";
import { random_int } 
  from "./random_int.js";
import { random_point } 
  from "./random_point.js";
import {random_figure_point} 
  from "./random_figure_point.js";
import { random_range } 
  from "./random_range.js";

export class BtjsRandom extends BtjsMath {

    // RANDOM ----------------------------
    
        static random_bool() {
          return random_bool()
        }
    
        static random_figure_point(size) {
          return random_figure_point(size)
        }
    
        static random_point(min, max) {
            return random_point(min, max)
        }
    
        static random_element(ARRAY) {
            random_element(ARRAY)
        }
      
        static random_probability(probability) {
          return random_probability(probability)
        }
    
        static random_int(min, max) {
          return random_int(min, max)
        }
    
        static random_string(SIZE, 
          CHAR_STRING = null) {
            return random_string(SIZE, 
              CHAR_STRING)
        }
    
        static random_rgb(rgb_limit 
            = [256, 256, 256]) {
          return random_rgb(rgb_limit)
        }

        static random_range(min, max) {
          return random_range(min, max)
        }

}