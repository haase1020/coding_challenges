// 🔎 LeetCode problem: given n non-negative integers a1,a,2....an, where each represents a point at coordinate (i,ai) n vertical lines
// are drawn such that the two endpoints for the line i is at (i,ai) and (i,0). Find two lines, which, together with the x-axis forms a container
// such that the container contains the most water. You can't slant the container.🔎

// 💪 brute force solution | 0(n^2) time complexity | 0(1) space complexity
// var maxArea = function (height) {
//   let maxArea = 0;
//   for (let a = 0; a < height.length; a++) {
//     for (let b = a + 1; b < height.length; b++) {
//       const height1 = Math.min(height[a], height[b]);
//       const width = b - a;
//       const area = height1 * width;
//       maxArea = Math.max(maxArea, area);
//     }
//   }
//   return maxArea;
// };

// 💯 optimized solution | time complexity 0(n) | space complexity
const getMaxWaterContainer = function (heights) {
  let a = 0;
  let b = heights.length - 1;
  let maxArea = 0;
  while (a < b) {
    const height = Math.min(heights[a], heights[b]);
    const width = b - a;
    const area = height * width;
    maxArea = Math.max(maxArea, area);
    if (heights[a] <= heights[b]) {
      a++;
    } else {
      b--;
    }
  }
  return maxArea;
};
console.log(getMaxWaterContainer([7, 1, 2, 3, 9])); //28
