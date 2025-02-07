





//CHECKERS -----------------------------------

import { in_range } 
  from "./mod/checkers/in_range.js";
import { are_all_same } 
  from "./mod/structures/are_all_same.js";
import { is_null_return } 
  from "./mod/checkers/is_null_return.js";
import { is_byte127 } 
  from "./mod/checkers/is_byte_256.js";
import { is_byte256 } 
  from "./mod/checkers/is_byte_256.js";
import { is_RGB } 
  from "./mod/checkers/is_rgb.js";
import { is_RGBA } 
  from "./mod/checkers/is_rgb.js";
import { is_point_2d } 
  from "./mod/checkers/is_point.js";
import { is_point_3d } 
  from "./mod/checkers/is_point.js";
import { is_object_js } 
  from "./mod/checkers/is_object_js.js";

//-----------------------------------------

// GUI -----------------------------------

import { ListOl } from "./mod/gui/ListOl.js";
import { ListUl } from "./mod/gui/ListUl.js";
import { Selector } from "./mod/gui/Selector.js";
import { TextArea } from "./mod/gui/TextArea.js";
import { Button } from "./mod/gui/Button.js";
import { ColorSelector } from "./mod/gui/ColorSelector.js";
import { Body } from "./mod/gui/Body.js";
import { LabelArea } from "./mod/gui/LabelArea.js";
import { Link } from "./mod/gui/Link.js";
import { Quote } from "./mod/gui/Quote.js";
import { Article } from "./mod/gui/Article.js";
import { TitleBar } from "./mod/gui/TitleBar.js";
import { Card } from "./mod/gui/Card.js";
import { PageStructure } from "./mod/gui/PageStructure.js";
import { References } from "./mod/gui/References.js";
import { VideoFigure } from "./mod/gui/VideoFigure.js";
import {Image} from "./mod/gui/Image.js";
import { CheckBoxTicket } from "./mod/gui/CheckBoxTicket.js";
import { InputList } from "./mod/gui/InputList.js";
import { ClickIconBox } from "./mod/gui/ClickIconBox.js";
import { ClickTextBox } from "./mod/gui/ClickTextBox.js";
import { InputSlider } from "./mod/gui/InputSlider.js";
import { DataBar } from "./mod/gui/DataBar.js";
import { RadioButtonList } from "./mod/gui/RadioButtonList.js";
import { CommentBox } from "./mod/gui/CommentBox.js";
import { ButtonList } from "./mod/gui/ButtonList.js";
import { SwipperNumber } from "./mod/gui/SwipperNumber.js";
import { CheckButton } from "./mod/gui/CheckButton.js";
import { Canvas } from "./mod/gui/Canvas.js";
import { ScrollList } from "./mod/gui/ScrollList.js";
import { ChangeColorButton } from "./mod/gui/ChangeColorButton.js";
import {Book } from "./mod/gui/Book.js";
import { Gauge } from "./mod/gui/Gauge.js";
import { BookMenu } from "./mod/gui/BookMenu.js";
import { ButtonChest } from "./mod/gui/ButtonChest.js";
import { ClickIconText } from "./mod/gui/ClickIconText.js";
import { ClickIconTextOverlay } from "./mod/gui/ClickIconTextOverlay.js";
import { ClickIconOnly} from "./mod/gui/ClickIconOnly.js";
import { IconChart } from "./mod/gui/IconChart.js";
import {BarChart} from "./mod/gui/BarChart.js";
import { TextField } from "./mod/gui/TextField.js"; 
import { Table } from "./mod/gui/Table.js";
import { Sign } from "./mod/gui/Sign.js";
import { InnerStyle } from "./mod/gui/InnerStyle.js";
import {Label} from "./mod/gui/Label.js";
import { Frame } from "./mod/gui/Frame.js";
import { Dice } from "./mod/gui/Dice.js";
import { SwipperText } from "./mod/gui/SwipperText.js";

//-------------------------------------------

// DATA TYPES -------------------------------

import { LimitNumber } 
  from "./mod/data_types/LimitNumber.js";
import { IteratorMatrix2D } 
  from "./mod/data_types/IteratorMatrix2D.js";

//------------------------------------------

// STRUCTURES -------------------------------

import { clean_voids } 
  from "./mod/structures/clean_voids.js";
import { count } from "./mod/structures/count.js";

import { create_array } 
  from "./mod/structures/create_array.js";
import { find_value } 
  from "./mod/structures/find_value.js";
import { fit_list } 
  from "./mod/structures/fit_list.js";
import { join_jsobject } 
  from "./mod/structures/join_jsobject.js";
import { map2 } from "./mod/structures/map2.js";
import { repeat } from "./mod/structures/repeat.js";
import { min_in_dict } 
  from "./mod/structures/min_in_dict.js";
import { max_in_dict } 
  from "./mod/structures/max_in_dict.js";

//-----------------------------------------

// STRING -------------------------------

