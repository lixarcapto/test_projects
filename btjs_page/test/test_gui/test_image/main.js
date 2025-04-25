

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let image = Btjs.Image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Kukulk%C3%A1n_rodeada_de_azul..JPG/800px-Kukulk%C3%A1n_rodeada_de_azul..JPG"
    )
    image.set_size(300, 300)
    image.to_document()
}

main()