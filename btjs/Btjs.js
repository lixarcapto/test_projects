


import { OLElement } from "./mod/OlElement.js";
import { OptionElement } from "./mod/OptionElement.js";
import { InputText } from "./mod/InputText.js";
import { Icon } from "./mod/Icon.js";
import { Button } from "./mod/Button.js";
import { ColorSelector } from "./mod/ColorSelector.js";
import { StyleHead } from "./mod/StyleHead.js";
import { Div } from "./mod/Div.js";
import { Link } from "./mod/Link.js";
import { Quote } from "./mod/Quote.js";
import { Article } from "./mod/Article.js";
import { PageTitle } from "./mod/PageTitle.js";
import { Figure } from "./mod/Figure.js";
import { PageStructure } from "./mod/PageStructure.js";
import { References } from "./mod/References.js";
import { VideoFigure } from "./mod/VideoFigure.js";
import { replace_substring } from "./mod/replace_substring.js";

export class Btjs {

  /*
  Todo: Automatizar mas las referencias; 
  que al crear articulos y figuras se
  agreguen automaticamente. Tambien añadir
  numeracion automaticas a las figuras.
  */

    static random_element(array) {
        // Verificamos si el array tiene elementos
        if (array.length === 0) {
          return null; // Si el array está 
          // vacío, retornamos null
        }
    
        // Generamos un índice aleatorio dentro del rango del array
        const indiceAleatorio = Math.floor(Math.random() * array.length);
    
        // Retornamos el elemento en el índice aleatorio
        return array[indiceAleatorio];
    }
  
    static random_probability(probability) {
      let result = Math.floor(Math.random() 
        * (100 - 0 + 1)) + 0;
      console.log("result: " + String(result))
      if(result <= probability) {
        return true
      } else {
        return false
      }
    }

    static random_int(min, max) {
      return Math.floor(Math.random() 
        * (max - min + 1)) + min;
    }

  
    static button(text = "") {
      return new Button(text)
    }

    static ol(text, ARRAY) {
        return new OLElement(text, ARRAY)
    }

    static Div(text = "") {
      return new Div(text)
    }

    static option(text, ARRAY) {
      return new OptionElement(text, 
        ARRAY)
    }

    static input_text(TEXT) {
      return new InputText(TEXT)
    }

    static icon(URL, width, height) {
      return new Icon(URL, width, height)
    }

    static color_selector() {
      return new ColorSelector()
    }

    static style_head() {
      return new StyleHead()
    }

    static Link(text, url) {
      return new Link(text, url)
    }

    static Quote() {
      return new Quote()
    }

    static Article(title, text = "", 
        level = 0) {
      return new Article(title, 
        text, level)
    }

    static Figure(title, range_size, src, 
      description = "") {
        return new Figure(title, range_size,
          src, description)
    }

    static PageTitle(title, subtitle) {
      return new PageTitle(title, subtitle)
    }

    static PageStructure() {
      return new PageStructure()
    }

    static References() {
      return new References()
    }

    static VideoFigure() {
      return new VideoFigure()
    }

    /* 
      Modifica un character indicado por 
      el indice con la funcion enviada.
    */
    static modify_char(texto, 
        indice, FUNCTION) {
      
      const textoEnArreglo = texto.split('');
    
      // Validamos que el índice esté dentro de los límites del texto
      if (indice >= 0 && indice < textoEnArreglo.length) {
        // Reemplazamos el carácter en el índice especificado
        let char = textoEnArreglo[indice];
        textoEnArreglo[indice] = FUNCTION(char)
      } else {
        console.error('Índice fuera de rango');
        return texto; // Retornamos el texto original sin modificaciones
      }
    
      // Unimos el arreglo nuevamente en un string
      return textoEnArreglo.join('');
    }

    /* 
    Funcion que remplaza los saltos de 
    linea por etiquetas BR.
    */
    static replace_jumps(texto) {
      // Expresión regular para encontrar todos los saltos de línea (incluyendo diferentes tipos)
      const regex = /\r\n|\r|\n/g;
      // Reemplazar cada coincidencia con la etiqueta <br>
      const nuevoTexto = texto.replace(regex, '<br>');
      return nuevoTexto;
    }

    static capitalize(texto) {
      // Dividimos el texto en un array de palabras
      const palabras = texto.split(' ');
    
      // Iteramos sobre cada palabra y capitalizamos la primera letra
      const palabrasCapitalizadas = palabras.map(palabra => {
        return palabra.charAt(0).toUpperCase() + palabra.slice(1);
      });
    
      // Unimos las palabras capitalizadas en una nueva cadena
      return palabrasCapitalizadas.join(' ');
    }

    static divide_by_jumps(text) {
      // Expresión regular para encontrar uno o más saltos de línea consecutivos
      const regex = /\n{2,}/g;
      // Dividir el texto por los saltos de línea dobles encontrados
      const array = texto.split(regex);
      return array;
    }

    static divide_by_points(texto) {
      // Dividimos el texto por puntos, incluyendo los puntos al final de las frases
      const partes = texto.split(/\./g);
      // Eliminamos los espacios en 
      //blanco al inicio y final de cada parte
      const array = partes.map(parte => parte.trim());
      return array;
    }

    static delete_substring(cadena, inicio, fin) {
      // Verificamos que los índices sean válidos
      if (inicio < 0 || fin > cadena.length || inicio > fin) {
        return "Índices inválidos";
      }
    
      // Utilizamos slice() para obtener las partes antes y después de la subcadena a eliminar
      const parte1 = cadena.slice(0, inicio);
      const parte2 = cadena.slice(fin);
    
      // Concatenamos las partes para formar la nueva cadena
      return parte1 + parte2;
    }

    static replace_string(primal, string) {
      return primal.replace(
        new RegExp(string, 'g'), 
        '');
    }

    static replace_substring(cadena, 
          substring, interval) {
        return replace_substring(cadena, 
          substring, interval)
    }

    static find_substring(cadena, 
          substring) {
        // Encuentra el índice de la primera aparición del substring
        const indiceInicio = cadena.indexOf(
          substring);
    
        // Si se encontró el substring, 
        // calcula el índice final
        if (indiceInicio !== -1) {
          const indiceFinal = indiceInicio 
            + substring.length - 1;
          return { inicio: indiceInicio, 
            final: indiceFinal };
        } else {
          return null;
        }
    }

}