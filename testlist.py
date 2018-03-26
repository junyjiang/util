def checkthree(l):
    if l == None:
        return '列表为空'
    for i in range(len(l)):
        for j in range(1,len(l)):
            if l[i] + l[j] == 3:
                if i!=j:
                    print(i, j)
if __name__ == "__main__":
    li = {}
    print(checkthree(li))
