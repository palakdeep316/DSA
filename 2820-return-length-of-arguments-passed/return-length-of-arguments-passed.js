/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    j=0
    for (i in args){
        j++
    }
    return j
};

/**
 * argumentsLength(1, 2, 3); // 3
 */