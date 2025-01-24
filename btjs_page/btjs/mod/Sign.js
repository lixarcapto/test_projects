


import { Canvas } from "./Canvas.js";
import { StandardElement } from "./StandardElement.js";


export class Sign extends StandardElement {

    constructor(text, width, height) {
        super();
        this.__time_seconds = 0.2
        this.__text = text
        this.__text_size = 0
        this.__default_location = 0
        this.__font_size = 0
        this.__width = width
        this.__height = height
        this.__point = [0, 0]
        this.__interval = null
        this.second_init()
    }

    init_canvas() {
        this.node = new Canvas(
            this.__width, 
            this.__height
        )
        this.node.set_pen_color("white")
        this.node.font_size 
            = this.__font_size
    }

    calcule_data() {
        this.__font_size = this.__height
        this.__text_size 
            = (this.__font_size - 3)
            * this.__text.length
        //es la locacion Y donde se dibuja
        //el texto que tiene un error por
        //el alineamiento del canvas.
        this.__default_location 
            = Math.round(this.__font_size / 2) 
            + Math.round(this.__font_size / 3)
        this.__point 
            = [0, this.__default_location]
    }

    set_size(width, height) {
        this.__width = width
        this.__height = height
        this.calcule_data()
    }

    set_text(text) {
        this.__text = text
    }

    second_init() {
        this.calcule_data()
        this.init_canvas()
        this.init_interval()
    }

    init_interval() {
        this.__interval = setInterval(
            ()=>{
                this.node.update()
                this.node.draw_text(
                    this.__text, 
                    this.__point[0], 
                    this.__point[1]
                )
                this.__point[0] += 5
                if(this.__point[0] 
                        >= this.__width) {
                    this.__point[0] 
                    = this.__text_size *-1
                }
            }, 
            this.__time_seconds * 1000
        );
    }

    set_speed_seconds(seconds) {
        this.__time_seconds = seconds
    }

    to_document() {
        document.body.append(
            this.node.node)
    }

}