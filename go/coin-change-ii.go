func change(amount int, coins []int) int {
    memory_size := amount + 1
    memory := make([]int, memory_size)
    memory[0] = 1
    for i := 0; i < len(coins); i++ {
        for value := coins[i]; value <= amount; value++ {
            memory[value] += memory[value - coins[i]]
        }
    }
    return memory[amount]
}
