# Task 3
This task requires two scripts.

# JSON objects generator
The script generates a JSON object of specific size, no more than X. The limit X is defined in bytes
by passing the script an integer argument. THe object generated consists of key/value pairs. 
Keys are a sequence of numbers starting with 0 and incremented by 1, and values start with X decremented by 1 in each new pair.


## Dependencies
Run `npm install` in current folder to install required dependencies


## Usage
$ ls
generator.js
$ node generator.js 15
$ ls
data.json generator.js
$ cat data.json
{"0":15,"1":14}
$ wc -c data.json // displaying object size in bytes, it's less than limit
15
$ node generator.js 50 && cat data.json
{"0":50,"1":49,"2":48,"3":47,"4":46,"5":45,"6":44}
$ node generator.js 100 && cat data.json
{"0":100,"1":99,"2":98,"3":97,"4":96,"5":95,"6":94,"7":93,"8":92,"9":91,"10":90,"11":89,"12":88}
$ node generator.js 314572800
$ du -sh data.json // file size in MB
300M data.json

# Validator
This script reads `data.json`, and if the object is a valid JSON object, the following stats are displayed:
 * total pair count
 * First pair key:value
 * Last pair key:value

## Usage
`node validate.js`

# Note 
There are implementation-dependent memory constraints for different Node.js backends. 
In some environments, it refuses to allocate more than 600 Mb to JS engine and could not write a 300 MB file.
More info: [Github issue](https://github.com/nodejs/node-v0.x-archive/issues/14170)