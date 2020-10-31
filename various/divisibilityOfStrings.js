'use strict';


const s = 'lrrb'
const t ='lrrb'

function findSmallestDivisor(s, t) {
    const [smallerString, largerString] = [s, t].sort((a,b) => a.length - b.length);
    if(largerString.length % smallerString.length !== 0) {
      console.log("not working")
      
    };
    for (let i = smallerString.length; i > 0; i--) {
        const testString = smallerString.slice(0, i);
        const correctSmaller = !smallerString.split(testString).join('').length;
        console.log(correctSmaller)
        const correctLarger = !largerString.split(testString).join('').length;
        console.log(correctLarger)
        let subPattern = repeatedSubstringPattern(testString)
        if (correctSmaller && correctLarger && subPattern < testString.length ){
          return subPattern
        } else if(correctSmaller && correctLarger) {
          return testString.length
         } else {
           console.log("help")

         }
       }
}


function repeatedSubstringPattern(str) {
    var result = false;
    var sameCount = 1;
    for (var i=1; i<str.length; i++) {
        if (str[i] === str[i]) {
            sameCount++;
        }
    }
    // if (sameCount > 1 && sameCount === str.length) {
    //     result = true;
    // }
    // else {
        for (var i=2; i<=str.length; i++) {
            if (str.length % i === 0) {
                var sub = str.substring(0, i);
                console.log("sub",sub)
                let skip = false;
                for (var j=sub.length; j<=str.length; j++) {
                  console.log("j", j)
                    if (str.indexOf(sub, j) !== j) {
                        result = false;
                        skip = true;
                        console.log("this", str.indexOf(j))
                         break
                    }
                }
                if (!skip && j === str.length) {
                    result = true;
                    break;
                }
                return sub.length
            }
        }
    };
// };

findSmallestDivisor(s,t)