

import { Btjs } from "../../../btjs/Btjs.js";
import { InputFile } 
    from "../../../btjs/mod/gui/InputFile.js";
import { InputXLSX } from "../../../btjs/mod/gui/InputXLSX.js";

function main() {
    
    let ip = new InputXLSX("escribe aqui")
    ip.to_document()
    let btn = Btjs.Button("send image")
    btn.to_document()
    btn.add_click_listener(()=>{
        let file = ip.get_value_row_dict(
            (result)=>{
                console.log(result)
        })
    })

}

main()