// given an array of integers return the indices of the two numbers that add up to a given target
// assume all numbers are positive and no duplicate
// there may not always be a solution
// return null if there is no solution
// only one pair of numbers that will equal target

//brute force solution | 0(n^2) time complexity | 0(1) space complexity:
// const findTwoSum = function (nums, target) {
//   for (let a = 0; a < nums.length; a++) {
//     const numberToFind = target - nums[a];
//     for (let b = a + 1; b < nums.length; b++) {
//       if (nums[b] === numberToFind) {
//         return [a, b];
//       }
//     }
//   }
//   return null;
// };

// console.log(findTwoSum([1, 2, 7, 4, 5], 3));

// optimized solution | 0(n) time complexity | 0(n) space in worst case
const findTwoSum = function (nums, target) {
  const numsMap = {};
  console.log({ numsMap });
  for (let a = 0; a < nums.length; a++) {
    console.log({ a, value: nums[a] });
    const currentMapVal = numsMap[nums[a]];
    console.log({ currentMapVal });
    if (currentMapVal >= 0) {
      return [currentMapVal, a];
    } else {
      const numberToFind = target - nums[a];
      console.log({ numberToFind });
      numsMap[numberToFind] = a;
      console.log({ numsMap });
    }
  }
  return null;
};

console.log(findTwoSum([1, 2, 7, 4, 5], 3));
