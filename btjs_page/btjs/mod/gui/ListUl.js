

import { ListStandard } 
    from "./ListStandard.js";

export class ListUl extends ListStandard {

    constructor(text, array) {
        super("ul", text, array);
    }

}