

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let frame = Btjs.Frame("frame")
    frame.to_document()
    let btn = Btjs.Button("click")
    btn.to_document()
    frame.append(btn)

}

main()