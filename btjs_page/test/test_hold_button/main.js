

import { Btjs } from "../../btjs/Btjs.js";
import { HoldButton } 
    from "../../btjs/mod/HoldButton.js";

function main() {
    let e = new HoldButton("text", [0, 50])
    e.to_document()
    let btn = Btjs.Button("click")
    btn.to_document()
    btn.add_click_listener(()=>{
        console.log(e.get_value())
    })

}

main()