import { replace_substring } from "./mod/string/replace_substring.js";
import { delete_substring } 
  from "./mod/string/delete_substring.js";
import { has_substring } 
  from "./mod/string/has_substring.js";

//---------------------------------------

// RANDOM ----------------------------------

import { random_string } 
  from "./mod/random/random_string.js";

//-------------------------------------------

// CONVERTERS --------------------------

import { array_to_jsobject } 
  from "./mod/converters/array_to_jsobject.js";

//-----------------------------------------

export class Btjs {

  /*
  Todo: Automatizar mas las referencias; 
  que al crear articulos y figuras se
  agreguen automaticamente. Tambien añadir
  numeracion automaticas a las figuras.
  */

    body = null

    static {
        Btjs.body = Btjs.StyleHead()
    }

    //CHECKERS -----------------------------

    /*
    This function checks if the elements 
    of the passed array are all equal.
    */
    static are_all_same(array) {
      return are_all_same(array);
    }

    /*
    Function to identify if the input 
    number is contained within the 
    sending range.
    */
    static in_range(number, range_arr) {
      return in_range(number, range_arr);
    }

    /*
    Function that tests whether a value
    is a return error such as -1, undefined,
    none, void string, void dict, or void
    array
    */
    static is_null_return(data) {
      return is_null_return(data);
    }

    static is_byte127(data) {
      return is_byte127(data);
    }

    static is_byte256(data) {
      return is_byte256(data);
    }
    
    static is_RGB(data) {
      return is_RGB(data);
    }

    static is_RGBA(data) {
      return is_RGBA(data);
    }

    static is_float(data) {
      return data % 1 !== 0;
    }

    static is_array(data) {
      return Array.isArray(data)
    }

    static is_integer(data) {
      return Number.isInteger(data)
    }

    static is_string(data) {
      return typeof valor === 'string';
    }

    static is_object_js(data) {
      return is_object_js(data);
    }

    static is_function(data) {
      return typeof data == "function";
    }

    static is_map(data) {
      return data instanceof Map;
    }

    /*
    Función que verifica  el dato 
    enviado es un punto 2D
    */
    static is_point_2d(data) {
      return is_point_2d(data);
    }

    /*
    Función que verifica  el dato 
    enviado es un punto 3D
    */
    static is_point_3d(data) {
      return is_point_3d(data);
    }



    //------------------------------------
    // Array bucles ------------------------

    /*
    Funcion que convierte dos arrays en 
    un objeto javascript usando como claves
    el primer array y como valores el 
    segundo.
    */
    static array_to_jsobject(key_arr, values_arr) {
      return array_to_jsobject(key_arr, 
        values_arr);
    }


    /*
    Función que crea un nuevo array
    eliminando todos los valores 
    None y void
    */
    static clean_voids(ARRAY) {
      return clean_voids(ARRAY);
    }

    /*
    Funcion que cuenta el numero de 
    verificaciones con una funcion 
    checker enviada en un array o jsobject.
    Envia un lambda con esta estructura:
        (e)=>{return e == condicion};
    */
    static count(STRUCTURE, CHECKER) { 
      return count(STRUCTURE, CHECKER);
    }

    static create_array(SIZE, 
      DATA = null) {
        return create_array(SIZE, DATA);
    }

    static repeat(NUMBER, SECONDS, CALLBACK) {
      return repeat(NUMBER, SECONDS,
          CALLBACK)
    }

    static jsobject_to_map(jsobject) {
      return new Map(
        Object.entries(jsobject));
    }

    static map_to_jsobject(map) {
      return map.fromEntries()
    }

    static find_value(jsobject) {
      return find_value(jsobject)
    }

    static fit_list(ARRAY, SIZE, 
      DEFAULT_VALUE = null) {
        return fit_list(ARRAY, SIZE, 
          DEFAULT_VALUE);
    }

    static join_jsobject(jsobject_1, 
          jsobject_2) {
        return join_jsobject(jsobject_1, 
          jsobject_2);
    }

    /*
    Funcion que aplica un map a una 
    estructura que puede ser un array, 
    un map o un objeto javascript.
    */
    static map2(DATA, FUNCTION) {
      return map2(DATA, FUNCTION);
    }

    static min_in_dict(JSOBJECT) {
      return min_in_dict(JSOBJECT)
    }

    static max_in_dict(JSOBJECT) {
      return max_in_dict(JSOBJECT)
    }

    //------------------------------------
    // STRING ------------------------------

    /*
    Verifica si existe un sustin dentro 
    de otro String ignorando las mayúsculas
    */
    static has_substring(STRING, 
          SUBSTRING) {
        return has_substring(STRING, 
          SUBSTRING)
    }

    static random_string(SIZE, 
      CHAR_STRING = null) {
        return random_string(SIZE, 
          CHAR_STRING)
    }

    /*
    Elimina un String de un String enviado
    */
    static delete_substring(STRING, 
          SUBSTRING) {
        return delete_substring(STRING, 
          SUBSTRING)
    }

