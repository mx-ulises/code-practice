impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, mut n: i32) -> bool {
        if n == 0 {
            return true;
        }
        let len = flowerbed.len();
        let mut i = 0;
        while i < len {
            if flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.len() - 1 || flowerbed[i + 1] == 0) {
                if let Some(elem) = flowerbed.get_mut(i) {
                    *elem = 1;
                    n -= 1;
                    if n == 0 {
                        return true;
                    }
                }
            }
            i += 1;
        }
        return false;
    }
}
