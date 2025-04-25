



function get_first_key(jsobject_arr) {
    let jsobject = jsobject_arr[0]
    for(let k in jsobject) {
        return k
    }
}

function get_all_first_values(jsobject_arr) {
    let keys_array = []
    let jsobject = null
    let count_key = 0
    for(let i in jsobject_arr) {
        jsobject = jsobject_arr[i]
        for(let k in jsobject) {
            keys_array.push(jsobject[k])
            break
        }
    }
    return keys_array
}

function get_first_row(jsobject_arr) {
    let jsobject = jsobject_arr[0]
    let row_arr = []
    let n = 0
    for(let k in jsobject) {
        if(n != 0) {
            row_arr.push(k)
        }
        n += 1
    }
    return row_arr
}

function get_rows_matrix(jsobject_arr) {
    let rows_matrix = []
    let row_arr = []
    let count_key = 0
    let jsobject = null
    for(let i in jsobject_arr) {
        jsobject = jsobject_arr[i]
        row_arr = []
        for(let k in jsobject) {
            if(count_key != 0) {
                row_arr.push(jsobject[k])
            }
            count_key += 1
        }
        count_key = 0
        rows_matrix.push(row_arr)
    }
    return rows_matrix
}

/*
Función que convierte un excel de lista 
de diccionarios en un Excel de 
diccionario de filas. Corrige las 
primeras filas desordenadas durante 
la conversión.
*/
export function dict_xlsx_to_row_list(
        jsobject_arr) {
    let keys_array = []
    let values_arr = get_all_first_values(
            jsobject_arr)
    let first_key = get_first_key(
        jsobject_arr)
    keys_array = keys_array.concat(
        values_arr)
    let row_dict = {}
    let rows_matrix = get_rows_matrix(
        jsobject_arr)
    let first_row = get_first_row(
        jsobject_arr)
    for(let i in keys_array) {
        if(i == 0) {
            row_dict[keys_array[i]]
                = first_row
            continue;
        }
        row_dict[keys_array[i]]
            = rows_matrix[i]
    }
    //añade la primera fila rota
    row_dict[first_key] = first_row
    return row_dict
}