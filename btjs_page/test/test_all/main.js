

import { Btjs } from "../../btjs/Btjs.js";
import { is_byte127 } from "../../btjs/mod/is_byte_256.js";

function main() {
    let n = Btjs.LimitNumber(5, [0, 10])
    n.set(16)
    console.log(n.reach_max())
    console.log(n.reach_min())
}

main()