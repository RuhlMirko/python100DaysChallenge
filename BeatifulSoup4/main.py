from bs4 import BeautifulSoup


with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
# all_anchors = soup.find_all(name="a")
# for tag in all_anchors:
#     # print(tag.getText())
#     print(tag.get("href"))


# first_li = soup.find_all(name="li")
# print(first_li[0])

test = soup.select(selector=".heading")
print(test)
