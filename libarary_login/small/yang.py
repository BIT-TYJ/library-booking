"""模拟登录预约系统+自动预约"""
import requests
from selenium import webdriver
import time
url = "https://passport2.chaoxing.com/login?newversion=true&refer=http%3A%2F%2Freserve.chaoxing.com%2Ffront%2Fweb%2Fapps%2Freservepc%2Fitem%3FitemId%3D6241%26reserveId%3D3646%26fidEnc%3D9435181f6d5f71dc"
username = '13615605026'
pwd = 'yzy20020622'
# 判断是否有错误提示弹出框
def alert_is_present(driver):
    try:
        alert = driver.switch_to.alert
        alert.text
        return alert
    except:
        return False

if __name__ == '__main__':
	#############登录
    
    driver=webdriver.Firefox()
    while 1:
        driver.get(url)
        driver.find_element_by_id("phone").send_keys("13615605026")
        driver.find_element_by_id("pwd").send_keys("yzy20020622")
        login=driver.find_element_by_id("loginBtn" ) #根据id找到登录按钮
        login.click()
        time.sleep(4)

    
        #############预约
        yuyue=driver.find_elements_by_class_name('row1'and'data_td')      #and not 'my_order'   and not "other_order"
        if yuyue!=[]:
            #开始预约
            num_of_box=0  #判断处在四个中的哪个框  左上  左下  右上 右下  
            num_of_reserved=0  #统计已预约的次数，达到两次则停止抢座
            # for i in yuyue:
            #     if "已预约" in i.text:
            #         num_of_reserved= num_of_reserved+1
            # #只有已预约次数小于2次才进行抢座，否则抢不了  这个好像出bug了，网站上可以预约4次
            # if  num_of_reserved < 4:        
            for i in yuyue: 
                num_of_box = num_of_box + 1
                if "预约"  not in i.text:       #排除"已预约"和"不可预约"两种情况
                    if "60/60" not in i.text:
                        i.click()
                        # print(num_of_box)
                        #点击  "提交预约"
                        driver.find_element_by_class_name('make_bottom').click()  
                        time.sleep(2)
                        # if alert_is_present(driver):   ## 如果有弹出框 :提示未选择时段 点击确定，此时人数已满，预约不了了
                        #     driver.switch_to.alert.accept()
                        #     time.sleep(3)
                        # #点击"确定",表示确定预约
                        # else :
                        driver.find_element_by_class_name('ml20').click()  
                    else:
                        print("人满了")
                else:
                    print("现在没有可预约但没有预约的时间段")
        else:
            print("error")
        time.sleep(60)
    
