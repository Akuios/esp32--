# esp32-网页开关电灯。
使用环境：micropython环境。
早在几年前就听说了物联网开发板玩着很有意思，那时网上也有很多教程，和学习思路，但是都涉及到有关c语言的一些项目操作，想着c语法不怎么好的我也没有寻思着折腾。
突然一天有幸了解到，esp32这块开发板可以运行python，于是在有着python基础的前提下，走了一些弯路，做了这个小项目，其中还是有很多不足之处，大佬们也可以进行二次开发。

# 使用方法
在windows下，配置好Thonny环境，将boot.py index.html guandeng.html kaideng.html shandeng.html 文件下载到esp32里上电运行即可。

#需要注意的地方
由于考虑到不同人使用的环境问题，可以修改在boot.py文件里修改要连接的WiFi名称，WiFi密码，端口号。
