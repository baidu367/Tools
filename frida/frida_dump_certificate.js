// 服务器校验客户端的情形下，帮助dump客户端证书，并保存为p12的格式，证书密码为1234


Java.perform(function () {
    console.log("Enter!")

    function storeP12(pri, p7, p12Path, p12Password) {
        try {
            var X509Certificate = Java.use("java.security.cert.X509Certificate")
            var p7X509 = Java.cast(p7, X509Certificate);
            var chain = Java.array("java.security.cert.X509Certificate", [p7X509])
            var ks = Java.use("java.security.KeyStore").getInstance("PKCS12", "BC");
            ks.load(null, null);
            ks.setKeyEntry("client", pri, Java.use('java.lang.String').$new(p12Password).toCharArray(), chain);
            var out = Java.use("java.io.FileOutputStream").$new(p12Path);
            ks.store(out, Java.use('java.lang.String').$new(p12Password).toCharArray())
        } catch (exp) {
            console.log(exp)
        }
    }

    Java.use("java.security.KeyStore$PrivateKeyEntry").getPrivateKey.implementation = function () {
        var result = this.getPrivateKey()
        var packageName = Java.use("android.app.ActivityThread").currentApplication().getApplicationContext().getPackageName();
        storeP12(this.getPrivateKey(), this.getCertificate(), '/sdcard/Download/' + packageName + '.p12', '1234');
        console.log("dumpClinetCertificate=>" + '/sdcard/Download/' + packageName + '.p12' + '   pwd: 1234');
        return result;
    }
    Java.use("java.security.KeyStore$PrivateKeyEntry").getCertificateChain.implementation = function () {
        var result = this.getCertificateChain()
        var packageName = Java.use("android.app.ActivityThread").currentApplication().getApplicationContext().getPackageName();
        storeP12(this.getPrivateKey(), this.getCertificate(), '/sdcard/Download/' + packageName + '.p12', '1234');
        console.log("dumpClinetCertificate=>" + '/sdcard/Download/' + packageName + '.p12' + '   pwd: 1234');
        return result;
    }
})


// setImmediate(main)