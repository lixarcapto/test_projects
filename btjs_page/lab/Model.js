


import { Char } from "./Char.js"
import { Battle } from "./Battle.js"

export class Model {

    constructor() {
        this.battle = new Battle()
    }

    __combat() {

    }

    request(request) {
        let response = {
            "message": "",
            "data": {}
        }
        if(request["message"] == "render") {
            response.data = this
                .battle.capture_render()
        }
        if(request["message"] == "advance_time") {
            response.data = this
                .battle.advance_time()
        }
        return response
    }

}