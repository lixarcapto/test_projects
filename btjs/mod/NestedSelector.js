



export class NestedSelector {

    /*XXX: no esta terminado */

    constructor() {
        this.node = document
            .createElement("section")
        this.first_select = document
            .createElement("select")
        this.node.append(first_select.node)
        this.dict_selector = {}
        let nested_select = document
            .createElement("select")
        this.node.append(nested_select.node)
    }

    add_nested_selector(key, dict) {
        this.dict_selector[key] = dict
    }

    create_selector(key, text_arr) {
        let option = null
        
        for(let i in text_arr) {
            
        }
    }

}