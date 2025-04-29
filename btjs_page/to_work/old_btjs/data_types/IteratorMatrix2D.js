


export class IteratorMatrix2D {

    /*
    Iterador para navegar atraves de 
    matrizes de datos de dos dimensiones.
    Las principales funcione son:
    * get: obtiene el actual elemento.
    * set: modifica el actual elemento.
    * next: avansa al siguiente elemento.
    */

    constructor(matrix2d) {
      this.__y = 0;
      this.__x = 0;
      this.__matrix2d = [];
      this.set_matrix2d(matrix2d);
    }

    // PUBLIC ----------------------------
  
    set_matrix2d(matrix) {
      this.__matrix2d = matrix;
    }
  
    next() {
      const size_x = this.__matrix2d[this.__y].length;
      const size_y = this.__matrix2d.length;
  
      if (size_x - 1 > this.__x) {
        this.__x += 1;
      } else {
        this.__x = 0;
        if (size_y - 1 > this.__y) {
          this.__y += 1;
        } else {
          return false; // No more elements
        }
      }
      return true; // Next element exists
    }
  
    reset() {
      this.__x = 0;
      this.__y = 0;
    }
  
    get() {
      return this.__matrix2d[this.__y][this.__x];
    }
  
    set(element) {
      this.__matrix2d[this.__y][this.__x] = element;
    }
  
    get_matrix2d() {
      return this.__matrix2d;
    }
  
    write() {
      return `x: ${this.__x}\ny: ${this.__y}`;
    }
  
    toString() {
      return this.write();
    }
  }