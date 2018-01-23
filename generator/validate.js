'use strict'
//var clarinet = require('clarinet'), parser = clarinet.parser();
var fs = require('fs');
var t = require('util').format;

const fName = 'data.json'

var options = {};
var stream = require("clarinet").createStream(options);
stream.on("error", function (e) {
  console.error("error!", e)
  // clear the error
  this._parser.error = null
  this._parser.resume()
});

var firstKey = undefined;
var firstVal = undefined;
var lastKey;
var lastVal;
var keyCount = 0;

stream.on("openobject", function (node) {
    //console.log(node);
});

stream.on("key", function (key) {
    //console.log(key);
    if (firstKey === undefined) {
        firstKey = key;
    }
    lastKey = key;                  // Cheaper not to write else
});

stream.on("value", function (value) {
    //console.log(key);
    if (firstVal === undefined) {
        firstVal = value;
    }
    lastVal = value;                // Cheaper not to write else
    keyCount++;
});

stream.on("end", function() {
    console.log(t("Stats for %s:", fName));
    console.log(t("Pairs found: \t%d", keyCount));
    console.log(t("First pair: \t%d:%d", firstKey, firstVal));
    console.log(t("Last pair: \t%d:%d", lastKey, lastVal));
});

fs.createReadStream(fName).pipe(stream)

