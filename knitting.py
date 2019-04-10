from math import log
from math import exp

initialWeight = 93.08

rowWeights = [92.88, 92.59, 92.20, 92.04, 91.71, 91.40, 91.08, 90.74,
              90.42, 90.04, 89.71, 89.34]

wrongSideRows = rowWeights[1::2]
rightSideRows = rowWeights[::2]


def decay(Wr, R):
    # this function calculates the exponential decay rate of yarn ball weight
    # given some row R and the weight (Wr) of the yarn ball after row R
    value = log((Wr / initialWeight)) / R
    return value


print('\nDecay Rate For Last 4 Rows:')

decayRates = []

for index, weight in enumerate(rowWeights):
    # calculate the decay rates for all rows
    # because of the off-by-one nature of indexes, row R is index + 1
    rate = decay(weight, index + 1)
    decayRates.append(rate)

    # print the decay rates for the past 4 rows
    if index - len(rowWeights) >= -4:
        print(f'Row {index + 1}: {round(rate, 4)} / {round(rate, 3)}')

avgRate = sum(decayRates) / len(decayRates)

print('\nAverage Decay Rate:')
print(f'{round(avgRate, 5)} / {round(avgRate, 3)}\n')

futureWeight = initialWeight * exp(decayRates[-1] * (len(rowWeights) + 3))

print('Predicted Weight After Next 3 Rows:')
print(f'{round(futureWeight, 3)} grams\n')


def predictAhead(list_name, aheadBy):
    for index, decay in enumerate(decayRates):
        predicate = initialWeight * exp(decay * (index + aheadBy + 1))
        if index < len(rowWeights) - aheadBy:
            pairs = (round(predicate, 2), rowWeights[index + aheadBy])
            list_name.append(pairs)


predicted_3_ahead = []
predictAhead(predicted_3_ahead, 3)
# print(predicted_3_ahead)

predicted_1_ahead = []
predictAhead(predicted_1_ahead, 1)
# print(predicted_1_ahead)
