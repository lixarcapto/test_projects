


export class ChartLegends {

    constructor() {
        this.node = document
            .createElement("span")
        this.node.setAttribute("style", 
            `
            display: block;
            background-color: white; /* Color de fondo negro */
            padding: 10px;
            border: 3px solid gray;
            `
        )
        this.legend_arr = []
    }

    create_legends(map) {
        for(let[key, value] of map) {
            this.add_leyend(key, value)
        }
    }

    add_leyend(key, color) {
        let label = document
            .createElement("span")
        let square = this.create_square(color)
        label.append(square)
        label.innerHTML += "&nbsp&nbsp" + key 
        label.style.display = "inline-flex";
        label.style.padding = "3px"
        this.legend_arr.push(label)
        this.node.append(label)
    }

    create_square(color) {
        let square = document
            .createElement("span")
        square.setAttribute("style", `
            width: 16px;
            height: 16px;
            background-color: ${color}; /* Puedes cambiar el color aquí */
            border: 2px solid black; /* Borde negro de 2px */    
        `)
        return square
    }

}