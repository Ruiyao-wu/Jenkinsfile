import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException


class DriverBuilder():
    '''
    build a firefox driver to download the JIRA_report automatically
    attribute: path: download to explicit path
    input of download_from_friver: url: Jira Tickets filter
    '''
    def __init__(self, path):
        self.path = path

    def get_firefox_driver(self):
        download_path = self.path
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", "<path_to_downlaod_directory>")
        profile.set_preference("browser.download.dir", download_path)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/vnd.ms-excel")
        #*firefox.exe path
        binary = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
        options = Options()
        options.binary = binary
        #*geckodriver.exe path
        driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile, executable_path=r"C:\Users\WUU7FE\.conda\envs\FROP\Lib\site-packages\selenium\geckodriver.exe")
        return driver

    def wait_until_file_exists(self, file_path):
        try:
            while 1:
                f_list = os.listdir(file_path)
                # print f_list
                for i in f_list:
                    #split name and extension
                    if os.path.splitext(i)[1] == '.xls':
                        path = file_path + '\\' + str(i)
                        file_size = os.path.getsize(path)
                        if file_size != 0:
                            raise StopIteration
        except StopIteration:
            pass

    def getFileName(self, path):
        ''' get file name regarding the Filename Extension '''
        f_list = os.listdir(path)
        # print f_list
        for i in f_list:
            #split name and extension
            if os.path.splitext(i)[1] == '.xls':
                return str(i)

    def download_from_friver(self,url):
        expected_download = os.path.join(self.path, "Daily_FBWM_Metric_Download.xls")
        try:
            os.remove(expected_download)
        except OSError:
            pass
        assert (not os.path.isfile(expected_download))
        driver = self.get_firefox_driver()
        driver.set_page_load_timeout(30)
        try:
            driver.get(url)
        except TimeoutException:
            self.wait_until_file_exists(self.path)
            driver.close()
        old_filename = self.getFileName(self.path) 
        os.rename(old_filename,"Daily_FBWM_Metric_Download.xls")
        assert (os.path.isfile(expected_download))
        print("--------download is done---------")

#END OF CLASS DriverBuilder