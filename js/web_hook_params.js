// hook cookie, 寻找 cookie被赋值的地方--->视图找到cookie的加密生成方式
(function () {
    'use static';
    var resule = ''
    Object.defineProperty(
        document, 'cookie', {
            set: function (params) {
                if (cookie.indexOf('cookie参数名') != -1) {
                    debugger;
                }
                resule = params;
                return params;
            },
            get: function (params) {
                return resule;
            }
        })
})();


// hook window的_$ss属性被赋值的地方
(function () {
    Object.defineProperty(window, '_$ss', {
        set: function (cookie) {
            debugger;
            console.log(cookie);
            return cookie;
        }
    })
})();


// 检测常规加解密函数并拦截
(function () {
    'use strict';
    var source = ['decodeData', 'base64decode', 'md5', 'decode', 'btoa', 'MD5', 'RSA', 'AES', 'CryptoJS', 'encrypt', 'strdecode', "encode", 'decodeURIComponent', 'JSON.stringify', 'String.fromCharCode', 'fromCharCode'];
    console.log("开始测试是否有解密函数");
    let realCtx,
        realName;

    function getRealCtx(ctx, funcName) {
        let parts = funcName.split(".");
        let realCtx = ctx;
        for (let i = 0; i < parts.length - 1; i++) {
            realCtx = realCtx[parts[i]];
        }
        return realCtx;
    }

    function getRealName(funcName) {
        let parts = funcName.split(".");
        return parts[parts.length - 1];
    }

    function hook(ctx, funcName, level, originFunc) {
        ctx[funcName] = function (a) {
            var result = originFunc(a)
            console.log("拦截等级:" + level + " 函数名称:" + funcName, a, " 结果:", result);
            let regexp = / [\S]*\(.*\)\;/g;
            let match = originFunc.toString().match(regexp)
            console.log(match);
            debugger;
            return result;
        };
    }

    function scanning(ctx, level) {
        for (let i = 0; i < source.length; i++) {
            let f = source[i];
            let realCtx = getRealCtx(ctx, f);
            let realName = getRealName(f);
            let chars = realCtx[realName];
            hook(realCtx, realName, level, chars);
        }
    }

    scanning(window, 1);
})();