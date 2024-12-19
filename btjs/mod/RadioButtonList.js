



export class RadioButtonList {

    static last_id = 0

    constructor(title, text_arr) {
        this.node = document
            .createElement("div")
        this.radio_arr = []
        this.label_arr = []
        this.title = document
            .createElement("label")
        this.title.innerHTML = title
        this.node.append(this.title)
        this.unique_id = String(
            RadioButtonList.last_id)
        RadioButtonList.last_id += 1
        this.node.setAttribute("tag", 
            "radio_button_list")
        this.create_list(text_arr)
    }

    set_title(text) {
        this.title.innerHTML = text
    }

    get_value() {
        for(let i in this.radio_arr) {
            if(this.radio_arr[i].checked) {
                return this.label_arr[i]
                    .innerHTML
            }
        }
        return "none"
    }

    create_list(text_arr) {
        let radio = null
        let label = null
        for(let i in text_arr) {
            radio = document
                .createElement("input")
            radio.setAttribute(
                "type", "radio")
            radio.setAttribute(
                "name", this.unique_id)
            label = document
                .createElement("label")
            label.innerHTML = text_arr[i]
            this.node.append(radio)
            this.radio_arr.push(radio)
            this.node.append(label)
            this.label_arr.push(label)
        }
    }

}