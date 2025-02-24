


// return bool
export function is_byte_256(ANY) {
    if( ! Number.isInteger(ANY)) {
        return false;
    }
    if(ANY >= 256) { return false; }
    if(ANY < 0) { return false; }
    return true;
}