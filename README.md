# arb-lex-sort
Arbitrary lexicographic sorting of strings

##### Runtime analysis:
If m is the number of strings to be sorted and n is the length of the longest such string, the every-case time complexity of the `arb_lex_sort` function is O(mn). Reasoning is as follows. The for loop starting on line 4 will have m iterations, and thus is O(m) (since `len` is a constant-time function for strings). The slice operations on lines 9 and 10 are also O(m). Now consider the nested for loop structure starting on line 12. If p is the length of the letter precedence string (i.e. the second parameter of `arb_lex_sort`), then the innermost for loops on lines 16 and 22 will have mn and mnp iterations, respectively. However, note that p is bounded by 26 and hence can be ignored in the asymptotic analysis. Thus, the entire nested for loop structure starting on line 12 is O(mn). Since this subsumes the earlier time complexities, the `arb_lex_sort` function as a whole is O(mn).
