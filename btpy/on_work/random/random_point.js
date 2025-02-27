



export function random_point(min, max) {
    return [
        Math.floor(Math.random() 
        * (max - min + 1)) + min,
        Math.floor(Math.random() 
        * (max - min + 1)) + min
    ]
}