def maxDomino(row,column):
    area=row*column//2
    return area
row, column = map(int, input().split())
row=3
column=3
print(maxDomino(row,column))
