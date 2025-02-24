

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let r = Btjs.in_range(5, [0, 6])
    console.log(r == true)
    //
    r = Btjs.in_range(5, [0, 5])
    console.log(r == true)
    //
    r = Btjs.in_range(0, [0, 5])
    console.log(r == true)
    //
    r = Btjs.in_range(-1, [0, 5])
    console.log(r == false)
    //
    r = Btjs.in_range(6, [0, 5])
    console.log(r == false)
    //
    r = Btjs.in_range("6", [0, 5])
    console.log(r == false)
    //
    r = Btjs.in_range(5.0, [0, 5])
    console.log(r == true)
    //
    r = Btjs.in_range(5.4, [0, 5])
    console.log(r == false)
    //
    r = Btjs.in_range(5.4, [0, 5])
    console.log(r == false)
    //
    console.log("si el rango no es array")
    r = Btjs.in_range(5.4, 6)
    console.log(r == false)
    //
    console.log("si el rango no es array x2")
    r = Btjs.in_range(5.4, [0, 5, 5])
    console.log(r == false)
}

main()