


import { Char } from "./Char.js"
import { Scenario } from "./Scenario.js"

export class Model {

    constructor() {
        this.scenario = new Scenario()
    }

    __combat() {

    }

    request(request) {
        console.log("request", request)
        let response = {
            "message": "",
            "data": {}
        }
        if(request["message"] == "render") {
            response.data = this
                .scenario.capture_render()
        }
        if(request["message"] == "advance_time") {
            response.data = this
                .scenario.advance_time()
        }
        if(request["message"] == "select_card") {
            this.scenario.select_card(
                request.data, 1)
        }
        return response
    }

}