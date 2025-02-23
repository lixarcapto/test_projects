

import { Btjs } from "../../../btjs/Btjs.js";
import { Iterator1d } 
    from "../../../btjs/mod/structures/Iterator1d.js";

function main() {
    let it = Btjs.Iterator1d([
        "a", "b", "c", "d", "e", "f"
    ])
    it.set_is_cycle(true)
    it.set_is_inverted(true)
    let n = 0
    while(it.has_next()) {
        console.log(it.get())
        it.next()
        n += 1
        if(n> 100) {break}
    }

}

main()