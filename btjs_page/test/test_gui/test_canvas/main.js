

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let canvas = Btjs.Canvas(500, 400)
    canvas.to_document()
    canvas.set_pen_color("blue")
    canvas.set_pen_width(3)
    canvas.draw_fill_rect_centered(
        [50,0], [100, 200])
}

main()