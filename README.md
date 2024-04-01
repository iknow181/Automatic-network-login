# 一.准备工作

  在开始之前，我们需要一些准备工作，一个能够编写并运行python代码的IDE（如：PyCharm）、安装Python第三方函数库 Selenium、安装Python第三方函数库 pywifi、安装浏览器驱动。

## 1、IDE安装

网上教程太多了，而且也没什么大问题，这里就不过多阐述了。

## 2、安装Selenium

### 1.介绍

Selenium是广泛使用的模拟浏览器运行的库，它是一个用于Web应用程序测试的工具。 Selenium测试直接运行在浏览器中，就像真正的用户在操作一样，并且支持大多数现代 Web 浏览器。

### 2.下载

这里建议用selenium4.1.1版本，因为我发现高版本会报错，这个版本就没什么问题

下载清华镜像（快一点）

pip下载：打开命令提示符，输入下载命令：

```
pip install selenium==4.1.1 -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 3、安装pywifi

#### 1.介绍

pywifi是在python中一个用于操作无线接口的模块，可以跨平台使用，Windows和Linux都支持

#### 2.下载

pip下载：打开命令提示符，输入下载命令：

```
pip3 install pywifi
```

由于此模块基于comtypes模块，因此同时需要下载此模块：

```undefined
pip3 install comtypes
```

对于PyCharm，则直接下载两个模块即可

## 4、下载浏览器驱动

首先的一点就是查看你的浏览器的版本，一定要下载与之对应版本的webdriver驱动文件

1. Chrome驱动文件下载：[点击下载chromedrive](https://chromedriver.storage.googleapis.com/index.html?path=2.35/)
2. Firefox驱动文件下载:[点解下载geckodriver](https://github.com/mozilla/geckodriver/releases)
3. Edge驱动文件下载：[点击下载msedgediver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

将下载好的压缩包解压到任意位置，并把当前路径保存到环境变量。（建议将其保存到运行程序的相同级目录下

，这样不需要再添加环境变量了）

到此前期准备工作就完成了

# 二、登录校园网

## 1、打开浏览器

接下来我们开始第一步：打开一个网页，这里以baidu.com为例，在python源程序中输入并运行下列代码：

```python
#引入selenium库中的 webdriver 模块
from selenium import webdriver

#打开Edge浏览器
driver = webdriver.Edge()
#打开百度搜索主页
driver.get('https://www.baidu.com')
```


如果弹出百度页面，那么说明前期工作没毛病，恭喜你已经成功一半了

## 2、在网页中输入信息

以百度搜索主页为例，我们在使用时，需要在搜索框中输入我们需要搜索的信息，那我们怎么捕捉到页面中的搜索框并在其中输入信息呢？这时我们需要使用到selenium库中的元素定位方法，这里我们希望通过 XPath 定位搜索框在网页中的 <input> 标签 ，调用find_element_by_xpath()方法，在参数中输入路径表达式来定位搜索框，代码如下：


```python
#调用selenium库中的find_element_by_xpath()方法定位搜索框，同时使用send_keys()方法在其中输入信息
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('Hello World!')
```

那么大家现在可能会有一个疑问是，应该如何获取搜索框的路径表达式呢？我们按 F12 或右键打开网页的元素审查窗口，点击窗口顶部的元素选择按钮，之后选中搜索框，此时已定位到搜索框在网页中的 <input> 标签，右键选择Copy XPath即可。详细步骤看图：

## 3、对网页进行点击

在搜索框中输入将要搜索的信息之后，需要点击搜索按钮进行搜索，搜索按钮的路径表达式获取方式与步骤二一致，代码如下：

```python
#调用selenium库中的find_element_by_xpath()方法定位搜索按钮，同时使用click()方法对按钮进行点击
driver.find_element_by_xpath('//*[@id="su"]').click()
```

步骤①至③完整代码如下：

```python
# 引入selenium库中的 webdriver 模块
from selenium import webdriver

