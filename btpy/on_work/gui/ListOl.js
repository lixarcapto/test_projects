

import { ListStandard } 
    from "./ListStandard.js";

export class ListOl extends ListStandard {

    constructor(text, array) {
        super("ol", text, array);
    }

}