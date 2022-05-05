# adb常用命令

```shell
查看连接状态
adb devices  

连接夜神模拟器
adb connect 127.0.0.1:62001 

连接逍遥模拟器
adb connect 127.0.0.1:21503 

查看连接状态
adb shell dumpsys activity top 

获取当前窗口运行的应用包名
adb shell dumpsys window w |findstr \/ |findstr name= 

进入安卓目录
adb shell 

查看日志
adb logcat 

清除日志
adb logcat -c 

查看手机安装的所有应用包名
adb shell pm list packages 

安装应用
adb install 

应用存在,覆盖安装
adb install -r 

卸载应用
adb uninstall 

获取应用程序安装地址
adb shell pm path XXX（包名） 

复制应手机文件本地
adb pull

复制本地文件到手机
adb push

关闭adb服务
adb kill-server

启动adb服务
adb start-server

强制停止运行程序
adb shell am force-stop XXX（包名） 

清除缓存数据
adb shell pm clear XXX（包名） 

指定APP产生随机事件100次
adb shell monkey -p XXX（包名） 100 

指定APP产生随机事件100次并发送详细的activity信息
adb shell monkey -p XXX（包名） -v -v 100

查看当前包名和主Activity
adb shell dumpsys window | findstr mCurrentFocus 

屏幕截图
adb shell screencap 手机路径/xxx.png

录制视频
adb shell screenrecord 手机路径/xxx.mp4

frida端口转发
adb forward tcp:27042 tcp:27042

ida端口转发
adb forward tcp:23946 tcp:23946 

查看机器的序列号
adb shell getprop ro.serialno 

查看机器的CID号
adb shell getprop ro.carrier 

查看机器板子代号
adb shell getprop ro.hardware

查看SPL(Hboot)版本号
adb shell getprop ro.bootloader 

查看芯片是32位还是64位
adb shell getprop ro.product.cpu.abi 

查看设备制造商
adb shell getprop ro.product.manufacturer

查看手机品牌
adb shell getprop ro.product.brand 

查询手机内部代号（型号）
adb shell getprop ro.product.model 

查看安卓版本
adb shell getprop ro.build.version.release 

获取手机分辨率
adb shell “dumpsys window | grep mUnrestrictedScreen”
```