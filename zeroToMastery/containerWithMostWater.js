// LeetCode problem: given n non-negative integers a1,a,2....an, where each represents a point at coordinate (i,ai) n vertical lines
// are drawn such that the two endpoints for the line i is at (i,ai) and (i,0). Find two lines, which, together with the x-axis forms a container
// such that the container contains the most water. You can't slant the container.

// brute force solution
var maxArea = function (height) {
  let maxArea = 0;
  for (let a = 0; a < height.length; a++) {
    for (let b = a + 1; b < height.length; b++) {
      const height1 = Math.min(height[a], height[b]);
      const width = b - a;
      const area = height1 * width;
      maxArea = Math.max(maxArea, area);
    }
  }
  return maxArea;
};

console.log(maxArea([7, 1, 2, 3, 9])); //28
