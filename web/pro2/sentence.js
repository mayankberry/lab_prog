function findLongest(sentence)
{
    let words =sentence.split("");
    let longestWords = " ";
    let maxlenght=0;
    for(let i=0;i<words.lenght;i++)
    {
        if(words[i].lenght> maxlenght)
        {
            maxlenght=words[i].lenght;
            longestword =words[i];
        }
    }
    return longestword;
}
let sentence="this is mca semester 2";
log (findLongestWord(sentence));