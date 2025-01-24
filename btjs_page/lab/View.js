

import { Btjs } from "../btjs/Btjs.js";
import { TextField } 
    from "../btjs/mod/TextField.js";
import { Model } from "./Model.js";
import { DetailCard } from "./DetailCard.js";

export class View {

    constructor() {
        this.model = new Model()
        //
        document.body.setAttribute("style",
            `
            display: flex; /* Establecemos el contenedor como un contenedor flex */
            justify-content: space-around; /* Distribuye los elementos de forma equitativa 
            `
        )
        this.title_bar = Btjs.TitleBar(
            "desktop")
        this.title_bar.to_document()
        //
        this.btn_end = Btjs.ClickIconOnly(
            "advance", "res/advance_hearth.png")
        this.btn_end.to_document()
        this.btn_end.add_click_listener(
            ()=>{
                this.update()
            }
        )
        //
        this.card = new DetailCard()
        document.body.append(this.card.node)
        this.card2 = new DetailCard()
        document.body.append(this.card2.node)
        
        this.update()
    }

    update() {
        let message = this.model.request(
            {"message":"advance_time"}
        )
        this.model.request(message)
        message = this.model.request(
            {"message":"render"}
        )
        this.paint_render(message)
    }

    paint_render(json) {
        let json_arr = json["data"]
        let render_char_1 = json_arr[0]
        let render_char_2 = json_arr[1]
        this.card.load_json_data(
            render_char_1)
        this.card2.load_json_data(
            render_char_2)
    }

}