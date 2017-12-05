from selenium import webdriver
import time
import os
import requests
import datetime
import sys
from github.python_log import JobLogging

class Huaban():
    # 实例化日志
    def __init__(self, log_lev='INFO'):
        date_today = datetime.datetime.now().date()
        log_name = os.path.splitext(os.path.split(sys.argv[0])[1])[0]
        log_dir = os.getenv('TASK_LOG_PATH')
        if log_dir is None:
            log_dir = 'E:\PycharmProjects\logs'
        log_dir += '/' + date_today.strftime("%Y%m%d")
        if not os.path.isdir(log_dir):
            try:
                os.makedirs(log_dir)
            except:
                pass
                #        self.ignore_error = ignore_error
        mylog = JobLogging(log_name, log_dir)
        self.log = mylog.get_logger()
        self.log.info("Log create success")

    #获取图片url并存到列表urls_list
    def get_picture_url(self, content):
        global path
        path = "E:\spider\pictures\huaban" + '\\' + content
        # 保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的文件夹
        if not os.path.exists(path):
            os.makedirs(path)
        url = "http://huaban.com"
        """
        headers = {
        '_uab_collina':'149645626983185501866353',
        'UM_distinctid':'15de6c295384ac-0c8628c347e125-5393662-144000-15de6c2953a177',
        '_umdata':'6AF5B463492A874D2573E3BE737674883A6BD66BF1905C8CEDBE1E21394ABEBA51F381B358DBA371CD43AD3E795C914C1020C2A44E148760B74EAEF0F1E95334',
        '__gads=ID':'cd56a9f7511c7203:T=1503359242:S=ALNI_MZep4pVNcnP3K3kk09WhpP6i-E5ZA',
        '_hmt':'1',
        '_f':'iVBORw0KGgoAAAANSUhEUgAAADIAAAAUCAYAAADPym6aAAABJElEQVRYR%2B1VOxYCIQwMF7KzsvFGXmW9kY2VnQfxCvgCRmfzCD9lnz53myWQAJOZBEfeeyIi7xz%2FyEXzZRPFhYbPc3hHXO6I6TbFixmfEyByeQQSxu6BcAXSkIGMazMjuBcz8pQcq44o0Iuyyc1p38C62kNsOdeSZDOQlLRQ80uOMalDgWCGMfsW2B5%2FATMUyGh2uhgptV9Ly6l5nNOa1%2F6zmjTqkH2aGEk2jY72%2B5k%2BNd9lBfLMh8GIP11iK95vw8uv7RQr4oNxOfbQ%2F7g5Z4meveyt0uKDEIiMLRC4jrG1%2FjkwKxCRE2e5lF30leyXYvQ628MZKV3q64HUFvnPAMkVuSWlEouLSiuV6dp2WtPBrPZ7uO5I18tbXWvEC27t%2BTcv%2Bx0JuJAoUm2L%2FQAAAABJRU5ErkJggg%3D%3D%2CWin32.1536.864.24',
        '_dc':'1',
        'wft':'1',
        '_cnzz_CV1256903590':'is-logon%7Clogged-out%7C1504191041292',
        '_ga':'GA1.2.1392511582.1496247236',
        '__asc':'001c858215e38ada143bbf682dc',
        '__auc':'cb7bc83c15de6c296cd1a82cbdc',
        'CNZZDATA1256903590':'99862304-1502810462-%7C1504187892',
        'sid':'32167kiJIHuIQDHyrI9JqtTbF9h.LiYQJuqf%2FOh6zGW0MAsx4VTmcnx4qeZ%2BbtYxUZW8YXc',
        }
        """
        # 使用Chrome浏览器模拟打开网页，但是要把下载的chromedriver.exe放在python的文件路径下,
        # 调试好之后换成PhantomJs,速度应该会快一点
        # driver = webdriver.PhantomJs()
        # 下拉滑动浏览器屏幕，具体下拉多少根据自己实际情况决定
        #driver = webdriver.PhantomJS()
        driver = webdriver.Chrome()
        # 设置全屏
        driver.maximize_window()
        driver.get(url)
        #driver.delete_all_cookies()
        #driver.add_cookie(headers)
        #driver.add_cookie({'name': 'uid', 'value': '21839587	'})
        #driver.get(url)
        #driver.refresh()
        #driver.get(url, headers = headers)
        time.sleep(8)

        # 点击登录、呼起登录窗口
        driver.find_elements_by_xpath('//a[@class="login btn wbtn"]')[0].click()
        # sign in the username
        try:
            driver.find_elements_by_xpath('//input[@name="email"]')[0].send_keys('wjx411527@163.com')
            print('user success!')
        except:
            print('user error!')
        time.sleep(3)
        # sign in the pasword
        try:
            driver.find_elements_by_xpath('//input[@name="password"]')[0].send_keys('1223353177wjx')
            print('pw success!')
        except:
            print('pw error!')
        time.sleep(3)
        # click to login
        try:
            driver.find_elements_by_xpath('//a[@class="btn btn18 rbtn"]')[0].click()
            print('click success!')
        except:
            print('click error!')
        time.sleep(3)


        #搜索图片
        driver.find_elements_by_xpath('//input[@placeholder="搜索你喜欢的"]')[0].send_keys(content)
        driver.find_elements_by_xpath('//form[@id="search_form"]/a')[0].click()
        time.sleep(5)
        i = 0
        page = 1
        global name
        global store_path
        global urls_list
        urls_list = []
        #获取图片的总数
        pictures_count = driver.find_elements_by_xpath('//a[@class="selected"]/i')[0].text
        print(pictures_count)
        pages = int(int(pictures_count) / 20)
        print(pages)
        #匹配到图片url所在的元素
        url_elements = driver.find_elements_by_xpath('//span[@class="stop"]/../img')
        #遍历图片元素的列表获取图片的url
        for url_element in url_elements:
            picture_url = url_element.get_attribute("src")[:-3] + "658"
            #防止获取重复的图片url
            if picture_url not in urls_list:
                urls_list.append(picture_url)
        while page <= pages:
            while len(urls_list) < 20*page:
                driver.execute_script("window.scrollBy(0,1000)")
                time.sleep(6)
                url_elements = driver.find_elements_by_xpath('//span[@class="stop"]/../img')
                for url_element in url_elements:
                    picture_url = url_element.get_attribute("src")[:-3] + "658"
                    if picture_url not in urls_list:
                        urls_list.append(picture_url)
            print("第%s页" % page)

            for download_url in urls_list[20*(page-1):20*page]:
                i += 1
                name = content + "_" + str(i)
                store_path = name + '.jpg'
                self.store(download_url)
            page += 1
        #最后一页
        print("第%s页" % int(page))

        while len(urls_list) < int(pictures_count):
            driver.execute_script("window.scrollBy(0,1000)")
            time.sleep(6)
            url_elements = driver.find_elements_by_xpath('//span[@class="stop"]/../img')
            for url_element in url_elements:
                picture_url = url_element.get_attribute("src")[:-3] + "658"
                if picture_url not in urls_list:
                    urls_list.append(picture_url)
        for download_url in urls_list[20*(page-1): ]:
            i += 1
            name = content + "_" + str(i)
            store_path = name + '.jpg'
            self.store(download_url)
    #存储图片到本地
    def store(self, picture_url):
        picture = requests.get(picture_url)
        f = open(path + '\\'+ store_path, 'wb')
        f.write(picture.content)
        print('正在保存图片：' + picture_url)
        print('文件：' + name)


if __name__ == "__main__":
    content = '迪丽热巴'
    huaban = Huaban()
    huaban.get_picture_url(content)
