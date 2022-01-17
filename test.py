def testingfound():
    firstinput =  [5, 7, 11, 20, 2, 13, 9]
    sum1 = 22
    sum2 = 21
    secondinput =  [10, 39, 34, 5, 55, 44]
    sum3 = 44
    resultone = [5, 6]
    resulttwo = None
    result3 = [1,3]
    assert set(findingthesum(firstinput,sum1)) == set(resultone)
    assert findingthesum(firstinput,sum2) == resulttwo
    assert set(findingthesum(secondinput,sum3)) == set(result3)



def findingthesum(data,sum):
    list = []
    for i in range(len(data)):
        if data[i]%2!=0:
            for j in range(len(data)):
                if data[j]%2 !=0 and j!=i:
                    if data[i]+data[j]==sum:
                        return [i,j]
    return None

def testingodds():
    firstinput =  [99, 10, 200, 113, 54, 89, 23]  
    secondinput =  [555, 666, 20, 579, 174, 999, 21] 
    resultone = [10, 54, 200]
    resulttwo = [20, 174, 666]
    assert set(oddnumberremoval(firstinput)) == set(resultone)
    assert set(oddnumberremoval(secondinput)) == set(resulttwo)

def oddnumberremoval(data):
    list = []
    for i in data:
        if i%2==0:
            list.append(i)
    return list


testingodds()
print("Testing for both Inputs in oddnumberremoval() is passed.")
testingfound()
print("Testing for both Inputs in findingthesum() is passed.")