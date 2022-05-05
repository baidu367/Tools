# adb常用命令
#
查看连接状态
```shell
adb devices 
```
连接夜神模拟器
```shell
adb connect 127.0.0.1:62001 
```
连接逍遥模拟器
```shell
adb connect 127.0.0.1:21503
```
查看连接状态
```shell
adb shell dumpsys activity top 
```
获取当前窗口运行的应用包名
```shell
adb shell dumpsys window w |findstr \/ |findstr name= 
```
进入安卓目录
```shell
adb shell 
```
查看日志
```shell
adb logcat 
```
清除日志
```shell
adb logcat -c 
```
查看手机安装的所有应用包名
```shell
adb shell pm list packages
```
安装应用
```shell
adb install 
```
应用存在,覆盖安装
```shell
adb install -r 
```
卸载应用
```shell
adb uninstall 
```
获取应用程序安装地址
```shell
adb shell pm path XXX（包名） 
```
复制应手机文件本地
```shell
adb pull
```
复制本地文件到手机
```shell
adb push
```
关闭adb服务
```shell
adb kill-server
```
启动adb服务
```shell
adb start-server
```
强制停止运行程序
```shell
adb shell am force-stop XXX（包名） 
```
清除缓存数据
```shell
adb shell pm clear XXX（包名）
```
指定APP产生随机事件100次
```shell
adb shell monkey -p XXX（包名） 100
```
指定APP产生随机事件100次并发送详细的activity信息
```shell
adb shell monkey -p XXX（包名） -v -v 100
```
查看当前包名和主Activity
```shell
adb shell dumpsys window | findstr mCurrentFocus 
```
屏幕截图
```shell
adb shell screencap 手机路径/xxx.png
```
录制视频
```shell
adb shell screenrecord 手机路径/xxx.mp4
```
端口转发
```shell
adb forward tcp:端口 tcp:端口
```
查看机器的序列号
```shell
adb shell getprop ro.serialno 
```
查看机器的CID号
````shell
adb shell getprop ro.carrier 
````
查看机器板子代号
```shell
adb shell getprop ro.hardware
```
查看SPL(Hboot)版本号
```shell
adb shell getprop ro.bootloader 
```
查看芯片是32位还是64位
```shell
adb shell getprop ro.product.cpu.abi
```
查看设备制造商
```shell
adb shell getprop ro.product.manufacturer
```
查看手机品牌
```shell
adb shell getprop ro.product.brand 
```
查询手机内部代号（型号）
```shell
adb shell getprop ro.product.model 
```
查看安卓版本
```shell
adb shell getprop ro.build.version.release 
```
获取手机分辨率
```shell
adb shell “dumpsys window | grep mUnrestrictedScreen”
```
