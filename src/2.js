/* Given an array of integers, return a new array such that each element at index i of the new
array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? */

/* Implementation */
const prodArray = (ogArray) => {
  const prods = [];

  ogArray.forEach((_e, i) => {
    // build a duplicate array but omit the current value, calculate the product of the new array
    const arraySansIndex = ogArray.slice(0, i).concat(ogArray.slice(i + 1));
    const product = arraySansIndex.reduce((a, b) => a * b); // division is not used
    prods.push(product);
  });

  return prods;
};

/* Testing */
console.assert(JSON.stringify(prodArray([1, 2, 3, 4, 5]))
  === JSON.stringify([120, 60, 40, 30, 24]));
console.assert(JSON.stringify(prodArray([3, 2, 1]))
  === JSON.stringify([2, 3, 6]));
