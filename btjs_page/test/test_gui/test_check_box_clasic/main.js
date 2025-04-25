

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let button = Btjs.CheckBoxClasic(
        "title", [
            "a",
            "b",
            "c",
            "d"
        ]
    )
    button.set_in_horizontal()
    button.to_document()
    let button2 = Btjs.CheckBoxClasic(
        "title", [
            "a",
            "b",
            "c",
            "d"
        ]
    )
    button2.set_in_vertical()
    button2.to_document()
    let button3 = Btjs.CheckBoxClasic(
        "title", [
            "a",
            "b",
            "c",
            "d"
        ]
    )
    button3.set_in_horizontal()
    button3.to_document()

}

main()