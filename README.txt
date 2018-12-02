1.  Description
   1. Build a web service that will scrape  Open graph tags. For any given URL.
   2. See http://ogp.me/ for definitions
   3. See https://developers.facebook.com/tools/debug/sharing/?q=http%3A%2F%2Fogp.me%2F for an example implementation
2. Requirements
   1. We have provided a server located at raanand.hiring.keywee.io. You can find connection details below.
   2. The server has a minimal OS install (Ubuntu 16.04) and nothing else.
   3. To login VIA SSH:
      1. ssh -i scraper-machine.pem ubuntu@raanand.hiring.keywee.io  - pem file is attached to email
   4. The server should provide the following JSON API 
      1. Request
         1. POST raanand.hiring.keywee.io/stories?url={some_url}
      1. Response
         1. An ID representing the canonical URL of the given url (each canonical url should have a single matching id in the system) 
      1. Request
         1. GET raanand.hiring.keywee.io/stories/{canoniacl-url-id}
      1. Response
         1. scrape_status field can be (done,error,pending)
         2. {
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
	      scrape_status: "done",
              "id": "10150237978467733"
          }
3. Notes
  1.  Use any stack or infrastructure you would like
  2.  Treat any response status other than 200 as an error
4. Please supply curl example which demonstrate the usage of the service (IMPORTANT!!!!).
