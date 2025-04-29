

import {BtjsStructures} 
    from "../structures/BtjsStructures.js";
import { LimitNumber } from 
    "./mod/LimitNumber.js";

export class UtilBtjs extends BtjsStructures {

    static print(text) {
        document.body.innerHTML 
            += "<br>" + text
    }

    static LimitNumber(range_arr, 
            number = -1) {
        return new LimitNumber(
            range_arr, number)
    }


}