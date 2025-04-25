

import { Btjs } from "../../../btjs/Btjs.js";
import { IconBar } 
    from "../../../btjs/mod/gui/IconBar.js";

function main() {
    
    Btjs.body.set_background("red")
    let fish = 0
    let e = new IconBar()
    e.to_document()
    e.set_image("http://localhost/web_projects/btjs_page/res/char_icon/fish_50x50.png",
       50, 50)
    Btjs.repeat_each(0.8, (n)=>{
        if(n == 5) {return true}
        fish += 1
        e.draw_icon(fish)
    })

}

main()