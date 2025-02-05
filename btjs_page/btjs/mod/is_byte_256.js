



export function is_byte256(data) {
    if( ! Number.isInteger(data)) {
        return false;
    }
    if(data >= 256) { return false; }
    if(data < 0) { return false; }
    return true;
}

export function is_byte127(data) {
    if( ! Number.isInteger(data)) {
        return false;
    }
    if(data >= 127) { return false; }
    if(data <= -127) { return false; }
    return true;
}