// frida hook 加密算法


function showStacks() {
    // 调用栈
    Java.perform(function () {
        send(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
    });
};

function bytesToHex(arr) {
    var str = '';
    var k, j;
    for (var i = 0; i < arr.length; i++) {
        k = arr[i];
        j = k;
        if (k < 0) {
            j = k + 256;
        }
        if (j < 16) {
            str += "0";
        }
        str += j.toString(16);
    }
    return str;
};

function bytesToBase64(arr) {
    var base64EncodeChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    var r, a, c, h, o, t;
    for (c = arr.length, a = 0, r = ''; a < c;) {
        if (h = 255 & arr[a++], a == c) {
            r += base64EncodeChars.charAt(h >> 2),
                r += base64EncodeChars.charAt((3 & h) << 4),
                r += '==';
            break
        }
        if (o = arr[a++], a == c) {
            r += base64EncodeChars.charAt(h >> 2),
                r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
                r += base64EncodeChars.charAt((15 & o) << 2),
                r += '=';
            break
        }
        t = arr[a++],
            r += base64EncodeChars.charAt(h >> 2),
            r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
            r += base64EncodeChars.charAt((15 & o) << 2 | (192 & t) >> 6),
            r += base64EncodeChars.charAt(63 & t)
    }
    return r
};

function bytesToString(arr) {
    var str = "";
    for (var i = 0; i < arr.length; i++) {
        var tmp = arr[i];
        if (tmp < 0) {
            tmp = (255 + tmp + 1).toString(16);
        } else {
            tmp = tmp.toString(16);
        }
        if (tmp.length == 1) {
            tmp = "0" + tmp;
        }
        str += tmp;
    }
    return str;
};

function byteToString(arr) {
    if (typeof arr === 'string') {
        return arr;
    }
    var str = '',
        _arr = arr;
    for (var i = 0; i < _arr.length; i++) {
        var one = _arr[i].toString(2),
            v = one.match(/^1+?(?=0)/);
        if (v && one.length == 8) {
            var bytesLength = v[0].length;
            var store = _arr[i].toString(2).slice(7 - bytesLength);
            for (var st = 1; st < bytesLength; st++) {
                store += _arr[st + i].toString(2).slice(2);
            }
            str += String.fromCharCode(parseInt(store, 2));
            i += bytesLength - 1;
        } else {
            str += String.fromCharCode(_arr[i]);
        }
    }
    return str;
};


Java.perform(function () {
    var secretKeySpec = Java.use('javax.crypto.spec.SecretKeySpec');
    secretKeySpec.$init.overload('[B', 'java.lang.String').implementation = function (a, b) {
        // showStacks();
        var result = this.$init(a, b);
        send("======================================");
        send("算法名：" + b + "|Dec密钥:" + bytesToString(a));
        send("算法名：" + b + "|Hex密钥:" + bytesToHex(a));
        return result;
    }
    var mac = Java.use('javax.crypto.Mac');
    mac.getInstance.overload('java.lang.String').implementation = function (a) {
        // showStacks();
        var result = this.getInstance(a);
        send("======================================");
        send("算法名：" + a);
        return result;
    }
    mac.update.overload('[B').implementation = function (a) {
        // showStacks();
        this.update(a);
        send("======================================");
        send("javax.crypto.Mac.update重载一")
        send("update(byteToString):" + byteToString(a))
    }
    mac.update.overload('[B', 'int', 'int').implementation = function (a, b, c) {
        // showStacks();
        this.update(a, b, c)
        send("======================================");
        send("javax.crypto.Mac.update重载二")
        send("update(byteToString):" + byteToString(a) + "|" + b + "|" + c);
    }
    mac.doFinal.overload().implementation = function () {
        // showStacks();
        var result = this.doFinal();
        send("======================================");
        send("javax.crypto.Mac.doFinal重载一")
        send("doFinal结果(bytesToHex):" + bytesToHex(result));
        send("doFinal结果(bytesToBase64):" + bytesToBase64(result));
        return result;
    }
    mac.doFinal.overload('[B').implementation = function (a) {
        // showStacks();
        var result = this.doFinal(a);
        send("======================================");
        send("javax.crypto.Mac.doFinal重载二")
        send("doFinal参数(byteToString):" + byteToString(a));
        send("doFinal结果(bytesToHex):" + bytesToHex(result));
        send("doFinal结果(bytesToBase64):" + bytesToBase64(result));
        return result;
    }
    var md = Java.use('java.security.MessageDigest');
    md.getInstance.overload('java.lang.String', 'java.lang.String').implementation = function (a, b) {
        // showStacks();
        send("======================================");
        send("java.security.MessageDigest.getInstance重载一")
        send("算法名：" + a);
        return this.getInstance(a, b);
    }
    md.getInstance.overload('java.lang.String').implementation = function (a) {
        // showStacks();
        send("======================================");
        send("java.security.MessageDigest.getInstance重载二")
        send("算法名：" + a);
        return this.getInstance(a);
    }
    md.update.overload('[B').implementation = function (a) {
        // showStacks();
        send("======================================");
        send("java.security.MessageDigest.update重载一")
        send("update(byteToString):" + byteToString(a))
        return this.update(a);
    }
    md.update.overload('[B', 'int', 'int').implementation = function (a, b, c) {
        // showStacks();
        send("======================================");
        send("java.security.MessageDigest.update重载一")
        send("update(byteToString):" + byteToString(a) + "|" + b + "|" + c);
        return this.update(a, b, c);
    }
    md.digest.overload().implementation = function () {
        // showStacks();
        send("======================================");
        send("java.security.MessageDigest.digest重载一")
        var result = this.digest();
        send("digest结果(bytesToHex):" + bytesToHex(result));
        send("digest结果(bytesToBase64):" + bytesToBase64(result));
        return result;
    }
    md.digest.overload('[B').implementation = function (a) {
        // showStacks();
        send("======================================");
        send("java.security.MessageDigest.digest重载二")
        send("digest参数(byteToString):" + byteToString(a));
        var result = this.digest(a);
        send("digest结果(bytesToHex):" + bytesToHex(result));
        send("digest结果(bytesToBase64):" + bytesToBase64(result));
        return result;
    }
    var ivParameterSpec = Java.use('javax.crypto.spec.IvParameterSpec');
    ivParameterSpec.$init.overload('[B').implementation = function (a) {
        // showStacks();
        var result = this.$init(a);
        send("======================================");
        send("iv向量(bytesToString):" + bytesToString(a));
        send("iv向量(bytesToHex):" + bytesToHex(a));
        return result;
    }
    var cipher = Java.use('javax.crypto.Cipher');
    cipher.getInstance.overload('java.lang.String').implementation = function (a) {
        // showStacks();
        var result = this.getInstance(a);
        send("======================================");
        send("模式填充:" + a);
        return result;
    }
    cipher.update.overload('[B').implementation = function (a) {
        // showStacks();
        var result = this.update(a);
        send("======================================");
        send("javax.crypto.Cipher.update重载一")
        send("update(byteToString):" + byteToString(a));
        return result;
    }
    cipher.update.overload('[B', 'int', 'int').implementation = function (a, b, c) {
        // showStacks();
        var result = this.update(a, b, c);
        send("======================================");
        send("javax.crypto.Cipher.update重载一")
        send("update(byteToString):" + byteToString(a) + "|" + b + "|" + c);
        return result;
    }
    cipher.doFinal.overload().implementation = function () {
        // showStacks();
        var result = this.doFinal();
        send("======================================");
        send("javax.crypto.Cipher.doFinal重载一")
        send("doFinal结果(bytesToHex):" + bytesToHex(result));
        send("doFinal结果(bytesToBase64):" + bytesToBase64(result));
        return result;
    }
    cipher.doFinal.overload('[B').implementation = function (a) {
        // showStacks();
        var result = this.doFinal(a);
        send("======================================");
        send("javax.crypto.Cipher.doFinal重载二")
        send("doFinal参数(byteToString):" + byteToString(a));
        send("doFinal结果(bytesToHex):" + bytesToHex(result));
        send("doFinal结果(bytesToBase64):" + bytesToBase64(result));
        return result;
    }
    var x509EncodedKeySpec = Java.use('java.security.spec.X509EncodedKeySpec');
    x509EncodedKeySpec.$init.overload('[B').implementation = function (a) {
        // showStacks();
        var result = this.$init(a);
        send("======================================");
        send("RSA密钥:" + bytesToBase64(a));
        return result;
    }
    var rSAPublicKeySpec = Java.use('java.security.spec.RSAPublicKeySpec');
    rSAPublicKeySpec.$init.overload('java.math.BigInteger', 'java.math.BigInteger').implementation = function (a, b) {
        // showStacks();
        var result = this.$init(a, b);
        send("======================================");
        //send("RSA密钥:" + bytesToBase64(a));
        send("RSA密钥N:" + a.toString(16));
        send("RSA密钥E:" + b.toString(16));
        return result;
    }
});
