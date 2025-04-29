

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let table = Btjs.Table("titulo")
    table.to_document()
    table.create_first_row(
        ["name", "age", "group"]
    )
    table.add_row(
        ["Juan", "17", "A"]
    )
}

main()