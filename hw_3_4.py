def main_function(function_name, *args):
    name = function_name.__name__.title().replace('_', ' ')
    print(name, *args)


def open_browser(browser_name):
    main_function(open_browser, browser_name.lower())


def go_to_companyname_homepage(page_url):
    main_function(go_to_companyname_homepage, page_url.upper())


def find_registration_button_on_login_page(page_url, button_text):
    main_function(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_companyname_homepage('https://github.com/')
find_registration_button_on_login_page('https://github.com/', 'Sign in')