/* Given an array of integers, return a new array such that each element at index i of the new
array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? */

const prodArray = (ogArray) => {
  const prods = [];

  ogArray.forEach((e, i) => {
    const arraySansIndex = ogArray.slice(0, i).concat(ogArray.slice(i + 1));
    prods.push(arraySansIndex.reduce((a, b) => a * b));
  });

  return prods;
};

prodArray([1, 2, 3, 4, 5]); // [120, 60, 40, 30, 24]
prodArray([3, 2, 1]); // [2, 3, 6]
