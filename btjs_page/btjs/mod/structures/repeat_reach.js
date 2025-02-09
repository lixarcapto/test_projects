


/*
    Esta funcion sirve para ejecutar
    una callback cada determinados segundos;
    la callback debe recibir un numero que 
    es un contador de repeticiones; y si 
    retorna true se detiene.

    repeat_each(seconds, (n)=>{
        return true    
    })
*/

export function repeat_each(SECONDS, 
        CALLBACK) {
    let was_finished = false
    let n = 1
    CALLBACK(n);
    let inverval = setInterval(()=>{
        was_finished = CALLBACK(n)
        if(was_finished) {
            clearInterval(inverval)
        }
        n += 1
    }, SECONDS * 1000);
}