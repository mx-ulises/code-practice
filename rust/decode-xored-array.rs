impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        let mut arr = Vec::new();
        arr.push(first);
        for i in 0..encoded.len() {
            arr.push(arr[i] ^ encoded[i]);
        }
        return arr;
    }
}