# 打开谷歌浏览器
driver = webdriver.Edge()
# 打开百度搜索主页
driver.get('https://www.baidu.com')
# 调用selenium库中的find_element_by_xpath()方法定位搜索框，同时使用send_keys()方法在其中输入信息
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('Hello World!')
# 调用selenium库中的find_element_by_xpath()方法定位搜索按钮，同时使用click()方法对按钮进行点击
driver.find_element_by_xpath('//*[@id="su"]').click()
```

## 4、打开并登录校园网

如果你对上述三个基础操作有了足够清楚的认识，那么如何实现打开并登录校园网，你的心里一定有了一些想法。每个学校的校园网不同，但是大同小异，下面以我的校园网为例，代码如下：

```python
# 引入selenium库中的 webdriver 模块
from selenium import webdriver
# 引入time库
import time

stu_id = 'XXXXXXXX'  # 学号
passwd = 'XXXXXX'  # 密码
ip_add = 'X.X.X.X'  # 校园网IP

stu_id_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[2]'  # 学号的XPath
passwd_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[3]'  # 密码的XPath
login_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[1]'  # 登录按钮的XPath

'''
考虑到网页打开的速度取决于每个人的电脑和网速，使用time库的隐式等待
隐式等待会在页面加载完成之后，才开始。在元素的查找过程中，会持续性地获取指定元素对象。
如果提前获取到元素，则会继续进行后续的操作。如果没有获取到，则会等待最大的等待时间，也会继续进行后续的操作。
设置隐式等待之后，每一行代码的操作都会调用隐式等待。
'''

# 打开Edge浏览器
driver = webdriver.Edge()
# 隐式等待
driver.implicitly_wait(10)
# 打开校园网
driver.get(f'http://{ip_add}/')
# 输入账号和密码
driver.find_element_by_xpath(stu_id_add).send_keys(stu_id)
driver.find_element_by_xpath(passwd_add).send_keys(passwd)
# 统一网页最大化，防止位置不对
driver.maximize_window()
# 点击登录按钮
driver.find_element_by_xpath(login_add).click()
# 关闭浏览器
driver.close()
driver.quit()
```

# 三、打开网卡

现在开机自启动（不难）和连接校园网（有ip）都可以实现，但是我发现，刚开机的时候，我们的电脑应该是没有IP地址的，等待有个DHCP服务器分配给我一个ip，如果自己写个DHCP报文发送程序主动寻找请求太麻烦了。

功夫不负有心人，终于让我发现一个巧方法！！！

经过多次实验发现，在windows桌面，图形化界面上只要我打开WLAN，然后点击我要连接wife的名字，这时候查看无线局域网适配器 WLAN时（在命令行查看，输入ipconfig），发现有ip了。知道了流程，那么我们可以用编程来实现这些步骤。

```python
#  引入pywifi库及所带常量库
import pywifi
from pywifi import const, Profile
 
    
#  获取网卡接口
wifi = pywifi.PyWiFi()
 
#  得到第一个无线网卡
ifaces = wifi.interfaces()[0]
 
#  切断网卡连接
ifaces.disconnect()
 
#  获取wifi的连接状态
wifistatus = ifaces.status()
 
#  检查wifi是否处于切断状态
if wifistatus == const.IFACE_DISCONNECTED:
   #  网卡已被切断
    pass
#  如果网卡没有被切断
#  或者使用 " if wifistatus == const.IFACE_CONNECTED: "
else:
    #  已连接wifi
    pass
 
