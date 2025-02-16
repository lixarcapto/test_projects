



export function random_range(min, max) {
    let max_for_min = max -1
    let min_result = Math.floor(Math.random() 
        * (max_for_min - min + 1)) + min
    let max_result = Math.floor(Math.random() 
        * (max - min_result + 1)) + min_result
    return [
        min_result,
        max_result
    ]
}