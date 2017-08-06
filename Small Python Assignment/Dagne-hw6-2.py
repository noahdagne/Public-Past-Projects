# Noah Dagne
# INST326
def is_palindrome(t):
    reverse_t = ""
    i = len(t) - 1
    while i >= 0:
        reverse_t = reverse_t + t[i]
        i -= 1
    if reverse_t == t:

        return True

    else:

        return False

f = open('palindromes.txt','r')

def read_to_list():
    palindromefile = f.readlines()
    palindromefile = [i.replace('\n','') for i in palindromefile]
    f.close()
    return palindromefile

read_to_list()

