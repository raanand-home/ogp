import scrapper
from lxml import html


def test_sample():
    data = open('sample.html', 'r').read()
    result = scrapper.get_graph_data(data)
    expected = {'title': 'Open Graph protocol',
                'type': 'website',
                'url': 'http://ogp.me/',
                'image': {'url': 'http://ogp.me/logo.png',
                          'type': 'image/png',
                          'width': '300',
                          'height': '300',
                          'alt': 'The Open Graph logo'},
                'description':
                'The Open Graph protocol enables any web page to become a rich object in a social graph.'}
    assert result == expected


def test_recuring_data():
    data = open('sample.html', 'r').read()
    data = html.fromstring(data)
    meta = html.fragment_fromstring(
        '<meta property="og:image:width" content="300">')
    head = data.xpath('./head')
    head[0].append(meta)
    data = html.tostring(data)
    result = scrapper.get_graph_data(data)
    expected = {'title': 'Open Graph protocol',
                'type': 'website',
                'url': 'http://ogp.me/',
                'image': {'url': 'http://ogp.me/logo.png',
                          'type': 'image/png',
                          'width': ['300', '300'],
                          'height': '300',
                          'alt': 'The Open Graph logo'},
                'description':
                'The Open Graph protocol enables any web page to become a rich object in a social graph.'}
    assert result == expected
