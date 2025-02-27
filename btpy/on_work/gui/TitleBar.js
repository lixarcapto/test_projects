

import { Btjs } from "../../Btjs.js";
import { active_full_screen } from "./active_full_screen.js";
import { quit_full_screen } from "./quit_full_screen.js";
import { StandardElement } from "./StandardElement.js"

export class TitleBar extends StandardElement {

    constructor(title) {
        super();
        this.node = document.createElement(
            "div")
        this.node.setAttribute("style",
            `
            display: flex;
            gap: 2px;
            align-items: center;
            padding: 0px;
            background-color: #f0f0f0;
            height: 30px;
            `
        )
        this.init_buttons()
        this.title = document.createElement(
            "label")
        this.title.setAttribute("style",
            "height: 30px;"
        )
        this.set_titles(title)
        this.node.append(this.title)
        
    }

    init_buttons() {
        let style_btn = `
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 3px;
            width: 30px;
            height: 30px;
            `
        this.btn_fullscreen = document
            .createElement("button")
        this.btn_fullscreen.setAttribute(
            "style", style_btn)
        this.btn_fullscreen.innerHTML = " + "
        this.btn_fullscreen.addEventListener(
            "click",
            ()=>{
                active_full_screen()
            }
        )
        this.node.append(this.btn_fullscreen)
        this.btn_quit_fscreen = document
            .createElement("button")
        this.btn_quit_fscreen.setAttribute(
            "style", style_btn)
        this.btn_quit_fscreen.innerHTML = " - "
        this.btn_quit_fscreen.addEventListener(
            "click",
            ()=>{
                quit_full_screen()
            }
        )
        this.node.append(this.btn_quit_fscreen)
    }

    set_titles(title) {
        title = Btjs.capitalize(title)
        this.title.innerHTML = title
        document.title = title
    }

}