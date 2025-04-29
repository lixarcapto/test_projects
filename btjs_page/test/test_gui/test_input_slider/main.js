

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let button = Btjs.InputSlider("title",
        [0, 100]
    )
    button.set_value(45)
    button.to_document()

}

main()