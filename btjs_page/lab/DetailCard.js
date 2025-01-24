


import { Btjs } from "../btjs/Btjs.js"

export class DetailCard {

    constructor() {
        this.node = document
            .createElement("span")
        this.node.style.border = "1px solid gray"
        //
        this.image = Btjs.Image()
        this.node.append(this.image.node)
        //
        this.table = Btjs.Table("tabla")
        this.node.append(this.table.node)
        //
        Btjs.jump()
        this.bar = Btjs.DataBar("life")
        this.node.append(this.bar.node)
    }

    load_json_data(data) {
        this.bar.set_range_arr(
            data["range_life"])
        this.bar.set_value(data["life"])
        this.image.set_url(data["image_url"])
        this.table.load_matrix_of_rows([
            ["attack", "defense"],
            [data["attack"], data["defense"]]
        ])
    }

}