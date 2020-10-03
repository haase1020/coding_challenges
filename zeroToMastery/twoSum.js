// given an array of integers return the indices of the two numbers that add up to a given target
// assume all numbers are positive and no duplicate
// there may not always be a solution
// return null if there is no solution
// only one pair of numbers that will equal target

//brute force solution:
const findToSum = function (nums, target) {
  for (let a = 0; a < nums.length; a++) {
    const numberToFind = target - nums[a];
    for (let b = a + 1; b < nums.length; b++) {
      if (nums[b] === numberToFind) {
        return [a, b];
      }
    }
  }
  return null;
};

console.log(findToSum([1, 2, 7, 4, 5], 3));
