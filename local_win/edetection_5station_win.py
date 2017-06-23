# coding=utf-8

# ******************************************建立项目*********************************************
from selenium import webdriver
from time import sleep
import time

browser = webdriver.Chrome()
# browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
# browser.maximize_window()

browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
browser.find_element_by_id("userId").send_keys("15609100803")
browser.find_element_by_id("password").send_keys("123456")
browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/button').click()

sleep(3)
browser.find_element_by_link_text("创建工程").click()
sleep(1)
browser.switch_to.frame("mainFrame")
browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/add")

# 获取时间字符串
timeFF = time.strftime("%Y_%m_%d %H:%M:%S")
browser.find_element_by_id("contractName").send_keys(u"合同项目测试%s" % timeFF)
browser.find_element_by_id("contractNoA").send_keys(u"CQ100000001")
browser.find_element_by_id("contractNoB").send_keys(u"CQ100000002")
browser.find_element_by_id("signedTime").click()
sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[5]/td[2]').click()

# 选择发包方变电站
sleep(1)
# 乌鲁木齐电业局
browser.find_element_by_xpath('//*[@id="enterpriseId"]/option[7]').click()
# 运维站
# browser.find_element_by_xpath('//*[@id="enterpriseId"]/option[9]').click()

browser.find_element_by_id("contacts").send_keys(u"许臻")
browser.find_element_by_id("contactMobile").send_keys(u"15609100803")
browser.find_element_by_id("contactEamil").send_keys(u"xuzhen@si-top.com")
browser.find_element_by_name("companyId").click()
sleep(1)
browser.find_element_by_xpath('//*[@name="companyId"]/option[4]').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[1]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[2]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[3]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[4]/input').click()
browser.find_element_by_xpath('//*[@id="substation"]/div[5]/input').click()
browser.find_element_by_link_text("下一步").click()
sleep(1)
browser.switch_to.alert.accept()
sleep(10)
browser.quit()

#************************* 变电站建立***************************************************
# 单页变电站数目
a = 1

for i in range(1, 6):
    sleep(2)
    browser = webdriver.Chrome()
    # browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    # browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").clear()
    browser.find_element_by_id("userId").send_keys("15609100803")
    browser.find_element_by_id("password").clear()
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[3]/button").click()

    sleep(3)
    browser.find_element_by_link_text("工程管理").click()
    sleep(1)
    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/list")
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/span[1]/img').click()
    sleep(1)

    sleep(3)
    browser.switch_to.parent_frame()
    el = browser.find_element_by_xpath('//*[@id="ext-gen34"]/iframe')
    browser.switch_to.frame(el)

    # browser.switch_to.frame("/sito2000/action/sd/wf/contractProject/getContract?contractId=%s" %a)
    browser.find_element_by_link_text("站点信息").click()
    sleep(3)

    print a
    # 选择站点
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[%s]/div[1]/div/span[1]/img' % a).click()
    sleep(3)

    browser.switch_to.parent_frame()
    el = browser.find_element_by_xpath('//*[@id="ext-gen39"]/iframe')
    browser.switch_to.frame(el)
    # browser.switch_to.frame('/sito2000//workflow/project_add.jsp?contractId={}&projectId={}&projectState=1' .format(a, b))
    sleep(3)
    browser.find_element_by_id('manageruser').click()
    sleep(3)
    browser.find_element_by_xpath('//*[@id="ext-gen113"]/div[1]/div').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="deviceuser"]').click()
    sleep(3)
    browser.find_element_by_xpath('//*[@id="ext-gen116"]/div[2]/div').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="safesuser"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen124"]/div[3]/div').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen63"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="deviceType"]').click()
    sleep(1)
    # 红外精确测温
    browser.find_element_by_xpath('//*[@id="ext-gen176"]/div[2]/div').click()
    # SF6气体成分检测
    browser.find_element_by_xpath('//*[@id="ext-gen176"]/div[5]/div').click()

    sleep(1)
    browser.find_element_by_xpath('//*[@id="deviceType"]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen149"]').click()

    # 选择台账1
    sleep(3)
    browser.find_element_by_link_text('红外精确测温').click()

    # 设备列表
    # sleep(1)
    # browser.find_element_by_xpath('//*[@id="ext-gen294"]/div/table/thead/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen232"]/div[1]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen232"]/div[2]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen232"]/div[3]/table/tbody/tr/td[2]/div/div').click()

    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen253"]/div/table/tbody/tr/td[2]/div/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen273"]/div/table/thead/tr/td[2]/div').click()

    # ****************************************************************************
    # 选择台账2
    sleep(3)
    browser.find_element_by_link_text('SF6气体成分检测').click()

    # 设备列表
    # sleep(1)
    # browser.find_element_by_xpath('//*[@id="ext-gen294"]/div/table/thead/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen318"]/div[1]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen318"]/div[2]/table/tbody/tr/td[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="ext-gen318"]/div[3]/table/tbody/tr/td[2]/div/div').click()

    # 检测仪器
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen339"]/div/table/tbody/tr/td[2]/div/div').click()

    # 人员列表
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen359"]/div/table/thead/tr/td[2]/div').click()

    # 保存
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen65"]').click()
    sleep(10)

    a = a + 1

    print 'test项目test'

    sleep(1)
    browser.quit()

