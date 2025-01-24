

export class Char {

    constructor(type = "") {
        this.name = ""
        this.attack = 3
        this.defense = 5
        this.life = 30
        this.image_url = "res/camarera.png"
        this.range_life = [0, 50]
        this.money = 0
        this.fabric(type)
    }

    fabric(type) {
        if(type == "") {
            this.name = ""
            this.attack = 3
            this.defense = 5
            this.life = 30
            this.image_url = "res/camarera.png"
            this.range_life = [0, 50]
            this.money = 0
        } else if(type == "princess") {
            this.name = ""
            this.attack = 5
            this.defense = 2
            this.life = 24
            this.image_url = "res/princess_400x400.png"
            this.range_life = [0, 24]
            this.money = 5
        }
    }

    //return json
    capture_render() {
        return {
            "name": this.name,
            "attack": this.attack,
            "defense": this.defense,
            "life": this.life,
            "image_url": this.image_url,
            "money": this.money,
            "range_life": this.range_life
        }
    }

}