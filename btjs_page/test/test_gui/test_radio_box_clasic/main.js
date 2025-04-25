

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let button = Btjs.RadioBoxClasic(
        "title", [
            "a",
            "b",
            "c",
            "d"
        ]
    )
    button.to_document()
    button.set_in_horizontal()
    let button2 = Btjs.RadioBoxClasic(
        "title", [
            "a",
            "b",
            "c",
            "d"
        ]
    )
    button2.set_in_vertical()
    button2.to_document()

}

main()