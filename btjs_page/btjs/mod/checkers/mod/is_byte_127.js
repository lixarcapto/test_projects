


// return bool
export function is_byte_127(ANY) {
    if( ! Number.isInteger(ANY)) {
        return false;
    }
    if(ANY >= 127) { return false; }
    if(ANY <= -127) { return false; }
    return true;
}