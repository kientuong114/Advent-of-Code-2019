def main():
    startNum = 236491
    endNum = 713787
    count = 0
    for i in range(startNum, endNum +1):
        cond = False
        blackList = set()
        if ''.join(sorted(list(str(i)))) == str(i):
            for j in range(len(str(i))-1):
                if int(str(i)[j]) in blackList:
                    print("a")
                    cond = False
                    continue
                else:
                    blackList = set()
                if j+2 < len(str(i)) and str(i)[j] == str(i)[j+1] == str(i)[j+2]:
                    print("b")
                    cond = False
                    blackList.add(int(str(i)[j]))
                    print(blackList)
                elif j+2 < len(str(i)) and str(i)[j] == str(i)[j+1] and str(i)[j] != str(i)[j+2]:
                    print("c")
                    cond = True
                    break
                elif j+2 == len(str(i)) and str(i)[j] == str(i)[j+1]:
                    cond = True
        if cond == True:
            print(str(i))
            count += 1
            print("count inc")
    print(count)





if __name__ == "__main__":
    main()
