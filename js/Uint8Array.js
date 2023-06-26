// Uint8Array转字符串
function Uint8ArrayToString(fileData){
  var dataString = "";
  for (var i = 0; i < fileData.length; i++) {
    dataString += String.fromCharCode(fileData[i]);
  }

  return dataString

}

// 字符串转Uint8Array
function stringToUint8Array(str){
  var arr = [];
  for (var i = 0, j = str.length; i < j; ++i) {
    arr.push(str.charCodeAt(i));
  }

  var tmpUint8Array = new Uint8Array(arr);
  return tmpUint8Array
}

// int转byte[]
function intTobytes2(n) {
  var bytes = [];

  for (var i = 0; i < 2; i++) {
    bytes[i] = n >> (8 - i * 8);

  }
  return bytes;
}

// string转ArrayBuffer
function str2ab(str) {
  var buf = new ArrayBuffer(str.length * 2); // 每个字符占用2个字节
  var bufView = new Uint16Array(buf);
  for (var i = 0, strLen = str.length; i < strLen; i++) {
    bufView[i] = str.charCodeAt(i);
  }
  return buf;
}


// ArrayBuffer转String
function ab2str(buf) {
  return String.fromCharCode.apply(null, new Uint8Array(buf));
}