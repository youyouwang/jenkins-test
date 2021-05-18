from selenium import webdriver
from selenium import *
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from lib.web_auto import *
import time
import tkinter
from tkinter import *

#去掉自动化控制title
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)
#浏览器最大化
driver.maximize_window()
driver.get('file:///C:/Users/wangyouyou/Desktop/data-open-web/index.html#/index')
sleep(1)

window1 = tkinter.Tk()
# 标题栏名称
window1.title('数据开放平台')
# 去掉tkinter标题栏
#root.overrideredirect(True)
#定义窗口的宽和高
width1 = 300
height1 = 100
screenwidth1 = window1.winfo_screenwidth()
screenheight1 = window1.winfo_screenheight()
#定义窗口在页面居中显示
alignstr1 = '%dx%d+%d+%d' % (width1, height1, (screenwidth1 - width1) / 2, (screenheight1 - height1) / 2)
window1.geometry(alignstr1)
# 放一个标签将tkinter窗口的背景盖为白色
lbTime1 = tkinter.Label(window1, fg='black', bg='white', width=50, height=50)
lbTime1.place(x=0, y=0)
# 放一个标签文字显示在tkinter窗口（窗口，文本内容，字体类型及大小，字体颜色，背景颜色，标签相对于窗口的x，y位置）
lbl1 = Label(window1, text='1、首页预览', font=('microsoft yahei', 16),fg='black', bg='white', padx='70', pady='30')
# 显示标签内容
lbl1.grid(column=0, row=0)
window1.after(5000, window1.destroy)
window1.mainloop()

sleep(1)
#浏览器滑到主题分类/部门分类
js="window.scrollTo(0,document.body.scrollHeight/5)"
driver.execute_script(js)
sleep(1)
#浏览器滑到最新数据
js="window.scrollTo(0,document.body.scrollHeight/2.2)"
driver.execute_script(js)
sleep(1)
#回到顶部
js="window.scrollTo(0,0)"
driver.execute_script(js)
sleep(2)
elenment=driver.find_element_by_id('tab-second')
elenment.click()
sleep(1)
js="window.scrollTo(0,document.body.scrollHeight/2.5)"
driver.execute_script(js)
sleep(1)
#回到顶部
js="window.scrollTo(0,0)"
driver.execute_script(js)
sleep(2)
#定义第二个窗口

window2 = tkinter.Tk()
window2.title('数据开放平台')
width2 = 350
height2 = 100
screenwidth2 = window2.winfo_screenwidth()
screenheight2 = window2.winfo_screenheight()
alignstr2 = '%dx%d+%d+%d' % (width2, height2, (screenwidth2 - width2) / 2, (screenheight2 - height2) / 2)
window2.geometry(alignstr2)
lbTime2 = tkinter.Label(window2, fg='black', bg='white', width=50, height=50)
lbTime2.place(x=0, y=0)
lbl2 = Label(window2, text='2、数据开放页面功能预览', font=("microsoft yahei",16), fg='black', bg='white', padx='60', pady='30')
lbl2.grid(column=0, row=0)
window2.after(5000, window2.destroy)
window2.mainloop()

#定位数据开放元素并点击
elenment=driver.find_element_by_css_selector('#tabNav li:nth-child(2)>span')
elenment.click()
sleep(2)

window3 = tkinter.Tk()
window3.title('数据开放平台')
width3 = 500
height3 = 400
screenwidth3 = window3.winfo_screenwidth()
screenheight3 = window3.winfo_screenheight()
alignstr3 = '%dx%d+%d+%d' % (width3, height3, (screenwidth3 - width3) / 2, (screenheight3 - height3) / 2)
window3.geometry(alignstr3)
lbTime3 = tkinter.Label(window3, fg='black', bg='white', width=80, height=80)
lbTime3.place(x=0, y=0)
lbl3 = Label(window3, text='3、数据开放页面：\n\n左侧可查看开放数据的来源单位\n\n上侧可查看开放数据的分类\n\n该页面可按关键词搜索开放数据\n\n点击任意一条开放数据可查看开放数据的详情',
             font=("microsoft yahei", 16), fg='black', bg='white', padx='50', pady='70')
