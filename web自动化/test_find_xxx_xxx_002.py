from selenium import webdriver
import time

# 获取浏览器对象
browser = webdriver.Chrome()
browser.maximize_window()  # 窗口最大化
browser.get("http://admintest.guojiangjiaoyu.com/")
time.sleep(3)

# 业务操作 需求：打开登录注册页面，完成以下操作：1）通过脚本执行输入用户名和密码 2）间隔三秒，修改电话号码 3）间隔三秒，点击登录按钮
'''
browser.find_element_by_css_selector("#number").send_keys("19806586880")
browser.find_element_by_css_selector("#numPassword").send_keys("123456")
time.sleep(3)
browser.find_element_by_css_selector("#number").clear()
time.sleep(2)
browser.find_element_by_css_selector("#number").send_keys("18612048484")
browser.find_element_by_css_selector("button").click()
'''
# 需求 1）设置浏览器500*500  2）设置浏览器400
'''
browser.set_window_size(500,500)
time.sleep(2)
browser.set_window_position(0,300)
'''
# 业务操作需求：1）.打开点击忘记密码，暂停2s   2).回退到登录页面 3）前进到忘记密码页 4）刷新页面
browser.find_element_by_xpath("//*[text()='忘记密码']").click()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.refresh()
# 4.三秒后关闭浏览器窗口
time.sleep(3)

# 5.关闭浏览器释放资源
browser.quit()

