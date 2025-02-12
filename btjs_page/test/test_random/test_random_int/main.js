

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let array = []
    let r = 0
    for(let i=0;i<15;i++) {
        r = Btjs.random_int(0, 100)
        array.push(r)
    }
    console.log(array)

}

main()