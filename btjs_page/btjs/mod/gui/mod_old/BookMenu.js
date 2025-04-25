



export class BookMenu {

    constructor(title = "") {
        this.node = document.createElement(
            "div")
        this.book = document.createElement(
            "div")
        this.book.setAttribute("style",
            `
            display: grid;
            grid-template-columns: 1fr 4fr; /* Dos columnas de igual ancho */
            gap: 6px; /* Espacio entre columnas */
            `
        )
        this.title = document.createElement("label")
        this.node.append(this.title)
        this.title.innerHTML = title
        this.node.append(this.book)
        this.nav_menu = document.createElement(
            "div")
        this.nav_menu.style.display = "inline"
        this.nav_menu.style
            .backgroundColor = "blue"
        this.nav_menu.setAttribute("style",
            `
            display: grid;
            grid-template-columns: 1fr; /* Una sola columna que ocupa todo el ancho disponible */
            gap: 1px; /* Espacio entre los botones */
            `
        )
        this.book.append(this.nav_menu)
        this.sheet = document.createElement(
            "div")
        this.sheet.setAttribute("style",
            `
            display:inline;
            border: 2px solid black; /* Borde exterior */
            border-radius: 10px; /* Esquinas redondeadas */
            padding: 10px;
            box-sizing: border-box;
            `
        )
        this.nav_menu.style
            .backgroundColor = "red"
        this.book.append(this.sheet)
        this.dict_text = {}
    }

    update_sheet(key) {
        this.sheet.innerHTML
            = this.dict_text[key]
    }

    create_nave_menu(dict_text) {
        this.dict_text = dict_text
        let button = null
        let fn = null
        for(let e in this.dict_text) {
            button = document.createElement(
                "button")
            button.innerHTML 
                = `${e}`
            this.nav_menu.append(button)
            fn = ()=>{
                return ()=>{
                    return this
                        .update_sheet(e)
                }
            }
            button.addEventListener("click",
                fn()
            )
        }
    }

}