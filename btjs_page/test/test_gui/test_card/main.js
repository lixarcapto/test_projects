

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let e = Btjs.Card("carta",
      "http://localhost/web_projects/btjs_page/res/chica_catolica_mini.png",
      "El vestido azul cielo, ligero y veraniego, parecía flotar alrededor de la joven mientras caminaba por la orilla del mar. La tela, de algodón fresco y vaporoso, se mecía suavemente con la brisa marina, creando un efecto de movimiento y ligereza. El diseño sencillo del vestido, con tirantes finos y una falda que llegaba hasta las rodillas, resaltaba su juventud y su figura esbelta. Su cabello, suelto y alborotado por el viento, enmarcaba un rostro de piel bronceada y ojos alegres, cuyo brillo se intensificaba con el reflejo del sol en el agua. Unas sandalias planas completaban su atuendo, perfecto para un día de verano en la playa."
    )
    e.to_document()

}

main()