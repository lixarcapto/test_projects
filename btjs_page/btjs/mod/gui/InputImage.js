


import { InputFile } from "./InputFile.js";

export class InputImage extends InputFile {

    constructor(title) {
        super(title)
        this.set_file_type("image/*")
    }

    /*
    Esta función retorna una URL de la 
    imagen seleccionada por el usuario; 
    pero para recibir la URL se debe 
    enviar una callback de resultado 
    que reciba la URL como argumento 
    el almacén en una variable de 
    ámbito global o de clase estatico.
    */
    get_value(RESULT_CALLBACK) {
        let file = this.input.files[0];
        const reader = new FileReader();
        reader.onload = (e) => {
            RESULT_CALLBACK(
                e.target.result)
        };
        reader.readAsDataURL(file);
    }

}