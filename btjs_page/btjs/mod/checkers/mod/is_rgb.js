

import { is_byte_256 } from "./is_byte_256.js";

export function is_RGB(data) {
    if( ! Array.isArray(data)) {return false;}
    if( ! (data.length == 3)) {return false;}
    for(let i in data) {
        if( ! is_byte_256(data[i])) {
            return false;
        }
    }
    return true
}

export function is_RGBA(data) {
    if( ! Array.isArray(data)) {return false;}
    if( ! (data.length == 4)) {return false;}
    for(let i in data) {
        if( ! is_byte_256(data[i])) {
            return false;
        }
    }
    return true
}