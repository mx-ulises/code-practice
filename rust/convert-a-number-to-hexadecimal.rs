impl Solution {
    pub fn to_hex(mut num: i32) -> String {
        match num {
            0 => return "0".to_string(),
            -2147483648 => return "80000000".to_string(),
            _ => 0
        };
        let mut negative = false;
        if num < 0 {
            num = 2147483647 + (num + 1);
            negative = true;
        }
        let CHAR_MAP = "0123456789abcdef";
        let mut hex = Vec::new();
        while 0 < num {
            let c = CHAR_MAP.chars().nth((num % 16) as usize).unwrap();
            hex.push(c);
            num = num / 16;
        }
        if negative {
            let h = hex.pop().unwrap() as i32 - 40;
            let c = CHAR_MAP.chars().nth(h as usize).unwrap();
            hex.push(c);
        }
        hex.reverse();
        return  hex.iter().collect();
    }
}
