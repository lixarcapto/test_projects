

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let r = null
    //
    r = Btjs.is_range([0, 5])
    console.log(r == true)
    //
    console.log("es un rango corto")
    r = Btjs.is_range([1, 2])
    console.log(r == true)
    //
    console.log(
        "no existe el rango en el array")
    r = Btjs.is_range([2, 2])
    console.log(r == false)
    //
    console.log("es un rango con negativos")
    r = Btjs.is_range([-1, 1])
    console.log(r == true)
    //el rango esta invertido
    r = Btjs.is_range([5, 1])
    console.log(r == false)
    //el array es mas grande
    r = Btjs.is_range([0, 5, 5])
    console.log(r == false)
    //el array es mas pequeño
    r = Btjs.is_range([0])
    console.log(r == false)
    //no es un array
    r = Btjs.is_range(5)
    console.log(r == false)
    //es un string array
    r = Btjs.is_range("[0, 5]")
    console.log(r == false)
    //es un rango float
    r = Btjs.is_range([0.1, 5.5])
    console.log(r == true)
}

main()