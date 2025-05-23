

import { StandardElement } from "./StandardElement.js"
import { Comment } from "./Comment.js";

export class CommentBox extends StandardElement {

    /*
    Comment json structure:
    {
        "autor":"",
        "text":"",
        "image_url":""
    }
    */

    constructor(json_arr = []) {
        super();
        this.input_text = document
            .createElement("div")
        this.input_text.style.display = "inline"
        this.input_text.setAttribute("tag",
            "comment_box")
        this.comment_arr = []
        this.create_list(json_arr)
    }

    destroy() {
        super.destroy()
        this.comment_arr = []
        this.comment_arr = null
    }

    create_list(json_arr) {
        let json = null
        let comment = null
        this.comment_arr = []
        for(let k in json_arr) {
            json = json_arr[k]
            comment = new Comment(json)
            this.comment_arr.push(comment)
            this.input_text.append(comment.input_text)
        }
    }

}