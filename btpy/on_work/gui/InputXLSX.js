


import { InputFile } from "./InputFile.js";
import { dict_xlsx_to_row_list } 
    from "./dict_xlsx_to_row_list.js";

export class InputXLSX extends InputFile {

    static  {
        let script_import = document
            .createElement("script")
        script_import.src 
            = "https://cdn.sheetjs.com/xlsx-latest/package/dist/xlsx.full.min.js"
        document.body.append(script_import)
    }

    constructor(title) {
        super(title)
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
    get_value_row_dict(RESULT_CALLBACK) {
        let file = this.input.files[0];
        const reader = new FileReader();
        reader.onload = (e) => {
            const file = e.target.result;
            const workbook = XLSX.read(file, { type: 'binary' });
            const sheetName = workbook.SheetNames[0];
            const worksheet = workbook.Sheets[sheetName];
            let data = XLSX.utils.sheet_to_json(worksheet);
            data = dict_xlsx_to_row_list(
                data)
            RESULT_CALLBACK(data)
        };
        reader.readAsBinaryString(file);
    }

    get_value_dict_list(RESULT_CALLBACK) {
        let file = this.input.files[0];
        const reader = new FileReader();
        reader.onload = (e) => {
            const file = e.target.result;
            const workbook = XLSX.read(file, { type: 'binary' });
            const sheetName = workbook.SheetNames[0];
            const worksheet = workbook.Sheets[sheetName];
            let data = XLSX.utils.sheet_to_json(worksheet);
            RESULT_CALLBACK(data)
        };
        reader.readAsBinaryString(file);
    }

}