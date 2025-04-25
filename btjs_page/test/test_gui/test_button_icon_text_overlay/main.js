

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let button = Btjs.ButtonIconTextOverlay(
        "title", 
        "http://localhost/web_projects/btjs_page/res/char_icon/fish_50x50.png"
    )
    button.to_document()

}

main()