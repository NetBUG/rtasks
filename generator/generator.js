'use strict'
var fs = require('fs');
var util = require('util');

const fName = 'data1.json'

if (process.argv.length <= 2) {
    console.log(util.format("Usage: %s X\n  , where X is a positive integer defining maximum file length in bytes", __filename))
    process.exit(-1);
}

var maxLen = parseInt(process.argv[2]);
var x = 0;
var y = maxLen;
var sz = 0;

var obj = {}

while (true) {
    sz += x.toString().length + y.toString().length + 4;
    if (sz >= maxLen)
        break;
    obj[x++] = y--;
} ;

console.log("Generated!");
var json = JSON.stringify(obj);
console.log("Stringified!");
fs.writeFile(fName, json);
console.log("Written!");
