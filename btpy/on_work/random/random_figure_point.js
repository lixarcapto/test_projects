


import { random_point } 
    from "./random_point.js"

export function random_figure_point(size) {
    let point = [0, 0]
    let figure_point = []
    for(let i=0; i< size; i++) {
        point = random_point(0, 500)
        figure_point.push(point)
    }
    return figure_point
}