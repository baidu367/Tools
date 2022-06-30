// AES加密

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


var key = CryptoJS.enc.Utf8.parse("4683929779293864"),
    iv = CryptoJS.enc.Base64.parse("CgELBQQPBwkXAwEGCAwNWw==");

console.log('============================================')
string = '[{"page_name":"com.mumayi.market.ui.RecommendActivity","duration":36089},{"page_name":"com.mumayi.market.ui.MainFrameActivity","duration":874},{"page_name":"com.mumayi.market.ui.showapp.ShowAppActivity","duration":1737},{"page_name":"com.mumayi.market.ui.MainFrameActivity","duration":30617},{"page_name":"com.mumayi.market.ui.MainFrameActivity","duration":0},{"page_name":"com.mumayi.market.ui.SplashActivity","duration":3075}]';
var enctypy_str = cbc_encrypt(string);
console.log(string + '加密以后得到的结果是:\n' + enctypy_str)
console.log('============================================')
var decrypt_str = cbc_decrypt(enctypy_str)
console.log(enctypy_str + '解密以后得到的结果是:\n' + decrypt_str)
console.log('============================================')
