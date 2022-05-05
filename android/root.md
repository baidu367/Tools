# 判断手机是否root

* 判断是否存在包名

adb shell pm list packages | findstr xxx
```shell
com.noshufou.android.su
com.noshufou.android.su.elite
eu.chainfire.supersu
com.koushikdutta.superuser
com.thirdparty.superuser
com.yellowes.su
com.topjohnwu.magisk

```
* 判断是否存在需要root权限的应用
```shell
com.koushikdutta.rommanager
com.koushikdutta.rommanager.license
com.dimonvideo.luckypatcher
com.chelpus.lackypatch
com.ramdroid.appquarantine
com.ramdroid.appquarantinepro
com.android.vending.billing.InAppBillingService.COIN
com.chelpus.luckypatcher

```
* 检测目录是否有su文件
```shell
/data/local/
/data/local/bin/
/data/local/xbin/
/sbin/
/su/bin/
/system/bin/
/system/bin/.ext/
/system/bin/failsafe/
/system/sd/xbin/
/system/usr/we-need-root/
/system/xbin/
/cache/
/data/
/dev/
```
* 命令
```shell
which su
ro.debuggable
ro.secure
```