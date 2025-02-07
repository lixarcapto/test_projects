

import { Btjs } from "../../../btjs/Btjs.js";
import { SwipperText } from "../../btjs/mod/SwipperText.js";

function main() {
    let swipper_arr = []
    let swipper = null
    for(let i=0;i<12;i++) {
        swipper = Btjs.SwipperText(
            "swipper_text",
            ["perro", "gato", "raton"]
        );
        swipper.to_document()
    }
}

main()