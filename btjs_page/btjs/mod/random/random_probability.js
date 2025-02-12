


export function random_probability(
        probability) {
    let result = Math.floor(Math.random() 
      * (100 - 0 + 1)) + 0;
    if(result <= probability) {
      return true
    } else {
      return false
    }
}