


import { StandardElement } from "./StandardElement.js"

export class DataBar extends StandardElement {

    constructor(title, range_arr) {
        super();
        this.input_text = document.createElement(
            "span")
        this.input_text.style.display = "inline"
        this.input_text.setAttribute("tag",
            "progress_bar")
        this.input_text.setAttribute("style",
            `
            display: inline-block;
            border: 1px solid gray;
            overflow: hidden;
            justify-content: center;
            align-items: center;
            background-color: #EFEFEF;
            padding: 0px;
            `
        )
        this.title = document.createElement(
            "label")
        
        this.range_arr = [0, 0]
        this.bar = document.createElement(
            "progress")
        this.message = {}
        this.bar.setAttribute("style",
            `
                width: 300px;
                height: 27px;
                border: 4px solid rgb(0, 255, 51);
                background-color: #000000;
                background-color: #4CAF50;
            `
        )
        
        this.input_text.append(this.title)
        this.input_text.append(this.bar)
        //
        this.bar.value = 0
        this.set_range_arr([0, 100])
        this.set_text(title)
    }

    set_text(text) {
        this.title.innerHTML 
            =  text + "&nbsp:&nbsp" 
    }

    set_range_arr(range_arr) {
        this.range_arr = range_arr
        this.bar.setAttribute("min", 
            range_arr[0])
        this.bar.setAttribute("max", 
            range_arr[1])
    }

    reach_max() {
        let v = this.bar.value
        let max = this.range_arr[1]
        if(v >= max) { return true }
        return false
    }

    set_value(value) {
        this.bar.value = value
    }

    get_value() {
        return this.bar.value
    }

}