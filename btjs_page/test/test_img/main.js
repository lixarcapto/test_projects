

import { Btjs } from "../../btjs/Btjs.js";

function main() {
    let img = Btjs.Image(
        "http://localhost/web_projects/btjs_page/res/chica_catolica_mini.png")
    img.to_document()
    img.set_height_with_relation(300)

}

main()