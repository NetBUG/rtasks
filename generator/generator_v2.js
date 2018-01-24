'use strict'
var fs = require('fs');
var util = require('util');
var clarinet = require("clarinet");

const fName = 'data2.json';

if (process.argv.length <= 2) {
    console.log(util.format("Usage: %s X\n  , where X is a positive integer defining maximum file length in bytes", __filename))
    process.exit(-1);
}

var maxLen = parseInt(process.argv[2]);
var x = 0;
var y = maxLen;
var sz = 0;
var obj;

var stream = clarinet.createStream({});

stream.pipe(fs.createWriteStream(fName));
stream.write('{');

while (true) {
    obj = {};
    obj[x++] = y--;
    var so = JSON.stringify(obj);
    so = (x > 1 ? "," : "") + so.substring(1, so.length - 1);
    sz += so.length;
    if (sz >= maxLen - 1)
        break;
    stream.write(so);
} ;

stream.write('}');

