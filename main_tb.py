from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import random
from lxml import etree
def login(user,passwd):
    print("开始登录")
    driver.get("http://jwzx.cqupt.edu.cn/login.php")
    try:
        driver.find_element_by_xpath(r'//*[@id="login-tysfrz"]/p[1]/a/img').click()
        time.sleep(0.5)
        driver.find_element_by_xpath(r'//*[@id="username"]').send_keys(user)
        driver.find_element_by_xpath(r'//*[@id="password"]').send_keys(passwd)
        driver.find_element_by_xpath(r'//*[@id="casLoginForm"]/div[1]/div[3]/input[2]').click()
        time.sleep(0.5)
        assert (driver.current_url.find('http://jwzx.cqupt.edu.cn/') != -1), "登录失败!"
        print("登录成功")
    except:
        print('网络异常')
def xpj():
    driver.get('http://jwzx.cqupt.edu.cn/jxpj/xpjstu.php')
    time.sleep(0.2)
    temp = driver.find_element_by_xpath(r'//*[@id="xpjTab-ByJxb"]/table/tbody').get_attribute('innerHTML')
    html=etree.HTML(temp)
    url=html.xpath(r'//tr//td//a[@class="xpjBtn"]/@href')
    for i in range(0,len(url)):
        driver.find_element_by_xpath('// *[ @ id = "xpjTab-ByJxb"] / table / tbody / tr['+str(i+1)+'] / td[7] / a / img').click()
        tb()
        time.sleep(0.2)
def tb():
    time.sleep(1)
    driver.find_element_by_xpath(r'//*[@id="0-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="1-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="2-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="3-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="4-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="5-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="6-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="7-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="8-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="9-0"]').click()
    key1=getAdvantage()
    key2=getAdvantage()
    driver.find_element_by_xpath(r'//*[@id="popWindowPanel"]/form/table/tbody/tr[11]/td[2]/input').send_keys(key1)
    driver.find_element_by_xpath(r'//*[@id="popWindowPanel"]/form/table/tbody/tr[12]/td[2]/input').send_keys(key2)
    driver.find_element_by_xpath(r'//*[@id="popWindowPanel"]/form/div/button/span[2]').click()
    try:
        time.sleep(1)
        driver.execute_script('closeWindow()')
    except:
        pass
def fdy():
    url='http://jwzx.cqupt.edu.cn/jxpj/fdy.php'
    words='多融入学生生活'
    driver.get(url)
    driver.find_element_by_xpath(r'//*[@id="0-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="1-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="2-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="3-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="4-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="5-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="6-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="7-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="8-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="9-0"]').click()
    driver.find_element_by_xpath(r'//*[@id="fdyTabl-fdy"]/form/table/tbody/tr[11]/td[3]/input').send_keys(words)
    driver.find_element_by_xpath('//*[@id="fdyTabl-fdy"]/form/p/button').click()
    try:
        time.sleep(1)
        driver.execute_script('closeWindow()')
    except:
        pass
def bds():
    url='http://jwzx.cqupt.edu.cn/jxpj/fdy.php'
    driver.get(url)
    words = '多融入学生生活'
    driver.find_element_by_xpath('//*[@id="ui-id-2"]').click()
    opt1=driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[1]/td[8]/select')
    opt2=driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[2]/td[8]/select')
    opt3 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[3]/td[8]/select')
    opt4 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[4]/td[8]/select')
    opt5 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[5]/td[8]/select')
    opt6 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[6]/td[8]/select')
    opt7 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[7]/td[8]/select')
    opt8 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[8]/td[8]/select')
    opt9 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[9]/td[8]/select')
    opt10 = driver.find_element_by_xpath(r'//*[@id="fdyTabl-bds"]/form/table/tbody/tr[10]/td[8]/select')
    Select(opt1).select_by_visible_text('10')
    Select(opt2).select_by_visible_text('10')
    Select(opt3).select_by_visible_text('10')
    Select(opt4).select_by_visible_text('10')
    Select(opt5).select_by_visible_text('10')
    Select(opt6).select_by_visible_text('10')
    Select(opt7).select_by_visible_text('10')
    Select(opt8).select_by_visible_text('10')
    Select(opt9).select_by_visible_text('10')
    Select(opt10).select_by_visible_text('10')
    driver.find_element_by_xpath('//*[@id="fdyTabl-bds"]/form/table/tbody/tr[11]/td[3]/input').send_keys(words)
    driver.find_element_by_xpath('//*[@id="fdyTabl-bds"]/form/p/button/span[2]').click()
    try:
        time.sleep(1)
        driver.execute_script('closeWindow()')
    except:
        pass
def getAdvantage():
    words=['老师会举一些贴近生活的例子来帮助理解知识',
'一丝不苟的教学方式','用一些生动有趣的例子来告诉大家句子或词语的含义与道理',
           '对于考试的各方面分别进行讲解分析，教我们方法','举例子，使印象更深刻',
           '老师经常举一些生活中的例子，让我们更好地理解所教知识',
           '讲故事形式，使人印象深刻','列出各种解（答）题方法（结构图)',
            '课外延伸',
           '知识点讲得很细，每当说到一种修辞手法总会举例子',
           '上课专门点看上去不认真的听课的人，有助于提神，并且用有趣的语言授课，让人放松',
          '让学生提出自己的疑问，并解决；举一些生动形象的例子']
    key=random.choice(words)
    return key


print('输入账号:')
username=input()
print('输入密码:')
passwd=input()
driver=webdriver.Chrome()
login(username,passwd)
#你可以选择功能评价
try:
    xpj() #学评教
    print('学评教 success')
except:
    print('学评教error')
try:
    fdy() #辅导员评价
    print('辅导员评价 success')
except:
    print('辅导员评价error')
try:
    bds() #班导师评价
    print('班导师评价 success')
except:
    print('班导师评价error')