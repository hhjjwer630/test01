from appium import webdriver
import pytest
# server 启动参数
class Test001:
 def setup(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

# 声明driver对象
    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
 @pytest.mark.parametrize('keys', ['无线','网路'])
 def test01(self,keys):
     self.driver.find_element_by_id('com.android.settings:id/search').send_keys(keys)