    //------------------------------------

    //traspasando de BTPY.
    // SEGUIR EN BTPY_LIST DESDE 
    // MAX_DICT

    static ClickIconText(title, url) {
        return new ClickIconText(title, url);
    }

    static ClickIconTextOverlay(title, url) {
        return new ClickIconTextOverlay(title, 
          url);
    }

    static random_figure_point(size) {
      let point = [0, 0]
      let figure_point = []
      for(let i=0; i< size; i++) {
          point = Btjs.random_point(0, 500)
          figure_point.push(point)
      }
      return figure_point
    }

    static random_point(min, max) {
        return [
          Btjs.random_int(min, max),
          Btjs.random_int(min, max)
        ]
    }

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

    /*
    Iterador para navegar atraves de 
    matrizes de datos de dos dimensiones.
    Las principales funcione son:
    * get: obtiene el actual elemento.
    * set: modifica el actual elemento.
    * next: avansa al siguiente elemento.
    */
    static IteratorMatrix2D(matrix2d) {
      new IteratorMatrix2D(matrix2d)
    }

  
    static Button(text = "") {
      return new Button(text)
    }

    static Sign(text, width, height) {
      return new Sign(text, width, height)
    }

    static Table(title) {
      return new Table(title)
    }

    static IconChart(title) {
      return new IconChart(title)
    }

    static InnerStyle(class_code, 
        pseudoclass = "") {
      return new InnerStyle(class_code, 
          pseudoclass)
    }

    static Dice(size_x, size_y) {
      return new Dice(size_x, size_y)
    }

    static TextField(title) {
      return new TextField(title)
    }

    static BarChart(title) {
      return new BarChart(title)
    }

    static ClickIconOnly(title, url) {
      return new ClickIconOnly(title, url)
    }

    static BookMenu(text = "") {
      return new BookMenu(text)
    }

    static jump(number = 1) {
      let e = null
      for(let i=0;i< number; i++) {
        e = document.createElement("br")
        document.body.append(e)
      }
    }

    static to_body(widget_btjs) {
      document.body.append(widget_btjs.node)
    }

    static ListOl(text, ARRAY) {
      return new ListOl(text, ARRAY)
  }

  static ListUl(text, ARRAY) {
    return new ListUl(text, ARRAY)
}

    static LabelArea(text = "") {
      return new LabelArea(text)
    }

    static Gauge(text = "") {
      return new Gauge(text)
    }

    static Selector(text, ARRAY = []) {
      return new Selector(text, 
        ARRAY)
    }
    
    static Frame() {
      return new Frame()
    }
    
    static ButtonChest(title) {
      return new ButtonChest(title)
    }

    static Book() {
      return new Book()
    }

    static TextArea(key, text) {
      return new TextArea(key, text)
    }

    static color_selector() {
      return new ColorSelector()
    }

    static ChangeColorButton(text) {
      return new ChangeColorButton(text)
    }

    static StyleHead() {
      return new Body()
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

    static Card(title, src, 
      description = "") {
        return new Card(title,
          src, description)
    }

    static TitleBar(title) {
      return new TitleBar(title)
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

    static Label(text = "") {
      return new Label(text)
    }

    static Image(url) {
      return new Image(url)
    }

    static CheckBoxTicket(title, text_arr) {
      return new CheckBoxTicket(title, text_arr)
    }

    static InputList(text_arr) {
      return new InputList(text_arr)
    }

    static ClickTextBox(title, key_arr) {
      return new ClickTextBox(title,
         key_arr)
    }

    static ClickIconBox(title, key_arr) {
      return new ClickIconBox(title,
         key_arr)
    }

    static InputSlider(title, range_arr, 
          value) {
      return new InputSlider(title, 
          range_arr, value)
    }

    static DataBar(title) {
      return new DataBar(title)
    }

    static LimitNumber(range_arr, 
        number = -1) {
      return new LimitNumber(range_arr, 
        number)
    }

    static RadioButtonList(title, text_arr) {
      return new RadioButtonList(title, 
          text_arr)
    }

    static CommentBox(json_arr = []) {
      return new CommentBox(json_arr)
    }

    static ButtonList(title, text_arr) {
      return new ButtonList(title, text_arr)
    }

    static IconButton(image_url, text) {
      return new IconButton(image_url, text)
    }

    static SwipperNumber(name, range_arr) {
      return new SwipperNumber(name, 
        range_arr)
    }

    static SwipperText(name, content_array) {
      return new SwipperText(
        name, content_array)
    }

    static CircleButton(title) {
      return new CheckButton(title, 
        "radio")
    }

    static CheckButton(title) {
      return new CheckButton(title, 
        "checkbox")
    }

    static Canvas(size_x, size_y) {
      return new Canvas(size_x, size_y)
    }

    static ScrollList(text_arr, height) {
      return new ScrollList(text_arr, height)
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