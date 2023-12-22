import requests
import os

API_URL = f"http://127.0.0.1:8000/api/tasks/"
DATA = [
    {"task_id": 1, "content": "Task 1", "status": "todo", "due": "2024-02-11"},
    {"task_id": 2, "content": "Task 2", "status": "todo", "due": "2024-05-21"},
    {"task_id": 3, "content": "Task 3", "status": "todo", "due": "2024-04-21"},
    ]
PATCH_DATA = {"task_id": 1, "content": "Task 1", "status": "active", "due": "2024-02-11"}
PUT_DATA = {"task_id": 1, "content": "Task 100", "status": "done", "due": "2025-01-10"}

def result(response):
    print(f"url: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {response.json()}\n")
    return response.json()

def main():

    ## POSTリクエスト
    print("\nPOSTリクエスト")
    for task in DATA:
        response = requests.post(API_URL, json=task)
        print(f"status code: {response.status_code}")

    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(API_URL)
    response_data = result(response)


    ## /task_id GETリクエスト
    print("\nGETリクエスト")
    TASK_URL = os.path.join(API_URL, str(response_data[0]["task_id"]))
    response = requests.get(TASK_URL)
    result(response)

    ## /task_id PATCHリクエスト
    print("\nPATCHリクエスト")
    TASK_URL = os.path.join(API_URL, str(PATCH_DATA["task_id"])) + "/"
    response = requests.patch(TASK_URL, data=PATCH_DATA)
    result(response)

    ## /task_id PUTリクエスト
    print("\nPUTリクエスト")
    TASK_URL = os.path.join(API_URL, str(PUT_DATA["task_id"])) + "/"
    response = requests.patch(TASK_URL, data=PUT_DATA)
    result(response)

    ## /task_id DELETEリクエスト
    print("\nDELETEリクエスト")
    if response_data:
        for task in response_data:
            TASK_URL = os.path.join(API_URL, str(task["task_id"]))
            response = requests.delete(TASK_URL, json=task)
            print(f"status code: {response.status_code}")

    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(API_URL)
    result(response)

if __name__ == '__main__':
    main()