lbl3.grid(column=0, row=0)
window3.after(5000, window3.destroy)
window3.mainloop()
sleep(1)

#定位数据开放-第一条开放数据记录的元素并点击
elenment1=driver.find_element_by_css_selector('.list-box>div:nth-child(1)>div:nth-child(1)')
elenment1.click()
sleep(2)
#滚动查看开放数据详情页
scroll_to_bottom(driver)
#定义第四个页面
window4 = tkinter.Tk()
window4.title('数据开放平台')
width4 = 400
height4 = 100
screenwidth4 = window4.winfo_screenwidth()
screenheight4 = window4.winfo_screenheight()
alignstr4 = '%dx%d+%d+%d' % (width4, height4, (screenwidth4 - width4) / 2, (screenheight4 - height4) / 2)
window4.geometry(alignstr4)
lbTime4 = tkinter.Label(window4, fg='black', bg='white', width=80, height=80)
lbTime4.place(x=0, y=0)
lbl4 = Label(window4, text='4、点击数据预览可查看数据项字段信息', font=("microsoft yahei", 16), fg='black', bg='white', padx='20', pady='30')
lbl4.grid(column=0, row=0)
window4.after(5000, window4.destroy)
window4.mainloop()
sleep(1)

#将鼠标移到预览按钮上
ac = ActionChains(driver)
# 鼠标移动到 元素上
ac.move_to_element(
    driver.find_elements_by_css_selector('.sjkfList button')[0]
).perform()
sleep(0.5)

#找到预览按钮并点击
driver.find_elements_by_css_selector('.sjkfList button')[0].click()
sleep(2)
driver.back()
sleep(1)

window5 = tkinter.Tk()
window5.title('数据开放平台')
width5 = 560
height5 =100
screenwidth5 = window5.winfo_screenwidth()
screenheight5 = window5.winfo_screenheight()
alignstr5 = '%dx%d+%d+%d' % (width5, height5, (screenwidth5 - width5) / 2, (screenheight5 - height5) / 2)
window5.geometry(alignstr5)
lbTime5 = tkinter.Label(window5, fg='black', bg='white', width=80, height=80)
lbTime5.place(x=0, y=0)
lbl5 = Label(window5, text='5、点击数据图谱可即图像化展示该数据集的各类信息', font=("microsoft yahei", 16), fg='black', bg='white',padx='30', pady='30')
lbl5.grid(column=0, row=0)
window5.after(5000, window5.destroy)
window5.mainloop()


# 鼠标移动到数据图谱元素上
ac1 = ActionChains(driver)
ac1.move_to_element(
    driver.find_elements_by_css_selector('.sjkfList button')[1]
).perform()
sleep(0.5)
#找到数据图谱并点击
driver.find_elements_by_css_selector('.sjkfList button')[1].click()
sleep(2)
driver.back()
sleep(1)


window6 = tkinter.Tk()
window6.title('数据开放平台')
width6 = 550
height6 =100
screenwidth6 = window6.winfo_screenwidth()
screenheight6 = window6.winfo_screenheight()
alignstr6 = '%dx%d+%d+%d' % (width6, height6, (screenwidth6 - width6) / 2, (screenheight6 - height6) / 2)
window6.geometry(alignstr6)
lbTime6 = tkinter.Label(window6, fg='black', bg='white', width=80, height=80)
lbTime6.place(x=0, y=0)
lbl6 = Label(window6, text='6、点击接口预览可查看该开放数据申请的接口信息', font=("microsoft yahei", 16), fg='black', bg='white',padx='30', pady='30')
lbl6.grid(column=0, row=0)
window6.after(5000, window6.destroy)
window6.mainloop()

ac2 = ActionChains(driver)
ac2.move_to_element(
    driver.find_elements_by_css_selector('.sjkfList button')[2]
).perform()
sleep(0.5)

