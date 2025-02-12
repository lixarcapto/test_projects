

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let tips = Btjs.LimitNumber(
        [0, 100], 0)
    let url = "http://localhost/web_projects/btjs_page/res/camarera.png"
    let img = Btjs.ClickIconOnly("icon", url)
    img.to_document()
    let label = Btjs.Label("")
    label.to_document()
    let bar = Btjs.DataBar("tips $")
    bar.to_document()
    bar.set_range_arr([0, 100])
    let url_tip = "http://localhost/web_projects/btjs_page/res/dollar.png"
    let tip_btn = Btjs.ClickIconOnly(
        "tip_btn", url_tip)
    tip_btn.to_document()
    tip_btn.add_click_listener(()=> {
        tips.sum(5)
        bar.set_value(tips.get())
        if(tips.get() >= 60) {
            label.set_text(`
            Es suficiente gracias con
            5$ dolares bastaba cariño.    
            `)
        } else if(tips.get() <= 20) {
            label.set_text(`
            La propina es el 12% cariño, 
            y aqui hay solo $${tips.get()}.    
            `)
        } else {
            label.set_text("")
        }
    })
}

main()