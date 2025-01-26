

import { StandardElement } 
    from "./StandardElement.js"
import { CardTcg } from "./CardTcg.js"

export class CardBoxTGC extends StandardElement {

    constructor(quantity = 10) {
        super();
        this.node = document
            .createElement("span")
        this.value_index_card = 0
        this.node.setAttribute("style",
            `
            display:flex;
            `
        )
        this.card_arr = []
        this.create_card(quantity)
    }

    get_value() {
        return this.value_index_card
    }

    set_size_card(width, height) {
        for(let i in this.card_arr) {
            this.card_arr[i].set_size_card(
                width, height
            )
        }
    }

    /*
    {
        "image_url": "",
        "title": "",
        "description": "",
        "text_array": [],
        "color_array": []
    }
    */
    paint_objs_render_arr(objs_content_arr) {
        let objs = null
        for(let i=0;i<objs_content_arr.length;i++) {
            objs = objs_content_arr[i]
            this.card_arr[i]
                .set_title(
                    objs["title"])
            this.card_arr[i]
                .set_description(
                    objs["description"])
            this.card_arr[i]
                .set_image(
                    objs["image_url"])
            this.card_arr[i]
                .set_icon_content_arr(
                    objs["text_array"],
                    objs["color_array"]
                )
        }
    }

    get_quantity_elements() {
        return this.card_arr.length
    }

    create_card(quantity) {
        let card = null
        let fn = null
        for(let i=0;i<quantity;i++) {
            card = new CardTcg()
            this.card_arr.push(card)
            this.node.append(card.node)
            fn = ()=>{
                return ()=>{
                    this.value_index_card 
                        = i;
                    console.log(i)
                }
            }
            card.node.addEventListener("click",
                fn()
            )
        }
    }

}