

import { Btjs } from "../../../btjs/Btjs.js";
import {base64_img} from "./base64_img.js";
import { base64_img_2 } from "./base64_img_2.js";

function main() {
    console.log("test_1")
    let e = Btjs.Book()
    e.to_document()
    e.set_size(300, 400)
    e.set_component_objs_arr([
      {
         "image":base64_img,
         "title": "Maria",
         "description": `
         María, con su uniforme impecable y su sonrisa cálida, se movía con gracia entre las mesas del concurrido restaurante. Su cabello recogido en un moño alto dejaba al descubierto un rostro amable, surcado por las arrugas de la experiencia. Conocía el menú al dedillo y podía recomendarte el vino perfecto para acompañar cada plato. Su trato era cercano y profesional, haciendo sentir a cada cliente como si fuera el único.
         `
     },
     {
      "image":base64_img_2,
      "title": "Ana",
      "description": `
      Ana, nerviosa pero ilusionada, sostenía la bandeja con cuidado mientras se abría paso entre la multitud. Su uniforme, aún un poco grande, reflejaba su juventud y su entusiasmo. Su rostro, enmarcado por un flequillo rebelde, se iluminaba con cada sonrisa que dirigía a los clientes. Aunque a veces se equivocaba al tomar los pedidos, su amabilidad y su disposición a aprender compensaban cualquier error.
      `
  }
    ])

}

main()