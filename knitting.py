from math import log
from math import exp

rowWeights = [92.88, 92.59, 92.20, 92.04, 91.71, 91.40, 91.08, 90.74,
              90.42, 90.04, 89.71, 89.34]

wrongSideRows = rowWeights[1::2]
rightSideRows = rowWeights[::2]
initialWeight = 93.08


def decay(WT, R):
    # WT = weight at row t
    # R = number of rows since initial weight
    value = log((WT / initialWeight)) / R
    return value


decayRates = []

# calculate the decay rate for each new row
print('\nDecay Rate For Last 4 Rows:')
for index, weight in enumerate(rowWeights):
    rate = decay(weight, index + 1)
    rate_r3 = round(rate, 3)
    rate_r4 = round(rate, 4)

    decayRates.append(rate)

    if index - len(rowWeights) >= -4:
        print(f'Row {index + 1}: {rate_r4} / {rate_r3}')

avgRate = sum(decayRates) / len(decayRates)

print('\nAverage Decay Rate:')
print(f'{round(avgRate, 5)} / {round(avgRate, 3)}\n')

futureWeight = initialWeight * exp(decayRates[-1] * (len(rowWeights) + 3))


def predictAhead(list_name, aheadBy):
    for index, decay in enumerate(decayRates):
        predicate = initialWeight * exp(decay * (index + aheadBy + 1))
        if index < len(rowWeights) - aheadBy:
            pairs = (round(predicate, 2), rowWeights[index + aheadBy])
            list_name.append(pairs)


predicted_3_ahead = []
predictAhead(predicted_3_ahead, 3)
print(predicted_3_ahead)

predicted_1_ahead = []
predictAhead(predicted_1_ahead, 1)
print(predicted_1_ahead)

print('Predicted Weight After Next 3 Rows:')
print(f'{round(futureWeight, 3)} grams\n')

# figure out a way to predict the weight for x number of rows
# and combine that with the actual recorded weight for those rows?
