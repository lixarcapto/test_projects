

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
    go.set_has_gravity(false)
    go.set_has_air_resistance(false)
    go.set_has_acceleration(false)
    go.set_has_camara_tracking(false)
    go.add_image_name("fish")
    go.set_size(40, 40)
    go.set_position(150, 100)
    engine.set(go)
    let go2 = engine.Gobject("cosaXXX")
    go2.set_has_gravity(false)
    go2.set_has_air_resistance(false)
    go2.set_has_acceleration(false)
    go2.set_has_camara_tracking(false)
    go2.add_image_name("three")
    go2.set_size(40, 40)
    go2.set_position(250, 250)
    engine.set(go2)
    engine.add_key_listener("w",
        ()=>{
            engine.scenario
                .__add_event("up_force",
                    "cosa", {"force": 30})
        }
    )
    engine.add_key_listener("a",
        ()=>{
            engine.scenario
                .__add_event("left_force",
                    "cosa", {"force": 30})
        }
    )
    engine.add_key_listener("s",
        ()=>{
            engine.scenario
                .__add_event("down_force",
                    "cosa", {"force": 30})
        }
    )
    engine.add_key_listener("d",
        ()=>{
            engine.scenario
                .__add_event("right_force",
                    "cosa", {"force": 30})
        }
    )
    engine.create_scenario()

}

main()