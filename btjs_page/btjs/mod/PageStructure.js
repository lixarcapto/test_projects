


import { TitleBar } from "./TitleBar.js";
import { References } from "./References.js";

export class PageStructure {

    constructor() {
        this.title = new TitleBar(
            "Web Page", "None Title"
        )
        this.intro = document
            .createElement("section")
        this.intro.setAttribute("tag",
            "intro")
        this.main = document
            .createElement("section")
        this.main.setAttribute("tag",
            "main")
        this.references = References
        document.body.append(this.title.node)
        document.body.append(this.intro)
        document.body.append(this.main)
        document.body.append(
            this.references.node)
    }

    add(element) {
        if (element instanceof Node) {
            this.main.append(element)
        } else {
            this.main.append(element.node)
        }
    }

}