// frida hook so层方法


var getAuthString = Module.getExportByName('libnative-lib.so', 'getAuthString');
var native_lib_base_add = parseInt(getAuthString) - parseInt('0xA5364');
send('[*]native_lib_base_add:' + ptr(native_lib_base_add));

var md5_add = ptr(native_lib_base_add + parseInt('0x444CC'));
Interceptor.attach(
    md5_add,
    {
        onEnter: function (args) {
            //send('md5 参数1:'+ Memory.readUtf8String(args[0]));
            send('md5 参数1:' + Memory.readCString(args[0]));
            //send('md5 参数1:'+ Memory.readUtf8String(Memory.readPointer(args[0])));
        },
        onLeave: function (retval) {
            send('md5_result:' + Memory.readUtf8String(retval));
        }

    }
);