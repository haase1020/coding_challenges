// prompt:given a non-empty string of lowercase letters and a non-negative integer representing
// a key, write a function that returns a new string obtained by shifting every letter in the input
// string by k positions in the alphabet, where k is the key.
// note that letters should "wrap" around the alphabet; in other words, the letter z
// shifted by 1 returns the letter a.
// assuming alphabet only and lower case

// // Solution 1 0(n) time and space
// function caesarCipherEncryptor(string, key) {
//     const newLetters = []
//     const newKey = key % 26
//     for (const letter of string) {
//         newLetters.push(getNewLetter(letter, newKey));
//     }
//     return newLetters.join('');
// }

// function getNewLetter(letter, key) {
//     const newLetterCode = letter.charCodeAt() + key;
//     return newLetterCode <= 122 ? String.fromCharCode(newLetterCode) : String.fromCharCode(96 + (newLetterCode % 122))
// }

//Solution 2 0(n) time and space
function caesarCipherEncryptor(string, key) {
  const newLetters = [];
  const newKey = key % 26;
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
  for (const letter of string) {
    newLetters.push(getNewLetter(letter, newKey, alphabet));
  }
  return newLetters.join('');
}

function getNewLetter(letter, key, alphabet) {
  const newLetterCode = alphabet.indexOf(letter) + key;
  return alphabet[newLetterCode % 26];
}
