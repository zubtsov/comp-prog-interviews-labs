# https://edube.org/learn/pcpp1-5/lab-xml-lab-2

from xml.etree import ElementTree as ET

shop = ET.Element('shop')

category = ET.SubElement(shop, 'category', {'name': 'Vegan Products'})

products = [
    ('Good Morning Sunshine', 'cereals', 'OpenEDG Testing Service', 9.90, 'USD'),
    ('Spaghetti Veganietto', 'pasta', 'Programmers Eat Pasta', 15.49, 'EUR'),
    ('Fantastic Almond Milk', 'beverages', 'Drinks4Coders Inc.', 19.75, 'USD'),
]

for product_name, product_type, producer, price, currency in products:
    product = ET.SubElement(category, 'product', {'name': product_name})
    ET.SubElement(product, 'type').text = product_type
    ET.SubElement(product, 'producer').text = producer
    ET.SubElement(product, 'price').text = str(price)
    ET.SubElement(product, 'currency').text = currency

with open('shop.xml', 'wb') as f:
    ET.ElementTree(shop).write(f, encoding='UTF-8', xml_declaration=True)
