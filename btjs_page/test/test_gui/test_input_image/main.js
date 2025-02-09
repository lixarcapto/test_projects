

import { Btjs } from "../../../btjs/Btjs.js";
import { InputFile } 
    from "../../../btjs/mod/gui/InputFile.js";
import { InputImage } from 
    "../../../btjs/mod/gui/InputImage.js";

function main() {
    
    let ip = new InputImage("escribe aqui")
    ip.to_document()
    ip.set_file_type(Btjs.IMAGE)
    let btn = Btjs.Button("send image")
    btn.to_document()
    let img = Btjs.Image()
    img.to_document()
    btn.add_click_listener(()=>{
        let file = ip.get_value(
            (result)=>{
                img.set_image(result)
        })
    })

}

main()