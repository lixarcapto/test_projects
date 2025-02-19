

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let check = Btjs.CheckBoxTicket(
        "work it")
    check.to_document()
    check.add_checkbox_list([
        "blue", "red", "green", "yellow"
    ])
    let press = Btjs.Button("click")
    press.to_document()
    press.add_click_listener(()=>{
      let v = check.get_value()
      label.set_text(v)
    })
    let label = Btjs.Label("")
    label.to_document()
}

main()