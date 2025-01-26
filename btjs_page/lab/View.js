

import { Btjs } from "../btjs/Btjs.js";
import { TextField } 
    from "../btjs/mod/TextField.js";
import { Model } from "./Model.js";
import { DetailCard } from "./DetailCard.js";
import { CardBoxTGC } from "../btjs/mod/CardBoxTGC.js";

export class View {

    static CARDS_BY_PLAYER = 5

    constructor() {
        this.model = new Model()
        //
        document.body.setAttribute("style",
            `
            display: flex; /* Establecemos el contenedor como un contenedor flex */
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
        this.card_frame = Btjs.Frame()
        this.card_frame.to_document()
        this.card_box_1 = new CardBoxTGC(5)
        this.card_frame.append(
            this.card_box_1)
        this.card_box_1.set_size_card(
            100, 200)
        //
        this.card_box_2 = new CardBoxTGC(5)
        this.card_frame.append(
            this.card_box_2)
        this.card_box_2.set_size_card(
            100, 200)
        this.update()
    }

    update() {
        let message = {}
        message = this.model.request(
            {
                "message":"select_card",
                "data": this.card_box_1
                    .get_value()
            }
        )
        message = this.model.request(
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
        let render_char_1 = json_arr["army_1"]
        let render_char_2 = json_arr["army_2"]
        this.card_box_1.paint_objs_render_arr(
            render_char_1
        )
        this.card_box_2.paint_objs_render_arr(
            render_char_2
        )
    }

}