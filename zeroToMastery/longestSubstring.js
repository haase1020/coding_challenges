// given a string s, find the length of the longest substring without repeating characters.
// leetcode #3 Longest Substring Without Repeating Characters

//brute force | time complexity 0(n2) | Space 0(n)
// var lengthOfLongestSubstring = function (s) {
//   if (s.length <= 1) return s.length;

//   let longest = 0;

//   for (let left = 0; left < s.length; left++) {
//     let seenChars = {},
//       currentLength = 0;
//     for (let right = left; right < s.length; right++) {
//       const currentChar = s[right];
//       if (!seenChars[currentChar]) {
//         currentLength++;
//         seenChars[currentChar] = true;
//         longest = Math.max(longest, currentLength);
//       } else {
//         break;
//       }
//     }
//   }
//   return longest;
// };

// console.log(lengthOfLongestSubstring('abcbdca'));

/*
sliding window technique (similar to 2 pointers technique)
1. use a sliding window to represent the current substring
2. the size of the window will change based on new characters, and characters we've already seen before
3. our seen characters hashmap keeps track of what characters we have seen and the index we saw them at. 
0(n) time and space complexity
*/

var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) return s.length;
  const seen = {};
  let left = 0,
    longest = 0;
  for (let right = 0; right < s.length; right++) {
    const currentChar = s[right];
    const prevSeenChar = seen[currentChar];
    if (prevSeenChar >= left) {
      left = prevSeenChar + 1;
    }
    seen[currentChar] = right;
    longest = Math.max(longest, right - left + 1);
  }
  return longest;
};

console.log(lengthOfLongestSubstring('abcbdca'));
