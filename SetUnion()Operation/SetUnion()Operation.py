TotalEnglish = int(input())
RollOfEnglish = list(map(int, input().split()))
TotalFrench = int(input())
RollOfFrench = list(map(int, input().split()))
TotalBoth = 0

TotalRoll = set(RollOfEnglish) | set(RollOfFrench)

for i in TotalRoll:
    TotalBoth = TotalBoth + 1
print(TotalBoth)