def findword(word,file):
    with open(file,'r') as a:
        count=0
        rline=a.readlines()
        for i in rline:
            list1=i.split()
            for j in list1:
                if j==word:
                    count+=1
    print(count)


findword('same','yinwen.txt')
             