# ************************************************安卓录入数据******************************************
for x in range(1, 6):

    from appium import webdriver
    from time import sleep
    import random

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.0.2'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = 'Android Emulator'
    # desired_caps['udid'] = 'UW9555Q899999999'
    desired_caps['appPackage'] = 'com.sito.edetection'
    desired_caps['appActivity'] = '.view.login.LoginActivity'
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # sleep(5)
    # driver.find_element_by_id('edit_username').set_value('caishoujun')
    # driver.find_element_by_id('edit_password').set_value('123456')
    # driver.find_element_by_id('btn_signin').click()

    # 进入【检测任务】
    sleep(5)
    el = driver.find_element_by_id('com.sito.edetection:id/ll_check_project')
    el.click()

    # 开始项目
    sleep(5)
    driver.find_element_by_id('menu').click()
    sleep(1)
    driver.find_element_by_id('downloadTaskIv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    # 进入工程
    sleep(3)
    el = driver.find_elements_by_id('text_pro_name')[0]
    el.click()
    sleep(1)

    # 上传工程现场照片
    # 项目照片
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/tv_take_photo')
    el.click()

    # 选择
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/imageIv')
    el.click()

    # 相册
    sleep(1)
    el = driver.find_elements_by_id('com.sito.edetection:id/md_title')[1]
    el.click()

    # 进入相册程序
    sleep(1)
    driver.wait_activity('com.android.documentsui', 2)

    # 选择图片1
    driver.implicitly_wait(10)
    sleep(6)
    el = driver.find_elements_by_id('com.android.documentsui:id/icon_thumb')[0]
    el.click()

    # 返回
    sleep(6)
    el = driver.find_element_by_class_name('android.widget.ImageButton')
    el.click()

    # 红外精确测温
    sleep(1)
    driver.find_elements_by_id('text_name')[0].click()

    # 检测记时开始按钮
    sleep(1)
    driver.find_element_by_id('off_report_tv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    # 图片编号原始值
    # noinspection PyRedeclaration
    ff = 1

    for i in range(1, 6, 2):
        # ******************************************************************************************
        # 1* 设备数据输入
        sleep(1)
        el = driver.find_elements_by_id('layout_item')[i]
        el.click()

        # 第一条数据-本体
        driver.implicitly_wait(10)
        el = driver.find_elements_by_id('editBtn')[0]
        el.click()

        # 红外图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[1]
        el.set_value(ff)

        # 正常图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[2]
        el.set_value(ff + 1)

        # 最高温度
        sleep(1)
        el = driver.find_elements_by_id('edit')[3]
        el.set_value(random.randrange(10, 29))

        sleep(1)
        driver.find_element_by_id('saveTv').click()
        sleep(1)

        # (x,y, x,y, time)
        driver.swipe(500, 1500, 500, 500, 1000)
        sleep(3)

        # 第二条数据-冷却器
        sleep(1)
        el = driver.find_elements_by_id('editBtn')[1]
        el.click()

        # 红外图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[1]
        el.set_value(ff + 2)

        # 正常图片编号
        sleep(1)
        el = driver.find_elements_by_id('edit')[2]
        el.set_value(ff + 3)

        # 最高温度
        sleep(1)
        el = driver.find_elements_by_id('edit')[3]
        el.set_value(random.randrange(30, 60))

        sleep(1)
        driver.find_element_by_id('saveTv').click()
        sleep(1)

        # 返回按键
        driver.find_element_by_class_name('android.widget.ImageButton').click()
        sleep(1)

        # 图片编号自增
        ff = ff + 4

    # 检测记时结束按钮
    sleep(1)
    driver.find_element_by_id('off_report_tv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    # 添加环境数据
    sleep(1)
    driver.find_element_by_id('com.sito.edetection:id/envTv').click()
    # 湿度
    sleep(1)
    el = driver.find_elements_by_id('com.sito.edetection:id/enter')[0]
    el.set_value(random.randrange(20, 30))
    # 温度
    sleep(1)
    el = driver.find_elements_by_id('com.sito.edetection:id/enter')[1]
    el.set_value(random.randrange(20, 30))
    # 保存
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/menu')
    el.click()

    # 上传红外现场照片
    # 项目照片
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/tv_take_photo')
    el.click()

    # 选择
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/imageIv')
    el.click()

    # 相册
    sleep(1)
    el = driver.find_elements_by_id('com.sito.edetection:id/md_title')[1]
    el.click()

    # 进入相册程序
    sleep(1)
    driver.wait_activity('com.android.documentsui', 2)

    # 选择图片2
    sleep(6)
    el = driver.find_elements_by_id('com.android.documentsui:id/icon_thumb')[1]
    el.click()

    # 返回
    sleep(6)
    el = driver.find_element_by_class_name('android.widget.ImageButton')
    el.click()

    # 上传数据
    sleep(1)
    driver.find_element_by_id('menu').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(5)

    # 完成上传
    sleep(1)
    driver.find_element_by_id('btn_finish').click()

    # 返回按键
    driver.find_element_by_class_name('android.widget.ImageButton').click()

    # ******************************************************************

    # SF6气体成分检测
    sleep(1)
    driver.find_elements_by_id('text_name')[1].click()

    # 检测记时开始按钮
    sleep(1)
    driver.find_element_by_id('off_report_tv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    for i in range(1, 6, 2):
        # 1#电抗器
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/layout_item')[i]
        el.click()

        # 数据录入
        sleep(1)
        el = driver.find_elements_by_id('editBtn')[0]
        el.click()

        # SO2
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[1]
        el.set_value(random.uniform(0, 2))

        # H2S
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[2]
        el.set_value(random.uniform(0, 2))

        # CO
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[3]
        el.set_value(random.uniform(0, 2))

        # 纯度
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[4]
        el.set_value(random.randrange(95, 99))

        # 湿度
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[5]
        el.set_value(random.uniform(0, 2))

        # HF
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[6]
        el.set_value(random.uniform(0, 2))

        # 露点
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[7]
        el.set_value(random.uniform(0, 2))

        # CF4
        sleep(1)
        el = driver.find_elements_by_id('com.sito.edetection:id/edit')[8]
        el.set_value(random.uniform(0, 2))

        # 保存
        sleep(1)
        el = driver.find_element_by_id('com.sito.edetection:id/saveTv')
        el.click()

        # 返回按键
        driver.find_element_by_class_name('android.widget.ImageButton').click()
        sleep(1)

    # 检测记时结束按钮
    sleep(1)
    driver.find_element_by_id('off_report_tv').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(1)

    # 添加环境数据
    sleep(1)
    driver.find_element_by_id('com.sito.edetection:id/envTv').click()
    # 湿度
    sleep(1)
    el = driver.find_elements_by_id('com.sito.edetection:id/enter')[0]
    el.set_value(random.randrange(20, 30))
    # 温度
    sleep(1)
    el = driver.find_elements_by_id('com.sito.edetection:id/enter')[1]
    el.set_value(random.randrange(20, 30))
    # 保存
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/menu')
    el.click()

    # 上传SF6现场图片
    # 项目照片
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/tv_take_photo')
    el.click()

    # 选择
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/imageIv')
    el.click()

    # 相册
    sleep(1)
    el = driver.find_elements_by_id('com.sito.edetection:id/md_title')[1]
    el.click()

    # 进入相册程序
    sleep(1)
    driver.wait_activity('com.android.documentsui', 2)

    # 选择图片3
    sleep(6)
    el = driver.find_elements_by_id('com.android.documentsui:id/icon_thumb')[2]
    el.click()

    # 返回
    sleep(6)
    el = driver.find_element_by_class_name('android.widget.ImageButton')
    el.click()

    # 上传数据
    sleep(1)
    driver.find_element_by_id('menu').click()
    sleep(1)
    driver.find_element_by_id('md_buttonDefaultPositive').click()
    sleep(5)

    # 完成上传
    sleep(1)
    driver.find_element_by_id('btn_finish').click()

    # 返回按键
    driver.find_element_by_class_name('android.widget.ImageButton').click()

    sleep(3)
    driver.quit()

    # *************************BS上传图片***********************************************
    from selenium import webdriver
    from time import sleep
    import os

    browser = webdriver.Chrome()
    # browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    # browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    browser.find_element_by_id("userId").send_keys("15609100803")
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/button').click()

    sleep(3)
    browser.find_element_by_xpath('//*[@id="ext-gen29"]/b').click()
    sleep(1)
    browser.find_element_by_link_text('数据上传').click()
    sleep(1)

    # 框架转换
    sleep(1)
    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/workflow/task_data_upload_list.jsp")

    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen17"]/div[1]/table/tbody/tr/td[6]/div/a').click()

    # 框架转换
    sleep(1)
    browser.switch_to.parent_frame()
    el = browser.find_element_by_xpath('//*[@id="ext-gen34"]/iframe')
    browser.switch_to.frame(el)

    # 上传图谱
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen17"]').click()

    # 添加
    sleep(2)
    browser.find_element_by_id('SWFUpload_0').click()
    sleep(1)

    # 调用upflie.exe上传程序
    os.system("D:\\upfile515.exe")

    sleep(3)
    # 上传
    browser.find_element_by_xpath('//*[@id="ext-gen124"]').click()
    # 等待
    sleep(30)
    browser.find_element_by_xpath('//*[@id="ext-gen96"]').click()

    sleep(3)
    browser.quit()

    # *************************BS认证***************************************************
    from selenium import webdriver

    for j in range(1, 3):
        browser = webdriver.Chrome()
        # browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
        # browser.maximize_window()

        browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
        browser.find_element_by_id("userId").send_keys("15609100803")
        browser.find_element_by_id("password").send_keys("123456")
        browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[3]/button").click()

        sleep(3)
        browser.find_element_by_xpath('//*[@id="ext-gen29"]/b').click()
        sleep(1)

        sleep(1)
        browser.find_element_by_link_text('数据审核').click()
        sleep(1)

        sleep(1)
        browser.switch_to.frame("mainFrame")
        browser.switch_to.frame('/sito2000/workflow/task_data_check_list.jsp')

        sleep(1)
        browser.find_element_by_xpath('//*[@id="ext-gen17"]/div[1]/table/tbody/tr/td[6]/div/a').click()
        sleep(1)

        #
        sleep(1)
        browser.switch_to.parent_frame()
        el = browser.find_element_by_xpath('//*[@id="ext-gen34"]/iframe')
        browser.switch_to.frame(el)

        sleep(1)
        browser.find_element_by_xpath('//*[@id="ext-gen13"]').click()

        sleep(3)
        browser.quit()

    # *******************************app上删除项目************************************
    from appium import webdriver
    from time import sleep

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.0.2'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = 'Android Emulator'
    # desired_caps['udid'] = 'UW9555Q899999999'
    desired_caps['appPackage'] = 'com.sito.edetection'
    desired_caps['appActivity'] = '.view.login.LoginActivity'
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 进入【检测任务】
    sleep(10)
    el = driver.find_element_by_id('com.sito.edetection:id/ll_check_project')
    el.click()

    # 长按项目
    sleep(3)
    driver.tap([(500, 300)], 2000)
    # 确定是否删除
    sleep(1)
    el = driver.find_element_by_id('com.sito.edetection:id/md_buttonDefaultPositive')
    el.click()

    sleep(3)
    driver.quit()

    # ***************************BS上报告******************************
    from selenium import webdriver
    from time import sleep
    import time

    browser = webdriver.Chrome()
    # browser = webdriver.Chrome(executable_path='/Users/xuzhen/chromedriver')
    # browser.maximize_window()

    browser.get("http://192.168.8.88:8080/sito2000/login.jsp")
    # browser.get("http://114.215.94.141:8081/SITO2000/login.jsp")
    browser.find_element_by_id("userId").send_keys("15609100803")
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/button').click()

    sleep(3)
    browser.find_element_by_xpath('//*[@id="ext-gen35"]/b').click()
    sleep(1)
    browser.find_element_by_link_text("未生成报告").click()
    sleep(1)

    # 跳入框架
    browser.switch_to.frame("mainFrame")
    browser.switch_to.frame("/sito2000/workflow/no_generated_report_list.jsp")

    # 选择对应报告并生成报告
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen25"]/div[1]/table/tbody/tr/td[6]/div/a').click()
    # 生成确定
    sleep(1)
    browser.find_element_by_xpath('//*[@id="ext-gen94"]').click()

    sleep(3)
    browser.quit()
