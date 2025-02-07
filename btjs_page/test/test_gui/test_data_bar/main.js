

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let e = Btjs.DataBar("text")
    e.to_document()
    e.set_range_arr([0, 200])
    e.set_value(1)
    let value = 0
    let btn = Btjs.Button("work")
    btn.to_document()
    btn.add_click_listener(()=>{
        Btjs.repeat(5, 0.3, ()=>{
            e.set_value(value)
            value +=2
        })
    })
    let btn2 = Btjs.Button("reset")
    btn2.to_document()
    btn2.add_click_listener(()=>{
        e.set_value(0)
        value = 0
    })
}

main()