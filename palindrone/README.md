### Question 1: is_palindrome
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward (Wikipedia, 2016).
Write a function is_palindrome(s) which takes in a string s and outputs a boolean on whether s is a palindrome.
Sample execution:
> is_palindrome('abcdedcba')<br>
True

> is_palindrome('fooooo')<br> 
False

---

### Question 2: longest_palindrome
Write a function longest_palindrome(str) which takes in a string input str and computes the length of the longest palindrome within str. You may reuse the function is_palindrome from Question 1.
Sample execution:
> longest_palindrome('avkesekjhkj')<br>
5 # 'kesek'

> longest_palindrome('foobar')<br>
2 # 'oo'