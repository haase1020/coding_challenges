// for coding challenge test
const text = ['code', 'aaagmnrs', 'anagrams', 'doce', 4];

function groupAnagrams(text) {
  const filteredText = text.filter(word => typeof(word) ==="string");
  const anagrams = {};
  for (const word of filteredText){

    const sortedWord = word.split('').sort().join('');
    if (sortedWord in anagrams) {
      anagrams[sortedWord].push(word);
    } else {
      anagrams[sortedWord] = [word];
    }
  }
  const almostDoneArray = Object.values(anagrams)
  
  const finalArray =[]
  almostDoneArray.forEach((e) => {
finalArray[e[0]] = e[1]
  });
  const myAnswer = Object.keys(finalArray)
  const myAnswerSorted = myAnswer.sort()
 return myAnswerSorted;
}
console.log(groupAnagrams(text))

