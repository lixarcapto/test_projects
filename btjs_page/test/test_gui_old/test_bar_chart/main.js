

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    
    let e = Btjs.BarChart("grafico")
    e.to_document()
    e.set_data_bars([
        {
            "value":5,
            "key": "gente",
            "color": "green"
        },
        {
            "value":2,
            "key": "perros",
            "color": "red"
        },
        {
            "value":3,
            "key": "gatos",
            "color": "yellow"
        },
        {
            "value":6,
            "key": "peces",
            "color": "aquamarine"
        }
    ])

}

main()