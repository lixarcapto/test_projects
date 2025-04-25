

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let field = Btjs.TextField("name")
    field.to_document()
    field.set_placeholder("write a name")

}

main()