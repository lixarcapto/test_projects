




export function replace_substring(cadena, 
    substring, interval) {
        // Verificamos que los índices 
        //sean válidos
      if (inicio < 0 || fin > cadena.length || inicio > fin) {
        return "Índices inválidos";
      }
    
      // Utilizamos slice() para obtener 
      //las partes antes y después de la 
      //subcadena a eliminar
      const parte1 = cadena.slice(0, 
            interval[0]);
      const parte2 = cadena.slice(interval[1]);
    
      // Concatenamos las partes para formar la nueva cadena
      return parte1 + substring + parte2;
}