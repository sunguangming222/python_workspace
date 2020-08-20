from selenium import webdriver
import time

from selenium.webdriver.common.by import By
# 获取浏览器对象
browser = webdriver.Chrome()
browser.maximize_window()  # 窗口最大化
browser.get("http://admintest.guojiangjiaoyu.com/")
time.sleep(3)
# 需求：打开登陆页面点击超链接，使用link_text定位超链接并点击，最终返回登陆页面
'''
browser.find_element_by_link_text("验证码登录").click()
time.sleep(2)
browser.find_element_by_link_text("手机号登录").click()
'''
# 需求：对link_text进行补充优化，可以使用局部文本来进行查找匹配
'''
browser.find_element_by_partial_link_text("验证码").click()
time.sleep(2)
browser.find_element_by_partial_link_text("手机号").click()
'''
# 需求：打开登陆注册页面，完成以下操作 1).使用tag_name定位密码输入框（第二个input标签），并输入：123456
'''
elements = browser.find_elements_by_tag_name("input")
print(len(elements))
elements[0].send_keys("19806586880")
elements[1].send_keys("123456")
'''
# 需求：打开登陆注册页面，完成以下操作：1）使用绝对路径定位用户名输入框，并输入；2）使用相对路径定位密码输入框，并输入密码，3）点击登陆
'''
browser.find_element_by_xpath("/html/body/div/div/div/div/div[2]/form/div[1]/div[3]/div[1]/div[2]/div/div/span/span/input").send_keys('19806586880')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="numPassword"]').send_keys('123456')
time.sleep(2)
#browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/form/div[2]/div/div/span/button').click()
browser.find_element_by_class_name("ant-btn.login-form-button").click()
'''
# 需求：打开登陆注册页面，完成以下操作：1）.利用元素的属性信息精确定位用户名输入框，并输入账号密码
'''
browser.find_element_by_xpath("//*[@placeholder='手机号码']").send_keys('19806586880')
'''
# 需求：打开登陆注册页面，完成以下操作：1）.使用属性与逻辑结合定位策略，在账号框输入手机号
'''
browser.find_element_by_xpath("//*[@placeholder='手机号码' and @class='ant-input']").send_keys('19806586880')
'''
# 需求：打开登陆注册页面，完成以下操作：1）.使用层级和属性结合定位策略，点击账号登陆，输入admin和123456
'''
browser.find_element_by_xpath("//div[@class='ant-tabs-nav ant-tabs-nav-animated']/div/div[2]").click()
browser.find_element_by_xpath("//*[@id='userName']").send_keys('admin')
browser.find_element_by_xpath("//*[@id='password']").send_keys('123456')
'''
'''
# 需求：1.使用xpath包含的语法定位用户输入框输入手机号；
browser.find_element_by_xpath("//*[contains(@placeholder,'手机号码')]").send_keys("19806586880")
#      2.使用xpath属性值以**开头语法定位密码输入框输入密码；
browser.find_element_by_xpath("//*[starts-with(@placeholder,'密码')]").send_keys('123456')
#      3.使用xpath根据文本定位的语法定位登陆按钮并点击 对百校千企网站不行，改用class定位
time.sleep(2)
browser.find_element_by_class_name('ant-btn.login-form-button.ant-btn-primary').click()
'''
# 需求：打开注册登陆页面，完成以下操作：1）.使用CSS定位方式中id选择器定位用户名输入框并输入；2）.使用CSS定位方式中属性选择定位密码输入框并输入；
# 3）.使用CSS定位方式中class选择器定位5天内自动登陆；4）.使用CSS定位方式中元素选择器定位登陆按钮，并点击;
'''
browser.find_element_by_css_selector("#number").send_keys('19806586880')
time.sleep(1)
browser.find_element_by_css_selector("[id='numPassword']").send_keys('123456')
time.sleep(1)
browser.find_element_by_css_selector(".ant-checkbox-input").click()
time.sleep(2)
browser.find_element_by_css_selector("button").click()
'''
# 需求：使用CSS定位方式中的层级选择器定位用户名输入框，并输入手机号
'''
# 父子关系的层级选择器
browser.find_element_by_css_selector(".input-control>input[id='number']").send_keys('19806586880')
# 后代关系层级选择器
browser.find_element_by_css_selector(".ant-form-item-control input[id='numPassword']").send_keys('123456')
browser.find_element_by_css_selector(".ant-form-item-control button").click()
'''

# 延伸需求：使用CSS属性包含的表示定位用户名输入框，输入手机号
browser.find_element_by_css_selector("[placeholder*='手机']").send_keys('19806586880')

# 需求：打开注册登陆页面，完成以下操作：1）.定位用户名输入框并输入；2）.定位密码输入框并输入；
# 3）.定位5天内自动登陆；4）.定位登陆按钮，并点击;
'''
browser.find_element(By.CSS_SELECTOR , "#number").send_keys("19806586880")
time.sleep(1)
browser.find_element(By.ID,"numPassword").send_keys('123456')
time.sleep(1)
browser.find_element(By.CLASS_NAME,"ant-checkbox-input").click()
time.sleep(2)
browser.find_element(By.TAG_NAME,"button").click()
'''
# 4.三秒后关闭浏览器窗口
time.sleep(3)
# 5.关闭浏览器释放资源
browser.quit()

