
numBottles = int(input())
numExchange = int(input())

empty_Bottle = 0
count = 0
surplus = 1
while surplus != 0:
    count += numBottles
    surplus = numBottles // numExchange
    empty_Bottle += numBottles % numExchange

    numBottles = surplus
    if empty_Bottle >= numExchange:
        surplus += empty_Bottle // numExchange
        numBottles = surplus
        empty_Bottle = empty_Bottle % numExchange
print("最多能喝", count, "瓶酒")
