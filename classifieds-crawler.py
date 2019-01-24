import requests, webbrowser
from bs4 import BeautifulSoup
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:name>/")
    def hello(name):
    return render_template(
        'index.html',name=name)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
# cookies = {
#     'gdcABG': 'A',
#     '_ga': 'GA1.2.495393677.1546672795',
#     '_gid': 'GA1.2.905242110.1548359700',
#     '_fbp': 'fb.1.1548359699890.2072961725',
#     'pused': 'c9bd42662c193366b882603a8d1df2c85f2949e7bac9o+/Q2GPlK0pApn9k2N9KHLlL81KOHCp9CmkF5R08KMXCdezNw/d8NuQcwDdBChI6rfP297eTEnFVyHYBzqlgEZ68J02evmqfvAIi3aKIUfVqYGtXckL+EtjSfB6bK5GBcXtvFbXsVPnJr/R50YF96Dymrto6I7Bo92QtyhO3R5o=',
# }

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.usedvictoria.com/classified-ad/Samsung-28-4K-Monitor_32827310',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8,fr-CA;q=0.7',
}

params = (
    ('description', '4k monitor'),
)

# Commented out so we don't need to make additional requests during development
# r = requests.get('https://www.usedvictoria.com/classifieds/all', headers=headers, params=params)


# print(type(r.text))

# def createLocalPreview()
#     f = open('usedvic-site.html', 'w')
#     f.write(r.text)
#     webbrowser.open("usedvic-site.html")

# soup = BeautifulSoup(r.content, 'html.parser')


# soup = BeautifulSoup(open('usedvic-site.html'), 'html.parser')
# search_results = soup.select('#top-cards div.grid.grid__allcells6.gs8.jc-end div.grid.gs4 span')

# visit_count = visit_field[0].text.strip()
# print("Visits are " + visit_count[0] + " as of " + now)


#
# print(visit_field)