#  如果已经切断网卡，一般执行下述操作
if wifistatus == const.IFACE_DISCONNECTED:
    #  设置wifi连接文件
    profile: Profile = pywifi.Profile()
 
    #  你要连接的网络的名称
    profile.ssid = "    "
 
    #  网卡的开放状态
    #  " Auth - AP "的验证算法
    profile.auth = const.AUTH_ALG_OPEN
 
    #  wifi的加密算法
    #  通常的加密算法值为 " WPA "
    #  选择wifi的加密方式
    #  " Akm - AP "的密钥管理
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
 
    #  加密单元
    #  " Cipher - AP "的密码类型
    profile.cipher = const.CIPHER_TYPE_CCMP
 
    #  设置密码
    password = "   "
 
    #  回调密码（wifi密码）
    #  如果没有密码，则设置值为 " CIPHER_TYPE_NONE "
    profile.key = password
 
    #  删除已连接的所有wifi文件
    ifaces.remove_all_network_profiles()
 
    #  加载新的wifi连接文件
    tep_profile = ifaces.add_network_profile(profile)
 
    #  连接上面的wifi文件
    ifaces.connect(tep_profile)
 
    #  如果wifi已连接
    if ifaces.status() == const.IFACE_CONNECTED:
        print(True)
 
    #  如果仍未连接
    else:
        print(False)
```

# 四、检查本地是否获取到ip

还是那个问题，要等本地从DHCP服务器上获取到ip，写个函数检测一下，必须等有能连外网的ip才能登录校园网联网。

```python
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    flag = False
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        if ip:
            flag = True
            return flag
    finally:
        s.close()
        return flag
```

# 五、完整程序

```python
# 引入selenium库中的 webdriver 模块
from selenium import webdriver
# 引入time库
import time
#  引入pywifi库及所带常量库
import pywifi
from pywifi import const, Profile


# 打开wifi
def open_wlan():
    #  获取网卡接口
    wifi = pywifi.PyWiFi()
    #  得到第一个无线网卡
    ifaces = wifi.interfaces()[0]
    #  获取wifi的连接状态
    wifistatus = ifaces.status()
    #  如果网络断开，执行下述操作
    if wifistatus == const.IFACE_DISCONNECTED:
        #  设置wifi连接文件
        profile: Profile = pywifi.Profile()
        #  你要连接的网络的名称
        profile.ssid = "XXXXX"
        #  设置密码
        #  password = "   "
        #  如果没有密码，则设置值为 " CIPHER_TYPE_NONE "
        profile.key = "CIPHER_TYPE_NONE"
        #  加载新的wifi连接文件
        tep_profile = ifaces.add_network_profile(profile)
        #  连接上面的wifi文件
        ifaces.connect(tep_profile)

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    flag = False
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        if ip:
            flag = True
            return flag
    finally:
        s.close()
        return flag

# 连接校园网
def networking():
    stu_id = 'XXXXXXXX'  # 学号
    passwd = 'XXXXXX'  # 密码
    ip_add = 'X.X.X.X'  # 校园网IP

    stu_id_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[2]'  # 学号的XPath
    passwd_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[3]'  # 密码的XPath
    login_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[1]'  # 登录按钮的XPath

    # 打开Edge浏览器
    driver = webdriver.Edge()
    # 设置隐式等待
    driver.implicitly_wait(10)
    # 打开校园网
    driver.get(f'http://{ip_add}/')
    # 输入账号和密码
    driver.find_element_by_xpath(stu_id_add).send_keys(stu_id)
    driver.find_element_by_xpath(passwd_add).send_keys(passwd)
    # 统一网页最大化，防止位置不对
    driver.maximize_window()
    # 点击登录按钮
    driver.find_element_by_xpath(login_add).click()
    # 关闭浏览器
    driver.close()
    driver.quit()


if __name__ == "__main__":
    open_wlan()
    while True:
        if get_host_ip():
            sleep(5)  # 在这里等一会联网
            networking()
            break
