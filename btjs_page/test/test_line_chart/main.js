

import { Btjs } from "../../btjs/Btjs.js";
import { LineChart } 
    from "../../btjs/mod/LineChart.js";

var line_chart = null

function random_time_line_polygon(
        interval, height) {
    let polygon = []
    let line = []
    let x = 0
    let y = 0
    let balance_y = height / 2
    let restoration_force = 1
    let wave_interval = 2
    let counter_wave_time = 0
    let width = line_chart.get_width()
    for(let i=0; i< width / interval; i++) {
        if(counter_wave_time >= wave_interval) {
            if(Btjs.random_int(0, 1) == 1) {
                y = Btjs.random_int(0, height) 
            }
            counter_wave_time = 0
        }
        counter_wave_time += 1
        if(y > balance_y) {
            y -= restoration_force
        } else if(y < balance_y) {
            y += restoration_force
        }
        line = [x, y]
        x += interval
        polygon.push(line)
    }
    return polygon
}

function draw_chart() {
    line_chart.update()
    let polygon = random_time_line_polygon(
        5, line_chart.get_height()
    )
    line_chart.draw_object_line_array([
        {
            "line": polygon,
            "name": "personas",
            "color": "blue"
        }
    ])
    polygon = random_time_line_polygon(
        5, line_chart.get_height()
    )
    line_chart.draw_object_line_array([
        {
            "line": polygon,
            "name": "animales",
            "color": "red"
        }
    ])
    polygon = random_time_line_polygon(
        5, line_chart.get_height()
    )
    line_chart.draw_object_line_array([
        {
            "line": polygon,
            "name": "edificios",
            "color": "green"
        }
    ])
}

function main() {
    line_chart = new LineChart(
        300, 200
    )
    line_chart.to_document()
    draw_chart()

}

main()