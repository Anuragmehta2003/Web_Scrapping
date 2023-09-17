from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "_3pLy-c"})
print(len(containers))

#print(soup.prettify(containers[0]))

container=containers[0]
#product_name=container.find_all("div",{"class": "_4rR01T"})
#print(product_name[0].text)
#price=container.findAll("div", {"class": "_3I9_wc _27UcVY"})
#print(price[0].text)
#ratings=container.findAll("div", {"class": "_3LWZlK"})
#print(ratings[0].text)

filename="product_details.csv"
f=open(filename, "w")

headers="Product_Name, Pricing, Rating\n"
f.write(headers)

for container in containers:
    product_name_container=container.find_all("div",{"class": "_4rR01T"})
    product_name=product_name_container[0].text

    price_container = container.findAll("div", {"class": "_3I9_wc _27UcVY"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class": "_3LWZlK"})
    rating=rating_container[0].text

    print("Product_name:" + product_name)
    print("Price" + price)
    print("Ratings" + rating)
     #String Parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "RS." + rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]
    
    split_rating = rating.split(" ")
    final_rating = split_rating[0]
    #concatenate all three features
    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
f.close()