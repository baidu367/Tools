// ssl 证书效验
// 您可能需要配置浏览器或应用程序以信任Charles 根证书. 请在帮助菜单中查看 SSL 代理.


Java.perform(function () {
    function checkIsImplementeInterFace(clsName, interface_) {
        try {
            var cls = Java.use(clsName)
            if (cls.class.isInterface()) {
                return false
            }
            if (cls.class != undefined)
                if (interface_.class.isAssignableFrom(cls.class)) {
                    return true
                }
            return false
        } catch (e) {
            return false
        }
    }

    // Java.use("okhttp3.CertificatePinner").check.overload('java.lang.String', '[Ljava.security.cert.Certificate;').implementation = function () {
    //
    //     console.log("CertificatePinner check called!")
    // }
    // Java.use("okhttp3.CertificatePinner").check.overload('java.lang.String', 'java.util.List').implementation = function () {
    //
    //     console.log("CertificatePinner check called!")
    // }
    Java.enumerateClassLoaders({
        onMatch: function (loader) {
            try {
                if (loader.findClass("okhttp3.OkHttpClient$Builder")) {
                    console.log("Found the really Classloader")
                    Java.classFactory.loader = loader
                }
            } catch (e) {

            }
        },
        onComplete: function () {
            console.log("Search Loaders Completed!")
        }
    })

    // Java.use("okhttp3.OkHttpClient$Builder").certificatePinner.implementation = function (certificatePinner) {
    //     return this.certificatePinner(Java.use("okhttp3.CertificatePinner").DEFAULT.value) //CertificatePinner.DEFAULT
    // }
    var TrustManagerInterface = Java.use("javax.net.ssl.TrustManager")

    Java.enumerateLoadedClasses({
        onMatch: function (clsName, handle) {
            if (checkIsImplementeInterFace(clsName, TrustManagerInterface)) {
                console.log(clsName)
                var targetClass = Java.use(clsName)
                var len = targetClass["checkServerTrusted"].overloads.length
                for (var i = 0; i < len; i++) {
                    console.log(targetClass["checkServerTrusted"].overloads[i].returnType.name)
                    if (targetClass["checkServerTrusted"].overloads[i].returnType.name == 'V') {
                        targetClass["checkServerTrusted"].overloads[i].implementation = function () {
                            console.log(clsName + i + "checkServerTrusted Called!")
                        }
                    } else {
                        targetClass["checkServerTrusted"].overloads[i].implementation = function () {
                            console.log(clsName + i + "checkServerTrusted Called!")
                            return null
                        }
                    }
                }
            }
        },
        onComplete: function () {
            console.log("Search Classes Completed!")
        }

    })

})


