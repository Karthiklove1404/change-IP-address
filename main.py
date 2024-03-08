import os
import requests
from time import sleep


def main():
    print("To stop press ' ctrl + z '")
    chang = int(input("After how much second do you want to change: "))
    os.system("service tor start")
    url = "https://httpbin.org/ip"
    proxy = {'http': 'socks5://127.0.0.1:9050',
             'https': 'socks5://127.0.0.1:9050'}

    while True:
        request = requests.get(url, proxies=proxy)
        if request.status_code == 200:
            print("your current ip :: {}".format(request.json().get()))
        else:
            print("failed to get current ip")
        sleep(chang)
        os.system("service tor reload")


if __name__ == "__main__":
    main()
