# Some Notes

The requested output format is a bit problemetic.

Under the Open graph protocol
node could have both self value and children

```
og:image -> http://image
and 
og:image:width = 300
```

which is not clear how the requested json format can support it without adding exception to specific path see common/open_graph_protocol.py


```json

{
  "url": "http://ogp.me/",
  "type": "website",
  "title": "Open Graph protocol",
  "image": [
  {
    "url": "http://ogp.me/logo.png",
    "type": "image/png",
    "width": 300,
    "height": 300,
    "alt": "The Open Graph logo"
  },
  ],
  "updated_time": "2018-02-18T03:41:09+0000",
  "scrape_status": "done",
  "id": "10150237978467733"
}
```

## Installation Guide
* install docker;
* make build ;
* docker-compose up -d 
* iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-port 8080
* sudo iptables -t nat -A OUTPUT -o lo -p tcp --dport 80 -j REDIRECT --to-port 5001