driver.find_elements_by_css_selector('.sjkfList button')[2].click()
sleep(2)
driver.back()
sleep(1)

window7 = tkinter.Tk()
window7.title('数据开放平台')
# 去掉tkinter标题栏
#root.overrideredirect(True)
width7 = 520
height7 =100
screenwidth7 = window7.winfo_screenwidth()
screenheight7 = window7.winfo_screenheight()
alignstr7 = '%dx%d+%d+%d' % (width7, height7, (screenwidth7 - width7) / 2, (screenheight7 - height7) / 2)
window7.geometry(alignstr7)
# 放一个标签将tkinter窗口的背景盖为白色
lbTime7 = tkinter.Label(window7, fg='black', bg='white', width=80, height=80)
lbTime7.place(x=0, y=0)
# 放一个标签文字显示在tkinter窗口（窗口，文本内容，字体类型及大小，字体颜色，背景颜色，标签相对于窗口的x，y位置）
lbl7 = Label(window7, text='7、点击接口申请可利用该开放数据信息申请接口', font=("microsoft yahei", 16), fg='black', bg='white',padx='30', pady='30')
# 显示标签内容
lbl7.grid(column=0, row=0)
# 窗口显示倒计时
window7.after(5000, window7.destroy)
window7.mainloop()

ac3 = ActionChains(driver)
# 鼠标移动到数据图谱元素上
ac3.move_to_element(
    driver.find_elements_by_css_selector('.sjkfList button')[3]
).perform()
sleep(0.5)
driver.find_elements_by_css_selector('.sjkfList button')[3].click()
sleep(2)
driver.back()
sleep(1)

js="window.scrollTo(0,document.body.scrollHeight/3.5)"
driver.execute_script(js)
sleep(1)
window8 = tkinter.Tk()
window8.title('数据开放平台')
width8 = 500
height8 =350
screenwidth8 = window8.winfo_screenwidth()
screenheight8 = window8.winfo_screenheight()
alignstr8 = '%dx%d+%d+%d' % (width8, height8, (screenwidth8 - width8) / 2, (screenheight8 - height8) / 2)
window8.geometry(alignstr8)
lbTime8 = tkinter.Label(window8, fg='black', bg='white', width=70, height=50)
lbTime8.place(x=0, y=0)
lbl8 = Label(window8, text='8、查看数据项、分页接口、相关应用\n\n数据项：该开放数据关联的数据字段信息\n\n分页接口：该条开放数据接口的访问地址\n\n相关应用：该条开放数据申请的应用信息',
             font=("microsoft yahei", 16), fg='black', bg='white',padx='60', pady='60')
lbl8.grid(column=0, row=0)
window8.after(6000, window8.destroy)
window8.mainloop()


ac4 = ActionChains(driver)
ac4.move_to_element(
    driver.find_element_by_id('tab-1')
).perform()
sleep(0.5)
driver.find_element_by_id('tab-1').click()
sleep(2)

ac5 = ActionChains(driver)
ac5.move_to_element(
    driver.find_element_by_id('tab-2')
).perform()
driver.find_element_by_id('tab-2').click()
sleep(2)

js="window.scrollTo(0,document.body.scrollHeight/1.8)"
driver.execute_script(js)
sleep(1)

window9 = tkinter.Tk()
window9.title('数据开放平台')
width9 =900
height9 =100
screenwidth9 = window9.winfo_screenwidth()
screenheight9 = window9.winfo_screenheight()
alignstr9 = '%dx%d+%d+%d' % (width9, height9, (screenwidth9 - width9) / 2, (screenheight9 - height9) / 2)
window9.geometry(alignstr9)
lbTime9 = tkinter.Label(window9, fg='black', bg='white', width=150, height=150)
lbTime9.place(x=0, y=0)
lbl9 = Label(window9, text='9、数据开放评价：用户可在此对该条开放数据作出评分及评论，提交后需管理员审核', font=("microsoft yahei", 16),
            fg='black', bg='white',padx='50', pady='30')
