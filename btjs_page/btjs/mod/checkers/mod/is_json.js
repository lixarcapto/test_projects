

/*
Function that returns true if the 
data sent is a json string
*/
// return bool
export function is_json(ANY) {
    if(typeof ANY === 'string') {
        return false;
    }
    try {
      JSON.parse(ANY);
    } catch (e) {
      return false;
    }
    return true;
}