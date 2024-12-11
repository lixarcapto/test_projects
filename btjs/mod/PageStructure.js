


import { PageTitle } from "./PageTitle.js"
import { References } from "./References.js"

export class PageStructure {

    constructor() {
        this.title = new PageTitle(
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

}