# -*- coding:utf-8 -*-
# Time : 2022/4/24 9:22 
# FileName : process.py
# Author : Gecko
# Description：协程、多进程+协程
import asyncio
import time
import httpx
from aiomultiprocess import Pool

def run_time(seconds):
    """
    消耗时间格式化
    :param seconds: 时间戳之差
    :return: 输出中文格式化时间
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return "总用时%02d天%02d小时%02d分%02d秒" % (d, h, m, s)


async def get(url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.status_code


async def test_func(urls):
    async with Pool() as pool:
        await pool.map(get, urls)


if __name__ == '__main__':
    # 进程加协程
    start_time = time.time()
    task_request_url = ['https://www.baidu.com'] * 100
    task_request_url2 = [get(url) for url in task_request_url]
    asyncio.run(test_func(task_request_url))
    print(time.time() - start_time)
    print('*' * 50)

    # 协程
    start_time = time.time()
    new_loop = asyncio.new_event_loop()  # asyncio仅为主线程生成一个事件循环,在同一线程中，第二个协程受到第一个的干扰,需要初始化。
    asyncio.set_event_loop(new_loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_request_url2))
    print(time.time() - start_time)
    print('*' * 50)
