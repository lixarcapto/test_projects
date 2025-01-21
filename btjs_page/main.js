


import { Btjs } from "./btjs/Btjs.js"
import { Body } from "./btjs/mod/Body.js"
import { Gauge } from "./btjs/mod/Gauge.js"
import { ClickIconTextOverlay } from "./btjs/mod/ClickIconTextOverlay.js"
import {ClickIconText } from "./btjs/mod/ClickIconText.js"
import { ClickIconOnly } from "./btjs/mod/ClickIconOnly.js"

var icon = null
var saves = 0

function main() {
    let icon1 = new ClickIconOnly("cristianismo",
        "res/cross.png"
    )
    icon1.to_body()
    saves = 1500
    icon = Btjs.ClickIconText("cruz",
        "res/dollar_2.png")
    icon.put_upright()
    icon.set_foreground("green")
    icon.set_text("dolares")
    icon.to_body()
    setInterval(()=>{
        icon.set_text(saves + " $")
        saves += 5
    }, 1000);
}

main()