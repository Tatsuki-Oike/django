import requests
import os

BASE_URL = "http://127.0.0.1:8000/api/"

def main():

    # Userの作成
    print("\nUserの作成")
    user_url = BASE_URL + "users/"
    user_data = {"username": "your_username", "password": "userpass"}
    user_response = requests.post(user_url, json=user_data)
    user_response_data = user_response.json()
    print("User creation response:", user_response_data)


    # Tokenの作成
    print("\nTokenの作成")
    token_url = BASE_URL + "token/"
    token_data = {"username": "your_username", "password": "userpass"}
    token_response = requests.post(token_url, json=token_data)
    token_response_data = token_response.json()
    token = token_response_data.get("token")
    print("Token:", token)
    

    # Taskの作成
    print("\nTask Creation")
    task_creation_url = BASE_URL + "tasks/"
    task_data = {"task_id": 1, "content": "Task 1", "status": "todo", "due": "2023-12-31"}
    task_headers = {"Authorization": f"Token {token}"}
    task_creation_response = requests.post(task_creation_url,
                                           json=task_data, 
                                           headers=task_headers)
    print("Task creation response:", task_creation_response.json())

    # Taskの確認
    print("\nTask確認")
    task_retrieval_response = requests.get(task_creation_url, headers=task_headers)
    print("Task retrieval response:", task_retrieval_response.json())

    # Taskの消去
    print("\nTaskの消去")
    task_delete_url = task_creation_url + "1"
    task_delete_response = requests.delete(task_delete_url, headers=task_headers)
    print("Task delete response:", task_delete_response.status_code)


    # Tokenの作成 (パスワードが異なる失敗例)
    print("\nToken Creation")
    token_url = BASE_URL + "token/"
    token_data = {"username": "your_username", "password": "uncorrectpass"}
    token_response = requests.post(token_url, json=token_data)
    token_response_data = token_response.json()
    token = token_response_data.get("token")
    print(token_response_data)
    print("Token:", token)

    # Taskの確認 (Tokenなしの失敗例)
    print("\nTask確認")
    task_retrieval_response = requests.get(task_creation_url)
    print("Task retrieval response:", task_retrieval_response.json())


    # Userの消去
    print("\nUserの消去")
    user_detail_url = os.path.join(user_url, str(user_response_data["id"]))
    user_response = requests.delete(user_detail_url)
    print("User delete response:", user_response.status_code)

if __name__ == '__main__':
    main()