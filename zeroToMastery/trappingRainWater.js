// 🔎 Given n non-negative integers representing an elevation map where the width of each bar is 1,
// compute how much water it is able to trap after raining.
// assume all integers are positive 🔎

//💪 brute force solution | time complexity 0(n^2) | space complexity 0(1)

// const elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2];

// const getTrappedRainwater = function (heights) {
//   let totalWater = 0;

//   for (let p = 0; p < heights.length; p++) {
//     let leftP = p,
//       rightP = p,
//       maxLeft = 0,
//       maxRight = 0;
//     while (leftP >= 0) {
//       maxLeft = Math.max(maxLeft, heights[leftP]);
//       leftP--;
//     }
//     while (rightP < heights.length) {
//       maxRight = Math.max(maxRight, heights[rightP]);
//       rightP++;
//     }
//     const currentWater = Math.min(maxLeft, maxRight) - heights[p];
//     if (currentWater >= 0) {
//       totalWater += currentWater;
//     }
//   }
//   return totalWater;
// };

// console.log(getTrappedRainwater(elevationArray)); //8

//💯 optimzed solution | time complexity 0(n) | space complexity 0(1)
// 1. identify pointer with lesser value
// 2. is this pointer value lesser than or equal to max on that side
//  yes --> update max on that side   no --> get water for pointer value, add to total
// 3. move pointer inwards
// 4. repeat for other pointer

const elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2];
const getTrappedRainwater = function (heights) {
  let left = 0,
    right = heights.length - 1,
    totalWater = 0,
    maxLeft = 0,
    maxRight = 0;

  while (left < right) {
    if (heights[left] <= heights[right]) {
      if (heights[left] >= maxLeft) {
        maxLeft = heights[left];
      } else {
        totalWater += maxLeft - heights[left];
      }
      left++;
    } else {
      if (heights[right] >= maxRight) {
        maxRight = heights[right];
      } else {
        totalWater += maxRight - heights[right];
      }
      right--;
    }
  }
  return totalWater;
};

console.log(getTrappedRainwater(elevationArray)); //8
