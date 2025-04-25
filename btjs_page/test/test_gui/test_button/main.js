

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let button = Btjs.Button("text")
    button.to_document()
    button.add_click_listener(
        (e)=>{console.log("click")}
    )

}

main()