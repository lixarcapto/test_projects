



export class InputSlider {

    constructor(title, range_arr, value) {
        this.node = document.createElement(
            "section")
        this.node.setAttribute("tag",
            "input_slider")
        this.title = document.createElement(
            "label")
        this.title.innerHTML = title
        this.input = document.createElement(
            "input")
        this.input.setAttribute("type", 
            "range")
        this.result = document
            .createElement("label")
        this.node.append(this.title)
        this.node.append(this.input)
        this.node.append(this.result)
        this.set_range(range_arr)
        this.set_value(value)
        this.add_listener()
    }

    add_listener() {
        this.input.addEventListener(
            "change", 
            ()=>{
                this.update_text()
            }
        )
    }

    set_range(range_arr) {
        this.input.setAttribute("min", 
            range_arr[0])
        this.input.setAttribute("max", 
            range_arr[1])
    }

    set_value(value) {
        this.input.value = value
        this.update_text()
    }

    update_text() {
        this.result.innerHTML 
            = ` ${this.input.value} / 
            ${this.input.getAttribute("max")}`
        
    }

    get_value() {
        return this.input.value
    }

}