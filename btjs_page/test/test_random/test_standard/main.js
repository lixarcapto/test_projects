

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let label = Btjs.Label("hola mundo")
    label.to_document()
    let txt = ""
    for(let i=0;i<12;i++) {
        txt += "["+Btjs.random_range(0, 100)+"]"
    }
    label.set_text(txt)
}

main()