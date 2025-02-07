



export function is_object_js(data) {
    let r = Object.prototype.toString
      .call(data) === '[object Object]';
    return r == true;
}