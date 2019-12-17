'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if len(word) < 2:                          # if there are less than two then skip
        return 0
    elif word[:2] == 'th':                  #recursion, is th in the first two indexes?
        return 1 + count_th(word[1:])       # if so, jump to the next index but skip the first
    else:
        return count_th(word[1:])           # dont count, just remove that first index
    pass
