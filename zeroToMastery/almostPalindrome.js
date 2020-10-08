/*
🔎 LeetCode question #680: valid palindrome II
        Given a string, determine if it is almost a palindrome. A string is almost a palindrome if it becomes
        a palindrome by removing 1 letter. Consider only alphanumeric characters and ignore case sensitivity.
        A palindrome is considered almost a palindrome.

        ✅ step 1: Test cases --> "raceacar" True, "abccdba" True, "abcdefdba" False, "" True, "a" True, "ab" True
*/

/* 
🙋 solution
time complexity 0(n) | space complexity 0(1)
*/

const validSubPalindrome = function (s, left, right) {
  while (left < right) {
    if (s[left] !== s[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
};

const isValidPalindrome = function (s) {
  s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();

  let left = 0;
  right = s.length - 1;

  while (left < right) {
    if (s[left] !== s[right]) {
      return (
        validSubPalindrome(s, left + 1, right) ||
        validSubPalindrome(s, left, right - 1)
      );
    }
    left++;
    right--;
  }
  return true;
};

console.log(isValidPalindrome('raceacar'));
