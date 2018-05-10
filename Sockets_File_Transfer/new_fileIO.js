//import file system module
var fs = require('fs');

//populate buffer with file path from node arguments
var path = process.argv[2];
var buffer = fs.readFileSync(path);

var strBuff = buffer.toString()

var lines = strBuff.split('\n');
var numLines = lines.length - 1;

console.log(numLines);
