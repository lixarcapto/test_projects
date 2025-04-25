

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let swiper_list = []
    let swiper = null
    for(let i=0;i<12;i++) {
        swiper = Btjs.SwiperText(
            "swipper_text",
            ["perro", "gato", "raton"]
        );
        swiper.to_document()
    }
}

main()