var CryptoJS = require("crypto-js");

function cbc_encrypt(text) {
    // CBC模式加密
    var a = CryptoJS.AES.encrypt(text, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
    return a.toString();
}

function cbc_decrypt(text) {
    // CBC模式解密
    var a = CryptoJS.AES.decrypt(text, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
    return a.toString(CryptoJS.enc.Utf8);
}

function ecb_encrypt(text) {
    // ECB模式加密
    var a = CryptoJS.AES.encrypt(text, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    return a.toString();
}

function ecb_decrypt(text) {
    // ECB模式解密
    var a = CryptoJS.AES.decrypt(text, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    return CryptoJS.enc.Utf8.stringify(a).toString();
}


function cfb_encrypt(text) {
    // CFB模式加密
    var a = CryptoJS.AES.encrypt(text, key, {
        iv: iv,
        mode: CryptoJS.mode.CFB,
        padding: CryptoJS.pad.Pkcs7
    })
    return a.toString();
}

function cfb_decrypt(text) {
    // CFB模式解密
    var a = CryptoJS.AES.decrypt(text, key, {
        iv: iv,
        mode: CryptoJS.mode.CFB,
        padding: CryptoJS.pad.Pkcs7
    })
    return a.toString(CryptoJS.enc.Utf8);
}


var key = CryptoJS.enc.Utf8.parse("50579511308d0d8d7964121c6e34030bc8d26ffe5501b648d472375f3078b036"),
    iv = CryptoJS.enc.Utf8.parse("50579511308d0d8d7964121c6e34030bc8d26ffe5501b648d472375f3078b036");

console.log('============================================')
string = "中国";
var enctypy_str = cfb_encrypt(string);
console.log(string + '加密以后得到的结果是:\n' + enctypy_str)
console.log('============================================')
var decrypt_str = cfb_decrypt(enctypy_str)
console.log(enctypy_str + '解密以后得到的结果是:\n' + decrypt_str)
console.log('============================================')
