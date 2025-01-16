


import { Btjs } from "./btjs/Btjs.js"
import { Gauge } from "./btjs/mod/Gauge.js"

function main() {
    let gauge = new Gauge()
    let angle = 0
    Btjs.to_body(gauge)
    const intervalo = setInterval(
        ()=>{
            angle += 5
            gauge.set_range([angle, 100])
        }, 500);
    let btn = Btjs.Button("text")
    Btjs.to_body(btn)
}

main()