/*

🔎 subproblem: a problem we have to solve along the way to soving the main problem 🔎

 🔎 string: given a string, find the length of the longest substring without repeating characters. 
    💡 main problem: find length of ongest unique substring
    💡 sub problem: pattern matching - unique substring 
    💡 palindrome: a string that reads the same forwards and backwards/ take out all spaces and other characters!

    ✅ step 1: verify the constraints (write some test cases): "aaba","aabbaa","abc","a",""A man, a plan, a canal: Panama"

    💯💪
*/

// 🙋 solution 1: 2 pointers from center
const string = 'A man, a plan, a canal: Panama';
const isValidPalindrome = function (s) {
  s = s.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
  let left = Math.floor(s.length / 2),
    right = left;
  if (s.length % 2 === 0) {
    left--;
  }
  while (left >= 0 && right < s.length) {
    if (s[left] !== s[right]) {
      return false;
    }
    left--;
    right++;
  }
  return true;
};
console.log(isValidPalindrome(string));
