class Solution:
    def get_data(orders: List[List[str]], f: Callable, index: int) -> List[int]:
        data = set()
        for order in orders:
            data.add(f(order[index]))
        data = list(data)
        data.sort()
        return data

    def init_food_orders_per_table(tables: List[int], plates: List[str]) -> List[List[object]]:
        food_orders_per_table = [["Table"] + plates]
        for table in tables:
            table_order = [table] + [0] * len(plates)
            food_orders_per_table.append(table_order)
        return food_orders_per_table

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # Get list of tables and plates
        tables = Solution.get_data(orders, int, 1)
        plates = Solution.get_data(orders, str, 2)
        # Init output table
        food_orders_per_table = Solution.init_food_orders_per_table(tables, plates)
        # Get mappings of plate -> index and table -> index
        plates = {plates[i]: i + 1 for i in range(len(plates))}
        tables = {tables[i]: i + 1 for i in range(len(tables))}
        # Fill the food_orders_per_table
        for order in orders:
            table = int(order[1])
            plate = order[2]
            table_index = tables[table]
            plate_index = plates[plate]
            food_orders_per_table[table_index][plate_index] += 1
        # Format the output
        for i in range(len(food_orders_per_table)):
            food_orders_per_table[i] = map(str, food_orders_per_table[i])
        return food_orders_per_table
