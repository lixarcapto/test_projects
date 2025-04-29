

import {BtjsStructures} 
    from "../structures/BtjsStructures.js";

export class UtilBtjs extends BtjsStructures {

    static print(text) {
        document.body.innerHTML 
            += "<br>" + text
    }


}