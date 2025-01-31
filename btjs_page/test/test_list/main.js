

import { Btjs } from "../../btjs/Btjs.js"

function main() {
    let e = Btjs.ListUl("text", 
        [
            "Estados Unidos", 
            "Canadá", 
            "México", 
            "Francia", 
            "Alemania", 
            "Japón", 
            "China",
            "India", 
            "Brasil", 
            "Argentina"
        ]
    )
    e.to_document()
    let e2 = Btjs.ListOl("text", 
        [
            "Estados Unidos", 
            "Canadá", 
            "México", 
            "Francia", 
            "Alemania", 
            "Japón", 
            "China",
            "India", 
            "Brasil", 
            "Argentina"
        ]
    )
    e2.to_document()

}

main()