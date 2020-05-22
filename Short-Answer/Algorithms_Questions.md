# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

# this is o(n) because the dependence is placed on the n, no matter the times it is run. When the input size increases, the runtime will grow at the same rate.
```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

# This is O(n^2) because the first loop runs O(n) and teh second loop would also run n times O(n)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

# This is constant O(1) because the runtime is unaffected by the soze of input
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

# floor would be = O
# broken would be = False
# while: 
# is not broken
# Floor would += 1 
# if the egg breaks ,
# we exit the loop and return floor -1 = O(n)