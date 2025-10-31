import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
if response.status_code == 200:
    posts = response.json()
    print("Tổng số bài post:", len(posts))
    print("\nDanh sách các bài post đầu tiên:")
    for post in posts[:5]:
        print(f"userID: {post['userId']}, id: {post['id']}")
        print("Title:", post["title"])
        print("Body:", post["body"][:60], "...\n")
else:
    print("Không thể truy cập API.")
