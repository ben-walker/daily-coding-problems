/* Given an array of integers, find the first missing positive integer in linear time and
constant space. In other words, find the lowest positive integer that does not exist in the
array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place. */

/* Implementation */
const firstMissing = (input) => {
  let lowest = 1; // constant space: we only store the current lowest missing value
  input.forEach((e) => { // linear time: we only iterate over the input array once
    if (e === lowest) lowest += 1;
  });
  return lowest;
};

/* Testing */
console.assert(firstMissing([3, 4, -1, 1]) === 2);
console.assert(firstMissing([1, 2, 0]) === 3);
console.assert(firstMissing([]) === 1);
