

import { Btjs } from "../../../btjs/Btjs.js";
import { Engine } 
    from "../../../btjs/mod/engine/Engine.js";



function main() {
    let canvas = Btjs.Canvas(400, 400)
    canvas.to_document()
    let engine = new Engine()
    engine.set_size(300, 300)
    let g1 = engine.Gobject("a")
    g1.image_name = "img1"
    g1.set_size(50, 50)
    g1.has_gravity = true
    g1.add_behavior_callback("nose", (e)=>{
        if(e.is_colliding) {
            e.set_location(0, 0)
        }
        return e
    })
    engine.set(g1)
    let g2 = engine.Gobject("b")
    g2.set_location(0, 200)
    g2.set_size(50, 50)
    g2.image_name = "three"
    engine.set(g2)
    canvas.add_click_listener((e)=>{
        let gog = engine.Gobject()
        gog.set_location(
            canvas.cursor_point[0], 
            canvas.cursor_point[1]
        )
        gog.set_size(50, 50)
        gog.image_name = "img1"
        gog.has_gravity = true
        engine.set(gog)
    })
    engine.folder_resource_url = 
        "http://localhost/web_projects/btjs_page/res"
    engine.set_image_keyval("img1",
        "/char_icon/fish_50x50.png"
    )
    engine.set_image_keyval("three",
        "/char_icon/three_50x50.png"
    )
    function update() {
        canvas.clear()
        let order_list = engine
            .get_image_order_list()
        canvas.draw_image_order_list(
            order_list)
        canvas.end_paint()
    }
    let p = [0, 0]
    Btjs.repeat_each(0.7, (n)=>{
        engine.update()
        update()
        console.log("update", n)
        if(n >= 50) {
            return true
        }
    })
    
}

main()