```

# 六、设置开机自启动

## 自启动方法一：系统自启动

设置python程序开机自启动

1、创建一个xxx.bat文件（将文件扩展名改为bat），右键编辑

2、在xxx.bat文件里面写入以下内容后保存：（可以按照如下流程自己去cmd中测试一下）

```
@echo off
#关闭回显功能，也就是屏蔽执行过程，建议放置在批处理的首行。
```

```
d：
#如果需要开机自启动的python程序在c盘，不需要这一行程序；如果需要自启动的python程序在d盘（或其他盘），需要先切换到d盘（或其他盘）
```

```
cd path 
#path为你所要开机自启动的python程序所在的文件夹
```

```
python xxx.py 
#xxx.py为path文件夹内需要自启动的python程序
```

例如：

```
@echo off 
D:
cd D:\study\Python\project\AutomaticLogin\
python test1.py
```

3、将xxx.bat文件复制到windows的自启动文件夹内，即可开机自启动python程序windows自启动文件夹：

```
C:\ProgramData MicrosoftIWindows\Start Menu Programs\StartUp
```

或者win + r 输入shell:startup直接打开自启动文件夹

！注意！：最好在电脑的命令行界面将所需的模块库装一遍，否则可能会出现在PyCharm可以运行，在命令行运行却报错的情况。
可以在命令行窗口输入pip list，可以在windows上查看python安装了哪些库

## 自启动方法二：注册服务

### 1、打包成exe文件

#### a.概述

服务的优势就在于可以开机自启动

而在windows上，python不能直接将脚本注册为服务，需要将其先打包成exe,再将exe注册为服务打包exe

#### b.安装 PyInstalle

Python 默认并不包含 PyInstaller 模块，因此需要自行安装 PyInstaller 模块。

安装 PyInstaller 模块与安装其他 Python 模块一样，使用 pip 命令安装即可。在命令行输入如下命令：

```
pip install pyinstaller
```

这边强烈建议使用 pip 在线安装的方式来安装 PyInstaller 模块，不要使用离线包的方式来安装，因为 PyInstaller 模块还依赖其他模块，pip 在安装 PyInstaller 模块时会先安装它的依赖模块。

运行上面命令，应该看到如下输出结果：

```
Successfully installed pyinstaller-x.x.x
```

其中的 x.x.x 代表 PyInstaller 的版本。（installed后面可能会跟上一堆依赖，只要里面有pyinstaller就行）

在 PyInstaller 模块安装成功之后，在 Python 的安装目录下的Scripts目录下会增加一个 pyinstaller.exe 程序，接下来就可以使用该工具将 Python 程序生成 exe 程序了。

#### c.PyInstaller生成可执行程序

安装好pyinstaller包后，在cmd/pycharm的终端里运行如下代码打包(进入脚本所在目录)：

```
pyinstaller -F demo.py --noconsole
```

-F表示不带依赖exe，大工程可能会启动较慢；改成-D则表示带依赖；小工程直接-F即可
test1.py是我的脚本文件名称，这里换成自己的
-noconsole表示不带黑框

注意：由于该程序没有图形用户界面，因此如果读者试图通过双击来运行该程序，则只能看到程序窗口一闪就消失了，是正常现象。

### 2、注册服务

1.下载最新版本

下载地址：[NSSM - the Non-Sucking Service Manager](https://nssm.cc/download)

2.根据自己的平台，将32/64位**nssm**.exe文件解压至任意文件夹。

3.来到nssm所在目录，在文件路径处输入cmd，可打开命令窗口

4.在命令窗口内输入

```
nssm install {服务名称}
```

即注册服务的名称。
我这里是AutomaticLogin，是我注册后的服务的名称，这里随意，但不可出现中文，最好不要有空格、特殊符号

注册服务弹出如下**NSSM**界面。

5.Application标签设置：

```
Application Path: 选择系统安装的exe(cmd也可以)。
Startup directory: 选择exe项目的根目录。
Arguments: 输入启动参数
```

点击 Application Path右边的省略号按钮，选中前边生成的exe

Startup directory同理，选择exe项目的根目录（不过一般选好了Application Path，Startup directory自动生成）

在details下，输入服务名和对服务的描述，点击Install service

注册成功

打开任务管理器，服务


如果状态这里并不是启动状态，可以右键启动
如果注册之前就开着服务窗口，注册后可能看不到，右键刷新一下即可
启动类型为自动，即可开机自启动







