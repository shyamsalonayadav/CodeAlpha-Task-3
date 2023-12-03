import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.base62_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def shorten_url(self, long_url):
        # Hash the long URL to generate a unique identifier
        hash_object = hashlib.md5(long_url.encode())
        hash_hex = hash_object.hexdigest()

        # Convert the hash to base62 to create a short URL
        short_url = self.encode_base62(int(hash_hex, 16))

        # Store the mapping in the dictionary
        self.url_mapping[short_url] = long_url

        return f"short.url/{short_url}"

    def expand_url(self, short_url):
        # Retrieve the long URL from the dictionary using the short URL
        long_url = self.url_mapping.get(short_url.replace("short.url/", ""))
        return long_url if long_url else "URL not found"

    def encode_base62(self, num):
        base62 = ""
        while num > 0:
            num, remainder = divmod(num, 62)
            base62 = self.base62_chars[remainder] + base62
        return base62 or "0"

# Example usage
url_shortener = URLShortener()
long_url = "https://www.example.com/some/long/url"
short_url = url_shortener.shorten_url(long_url)
print(f"Short URL: {short_url}")

expanded_url = url_shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")
