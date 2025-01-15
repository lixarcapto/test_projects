


import { Btjs } from "./btjs/Btjs.js"
import { DataConst } from "./DataConst.js"

function main() {
    let btn = Btjs.Icon("res/cross.png")
    Btjs.to_body(btn)
    Btjs.jump(7)
    Btjs.body.set_background_image("res/chica_catolica.png")
    let label = Btjs.Label(DataConst.text)
    label.set_size(500, 100)
    Btjs.to_body(label)
    let e = Btjs.TextArea()
    e.set_lines_size(10, 40)
    Btjs.to_body(e)
    let change = Btjs.ChangeColorButton(
        "press")
    Btjs.to_body(change)
    btn.add_click_listener(()=>{
        console.log(change.get_value())
    })
}

main()