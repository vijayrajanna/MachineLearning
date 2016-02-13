# The program will scale input features to a range between 0 to 1
from sklearn.preprocessing import MinMaxScaler
import numpy

weights = numpy.array([[3.4], [5.6], [7.3],[6.8], [4.1], [5.4], [3.3],[8.4]])
heights = numpy.array([[115.0], [120.0], [130.0],[140.0], [150.0], [160.0], [170.0],[175.0]])

scaler = MinMaxScaler()

rescaledWeight = scaler.fit_transform(weights)
rescaledHeight = scaler.fit_transform(heights)

newFeature = []

index = 0
for x in rescaledHeight:
    newFeature.append(x[0] + (rescaledWeight[index])[0])
    index += 1

print '========================='
print rescaledWeight
print '========================='
print rescaledHeight
print '========================='
print newFeature