lbl9.grid(column=0, row=0)
window9.after(5000, window9.destroy)
window9.mainloop()

js="window.scrollTo(0,0)"
driver.execute_script(js)
sleep(1)

window10 = tkinter.Tk()
window10.title('数据开放平台')
width10 = 300
height10 = 100
screenwidth10 = window10.winfo_screenwidth()
screenheight10 = window10.winfo_screenheight()
alignstr10 = '%dx%d+%d+%d' % (width10, height10, (screenwidth10 - width10) / 2, (screenheight10 - height10) / 2)
window10.geometry(alignstr10)
lbTime10 = tkinter.Label(window10, fg='black', bg='white', width=50, height=50)
lbTime10.place(x=0, y=0)
lbl10 = Label(window10, text='10、应用成果页面预览', font=("microsoft yahei", 16), fg='black', bg='white', padx='45', pady='30')
lbl10.grid(column=0, row=0)
window10.after(5000, window10.destroy)
window10.mainloop()

#定位到应用成果页面并点击
driver.find_element_by_css_selector('#tabNav li:nth-child(3)>span').click()
sleep(2)

window11 = tkinter.Tk()
window11.title('数据开放平台')
width11 = 380
height11 = 300
screenwidth11 = window11.winfo_screenwidth()
screenheight11 = window11.winfo_screenheight()
alignstr11 = '%dx%d+%d+%d' % (width11, height11, (screenwidth11 - width11) / 2, (screenheight11 - height11) / 2)
window11.geometry(alignstr11)
lbTime11 = tkinter.Label(window11, fg='black', bg='white', width=50, height=50)
lbTime11.place(x=0, y=0)
lbl11 = Label(window11, text='11、应用成果页面：\n\n左侧为应用成果分类\n\n右侧为应用成果数据\n\n任意选择一条数据可查看成果详情',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='30', pady='50')
lbl11.grid(column=0, row=0)
window11.after(6000, window11.destroy)
window11.mainloop()
sleep(1)

#定位到第一条成果数据
driver.find_element_by_css_selector('.list-box>.list-center:nth-child(1)').click()
sleep(2)
scroll_to_bottom(driver)
sleep(2)
window12 = tkinter.Tk()
window12.title('数据开放平台')
width12 = 710
height12 = 100
screenwidth12 = window12.winfo_screenwidth()
screenheight12 = window12.winfo_screenheight()
alignstr12 = '%dx%d+%d+%d' % (width12, height12, (screenwidth12 - width12) / 2, (screenheight12 - height12) / 2)
window12.geometry(alignstr12)
lbTime12 = tkinter.Label(window12, fg='black', bg='white', width=100, height=100)
lbTime12.place(x=0, y=0)
lbl12 = Label(window12, text='12、应用成果：显示该成果的基本信息，扫描右侧二维码可下载该应用',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='30', pady='30')
lbl12.grid(column=0, row=0)
window12.after(5000, window12.destroy)

window12.mainloop()
sleep(1)

js="window.scrollTo(0,document.body.scrollHeight/4)"
driver.execute_script(js)
sleep(2)

window13 = tkinter.Tk()
window13.title('数据开放平台')
width13 = 820
height13 = 100
screenwidth13 = window13.winfo_screenwidth()
screenheight13 = window13.winfo_screenheight()
alignstr13 = '%dx%d+%d+%d' % (width13, height13, (screenwidth13 - width13) / 2, (screenheight13 - height13) / 2)
window13.geometry(alignstr13)
lbTime13 = tkinter.Label(window13, fg='black', bg='white', width=120, height=120)
lbTime13.place(x=0, y=0)
lbl13 = Label(window13, text='13、应用评价：用户可在此对该条开放数据作出评分及评论，提交后需管理员审核',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='30', pady='30')
lbl13.grid(column=0, row=0)
window13.after(5000, window13.destroy)
window13.mainloop()
sleep(2)

js="window.scrollTo(0,0)"
driver.execute_script(js)
sleep(1)

