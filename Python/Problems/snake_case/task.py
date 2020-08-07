def change_case():
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in word]).lstrip('_')


word = input()
print(change_case())
