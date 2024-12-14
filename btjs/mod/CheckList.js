



export class CheckList {

    constructor(title, text_arr) {
        this.node = document
            .createElement("section")
        this.title = document
            .createElement("p")
        this.title.innerHTML = title
        this.node.append(this.title)
        this.check_arr = []
        this.label_arr = []
        this.create_list(text_arr)
    }

    /*
    Retorna los textos de los 
    checkbox marcados.
    */
    get_checked_list() {
        let text_arr = []
        let e = null
        let value = ""
        for(let i in this.check_arr) {
            e = this.check_arr[i]
            if(e.checked == true) { 
                text_arr.push(
                    this.label_arr[i]
                    .innerHTML
                )
            }
        }
        return text_arr
    }

    create_list(text_arr) {
        let checkbox = null
        let label = null
        this.check_arr = []
        for(let i in text_arr) {
            checkbox = document
                .createElement("input")
            checkbox.setAttribute("type",
                "checkbox")
            this.check_arr.push(checkbox)
            this.node.append(checkbox)
            label = document
                .createElement("label")
            label.innerHTML = text_arr[i]
            this.label_arr.push(label)
            this.node.append(label)
        }
    }

}