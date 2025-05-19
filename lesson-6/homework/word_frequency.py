try:
    with open("sample.txt", 'r') as file:
        pass
except:
    text = input("Enter any text or paragraph: ")
    with open("sample.txt", 'w') as file:
        file.write(text)

words = []
word = {}
with open("sample.txt", 'r') as file:
    text = file.read()
    text = text.lower()
    st = ''
    for i in text:
        if i >= 'a' and i <='z' or i == "'":
            st += i
        elif st != '':
            words.append(st)
            st = ''
    if st != '':
        words.append(st)
        words.count
    #print(words)
    for i in words:
        if not(i is word.keys()):
            x = words.count(i)
            word.update({i : x})
    num = int(input('Enter how many "top common words" to display: '))
    print("Word Count Report")
    print("Total Words:", len(word))
    print(f"Top {num} Words:")
    word = dict(sorted(word.items(), key=lambda item:item[1], reverse=True))
    count = 0
    for i in word:
        print(i, '-', word[i])
        count += 1
        if count > num-1:
            break
