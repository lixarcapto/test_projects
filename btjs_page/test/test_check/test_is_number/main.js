

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let r = null
    //
    r = Btjs.is_number(5)
    console.log(r == true)
    //
    r = Btjs.is_number(-1)
    console.log(r == true)
    //
    r = Btjs.is_number(0)
    console.log(r == true)
    //si es string
    r = Btjs.is_number("1")
    console.log(r == false)
    //si es array
    r = Btjs.is_number([1])
    console.log(r == false)
    //si es float
    r = Btjs.is_number(0.5)
    console.log(r == true)
    //si es numero grande
    r = Btjs.is_number(10 ** 10)
    console.log(r == true)
}

main()