from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    context.browser = webdriver.Chrome(executable_path='/home/rizkimp/Documents/codemi/feature/browsers/chromedriver',chrome_options=options)
    #context.browser = webdriver.Chrome('/home/rizkimp/Documents/codemi/feature/browsers/chromedriver')
    context.browser.set_window_size(1440,900)
    twitter = context.config.userdata.get("twitter")
    context.browser.get(twitter)

def after_all(context):
    context.browser.quit()
