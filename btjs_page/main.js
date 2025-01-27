


import { Btjs } from "./btjs/Btjs.js"
import { lab_main } from "./lab/lab_main.js"
import { ComicStrip } from "./btjs/mod/ComicStrip.js"
import { json_comic } from "./res/json_comic.js"
import { CardBoxTGC } from "./btjs/mod/CardBoxTGC.js"
import { Card } from "./btjs/mod/Card.js"

function main() {
   let btn = Btjs.Button("** click **")
   btn.to_document()
   let icon_box = Btjs.ClickIconBox("iconos",
      ["perro", "gato", "raton"]
   )
   icon_box.to_document()
   icon_box.set_content_array(
      [
         "res/char_icon/fish_50x50.png",
         "res/char_icon/three_50x50.png",
         "res/char_icon/water_50x50.png"
      ]
   )
   icon_box.add_listener_to("raton", ()=>{
      console.log("si funciona lol")
   })
}

main()