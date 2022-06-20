def number_sum(*args):
    sum_negatives = sum(x for x in args if x >= 0)
    sum_positives = sum(y for y in args if y < 0)
    return sum_negatives, sum_positives


nums = list(map(int, input().split()))
negativ_sum, positiv_sum = number_sum(*nums)
print(negativ_sum)
print(positiv_sum)
if positiv_sum > abs(negativ_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
