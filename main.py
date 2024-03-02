import requests
from bs4 import BeautifulSoup
import csv
import time




headers = {
    "Accept": "*/*"
    "User-Agent" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36"
}
with open("123.csv", "w", encoding="cp1251") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        ("Категория", "Название", "Цена", "Артикул", "Картинка", "описание")
    )
# url = "https://aquatermix.ru/zapchasti-dlya-kotlov/baxi6/"
count = 0
for i in range(1,9):
    url = f"https://aquatermix.ru/zapchasti-dlya-kotlov/baxi6/?page={i}"
    req = requests.get(url, headers=headers)
    src = req.text
    # with open("index.html", "w", encoding="utf-8") as file:
    #     file.write(src)
    # with open("index.html", "r", encoding="utf-8") as file:
    #     src = file.read()


    soup = BeautifulSoup(src, "lxml")
    element = soup.find(class_="product-list")



    for elem in element:
        try:
            # product = elem.find("div", class_='image')
            # print(product)
            product_url = elem.find('a').get('href')
            # url = "https://aquatermix.ru/zapchasti-dlya-kotlov/baxi6/kolca_-prokladki/uplotnenie-9x4x3-baxi--5410320-.html"
            req = requests.get(product_url, headers=headers)
            src = req.text

            soup = BeautifulSoup(src, "lxml")
            product_category = soup.find(class_="breadcrumb").find_all("a")[-1].text
            product_name = soup.find("h1", style="padding-left: 20px;").text
            product_price = soup.find("div", class_="price").text[6:].strip()
            try:
                product_article = soup.find("div", class_="tab-content").find_all("p")[2].text[18:].strip()
                product_article = int(product_article)

            except:
                product_article = "Артикул продукта не найден"
            product_image = soup.find("a", class_="colorbox").get("href")
            product_discription = soup.find("div", class_="tab-content").find_all("p")[2].text
            with open("123.csv", "a", encoding="cp1251") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(
                    (
                        product_category,
                        product_name,
                        product_price,
                        product_article,
                        product_image,
                        product_discription
                    )
                )
        except:
            continue
        count += 1
        print(f"[INFO]Страница: {i}/9",
              f"Всего элементов собрано: {count}[INFO]")

