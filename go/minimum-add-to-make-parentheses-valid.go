func minAddToMakeValid(s string) int {
    balance := 0
    add := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            balance += 1
        }
        if s[i] == ')' {
            balance -= 1
        }
        if balance < 0 {
            balance = 0
            add += 1
        }
    }
    add += balance
    return add
}
