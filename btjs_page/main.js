


import { Btjs } from "./btjs/Btjs.js"
import { lab_main } from "./lab/lab_main.js"
import { ComicStrip } from "./btjs/mod/ComicStrip.js"
import { json_comic } from "./res/json_comic.js"
import { TextField } from "./btjs/mod/TextField.js"
import { Canvas } from "./btjs/mod/Canvas.js"

function main() {
    let sign = Btjs.Sign(
        "cartel desplazable",
    250, 30)
    sign.to_document()
    let chart = Btjs.IconChart("cosas")
    chart.to_document()
    chart.set_dict_arr([
        {
            "quantity": 10,
            "name": "",
            "url": "res/char_icon/fish_50x50.png"
        },
        {
            "quantity": 30,
            "name": "",
            "url": "res/char_icon/three_50x50.png"
        },
        {
            "quantity": 60,
            "name": "",
            "url": "res/char_icon/water_50x50.png"
        }
    ], 50,50)
}

main()