# import os, sys
# sys.path.append(os.path.join(os.path.dirname(__file__), "../"))



# from fastapi.testclient import TestClient



# def test_ブログを作成する(client: TestClient):
#     response = client.post(
#         "/blog/",
#         json={
#             "title": "test_title",
#             "body": "test_content",
#             "user_id": 1,
#         }
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": 5,
#         "title": "test_title",
#         "body": "test_content",
#         "user_id": 1,
#     }

# def test_ブログを全件取得する(client: TestClient):
#     response = client.get("/blog")
#     assert response.status_code == 200
#     assert response.json() == [
#         {
#             "id": 1,
#             "title": "test_title1",
#             "body": "test_content1",
#             "user_id": 1,
#         },
#         {
#             "id": 2,
#             "title": "test_title2",
#             "body": "test_content2",
#             "user_id": 1,
#         },
#         {
#             "id": 3,
#             "title": "test_title3",
#             "body": "test_content3",
#             "user_id": 2,
#         },
#         {
#             "id": 4,
#             "title": "test_title4",
#             "body": "test_content4",
#             "user_id": 3,
#         },
#         {
#             "id": 5,
#             "title": "test_title",
#             "body": "test_content",
#             "user_id": 1,
#         },
#     ]

# def test_IDでブログを返す(client: TestClient):
#     response = client.get("/blog/1")
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": 1,
#         "title": "test_title1",
#         "body": "test_content1",
#         "user_id": 1,
#     }

# def test_ブログを削除する(client: TestClient):
#     response = client.delete("/blog/1")
#     assert response.status_code == 200
#     assert response.json() == {
#         "message": "done"
#     }
    
# def test_ブログを更新する(client: TestClient):
#     response = client.put(
#         "/blog/2",
#         json={
#             "title": "test_title2",
#             "body": "test_content2",
#             "user_id": 1,
#         }
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": 2,
#         "title": "test_title2",
#         "body": "test_content2",
#         "user_id": 1,
#     }

# def test_ブログをユーザーIDで取得する(client: TestClient):
#     response = client.get("/blog/user/1")
#     assert response.status_code == 200
#     assert response.json() == [
#         {
#             "id": 1,
#             "title": "test_title1",
#             "body": "test_content1",
#             "user_id": 1,
#         },
#         {
#             "id": 2,
#             "title": "test_title2",
#             "body": "test_content2",
#             "user_id": 1,
#         },
#         {
#             "id": 5,
#             "title": "test_title",
#             "body": "test_content",
#             "user_id": 1,
#         },
#     ]

# def test_ブログをユーザーIDで取得する_ユーザーIDが存在しない(client: TestClient):
#     response = client.get("/blog/user/100")
#     assert response.status_code == 404
#     assert response.json() == {
#         "detail": "User with the id 100 is not available"
#     }