

import { CompositeWidget } from 
    "./CompositeWidget.js";

export class Table extends CompositeWidget {

    constructor(TITLE_STR) {
        super(TITLE_STR);
        this.table = document
            .createElement("table")
        this.table.setAttribute("style",
            `
            border-collapse: collapse;

            `
        )
        this.has_first_line = false
        this.inner_span.append(this.table)
    }

    destroy() {
        this.table.remove()
    }

    format() {
        this.has_first_line = false
        this.table.innerHTML = ""
    }

    load_matrix_of_rows(matrix) {
        this.format()
        for(let i in matrix) {
            this.add_row(matrix[i])
        }
    }

    add_row(celd_arr) {
        if(this.has_first_line) {
            this.create_second_row(celd_arr)
            return null
        }
        this.create_first_row(celd_arr)
        this.has_first_line = true
    }

    create_first_row(celd_arr) {
        let element_key = null
        let row = document
            .createElement("tr")
        for(let i in celd_arr) {
            element_key = document
            .createElement("th")
            element_key.setAttribute("style",
                `
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                background-color: #f2f2f2;
                `
            )
            element_key.innerHTML 
                = celd_arr[i]
            row.append(element_key)
        }
        this.table.append(row)
    }

    create_second_row(celd_arr) {
        let row = document
            .createElement("tr")
        let element = null
        for(let i in celd_arr) {
            element = document.createElement(
                "td")
            element.setAttribute("style",
                `
                border: 1px solid black;
                padding: 8px;
                text-align: left;
                `
            )
            element.innerHTML = celd_arr[i]
            row.append(element)
        }
        this.table.append(row)
    }

}