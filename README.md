# 🧠 Leetcode 250 - Mastering Top Coding Interview Problems

Welcome to the **Leetcode 250** repository – a curated collection of the **250 most frequently asked Leetcode questions** with **clean Python solutions**, detailed explanations, and optimized code — ideal for preparing for **FAANG**, **Big Tech**, and startup coding interviews.

> ✅ If you’re searching for:  
> `Leetcode 250` · `Top 250 Leetcode Problems` · `FAANG Coding Prep` · `Python Interview Questions`  
> You’ve landed in the **right place**.

---

## 🚀 Why This Repository Stands Out

✔️ 250 curated questions to maximize your **DSA preparation**  
✔️ Clean and readable **Python solutions**  
✔️ Includes **intuition, approach, time/space complexity**  
✔️ Structured by topic for ease of learning  
✔️ Suitable for **Google, Amazon, Meta, Microsoft, Netflix**  
✔️ Regular updates and daily commit logs  
✔️ Easy folder navigation and problem search  

---

## 📚 Structured Problem Categories

| 💡 Topic                | 📌 Folder Name        |
|------------------------|-----------------------|
| Arrays & Strings       | `arrays_strings/`     |
| Linked Lists           | `linked_lists/`       |
| Trees & Binary Trees   | `trees/`              |
| Graphs & Traversals    | `graphs/`             |
| Dynamic Programming    | `dp/`                 |
| Sliding Window         | `sliding_window/`     |
| Binary Search          | `binary_search/`      |
| Backtracking           | `backtracking/`       |
| Stack & Queues         | `stack_queue/`        |
| Heap & Greedy          | `heap_greedy/`        |
| Bit Manipulation       | `bit_manipulation/`   |
| Math & Logic           | `math_logic/`         |
| Others & Miscellaneous | `others/`             |

📊 Progress Tracker
✅ Total Questions: 250
🔄 Solved: XX
📅 Updates: Daily commits
⭐ Stars, forks, and contributions are welcome!
⭐ Support & Share

If this project helps you:
🌟 Give it a star
🍴 Fork it to your profile

🗣️ Share with friends and aspiring interview candidates

## 🧠 Example Format for Each Solution

```python
"""
Problem: 121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Level: Easy

Approach:
- Track the minimum price seen so far
- Track the maximum profit if sold today

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit
---
