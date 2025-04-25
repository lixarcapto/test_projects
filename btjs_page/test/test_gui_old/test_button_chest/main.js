

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    
    let btn = Btjs.ButtonChest("chest")
    btn.to_document()
    btn.set_options_arr(["a", "b", "c"])

}

main()