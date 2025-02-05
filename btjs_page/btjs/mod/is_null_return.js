

/*
Function that tests whether a value
is a return error such as -1, undefined,
none, void string, void dict, or void
array
*/
export function is_null_return(data) {
    if(data == -1) { return true }
    if(data == null) { return true }
    if(data == {}) { return true }
    if(data == []) { return true }
    if(data == "") { return true }
    if(data == undefined) { return true }
    return false;
}