#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
a)  a = 0
    while (a < n * n * n): # this is equal to 0(n^3)
      a = a + n * n # the loop is essentially ... a + n * n < n * n * n
                    # if you take out n * n ... it comes back as a < n
                    # it comes out to be O(n)... it is linear ... it only multiplies n. 
                    # the loop ends when it reaches n^3


                    
                    ```
```
b)  sum = 0
    for i in range(n):     # O(n)
      j = 1                 
      while j < n:          # O(n)
        j *= 2              # O(log(n))... it is being halved
        sum += 1

                            # j is nested inside of i
                            # multiply O(n) * O(log(n))
                            # O(nlog(n))
                            # The inner loop runs in half the iterations because j reaches the values if n twice as fast as i
                            # The outer loop runs only or every value of n
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:                    # O(1)
        return 0

      return 2 + bunnyEars(bunnies-1)     # O(n-1)
                                          # O(1) + O(n-1) = O(n)
                                          # it only increases with with the size of n

```

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I think a binary search is needed.


You need a list of n for number of floors
then you have to find the midpoint (lowest/highest)
split the levels from (lowest/highest)
check if the egg will break at midpoint
if it breaks, you go through the steps again... but this time only use jus the lower floors
if it doesnt break then you skip the lower floors and focus on the highest floors
you go through the steps to find the midpoint for the highest floors where it breaks
at this point it should only be two floors
choose the floor where itr doesnt break

if you arte finding the number and hen dividing you have to use O(log n)