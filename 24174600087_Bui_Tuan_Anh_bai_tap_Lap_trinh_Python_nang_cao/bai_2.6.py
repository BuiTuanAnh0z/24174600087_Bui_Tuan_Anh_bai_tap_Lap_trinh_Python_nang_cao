import xml.etree.ElementTree as ET
import csv
# -------------------------------
# Giả lập dữ liệu RSS feed
# -------------------------------
rss_data = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Hindustan Times - Top News</title>
    <link>http://www.hindustantimes.com/rss/topnews/rssfeed.xml</link>
    <description>Latest top news headlines</description>
    <item>
      <title>India celebrates Independence Day</title>
      <link>http://www.hindustantimes.com/india-news/independence-day.html</link>
      <pubDate>Sat, 15 Aug 2025 10:00:00 GMT</pubDate>
    </item>
    <item>
      <title>New Education Policy announced</title>
      <link>http://www.hindustantimes.com/education/new-policy.html</link>
      <pubDate>Mon, 10 Aug 2025 09:30:00 GMT</pubDate>
    </item>
    <item>
      <title>Technology Summit held in Delhi</title>
      <link>http://www.hindustantimes.com/tech/summit.html</link>
      <pubDate>Wed, 05 Aug 2025 15:45:00 GMT</pubDate>
    </item>
  </channel>
</rss>
"""
# -------------------------------
# Ghi nội dung giả lập vào file XML
# -------------------------------
with open("rss_feed.xml", "w", encoding="utf-8") as f:
    f.write(rss_data)
# -------------------------------
# Phân tích file XML vừa tạo
# -------------------------------
tree = ET.parse("rss_feed.xml")
root = tree.getroot()
items = root.findall(".//channel/item")
# -------------------------------
# Trích xuất thông tin tiêu đề, link, ngày đăng
# -------------------------------
news_list = []
for item in items:
    title = item.find("title").text
    link = item.find("link").text
    pub_date = item.find("pubDate").text
    news_list.append([title, link, pub_date])
# -------------------------------
# Lưu kết quả vào file CSV
# -------------------------------
with open("rss_news.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Link", "Publication Date"])
    writer.writerows(news_list)
print(" Đã hoàn thành: rss_feed.xml và rss_news.csv")
