from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context, scenario_name):

    #Chrome
    # context.driver = webdriver.Chrome()
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, timeout=10)
    # context.app = Application(context.driver)


    #Firefox
    # context.driver = webdriver.Firefox()
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, timeout=10)
    # context.app = Application(context.driver)


    #Chrome - headless
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_argument("--window-size=1920,1080")
    # context.driver = webdriver.Chrome(
    #     options=options
    # )
    #
    # context.driver.implicitly_wait(4)
    # context.driver.wait = WebDriverWait(context.driver, timeout=10)
    # context.app = Application(context.driver)


    #BROWSERSTACK
    bs_user = ''
    bs_key = ''

    url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        "os" : "Windows",
        "osVersion" : "11",
        "browserVersion" : "latest",
        'browserName': 'Chrome',
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):

    try:
        if scenario.status == "passed":
            context.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", '
                '"arguments": {"status":"passed","reason": "Assertions passed"}}'
            )
        else:
            context.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", '
                f'"arguments": {{"status":"failed","reason": "{scenario.name} failed"}}}}'
            )

    except Exception as e:
        context.driver.execute_script(
            f'browserstack_executor: {{"action": "setSessionStatus", '
            f'"arguments": {{"status":"failed","reason": "{str(e)}"}}}}'
        )

    finally:
        context.driver.quit()
