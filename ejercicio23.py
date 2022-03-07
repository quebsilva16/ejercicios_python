from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


url_google_news = 'https://news.google.com/rss?hl=es-419&gl=MX&ceid=MX:es-419'
cliente = urlopen(url_google_news)
contenido_xml = cliente.read()
cliente.close()

pagina = soup(contenido_xml, 'xml')
items = pagina.findAll('item')

for item in items:
    print(item.title.text)
    print(item.link.text)
    print(item.pubDate.text)

    print('=' * 250)
