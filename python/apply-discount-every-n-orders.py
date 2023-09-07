class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self._product_prices = {products[i]: prices[i] for i in range(len(products))}
        self._n = n
        self._discount = 1 - (discount / 100.0)
        self._current_customer = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        for i in range(len(product)):
            price = self._product_prices[product[i]]
            bill += price * amount[i]
        self._current_customer += 1
        if self._current_customer == self._n:
            self._current_customer = 0
            bill *= self._discount
        return bill

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
