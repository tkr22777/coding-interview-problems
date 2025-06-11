# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from typing import List

class Solution:

    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        items = set()
        table = {}
        
        for order in orders:
            customerName, tableNumber, foodItem = order[0], order[1], order[2]
            items.add(foodItem)

            if tableNumber not in table:
                table[tableNumber] = {}

            if foodItem not in table[tableNumber]:
                table[tableNumber][foodItem] = 0

            table[tableNumber][foodItem] += 1

        ordered_items = sorted(list(items))
        result = [["Table"] + ordered_items]
        table_numbers = sorted([int(a) for a in list(table.keys())])

        for tn in table_numbers:
            tid = str(tn)
            row = [tid]

            for item in ordered_items:
                if item in table[tid]:
                    row.append(str(table[tid][item]))
                else:
                    row.append("0")

            result.append(row)

        return result
