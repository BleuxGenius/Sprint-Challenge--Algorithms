'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # counts starts at 0 
    counts = 0 
    # if the length of the word is greater than 2
    if len(word) < 2:
    # return 0 
        return 0
    # if the word we are extracting is equal to th
    if word[:2] == 'th':
    # the count will go up by 1     
        counts += 1
    # the count is adding to the variable.
    counts += count_th(word[1:])

    return counts     
