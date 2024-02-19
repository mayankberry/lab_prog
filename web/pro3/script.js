function checkPalindrome() {
    let userInput = prompt('Enter a string:');
    if (userInput !== null) {
        if (isPalindrome(userInput)) {
            document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>' + userInput + ' is a palindrome!</p>';
        } else {
            document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>' + userInput + ' is not a palindrome!</p>';
        }
    } else {
        document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>No input provided.</p>';
    }
}

function checkPrimeNumber() {
    let userInput = parseInt(prompt('Enter a number:'));
    if (!isNaN(userInput)) {
        if (isPrime(userInput)) {
            document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>' + userInput + ' is a prime number!</p>';
        } else {
            document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>' + userInput + ' is not a prime number!</p>';
        }
    } else {
        document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>Invalid input provided.</p>';
    }
}

function SwapVariables() {
    let a = 20;
    let b = 50;

    let outputBefore = '<p>Before swapping, a = ' + a + ', b = ' + b + '</p>';
    [a, b] = [b, a];

    let outputAfter = '<p>After swapping, a = ' + a + ', b = ' + b + '</p>';

    document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + outputBefore + outputAfter;
}


function CelciustoFarn(){
    let celsius = parseInt(prompt('Enter Celsius:'))
    const fahrenheit = (celsius * 1.8) + 32
    document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>Celsius : ' + celsius + ' Fahrenheit : ' + fahrenheit + '</p>';
}

function DigitAdd(){
    let num = parseInt(prompt('Enter Number: '))
    let sum = 0; 
    for (; num > 0; num = Math.floor(num / 10)) { 
        sum += num % 10; 
    } 
    return document.getElementById('outputContainer').innerHTML = '<h2>Program Output</h2>' + '<p>Sum of Number is : ' + sum;
}

function isPalindrome(str) {
    let j = str.length - 1
    for (let i = 0; i < str.length / 2; i++) {
        if (str[i] != str[j]) {
            return false;
        }
        j--;
    }
    return true;
}

function isPrime(num) {
    if (num <= 1) 
    return false; 

    for (let i = 2; i < num; i++) 
    if (num % i == 0) 
        return false; 

    return true;
}

