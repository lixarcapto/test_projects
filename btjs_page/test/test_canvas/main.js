

import { Btjs } from "../../btjs/Btjs.js";

function main() {
    let canvas = Btjs.Canvas(500, 400)
    canvas.to_document()
    canvas.set_pen_color("blue")
    canvas.set_pen_width(3)
    canvas.draw_vertical_grid(7, 100)
    let p = [1, 1]
    let increment = 1
    Btjs.repeat(4, 0.3, ()=>{
        for(let i=0;i<50;i++) {
            p[0] = p[0] + increment
            p[1] = p[1] + increment
            canvas.draw_point(p)
            increment + 2
        }
    })

}

main()