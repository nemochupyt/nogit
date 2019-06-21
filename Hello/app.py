import sys
import requests

r = requests.get(
    "https://www.youtube.com/watch?v=-nh9rCzPJ20&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=112&t=0s"
)
print(r.status_code)
print(r.ok)