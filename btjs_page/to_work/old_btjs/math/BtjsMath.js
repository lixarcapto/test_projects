

import { BtjsGui } 
    from "../gui/BtjsGui.js";
import {center_square} 
    from "./mod/center_square.js";
import {is_colliding_rect}
    from "./mod/is_colliding_rect.js";
import { point_in_rect } 
    from "./mod/point_in_rect.js";
import { left_point_rect } 
    from "./mod/left_point_rect.js";
import { mid } from "./mod/mid.js";
import {origin_by_center} 
    from "./mod/origin_by_center.js";
import { vector_sum } 
    from "./mod/vector_sum.js";
import { set_in_range } 
    from "./mod/set_in_range.js";
import { sum_in_range } 
    from "./mod/sum_in_range.js";
import { sum_point_in_range } 
    from "./mod/sum_point_in_range.js";
import {center_rect_in_origin}
    from "./mod/center_rect_in_origin.js";

export class BtjsMath extends BtjsGui {

    static is_colliding_rect(
            rectangulo1, rectangulo2) {
        return is_colliding_rect(rectangulo1, 
            rectangulo2)
    }

    static center_square(point_location,
            width, height) {
        return center_square(point_location,
            width, height)
    }

    /*
    Determina si un punto se encuentra 
    dentro de un rectángulo.
    */
    static point_in_rect(point_location, 
            width, height) {
        return point_in_rect(point_location, 
            width, height)
    }

    /*
    calcula las coordenadas del punto 
    inferior izquierdo de un rectángulo 
    dado su ubicación superior derecha 
    y su tamaño.
    */
    static left_point_rect(
            range_location, width, height) {
        return left_point_rect(
            range_location, width, height)
    }

    /*
    Función que calcula el
    promedio de los números en
    la matriz enviada.
    */
    static mid(array) {
        return mid(array)
    }

    /*
    Encuentra el punto de origen 
    (esquina superior izquierda) 
    de un rectángulo.
    Calculamos las coordenadas del 
    origen restando la mitad de las 
    dimensiones al centro
    */
    static origin_by_center(point, 
            width, height) {
        return origin_by_center(point, 
            width, height)
    }

    /*
    Función que suma los elementos 
    de dos arrays de números en la 
    misma posición del array.
    */
    static vector_sum(ARRAY_1, 
            ARRAY_2) {
        return vector_sum(ARRAY_1, 
            ARRAY_2)
    }

    /*
    Encuentra el nuevo punto de origen
    de un rectangulo centrandolo en su 
    anterior punto de origen.
    */
    static center_rect_in_origin(point, 
            sizeX, sizeY) {
        return center_rect_in_origin(point, 
            sizeX, sizeY)
    }

    /*
    Función que ajusta un valor en el 
    rango límite enviado.
    */
    static set_in_range(VALUE, RANGE_ARR) {
        return set_in_range(VALUE, 
            RANGE_ARR)
    }

    /*
    Funcion que suma dos valores en 
    un rango limitado, si supera o es 
    inferior al rango se limita a 
    ajustar el limite.
    */
    static sum_in_range(value_a, 
        value_b, range_arr) {
            return sum_in_range(value_a, 
            value_b, range_arr)
    }

    /*
    Función que desplaza un a otro 
    punto sin superar los límites 
    que los ejes enviados como 
    intervalos.
    */
    static sum_point_in_range( old_point, 
            new_point, range_x, range_y) {
        return sum_point_in_range( old_point, 
            new_point, range_x, range_y)
    }

}