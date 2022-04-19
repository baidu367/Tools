# -*- coding:utf-8 -*-
# Time : 2022/4/18 9:39 
# FileName : playWright.py
# Author : Gecko
# Description：playWright使用方法
"""
要求python3.7+以上版本
（1）安装Playwright依赖库
pip install playwright
（2）安装Chromium、Firefox、WebKit等浏览器的驱动文件
python -m playwright install

驱动自动存放路径： AppData\Local\ms-playwright
"""
import asyncio
from playwright.async_api import async_playwright  # 异步操作模块
from playwright.sync_api import sync_playwright  # 同步操作模块
from playwright._impl._api_types import TimeoutError


def sync_function():
    """
    同步方法
    :return:
    """
    with sync_playwright() as p:
        # 谷歌引擎(p.chromium)、火狐引擎(p.firefox)、浏览器引擎(p.webkit)
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            try:
                # 参数说明 timeout=毫秒， headless=True,False 是否开启无头模式
                browser = browser_type.launch(headless=False, timeout=10000)
                # 断开链接时，信息提醒。
                browser.on('disconnected', lambda: print('断开连接'))
                page = browser.new_page()
                page.goto('https://baidu.com/')
                # 截图操作
                page.screenshot(path=f'sync-{browser_type.name}.png')
            except TimeoutError:
                print('访问超时')
            except Exception as e:
                print(e)
            else:
                browser.close()


async def async_function():
    """
    异步方法
    :return:
    """
    url = 'https://www.baidu.com'
    async with async_playwright() as p:
        # 谷歌引擎(p.chromium)、火狐引擎(p.firefox)、浏览器引擎(p.webkit)
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            try:
                # 参数说明 timeout=毫秒， headless=True,False 是否开启无头模式
                browser = await browser_type.launch(headless=False, timeout=10000)
                # 断开链接时，信息提醒。
                browser.on('disconnected', lambda: print('断开连接'))
                context = await browser.new_context(
                    record_video_dir="videos/",
                    # 视频尺寸设置
                    # record_video_size={"width": 640, "height": 480}
                )
                # 执行录制视频
                page = await context.new_page()
                # 不执行录制视频
                # page = await browser.new_page()
                await page.goto(url)
                # 点击登陆按钮
                await page.click('//*[@id="s-top-loginbtn"]')
                username = '用户名'
                # 输入用户名
                # await page.fill('//*[@id="TANGRAM__PSP_11__userName"]', username)
                # 延迟输入用户名
                await page.type('//*[@id="TANGRAM__PSP_11__userName"]', username, delay=100)
                password = '用户密码'
                # 延迟输入密码
                await page.type('//*[@id="TANGRAM__PSP_11__password"]', password, delay=100)
                # 点击登陆
                await page.click('//*[@id="TANGRAM__PSP_11__submit"]')
                # 截图操作
                await page.screenshot(path=f'async-{browser_type.name}.png')
            except TimeoutError:
                print('访问超时')
            except Exception as e:
                print(e)
            else:
                await context.close()
                await browser.close()


if __name__ == '__main__':
    # # 同步操作
    # sync_function()

    # 异步操作
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_function())
