import numpy as np

class MultiLayerPerceptron:

    def __init__(self, input_layer, hidden_layer, output_layer, num_iteration=1000):
        '''
        A class representing a Multi-Layer Perceptron network.
        '''
        self.input_layer = input_layer
        self.hidden_layer = hidden_layer
        self.output_layer = output_layer
        self.num_iteration = num_iteration
        
        self.weights_to_hidden = np.random.randn(self.input_layer, self.hidden_layer) 
        self.weights_to_output = np.random.randn(self.hidden_layer, self.output_layer)


    def feed_forward(self, inputs):
        '''
        Forward propagate through the network calculating the output value of each perceptron.
        '''
        product_to_hidden = np.dot(inputs, self.weights_to_hidden)
        activation_of_hidden = self.activation_function(product_to_hidden)
        product_to_output = np.dot(activation_of_hidden, self.weights_to_output)
        activation_of_output = self.activation_function(product_to_output)
        return activation_of_output


    def activation_function(self, s, derivative=False):
        '''
        A simple sigmoid activation function. 
        '''
        if derivative:
            return s * (1 - s)
        return 1 / (1 + np.exp(-s))


    def back_propagation(self, inputs, expected_outputs, prediction):
        '''
        Back propagate through the network and calculate the error.
        '''



    def fit(self, inputs, expected_outputs):
        '''
        Train the network on the given input and output.
        '''
        for _ in range(self.num_iterations):
            prediction = self.feed_forward(inputs)
            self.back_propagation(inputs, expected_outputs, prediction)


def main():
    '''
    Firstly the network is trained and then it's tested against the leters.csv in
    order to find the letters J and M.
    '''
    # the letters J and M represented in a 10x10 matrix, 
    # 0 for blank and 1 for a colored cell 
    # csv file contents:
    # 2 x letter J,2 x letter m, 4 x random letter, letter L, letter I 
    inputs = np.genfromtxt('./train_letters.csv', delimiter=',')

    expected_outputs = np.array(([1], [1], [1], [1], [0], [0], [0], [0], [0], [0]))
    print(expected_outputs)

    mlp = MultiLayerPerceptron(input_layer=10, hidden_layer=20  , output_layer=1, num_iteration=10000)



if __name__ == '__main__':
    main()