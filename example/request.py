from json import loads
from requests import get

url = "https://some-random-api.ml/lyrics?title="
title = "Kendric Lamar DNA"

response_txt = str(get(url + title).text)
response_json = loads(response_txt)

lyrics = response_json["lyrics"]

print(lyrics)
