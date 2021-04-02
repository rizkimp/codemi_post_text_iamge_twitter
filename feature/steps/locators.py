class locator(object):
    #home
    button_signup = "//a[@data-testid='signupButton']"
    button_login_1 = "//a[@data-testid='loginButton']"
    #login_page
    input_username = "session[username_or_email]"
    input_password = "session[password]"
    button_login_2 = "//div[@data-testid='LoginForm_Login_Button']"
    #dashboard
    input_tweet = "//div[@data-testid='tweetTextarea_0']"
    input_file = "//input[@data-testid='fileInput']"
    button_tweet = "//div[@data-testid='tweetButtonInline']"
    alert_your_tweet_sent = "//span[contains(text(),'Your Tweet was sent.')]"
