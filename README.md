## #212 Word Search II (wordSearch.py) 
Given an `m x n` `board` of characters and a list of strings `words`, return _all words on the board_.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

```

**Constraints:**

-   `m == board.length`
-   `n == board[i].length`
-   `1 <= m, n <= 12`
-   `board[i][j]` is a lowercase English letter.
-   `1 <= words.length <= 3 * 10<sup>4</sup>`
-   `1 <= words[i].length <= 10`
-   `words[i]` consists of lowercase English letters.
-   All the strings of `words` are unique.

## #1323 Maximum 69 Number (max69.py)
*7th November 2022*

You are given a positive integer `num` consisting only of digits `6` and `9`.

Return _the maximum number you can get by changing **at most** one digit (_`6` _becomes_ `9`_, and_ `9` _becomes_ `6`_)_.

**Example 1:**

```
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

```

**Example 2:**

```
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

```

**Example 3:**

```
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

```

**Constraints:**

-   `1 <= num <= 10<sup>4</sup>`
-   `num` consists of only `6` and `9` digits.

## Make The String Great - LeetCode (makegreat.py)
*8th November 2022*

Given a string `s` of lower and upper case English letters.

A good string is a string which doesn't have **two adjacent characters** `s[i]` and `s[i + 1]` where:

-   `0 <= i <= s.length - 2`
-   `s[i]` is a lower-case letter and `s[i + 1]` is the same letter but in upper-case or **vice-versa**.

To make the string good, you can choose **two adjacent** characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return _the string_ after making it good. The answer is guaranteed to be unique under the given constraints.

**Notice** that an empty string is also good.

**Example 1:**

```
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

```

**Example 2:**

```
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

```

**Example 3:**

```
Input: s = "s"
Output: "s"

```

**Constraints:**

-   `1 <= s.length <= 100`
-   `s` contains only lower and upper case English letters.

## Remove All Adjacent Duplicates In String (adjDuplicates.py)
*10th November 2022*

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

We repeatedly make **duplicate removals** on `s` until we no longer can.

Return _the final string after all such duplicate removals have been made_. It can be proven that the answer is **unique**.

**Example 1:**

```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

```

**Example 2:**

```
Input: s = "azxxzy"
Output: "ay"

```

**Constraints:**

-   `1 <= s.length <= 10<sup>5</sup>`
-   `s` consists of lowercase English letters.

## Min Stack (minStack.py)
*10th November 2022*

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

-   `MinStack()` initializes the stack object.
-   `void push(int val)` pushes the element `val` onto the stack.
-   `void pop()` removes the element on the top of the stack.
-   `int top()` gets the top element of the stack.
-   `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

```

**Constraints:**

-   `-2<sup>31</sup> <= val <= 2<sup>31</sup> - 1`
-   Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
-   At most `3 * 10<sup>4</sup>` calls will be made to `push`, `pop`, `top`, and `getMin`.