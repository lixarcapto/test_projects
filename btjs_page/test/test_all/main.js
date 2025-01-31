

import { Btjs } from "../../btjs/Btjs.js";

function main() {
    Btjs.body.set_background("red")
    let icon = Btjs.ClickIconOnly("icono",
        "http://localhost/web_projects/btjs_page/res/coin.png"
    )
    icon.to_document()
    let number = 0
    let dice = Btjs.Dice(100, 100)
    dice.to_document()
    let widget_arr = []
    let e = null
    for(let i=0;i<10;i++) {
        e = Btjs.ClickIconText(
            "text",
            "http://localhost/web_projects/btjs_page/res/dollar.png"
        )
        e.to_document()
        widget_arr.push(e)
    }

    icon.add_click_listener(()=>{
        widget_arr[3].set_text(
            "dinero:" + number + "$")
        number += 50
    })

}

main()