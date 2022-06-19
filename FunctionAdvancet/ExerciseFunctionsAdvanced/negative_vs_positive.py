
numbers = list(map(int, input().split()))
sum_positives = sum(x for x in numbers if x >= 0)
sum_negatives = sum(x for x in numbers if x < 0)
print(sum_negatives)
print(sum_positives)
if sum_positives > abs(sum_negatives):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")