window14 = tkinter.Tk()
window14.title('数据开放平台')
width14 = 300
height14 = 100
screenwidth14 = window14.winfo_screenwidth()
screenheight14 = window14.winfo_screenheight()
alignstr14 = '%dx%d+%d+%d' % (width14, height14, (screenwidth14 - width14) / 2, (screenheight14 - height14) / 2)
window14.geometry(alignstr14)
lbTime14 = tkinter.Label(window14, fg='black', bg='white', width=50, height=50)
lbTime14.place(x=0, y=0)
lbl14 = Label(window14, text='14、开发者中心预览', font=("microsoft yahei", 16), fg='black', bg='white', padx='45', pady='30')
lbl14.grid(column=0, row=0)
window14.after(5000, window14.destroy)
window14.mainloop()

#定位到开发者中心并点击
driver.find_element_by_css_selector('#tabNav li:nth-child(4)>span').click()
sleep(2)

window15 = tkinter.Tk()
window15.title('数据开放平台')
width15 = 800
height15 = 100
screenwidth15 = window15.winfo_screenwidth()
screenheight15 = window15.winfo_screenheight()
alignstr15 = '%dx%d+%d+%d' % (width15, height15, (screenwidth15 - width15) / 2, (screenheight15 - height15) / 2)
window15.geometry(alignstr15)
lbTime15 = tkinter.Label(window15, fg='black', bg='white', width=120, height=120)
lbTime15.place(x=0, y=0)
lbl15 = Label(window15, text='15、开发者中心：介绍了数据开放平台简介及接口、应用申请接入等使用指南',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='30', pady='30')
lbl15.grid(column=0, row=0)
window15.after(5000, window15.destroy)
window15.mainloop()
sleep(3)


window16 = tkinter.Tk()
window16.title('数据开放平台')
width16 = 300
height16 = 100
screenwidth16 = window16.winfo_screenwidth()
screenheight16 = window16.winfo_screenheight()
alignstr16 = '%dx%d+%d+%d' % (width16, height16, (screenwidth16 - width16) / 2, (screenheight16 - height16) / 2)
window16.geometry(alignstr16)
lbTime16 = tkinter.Label(window16, fg='black', bg='white',  width=50, height=50)
lbTime16.place(x=0, y=0)
lbl16 = Label(window16, text='16、个人中心预览',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='50', pady='30')
lbl16.grid(column=0, row=0)
window16.after(5000, window16.destroy)
window16.mainloop()
sleep(1)


#定位到个人中心
driver.find_element_by_tag_name('a').click()

window17 = tkinter.Tk()
window17.title('数据开放平台')
width17 =650
height17 = 100
screenwidth17 = window17.winfo_screenwidth()
screenheight17 = window17.winfo_screenheight()
alignstr17 = '%dx%d+%d+%d' % (width17, height17, (screenwidth17 - width17) / 2, (screenheight17 - height17) / 2)
window17.geometry(alignstr17)
lbTime17 = tkinter.Label(window17, fg='black', bg='white',  width=120, height=120)
lbTime17.place(x=0, y=0)
lbl17 = Label(window17, text='17、个人信息：显示用户个人的姓名、身份证号等基本信息',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='45', pady='30')
lbl17.grid(column=0, row=0)
window17.after(5000, window17.destroy)
window17.mainloop()
sleep(2)

#定位个人中心-我的应用页面
driver.find_elements_by_xpath("//*[@class='r-list']/li")[1].click()
sleep(1)

window18 = tkinter.Tk()
window18.title('数据开放平台')
width18 =650
height18 = 100
screenwidth18 = window18.winfo_screenwidth()
screenheight18 = window18.winfo_screenheight()
alignstr18 = '%dx%d+%d+%d' % (width18, height18, (screenwidth18 - width18) / 2, (screenheight18 - height18) / 2)
window18.geometry(alignstr18)
lbTime18 = tkinter.Label(window18, fg='black', bg='white',  width=120, height=120)
lbTime18.place(x=0, y=0)
lbl18 = Label(window18, text='18、我的应用：用户可以在此查看自己申请或者添加的应用信息',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='30', pady='30')
lbl18.grid(column=0, row=0)
window18.after(5000, window18.destroy)
window18.mainloop()
sleep(2)

