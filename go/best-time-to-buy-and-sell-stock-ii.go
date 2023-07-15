func maxProfit(prices []int) int {
	BUY, SELL := 0, 1
	previousPrice := 10000
	purchasePrice := 0
	profit := 0
	nextOperation := BUY
	for _, price := range prices {
		if nextOperation == BUY && previousPrice < price {
			nextOperation = SELL
			purchasePrice = previousPrice
		} else if nextOperation == SELL && price < previousPrice {
			nextOperation = BUY
			profit += previousPrice - purchasePrice
		}
		previousPrice = price
	}
	if nextOperation == SELL {
		profit += previousPrice - purchasePrice
	}
	return profit
}
