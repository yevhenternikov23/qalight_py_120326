### My code:

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("=== TASK 1: POSTS COUNT ===")

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")

    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, "Status code is not 200"
    
    posts = response.json()

    print(f"Posts count: {len(posts)}")
    assert len(posts) == 100, f"Expected 100 posts, got {len(posts)}"
    print("TASK 1 PASSED\n")

if __name__ == "__main__":
    test_get_all_posts()

print("=== TASK 2: POST ID 10 ===")

def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/10")

    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, "Status code is not 200, got {response.status_code}"

    post = response.json()

    print(f"Post id: {post['id']}")
    assert post["id"] == 10, f"Wrong id: {post['id']}"

    required_fields = ["userId", "id", "title", "body"]

    for field in required_fields:
        print(f"Check field: {field}")
        assert field in post, f"Missing field: {field}"
    print("TASK 2 PASSED\n")
    
if __name__ == "__main__":
    test_get_post_by_id()

print("=== TASK 3: TODOS USER 2 ===")

def test_todos_user_2():
    response = requests.get(f"{BASE_URL}/todos", params={"userId": 2})

    todos = response.json()

    print(f"Todos count: {len(todos)}")

    for todo in todos:
        assert todo["userId"] == 2, f"Wrong userId: {todo['userId']})"
    print("All todos have userId = 2")
    print("TASK 3 PASSED\n")

if __name__ == "__main__":
    test_todos_user_2()

print("=== TASK 4: CREATE POST ===")

def test_create_new_post():
    payload = {
        "title": "Yevhens post title",
        "body": "Yevhens post body",
        "userId": 23
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    print(f"Status code: {response.status_code}")
    assert response.status_code == 201, f"Status code is not 201, got {response.status_code}"

    created_post = response.json()

    print(f"Title: {created_post['title']}")
    print(f"Body: {created_post['body']}")
    assert created_post["title"] == payload["title"], "Title does not match"
    assert created_post["body"] == payload["body"], "Body does not match"

    print("TASK 4 PASSED\n")

if __name__ == "__main__":
    test_create_new_post()

print("=== TASK 5: UPDATE POST ===")

def test_update_post_id_5():
    payload = {
        "title": "Yevhens new post title",
        "body": "Yevhens new post body",
        "Id": 5
    }

    response = requests.put(f"{BASE_URL}/posts/5", json=payload)

    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, f"Status code is not 200, got {response.status_code}"

    updated_post = response.json()

    print(f"Title: {updated_post['title']}")
    print(f"Body: {updated_post['body']}")
    assert updated_post['title'] == payload['title'], "Title was not updated"
    assert updated_post["body"] == payload["body"], "Body does not updated"
    assert updated_post["id"] == 5, f"Wrong id: {updated_post['id']}"
    print("TASK 5 PASSED\n")

if __name__ == "__main__":
    test_update_post_id_5()

print("=== TASK 6: PARTIAL UPDATE POST ===")

def test_partial_update_post():
    payload = {
        "title": "Yevhens partially updated title",
    }

    response = requests.patch(f"{BASE_URL}/posts/5", json=payload)

    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, f"Status code is not 200, got {response.status_code}"

    updated_post = response.json()

    print(f"New title: {updated_post['title']}")
    assert updated_post['title'] == payload['title'], "Title was not updated"
    print("TASK 6 PASSED\n")

if __name__ == "__main__":
    test_partial_update_post()

print("=== TASK 7: DELETE POST ===")

def test_delete_post():
    payload = {
        "Id": 5,
    }

    response = requests.delete(f"{BASE_URL}/posts/5", json=payload)

    print(f"Status code: {response.status_code}")
    assert response.status_code in (200, 204), f"Unexpected status code: {response.status_code}"
    print("TASK 7 PASSED\n")

if __name__ == "__main__":
    test_delete_post()

print("=== TASK 8: POST ISN'T EXIST===")

def test_get_post_is_not_exist():
    response = requests.get(f"{BASE_URL}/posts/999999")

    print(f"Status code: {response.status_code}")
    assert response.status_code == 404 or response.json() == {}, "Post not found"
    print("TASK 8 PASSED\n")
    
if __name__ == "__main__":
    test_get_post_is_not_exist()

print("=== TASK 9: POST WITHOUT REQUIRED FIELDS===")

def test_post_without_required_fileds():
    payload = {}

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    print(f"Status code: {response.status_code}")
    assert response.status_code in (200, 201), f"Unexpected status code: {response.status_code}"

    response_data = response.json()

    print(f"Response: {response_data}")
    assert isinstance(response_data, dict), "Response is not a dictionary"
    print("TASK 9 PASSED\n")

if __name__ == "__main__":
    test_post_without_required_fileds()

print("=== TASK 10: POST WITHOUT REQUIRED FIELDS===")

def test_get_with_custom_headers():
    headers = {
    "User-Agent": "QA Student"
    }

    response = requests.get(f"{BASE_URL}/posts", headers=headers)

    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, f"Request failed: {response.status_code}"
    print("Request executed successfully")
    print("TASK 10 PASSED\n")

if __name__ == "__main__":
    test_get_with_custom_headers()