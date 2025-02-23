

import { Btjs } from "../../../btjs/Btjs.js";
import { Engine } 
    from "../../../btjs/mod/engine/Engine.js";


function main() {
    let engine = new Engine(300, 300)
    let btn = Btjs.Button("stop/start")
    btn.to_document()
    btn.add_click_listener(()=>{
        if(engine.is_on) {
            engine.stop()
        } else {
            engine.start()
        }
        
        console.log("stop/start")
    })
    engine.set_folder_image_url(
        "http://localhost/web_projects/btjs_page/res"
    ) 
    engine.set_image_in_folder("fish",
        "/char_icon/fish_50x50.png"
    )
    engine.set_image_in_folder("three",
        "/char_icon/three_50x50.png"
    )
    let go = engine.Gobject("cosa")
    go.set_has_gravity(true, 0.1)
    go.set_image_name("fish")
    go.set_size(40, 40)
    go.set_position(150, 100)
    engine.set(go)
    engine.create_scenario()
    
}

main()