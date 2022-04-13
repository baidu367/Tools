# -*- coding:utf-8 -*-
# Time : 2021/8/24 10:05
# FileName : fridaHook.py
# Author : Gecko
# Description：frida注入模板
import sys
import frida

js_code = '''

'''


def on_message(message, data):
    if message["type"] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


if __name__ == "__main__":
    fv = frida.get_usb_device(timeout=1000)
    front_app = fv.get_frontmost_application()
    print("正在运行的应用为：", front_app)
    # 启动模式,重新启动应用并注入=====================
    # pid = fv.spawn(['com.ycwb.android.ycpai'])
    # process = fv.attach(pid)
    # fv.resume(pid)
    # 注入模式，不需要重启应用直接注入=====================
    process = fv.attach(front_app.pid)

    script = process.create_script(js_code)
    script.on("message", on_message)
    script.load()
    sys.stdin.read()
