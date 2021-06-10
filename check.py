import os
import sys
import time
import subprocess

#可以把这个ip换成自己路由器的地址，来变为检测路由器状态
ip = 'www.baidu.com'
start = time.time()#此为最后一次ping成功的时间
while True:
    try:
        # backInfo = os.system('start /B ping -c 1 -w 1 %s'%ip)
        backInfo = subprocess.call("ping -n 1 -w 1 %s"%ip,shell=True)
        print('backInfo=',backInfo)
        if backInfo == 1:#没有ping到，失败了
            print('本次ping失败，开始计时')
            now = time.time()#看目前时间与上次是否在60s以上
            if now - start > 60:
                print('已超过60s，即将进入关机流程')
                break
            else:
                print('未超过60s,检测网络中')
        else:#ping成功了，就更新计时
            start = time.time()
            print('成功')
    except:
        print('false')
        break
    time.sleep(1)#停一秒再继续，没必要一直ping
print('即将关机')
try:#这里调用mc的关机脚本
    mc_backInfo = subprocess.call('')
except:
    print('mc服务器关闭失败')

os.system('shutdown -s -t 3600')#关机,3600就是3600s，即一小时，可以改小一点
