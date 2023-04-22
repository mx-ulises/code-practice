class Codec:

    def __init__(self):
        self.mapper = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        i = len(self.mapper)
        self.mapper.append(longUrl)
        return f"http://tinyurl.com/{i}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        i = int(shortUrl.split("/")[-1])
        return self.mapper[i]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))