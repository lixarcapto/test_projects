

import { Btjs } from "../../btjs/Btjs.js";
import { Dice } from "../../btjs/mod/Dice.js";

function main() {
    console.log("test_1")
    let money = 0
    let option_arr = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6"
    ]
    let select = Btjs.Selector("bet", 
        option_arr
    )
    select.to_document()
    let e  = Btjs.Dice(100, 100)
    e.to_document()
    let money_btn = Btjs.ClickIconText(
        "Fichas", 
        "http://localhost/web_projects/btjs_page/res/dollar.png")
    money_btn.to_document()
    e.add_listener(
        (e)=>{
            let v = select.get_value()
            console.log(e)
            if(option_arr[e] == v) {
                console.log("you win")
                money += 1
                money_btn.set_text(
                    "money: " + money + " $")
            }
        }
    )
    
}

main()