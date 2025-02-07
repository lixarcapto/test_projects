


export function repeat(NUMBER, SECONDS, 
        CALLBACK) {
    // Convierte el intervalo a milisegundos
    // Ejecuta la tarea inicialmente
    CALLBACK();
    let n = 1
    // Luego, ejecuta la tarea repetidamente cada x segundos
    let inverval = setInterval(()=>{
        n += 1;
        if(n >= NUMBER) {
            clearInterval(inverval)
        }
        CALLBACK()
    }, SECONDS * 1000);
}