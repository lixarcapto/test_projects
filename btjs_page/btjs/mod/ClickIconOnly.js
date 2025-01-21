



import { ClickIcon } from "./ClickIcon.js";

export class ClickIconOnly extends ClickIcon {

    constructor(title, url) {
        super(title, url);
        this.set_text(title)
    }

    set_text(text) {
        this.set_text_bubble(text)
        this.img.alt = text
    }

}