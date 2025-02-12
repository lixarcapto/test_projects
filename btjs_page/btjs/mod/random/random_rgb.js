



/*
Genera un RGB array aleatorio; en el 
argumento se puede enviar un array RGB
con los limites para cada color.
*/
//return RGB array
export function random_rgb(
        rgb_limit = [256, 256, 256]) {
    return [
        Math.floor(Math.random() 
        * (rgb_limit[0] - 0 + 1)) + 0,
        Math.floor(Math.random() 
        * (rgb_limit[1] - 0 + 1)) + 0,
        Math.floor(Math.random() 
        * (rgb_limit[2] - 0 + 1)) + 0
    ]
}