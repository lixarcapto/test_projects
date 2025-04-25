

import {Canvas} from "./Canvas.js";
import { StandardElement } from "./StandardElement.js";

export class Dice extends StandardElement {

    /*
    Es un componente que representa un 
    dado que se lanza y gira al azar 
    hasta detenerse creando un número 
    aleatorio al mismo tiempo que muestra 
    una animación.
    */

    constructor(size_x, size_y) {
        super("button")
        this.canvas = new Canvas(
            size_x, size_y)
        this.node.setAttribute("style",
            `
            padding: 0px;
            `
        )
        this.append(this.canvas)
        this.cicles = 0
        this.image_array = []
        this.deceleration = 0.2
        this.init_speed = 0.2
        this.index = 0
        this.callback = ()=>{}
        this.limit_speed = 4
        this.speed = 0
        this.interval = null
        this.node.addEventListener("click",
            ()=>{
                this.react_to_bet()
            }
        )
        this.set_content_img_arr(
            this.get_default_images_arr())
    }

    get_value() {
        return this.index
    }

    set_value(value) {
        this.index = value
        this.update()
    }

    /*
    Permite añadir un listener al evento
    de finalizar el tiro de los dados; 
    la callback enviada debe recibir el
    index de la imagen del dado final.
    */
    add_listener(callback) {
        this.callback = callback
    }

    random_int(min, max) {
        // Verifica si los argumentos son números y si min es menor o igual que max
        if (typeof min !== 'number' || typeof max !== 'number' || min > max) {
          return "Argumentos inválidos. Debe proporcionar dos números enteros donde min sea menor o igual que max.";
        }
      
        // Genera un número aleatorio entre 0 (inclusivo) y 1 (exclusivo)
        const numeroAleatorio = Math.random();
      
        // Escala el número aleatorio al rango deseado (max - min + 1) y lo desplaza al valor mínimo (min)
        const enteroAleatorio = Math.floor(numeroAleatorio * (max - min + 1)) + min;
      
        return enteroAleatorio;
      }

    react_to_bet() {
        this.node.disabled = true
        this.cicles = 0
        this.speed = this.init_speed
        this.interval = setInterval(() => {
            this.change_image()
        }, 1000 * this.speed);
    }

    set_content_img_arr(image_array) {
        this.image_array = image_array
        this.update()
    }

    update() {
        this.canvas.clear()
        this.canvas.draw_image(
            this.image_array[this.index], 
            0, 0
        )
    }

    change_image() {
        let leng = this.image_array.length
        if(this.speed <= this.limit_speed) {
            this.speed += this.deceleration
            this.index = this.random_int(
                0, leng -1)
            this.cicles += 1
            this.update()
        } else {
            clearInterval(this.interval)
            this.node.disabled = false
            this.callback(this.get_value())
        }
    }

