//iterative solution  0(n) time and 0(1) space. See python file for prompt
function isPalindrome(string) {
  let leftIdx = 0;
  let rightIdx = string.length - 1;
  while (leftIdx < rightIdx) {
    if (string[leftIdx] !== string[rightIdx]) return false;
    leftIdx++;
    rightIdx--;
  }
  return true;
}

//see AlgoExpert solutions for other solutions such as recursion and naive solution.
