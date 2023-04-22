struct Codec {
    mapper: Vec<String>
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Codec {
            mapper: Vec::new(),
        }
    }

    // Encodes a URL to a shortened URL.
    fn encode(&mut self, longURL: String) -> String {
        let i = self.mapper.len();
        self.mapper.push(longURL);
        return format!("http://tinyurl.com/{i}");
    }

    // Decodes a shortened URL to its original URL.
    fn decode(&self, shortURL: String) -> String {
        let i: usize = shortURL.replace("http://tinyurl.com/", "").parse().unwrap();
        return self.mapper[i].to_string();
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let s: String = obj.encode(strs);
 * let ans: VecVec<String> = obj.decode(s);
 */
