import requests

# Lấy danh sách post nổi bật
url_posts = "https://jsonplaceholder.typicode.com/posts"
url_comments = "https://jsonplaceholder.typicode.com/comments?postId=1"

posts = requests.get(url_posts).json()
comments = requests.get(url_comments).json()

print("Danh sách 3 bài post nổi bật:")
for post in posts[:3]:
    print(f"Post ID: {post['id']}")
    print("Title:", post["title"])
    print("Body:", post["body"][:80], "...\n")

print("----- Bình luận của bài post có ID=1 -----")
for c in comments:
    print(f"Tên: {c['name']}")
    print(f"Email: {c['email']}")
    print("Nội dung:", c["body"], "\n")
