# this is the reference implementation of backpropotation 
# or in other words ,this is the first edition, reference from
# original Author Nell Schemenauer  and Modified Author 
# James Howard,  thanks to them.

import math
import random

random.seed(0)

# calculate random number between the given two number a and b
def rand(a,b):
	return (b-a)*random.random()+a


def BuildMatrix(I,J,fill=0.0):
	m=[]
	for i in range(I):
		m.append([fill]*J)
	return m

# the sigmoid function of ours, using tanh form
def sigmoid(x):
	return math.tanh(x)


def dsigmoid(y)
	return 1.0-y**2

def plot(inputs,outputs,actual):
	"""" plot a given function
	with inputs and outputs given,using for
	network debuging""""
	try:
         import matplotlib.pyplot
	except:
	 raise ImportError,"matplot package not found"
	fig= matplotlib.pyplot.figure()
	ax1=fig.add_subplot(1 1 1)
	ax1.plot(inputs,actual,'b-')
	ax1.plot(inputs,outputs,'r.')
	matplotlib.pyplot.draw()



class NN:
	def __init__(self,ni,nh,no,regression=False):
	# the NN constructor, ni,nh,no are number of nodes in input, hidden,output layer, regression is for choosing if network is to be trained

	self.regression = regression
	
	self.ni = ni+1   # +1 for bias 
	self.nh = nh+1
	self.no= no

	# activations for nodes
	self.ai = [1.0]*self.ni
	self.ah = [1.0]*self.ni
	self.ao = [1.0]*self.ni
	








