

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let link = Btjs.Link("Chichen Itza",
        "https://es.wikipedia.org/wiki/Chich%C3%A9n_Itz%C3%A1"
    )
    link.to_document()

}

main()