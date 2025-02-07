

import { Btjs } from "../../../btjs/Btjs.js"

function main() {
    let e = Btjs.SwipperNumber("swipper",
        [0, 4]
    )
    e.to_document()
    e.add_listeners(
        ()=>{console.log("funciona " + e.get_value())})

}

main()