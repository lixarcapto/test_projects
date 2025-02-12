

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let array = []
    for(let i=0;i<15;i++) {
        array.push(Btjs.random_bool())
    }
    console.log(array)

}

main()