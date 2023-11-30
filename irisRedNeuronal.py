import numpy as np
import csv

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

data = []
labels = []
with open('iris.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  
    for row in csv_reader:
        data.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
        labels.append(row[4])

data = np.array(data)
labels = np.array(labels)

unique_labels = np.unique(labels)
num_classes = len(unique_labels)
labels_encoded = np.zeros((len(labels), num_classes))
for i, label in enumerate(labels):
    labels_encoded[i, np.where(unique_labels == label)[0][0]] = 1


input_size = data.shape[1]
hidden_size1 = 10
hidden_size2 = 20
output_size = num_classes


np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size1)
W2 = np.random.randn(hidden_size1, hidden_size2)
W3 = np.random.randn(hidden_size2, output_size)


learning_rate = 0.1
epocas = 1000


for _ in range(epocas):

    hidden1 = sigmoid(np.dot(data, W1))
    hidden2 = sigmoid(np.dot(hidden1, W2))
    output = sigmoid(np.dot(hidden2, W3))

  
    error = output - labels_encoded
   

    e3=error * (output * (1 - output))
    dW3 = np.dot(hidden2.T, e3)
    e2  = np.dot(e3,W3.T)*(hidden2*(1-hidden2))
    dW2 = np.dot(hidden1.T, e2)
    e1  = np.dot(e2,W2.T)*(hidden1*(1-hidden1))
    dW1 = np.dot(data.T, e1)
    
    W3 -= learning_rate * dW3
    W2 -= learning_rate * dW2
    W1 -= learning_rate * dW1


hidden1 = sigmoid(np.dot(data, W1))
hidden2 = sigmoid(np.dot(hidden1, W2))
output = sigmoid(np.dot(hidden2, W3))
predic = np.argmax(output, axis=1)
precision = np.mean(predic == np.argmax(labels_encoded, axis=1))
print("precision: {:.2f}%".format(precision * 100))



prueba = [[6.1, 2.9, 4.7, 1.4]]
print ("datos para hacer la prediccion: ", prueba)
hidden1 = sigmoid(np.dot(prueba, W1))
hidden2 = sigmoid(np.dot(hidden1, W2))
output = sigmoid(np.dot(hidden2, W3))
predic = np.argmax(output, axis=1)
if predic==0:
    print("prediccion: iris setosa")
if predic==1:
    print("prediccion: iris versicolor")
if predic==2:
    print("prediccion: iris virginica")
