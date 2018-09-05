'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the diagonalDifference function below.
function diagonalDifference(arr) {
    var sumFirstArray = [],
        sumSecondArray = [],
        sum = 0;

    var arrayLength = arr.length;

    // Sum first results
    var first = 0;
    for (var i=0; i<arrayLength; i++) {
        sumFirstArray.push(arr[i][i]);
    }
    first = sumFirstArray.reduce((a,b)=>{ return a+b; });

    // Sum second results
    var i, j=arrayLength-1;
    var second = 0;
    for (i=0; i < arrayLength; i++) {
        sumSecondArray.push(arr[i][j-i]);
    }
    second = sumSecondArray.reduce((a,b)=>{ return a+b; });

    return second-first;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    let arr = Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = diagonalDifference(arr);

    ws.write(result + '\n');

    ws.end();
}


diagonalDifference()