    //return string array
    get_default_images_arr() {
        return [
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAFNSURBVHhe7dExTgUxFATBvf+lIbfEZx3Rg6qklzgauZ8vUp7zgb8lSIwgMYLECBIjSIwgMYLECBIjSIwgMYLECBIjSIwgMYLECBIjSIwgMYLECBIjSIwgMYLECBIjSIwgMYLECBIjSIwgMYLECBIjSIwgMYLECBIjSMxskOd5frxlc+vPz/90i6ZWnx/+5tZMLT4/+82tmVl8fvTNLZlZe37yzS2ZWXt+8s0tmVl7fvLNLZlZe37yzS2ZWXt+8s0tmVl7fvLNLZlae370m1sztfj87De3Zm7x+eGfbtHm6l/CLNte/w8JEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEiNIjCAxgsQIEvMNBrdr+8keDi0AAAAASUVORK5CYII=",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAGHaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyI+PHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj48dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPjwvcmRmOkRlc2NyaXB0aW9uPjwvcmRmOlJERj48L3g6eG1wbWV0YT4NCjw/eHBhY2tldCBlbmQ9J3cnPz4slJgLAAABfElEQVR4Xu3awQrDIBAA0dj//2d7ag8epC7sdpKddwxKQkYEQ8acc17CeK0X9F8GgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMQWBGxU8OY4z10lfB7W8lNcguxCrxMW4lbcs6iXEFxj9VWhDFpASJrvbovCdJCaI4g8AYBMYgMAaBMQhMSpDoqTs670lSgiguLcjpaj8d/1SpHxc/difwgtvfSkkQ/S5ty1KMQWAMAmMQGIPAGATGIDAGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMQWD8lRT273HrILsQq6rX1HbLOolxBcZHtQ1C1TJIdLVH551oGYTMIDAGgTEIjEFgWgapOuRFtAwSVRGybZDTl3s6Pqr1t6yP3YGv+vUYBKbtlkVlEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMQWAMAmMQGIPAGATGIDAGgXkDDfpOnKZQQloAAAAASUVORK5CYII=",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAGHaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyI+PHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj48dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPjwvcmRmOkRlc2NyaXB0aW9uPjwvcmRmOlJERj48L3g6eG1wbWV0YT4NCjw/eHBhY2tldCBlbmQ9J3cnPz4slJgLAAABt0lEQVR4Xu3ZwW6DMBAAUdP//2d6iSqVA+C1HWbZecfIVpQdQAG2fd/3Joyf4wd6lkFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaB2Va9oNq27fjRP4u+Nr0lZ8hVjHZzTUXTg/QMumdtFVODRAYc2fNm04KMDHZk79tMC6I5DAJjEBiDwBgExiAwBoGZFmTk2dTI3reZFqQFBxvZ82ZTg7TOAfesrWJ6kHZz0HfWVLTsfYhilpwhijMIjEFgDAJjEBiDwBgEJuV9yNU7+IQ/6U+6M+QqRvusubOOKE2QyJB71xOkCVJFiiAjR/rI3iekCFKJQWAMAmMQGIPAGAQmRZCRRyEje5+QIkglaYJEjvTInqf5tBcmZZA3S3PJqsIgMAaBMQiMQWAMAuPf3oOze5xvjMogH2chjlaOzEtWZ4wWWN/DIDDlg0SP9ui+K+WD0BgExiAwBoExCIxBYMoHid51R/ddKR+ExiCBo713fQ8fLh6c3YF/Y1QGgfGSBWMQGIPAGATGIDAGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgML/r82qjf5XzcQAAAABJRU5ErkJggg==",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAGHaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyI+PHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj48dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPjwvcmRmOkRlc2NyaXB0aW9uPjwvcmRmOlJERj48L3g6eG1wbWV0YT4NCjw/eHBhY2tldCBlbmQ9J3cnPz4slJgLAAAB4ElEQVR4Xu3bwW7DIBAAUdP//2f3FCnxwbALS8fpvGMEYp2JXMVt23me5yGMn+sL+lsGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBKZV/YKqtXZ96UPRsY9XEqQX46Xg6LTezLtmXX7L6l3Yu8jaSiNzjKxZYWmQzNCZPStFzo+szVoWZGbYmb0zMudm9kQsC6I1DAJjEBiDwBgExiAwBoFZFmTm0cLM3hmZczN7IpYFOZLDZvasFDk/sjZraZAjOHRkbaWROUbWrFDytPcYeMRQdOzjlQVRzvJbluYYBMYgMAaBMQiMQWAMAmMQGIPAGATGIDAGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMf/1+cfdvFDveqi1B7i7y2HShPb0Z31XOW37LGrnQ1trQuirRs6PrI8qCZN7k6PpvVBbkKbIfguy+npIgM8PO7P0GJUGUZxAYg8AYBMYgMP8+SPZbd3ZfT0mQmWFn9n6DkiBPE/0QRNdHlD5cjH7JKxxl2N3MO+YrDfJyd5HHpgt9ii1BNM6fITAGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMQWB+Ab8DfKkB3kyCAAAAAElFTkSuQmCC",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAGHaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyI+PHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj48dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPjwvcmRmOkRlc2NyaXB0aW9uPjwvcmRmOlJERj48L3g6eG1wbWV0YT4NCjw/eHBhY2tldCBlbmQ9J3cnPz4slJgLAAACDklEQVR4Xu3awVKEMBAAUfD//xkvbtW6h01mkoEO9DtaSTFsIwq6H8dxbML4+fyCrmUQGIPAGATGIDAGgTEIjEFgDAJjEBiDwBgExiAwBoExCIxBYPaqP1Dt+/75pX+KDru8kiCtGC8Fh05rzXzWrNNvWa0TexdZW6lnjp41M0wNkhk6s2emyPEja7OmBRkZdmTviMxxM3sipgXRHAaBMQiMQWAMAmMQGIPATAsy8mphZO+IzHEzeyKmBdmSw2b2zBQ5fmRt1tQgW3DoyNpKPXP0rJmh5G3v1vGKoeiwyysLopzptyyNMQiMQWAMAmMQGIPAGARmyeeQOz90Lvcd0oqx/a3pWUe0TJDMhxxdT7BMkKdYIsjIlT6y9wpLBHkSg8AYBMYgMAaBMQjMEkFGXoWM7L3CEkGeZJkgmSs9s+dqvu2FWTLInS1zy3oKg8AYBMYgMAaBMQiMv/Z++PaMc8ZHdUqQbye5nXSiLa0Z31XOW37L6jnRzH+UzBQ9dnR9RFmQzIccXX9HZUFWkb0IsvtaSoKMDDuy9w5KgijPIDAGgTEIjEFgHh8k+9Sd3ddSEmRk2JG9d1ASZDXRiyC6PqL05WL0Ia9wlG7fZj5jvtIgL99OcjvpRFdxShD182cIjEFgDAJjEBiDwBgExiAwBoExCIxBYAwCYxAYg8AYBMYgMAaBMQiMQWAMAmMQmF/GMJqmoCEOkwAAAABJRU5ErkJggg==",
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAGHaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49J++7vycgaWQ9J1c1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCc/Pg0KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyI+PHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIj48dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPjwvcmRmOkRlc2NyaXB0aW9uPjwvcmRmOlJERj48L3g6eG1wbWV0YT4NCjw/eHBhY2tldCBlbmQ9J3cnPz4slJgLAAACIUlEQVR4Xu3Z0W6DMBBEUbv//8/0KVKEqJ1d75ghvecxssWaG1GF9uM4jgYbP+cPcC+CmCGIGYKYIYgZgpghiBmCmCGIGYKYIYgZgpghiBmCmCGImc7/Q6713s8ftdZaU98uSZC/DtM2HGjVaPZ3qnOUBvn0ME14oBWR+ZvoDGV/Q6KHia7/L8qCPF3mC5LZM1MSJDtYdt83KwmCOgQxQxAzBDFDEDMlQRQ/kHbLnCGzZ6YkSJbiQE9XFiR6c6Prd4jMFFkbUfou62X0g09wOYm7ziAJgryyRxZqEMQMQcwQxAxBzBDEDEHMEMQMQcwQxAxBzBDEDEHMSN/23vUKe9Vo7iaeXRJkdqB3gsunReZuotnLH1nRQ0XXq2TmyOyZKQ+CNaVBst+Y7L4qK9df2XulNAjWEcQMQcwQxAxBzJQGUfxQ2mFl7pW9V0qDZFUf6snKg0RvbnS9SmaOzJ4Zybusl9GPJuFll43mbuLZpUEQV/7IwhqCmCGIGYKYIYgZgpghiBmCmCGIGYKY4dXJwOidluq2bQlyx8FWjOY9q55f+sjqvU8P98kaZ9Wzy4JEB42uV7l7DlmQJ8rGyO67IgmSHTC775tIgiCPIGYIYoYgZghihiBmJEGyrxOy+6pkr5/dd0USBHmyINFvTXS9SnSO6PoZ3vYO3DH3liD4nOyRhRyCmCGIGYKYIYgZgpghiBmCmCGIGYKYIYgZgpghiJlfpEy2iaBASS8AAAAASUVORK5CYII="
        ]
    }

}