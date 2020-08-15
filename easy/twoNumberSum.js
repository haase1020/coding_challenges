// two pointer option: 0(nlog(n)) time | 0(1) space
function twoNumberSum(array, targetSum) {
  array.sort((a, b) => a - b);
  let newArray = [];
  let left = 0;
  let right = array.length - 1;
  while (left < right) {
    const currentSum = array[left] + array[right];
    if (currentSum === targetSum) {
      newArray.push([array[left], array[right]]);
      right--;
    } else if (currentSum < targetSum) {
      left++;
    } else if (currentSum > targetSum) {
      right--;
    }
  }
  return newArray;
}

console.log(twoNumberSum([3, 5, 2, -4, 8, 11], 7));
