FirstElement = 1
def InsertionSort(TheData):
    for Count in range(FirstElement,len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while (NextValue >= 0 and Inserted != 1):
            if (DataToInsert < TheData[NextValue]):
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
            else:
                Inserted = 1
        TheData[NextValue + 1] = DataToInsert

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
InsertionSort(TheData)
print(TheData)