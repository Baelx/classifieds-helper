require 'rest-client'
require 'uri'

uri = URI.parse("https://www.usedvictoria.com/classifieds/all?description=4k+monitor")
request = Net::HTTP::Get.new(uri)
request["Connection"] = "keep-alive"
request["Pragma"] = "no-cache"
request["Cache-Control"] = "no-cache"
request["Upgrade-Insecure-Requests"] = "1"
request["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36"
request["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
request["Referer"] = "https://www.usedvictoria.com/"
request["Accept-Language"] = "en-US,en;q=0.9,fr;q=0.8,fr-CA;q=0.7"
request["Cookie"] = "gdcABG=A; _ga=GA1.2.495393677.1546672795; _gid=GA1.2.905242110.1548359700; _fbp=fb.1.1548446992611.1663196385; pused=a62e3106ce78a30d50e41dd37830d306eb7842453TV68BqYPjt8PkAmHt7epazxdK2ZdAhiKnTzkE4612yitmoDUaGH24PH9Vr9t3FCtBC+Kr6mn+g65NNDfd17Q9G/oom8PEo+ZPZese6CaRMnjSKBqW6rf2HLxaqGdeNQ6wHVvMuchN6uKA0zoz+8fDJsTBDaX+z+MFIRqBBjeG96GrA="



RestClient.get 'https://www.usedvictoria.com/classifieds/all?description=4k+monitor'

RestClient.get 'https://www.usedvictoria.com/classifieds/all?description=4k+monitor', {params: {id: 50, 'foo' => 'bar'}}
