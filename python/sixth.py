#variant 1
def count_of_words(string):
    res = {}
    res_string = ''
    for word in string.split():
        if word not in res.keys():
            res[word] = 0
        elif word in res.keys():
            res[word]+=1
        res_string+=f'{res[word]} '
    return res_string
print(count_of_words('one two one tho three'))