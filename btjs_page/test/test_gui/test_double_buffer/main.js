

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let canvas = Btjs.Canvas(400, 400)
    canvas.to_document()
    canvas.pen_color = "red"
    let point = [0, 0]
    let url = "http://localhost/web_projects/btjs_page/res/char_icon/fish_50x50.png"
    Btjs.repeat_each(0.3, (n)=>{
        console.log("update", n)
        canvas.clear()
        canvas.draw_image(url, point[0],
            point[1]
        )
        canvas.draw_image(url, 200,
            point[1]
        )
        point[1] += 5
        canvas.end_paint()
    })

}

main()