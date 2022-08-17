```javascript
// javascript 注入代码
try {
    window.transfer = '接收的内容';
(function () {
    var res = window.transfer;
    if (window.flag) {
        window.ws.send(res);
    } else {
        var ws = new WebSocket('ws://127.0.0.1:9999');
        window.ws = ws;
        window.flag = true;
        ws.open = function (evt) {
        };
        ws.onmessage = function (evt) {
            window.ws.send(res);
        }
    }
})()
}catch (e) {
    
}
```

```python
# 建立 websocket服务接收数据
import asyncio
import json
import websockets


async def chenk_permint(webSocket):
    send_text = 'hello'
    await webSocket.send(send_text)
    return True


async def recv_msg(webSocket):
    while True:
        recv_text = await webSocket.recv()
        print(recv_text)


async def main_logic(webSocket, path):
    await chenk_permint(webSocket)
    await recv_msg(webSocket)


if __name__ == '__main__':
    start_server = websockets.serve(main_logic, '127.0.0.1', '9999')
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

```