window19 = tkinter.Tk()
window19.title('数据开放平台')
width19 =600
height19 = 100
screenwidth19 = window19.winfo_screenwidth()
screenheight19 = window19.winfo_screenheight()
alignstr19 = '%dx%d+%d+%d' % (width19, height19, (screenwidth19 - width19) / 2, (screenheight19 - height19) / 2)
window19.geometry(alignstr19)
lbTime19 = tkinter.Label(window19, fg='black', bg='white',  width=120, height=120)
lbTime19.place(x=0, y=0)
lbl19 = Label(window19, text='19、点击查看：可看到该应用对应的接口申请信息',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='50', pady='30')
lbl19.grid(column=0, row=0)
window19.after(5000, window19.destroy)
window19.mainloop()
sleep(1)
driver.find_elements_by_css_selector(".el-table__row .cell>.el-button")[0].click()

sleep(2)
driver.find_elements_by_xpath("//*[@class='r-list']/li")[1].click()
sleep(2)

window20 = tkinter.Tk()
window20.title('数据开放平台')
width20 =900
height20 = 100
screenwidth20 = window20.winfo_screenwidth()
screenheight20 = window20.winfo_screenheight()
alignstr20 = '%dx%d+%d+%d' % (width20, height20, (screenwidth20 - width20) / 2, (screenheight20 - height20) / 2)
window20.geometry(alignstr20)
lbTime20 = tkinter.Label(window20, fg='black', bg='white',  width=150, height=150)
lbTime20.place(x=0, y=0)
lbl20 = Label(window20, text='20、点击添加应用，用户可编辑应用信息并提交审核，审核通过后可上架到数据开放平台',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='50', pady='30')
lbl20.grid(column=0, row=0)
window20.after(5000, window20.destroy)
window20.mainloop()
sleep(1)


#定位到我的应用-添加应用界面
driver.find_element_by_css_selector(".add-APP>.el-icon-circle-plus-outline").click()
sleep(2)
#点击返回
driver.find_elements_by_css_selector(".el-form-item__content>.el-button--primary")[1].click()
sleep(2)
#定位到个人中心-我的接口页面
driver.find_elements_by_xpath("//*[@class='r-list']/li")[2].click()
sleep(1)

window21 = tkinter.Tk()
window21.title('数据开放平台')
width21 =600
height21 = 100
screenwidth21 = window21.winfo_screenwidth()
screenheight21 = window21.winfo_screenheight()
alignstr21 = '%dx%d+%d+%d' % (width21, height21, (screenwidth21 - width21) / 2, (screenheight21 - height21) / 2)
window21.geometry(alignstr21)
lbTime21 = tkinter.Label(window21, fg='black', bg='white',  width=150, height=150)
lbTime21.place(x=0, y=0)
lbl21 = Label(window21, text='21、我的接口：可查看用户申请的接口信息、审核状态等',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='30', pady='30')
lbl21.grid(column=0, row=0)
window21.after(5000, window21.destroy)
window21.mainloop()
sleep(2)

window22 = tkinter.Tk()
window22.title('数据开放平台')
width22 =400
height22 = 300
screenwidth22 = window22.winfo_screenwidth()
screenheight22 = window22.winfo_screenheight()
alignstr22 = '%dx%d+%d+%d' % (width22, height22, (screenwidth22 - width22) / 2, (screenheight22 - height22) / 2)
window22.geometry(alignstr22)
lbTime22 = tkinter.Label(window22, fg='black', bg='white',  width=150, height=150)
lbTime22.place(x=0, y=0)
lbl22 = Label(window22, text='数据开放平台业务流程已演示完毕',
              font=("microsoft yahei", 16), fg='black', bg='white', padx='50', pady='130')
lbl22.grid(column=0, row=0)
window22.after(5000, window22.destroy)
window22.mainloop()
sleep(1)

driver.quit()

