// frida hook类中重载方法

Java.perform(function () {
    console.log('start hook');
    var ClassName = Java.use('com.trs.bj.zxs.utils.ClassName');
    ClassName.func.overload('android.content.Context').implementation = function (v1) {
        console.log('[*] func 参数1:' + v1);
        var res = this.func(v1);
        send('[*] func 返回结果：' + res)
        return res;
    };
});