

import { Btjs } from "../../../btjs/Btjs.js";

function main() {
    let canvas = document.createElement(
        "canvas")
    canvas.id = "canvas_a"
    canvas.width = 400
    canvas.height = 400
    let ctx = canvas.getContext('2d');
    canvas.setAttribute("style", 
        `
        position: absolute;
        background-color: black;
        `
    )
    document.body.append(canvas)
    // Crear el canvas "fuera de pantalla" (buffer)
    let buffer = document.createElement(
        'canvas');
    buffer.id = "canvas_b"
    buffer.width = canvas.width;
    buffer.height = canvas.height;
    buffer.setAttribute("style", 
        `
        position: absolute;
        background-color: black;
        `
    )
    document.body.append(buffer)
    let bufferCtx = buffer.getContext('2d');
    let point = [0, 0]
    let counter_draw = 0
    //
    function swapp_canvas() {
        let canvas_temp = canvas
        let buffer_temp = buffer
        canvas = buffer_temp
        buffer = canvas_temp
        bufferCtx = buffer.getContext('2d');
        ctx = canvas.getContext('2d');
        canvas.style.visibility
                = "visible"
        buffer.style.visibility
                = "hidden"
    }
    function dibujar() {
        // Limpiar el buffer
        bufferCtx.fillStyle = 'black';
        bufferCtx.fillRect(0, 0, 
            canvas.width, canvas.height);
        console.log(counter_draw)
        counter_draw += 1
        // Dibujar elementos en bufferCtx (ejemplo)
        bufferCtx.fillStyle = 'blue';
        bufferCtx.fillRect(point[0], 
            point[1], 100, 50);
        console.log(
            "buffer_canvas", buffer.id,
            "canvas", canvas.id
        )
        point[1] += 5
        // Copiar el buffer al canvas visible
        // Solicitar el siguiente frame 
        // de animación
        //requestAnimationFrame(dibujar);
        swapp_canvas()
    }

    Btjs.repeat_each(0.4, (n)=>{
        dibujar()
    })

}

main()