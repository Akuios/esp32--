def function_sk_server():
    import time
    import network
    import socket
    import re
    from machine import Pin

    wl = network.WLAN(network.STA_IF)
    wl.active(True)
        #扫描附近的WiFi名字并打印，这是一个字节类型，需要解码。
        #print(wl.scan())

        #t1 = b"WiFi\xe5\xaf\x86\xe7\xa0\x8112345678"
        #print(t1.decode())
        #wl.isconnected()
        #判断连接WiFi
        
        #print("esp32 正在尝试连接wifi。。。。。。")
    if not wl.isconnected():
        wl.connect('WiFi密码12345678','12345678')
        while not wl.isconnected():
            pass
            
    print("esp32 wifi连接成功。")
    ip = str(wl.ifconfig()[0])
    print("esp32的ip：",wl.ifconfig()[0])
    time.sleep(1)

    p14 =  Pin(14,Pin.OUT)
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server:Python20WS/2.1\r\n"
    response_blank = "\r\n"
    http = " HTTP/1.1"
    '''
    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sk.bind((ip,55443))
    sk.listen(128)
    '''
    while 1:
            '''
            ip = '192.168.1.12'
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server:Python20WS/2.1\r\n"
            response_blank = "\r\n"
            http = " HTTP/1.1"
            '''
            #判断是否连接上了wifi
            if not wl.isconnected():
                wl.connect('WiFi密码12345678','12345678')
                while not wl.isconnected():
                    pass
            sk = socket.socket()
            sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            sk.bind((ip,55443))
            sk.listen(5)
            
            #对应指令
            #print("服务器启动成功，等待客服端连接。。。。。。")
            
            data, addr = sk.accept()
            
                
            #print(f"成功连接到客服端ip:{addr[0]}  {addr[1]}")

            info = data.recv(30).decode()
            lines = info.splitlines()

            info_inf1 = re.match(r"[^/]+(/[^]*)", lines[0]).group(1)
            
            if info_inf1 == "/"+http:
                f = open("index.html", "r", encoding="utf-8")
                body = str(f.read())
                file = response_line + response_header + response_blank + body
                # print(file)
                # 发送对应的请求信息给浏览器
                data.send(file.encode())
                time.sleep(0.25)
                f.close()
                
            elif info_inf1 == "/kaideng.html"+http:
                p14.value(1)
                f = open("kaideng.html", "r", encoding="utf-8")
                body = str(f.read())
                file = response_line + response_header + response_blank + body
                # print(file)
                # 发送对应的请求信息给浏览器
                data.send(file.encode())
                time.sleep(0.25)
                f.close()
                
            elif info_inf1 == "/guandeng.html"+http:
                p14.value(0)
                f = open("guandeng.html", "r", encoding="utf-8")
                body = str(f.read())
                file = response_line + response_header + response_blank + body
                # print(file)
                # 发送对应的请求信息给浏览器
                data.send(file.encode())
                time.sleep(0.25)
                f.close()
                
            elif info_inf1 == "/shandeng.html"+http:
                for i in range(20):
                    p14.value(1)
                    time.sleep(0.15)
                    p14.value(0)
                    time.sleep(0.15)
                
                
            data.close()
            sk.close()
            
        
            
    
if __name__ =="__main__":           
    while 1:
        try :
            function_sk_server()
        except :
            function_sk_server()
         

