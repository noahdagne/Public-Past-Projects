# Noah Dagne
# INST326
t = ['Hey how are you', 'I am fine']
def count_chars(t):
    charlist = {}
    lent = len(t)
    d = dict()
    for i in t:
        for dictionary1 in i:
            if dictionary1 in charlist:
                charlist[dictionary1] = charlist[dictionary1] + 1
            else:
                charlist[dictionary1] = 1
    return charlist



f = open('palindromes.txt','r')

def read_to_list():
    palindromefile = f.readlines()
    palindromefile = [i.replace('\n','') for i in palindromefile]
    f.close()
    return palindromefile

print(count_chars(read_to_list(x)))
