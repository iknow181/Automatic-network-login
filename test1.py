# 引入selenium库中的 webdriver 模块
from selenium import webdriver
# 引入time库
import time
from time import sleep
#  引入pywifi库及所带常量库
import pywifi
from pywifi import const, Profile
import socket


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
        profile.ssid = "YZDX_GLXY"
        #  设置密码
        #  password = "   "
        #  如果没有密码，则设置值为 " CIPHER_TYPE_NONE "
        profile.key = "CIPHER_TYPE_NONE"
        #  加载新的wifi连接文件
        tep_profile = ifaces.add_network_profile(profile)
        #  连接上面的wifi文件
        ifaces.connect(tep_profile)


# 检查本地是否获取到ip
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
    stu_id = '000000001'  # 学号
    passwd = '123123'  # 密码
    ip_add = '10.9.97.1'  # 校园网IP

    stu_id_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[2]'  # 学号的XPath
    passwd_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[3]'  # 密码的XPath
    login_add = '//*[@id="edit_body"]/div[3]/div[1]/form/input[1]'  # 登录按钮的XPath
    '''
    打开Edge浏览器
    考虑到网页打开的速度取决于每个人的电脑和网速，使用time库的隐式等待
    隐式等待会在页面加载完成之后，才开始。在元素的查找过程中，会持续性地获取指定元素对象。
    如果提前获取到元素，则会继续进行后续的操作。如果没有获取到，则会等待最大的等待时间，也会继续进行后续的操作。
    设置隐式等待之后，每一行代码的操作都会调用隐式等待。
    '''
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


if __name__ == "__main__":

    open_wlan()
    while True:
        if get_host_ip():
            sleep(10)  # 在这里等一会联网
            networking()
            break


