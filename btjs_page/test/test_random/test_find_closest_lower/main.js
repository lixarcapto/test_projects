

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let r = Btjs.find_closest_lower_array([
        5, 7, 12, 3, 2, 0
    ], 4)
    console.log(r)
}

main()