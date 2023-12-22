import requests
import os

URL = f"http://127.0.0.1:8000/url/"
REQUEST_URL = f"http://127.0.0.1:8000/request/"
CLASS_URL = f"http://127.0.0.1:8000/request/class/"
DATA = {"key1": "value1"}

def result(response):
    print(f"url: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {response.json()}\n")

def main():

    # URLのリクエスト
    print("\nURLのリクエスト")

    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(URL)
    print(f"url: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {response.text}\n")

    ## /query GETリクエスト
    print("/query GETリクエスト")
    response = requests.get(os.path.join(URL, "query"), params=DATA)
    result(response)

    ## /param GETリクエスト
    print("/param GETリクエスト")
    response = requests.get(os.path.join(URL, "param", "5"))
    result(response)


    # REQUEST_URLのリクエスト
    print("\nREQUEST_URLのリクエスト")

    ## GETリクエスト
    print("GETリクエスト")
    response = requests.get(REQUEST_URL, params=DATA)
    result(response)

    ## POSTリクエスト
    print("POSTリクエスト")
    response = requests.post(REQUEST_URL, json=DATA)
    result(response)

    ## PUTリクエスト
    print("PUTリクエスト")
    response = requests.put(REQUEST_URL, json=DATA)
    result(response)

    ## DELETEリクエスト
    print("DELETEリクエスト")
    response = requests.delete(REQUEST_URL, params=DATA)
    result(response)


    # CLASS_URLのリクエスト
    print("\nCLASS_URLのリクエスト")

    ## GETリクエスト
    print("GETリクエスト")
    response = requests.get(CLASS_URL, params=DATA)
    result(response)

    ## POSTリクエスト
    print("POSTリクエスト")
    response = requests.post(CLASS_URL, json=DATA)
    result(response)

    ## PUTリクエスト
    print("PUTリクエスト")
    response = requests.put(CLASS_URL, json=DATA)
    result(response)

    ## DELETEリクエスト
    print("DELETEリクエスト")
    response = requests.delete(CLASS_URL, params=DATA)
    result(response)


if __name__ == '__main__':
    main()