// given a string s, find the length of the longest substring without repeating characters.
// leetcode #3 Longest Substring Without Repeating Characters

//brute force
var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) return s.length;

  let longest = 0;

  for (let left = 0; left < s.length; left++) {
    let seenChars = {},
      currentLength = 0;
    for (let right = left; right < s.length; right++) {
      const currentChar = s[right];
      if (!seenChars[currentChar]) {
        currentLength++;
        seenChars[currentChar] = true;
        longest = Math.max(longest, currentLength);
      } else {
        break;
      }
    }
  }
  return longest;
};

console.log(lengthOfLongestSubstring('abcbdca'));
