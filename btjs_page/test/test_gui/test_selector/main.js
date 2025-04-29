

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let button = Btjs.Button("click")
    button.to_document()
    let selector = Btjs.Selector("title",
        [
            "a",
            "b",
            "c",
            "d",
            "e"
        ]
    )
    selector.to_document()
    selector.add_on_change_listener(
        ()=>{
            console.log("funciona el add change listener")
        }
    )
    let fn = (e)=>{
        console.log(selector.get_value())
    }
    button.add_click_listener(fn)
    let selector2 = Btjs.Selector("title",
        [
            "a",
            "b",
            "c",
            "d",
            "e"
        ]
    )
    selector2.to_document()
    let selector3 = Btjs.Selector("title",
        [
            "a",
            "b",
            "c",
            "d",
            "e"
        ]
    )
    selector3.to_document()

}

main()