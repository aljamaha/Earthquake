# Modifies a traceList-based h5 file and turns it to an input file for the cnn code

import numpy as np
import h5py, os, sys, pickle
import pdb #pdb.set_trace()
import matplotlib.pyplot as plt
from copy import deepcopy

'General Inputs related to Earthquake parameters'
nplot  = 0
snrMin = 0
ns     = 400 # Samples used are nstart:nstart+ns
nstart = 101
augment = 0

'data loading'
infile  = '../onsetWforms_allM3p_180403_reduced.h5'
fin   = h5py.File(infile,'r')

print 'reading data ...'
print '=== keys in data set:==='
for name in fin: print name #prints the keys under data set [earthquake/noise/tele/regi]

print '=== keys under earthquake ==='
for name in fin['quake']: print name #printes attributes under quake [featureNames/featureVals/numMeta/wfrom]

# QUAKE QUAKE QUAKE QUAKE QUAKE QUAKE QUAKE QUAKE QUAKE QUAKE QUAKE
'Extracts different details fromt eh data [mainly wforms/featureVals/featureNames/numMeta]'
print('=== Reading quake data ====')
Xq       = fin['/quake/wforms'].value
Xq       = np.swapaxes(Xq,0,1)
Xq       = np.swapaxes(Xq,1,2)
Xq       = Xq[:,nstart:nstart+ns,:]
Fq       = fin['/quake/featureVals'].value
Fq       = np.swapaxes(Fq,0,2)
fqnames  = fin['/quake/featureNames'].value
metaVals = fin['/quake/numMeta'].value

'Time frame snippets [1,2,3,4]'
snippetList = fin['/tele/featureVals'].attrs['snippetList'].astype('int')
snippetT    = snippetList*0.5

'assigning variables to metaVas [earthquake magnitude, hypocentral distance, etc.]'
mq   = metaVals[0,:]
rq   = metaVals[1,:]
idq  = metaVals[4,:]
snrq = np.power(10,metaVals[3,:])
nq   = Xq.shape[1]

# NOISE NOISE NOISE NOISE NOISE NOISE NOISE NOISE NOISE NOISE NOISE
print('Reading noise data ..')
Xn       = fin['/noise/wforms'].value
Xn       = np.swapaxes(Xn,0,1)
Xn       = np.swapaxes(Xn,1,2)
Xn       = Xn[:,nstart:nstart+ns,:]
Fn       = fin['/noise/featureVals'].value
Fn       = np.swapaxes(Fn,0,2)
metaVals = fin['/noise/numMeta'].value
qvals    = fin['/noise/qval'].value

mn   = metaVals[0,:]
rn   = metaVals[1,:]
idn  = metaVals[4,:]
snrn = np.power(10,metaVals[3,:])
nn   = Xn.shape[1]

print 'finished reading data ...'

def waveform():
	'returns waveform of earthquakes and noise'
	return Xq, Xn

def magnitude():
	'returns magnitude of earthquakes and noise'
	return mq, mn

def attributes():
	'returns the 24 attributes of earthquakes and noise'
	return Fq, Fn


def plot_wform():
	'plotting a sample wform'
	i = 1 #random index of a wafeform
	xyz = 1 #choosing x form of the wfrom
	t = np.linspace(0,5,400) #generating x-axis (time) from 0 to 5 s
	plt.plot(t,Xq[i,:,xyz])
	plt.plot(t,Fq[1,:,1])
	plt.show() #if you want to view plot, remove #

def dim():
	'print dimensions of out inputs'
	print 'Xq [wafeform] shape = ', np.shape(Xq)
	print 'fqnames [featureNames] shape = ', fqnames.shape
	print 'metaVals [numMeta] shape = ', metaVals.shape
	print 'Fq [featureVals] shape = ', Fq.shape
	print 'keys in fqnames: ', fqnames


def plot_hist():
	'plot histogram'
	plt.hist(mq, bins='auto')
	plt.tick_params(labelsize=15)
	plt.xlabel('Earthquake Magnitude',fontsize=18)
	plt.ylabel('Number of Events',fontsize=18)
	plt.savefig("Histogram.png") #saving a figure
	plt.show() #if you want to view plot, remove #

def data_as_image():
	'saving data as images'
	data = {}
	import os
	cwd = os.getcwd()
	t = np.linspace(0,5,400) #generating x-axis (time) from 0 to 5 s
	for i in range(0,10000):
		if mq[i] > 4:
			j = 1
		else:
			j = 0
		data[i] = j

	pickle.dump(data, open("eq-mag.p", "wb"), 0)
	print pickle.load(open('eq-mag.p','rb'))

def aggregate_and_shuffle(Fq,Fn,mq,time=3,noise_data = 300000):
	'aggregates attributes and eq of noise and real quakes into the same matrix'
	'return a matrix with 24 attributes, and the last column is magnitude'
	Fq, Fn = attributes()
	fq = np.zeros([Fq.shape[0],Fq.shape[1]+1])
	fn = np.zeros([noise_data,Fn.shape[1]+1])
	fq[:,0:24] = Fq[:,:,3]
	fn[0:noise_data,0:24] = Fn[0:noise_data,:,3]
	fq[:,24]   = mq
	aggregate = np.concatenate((fq, fn))
	np.random.shuffle(aggregate)
	return aggregate

def shuffle_waveform(Xq,Xn,noise_data = 300000):
	'aggregates waveform of noise and earthquake and shuffles them'
	#Fq, Fn = attributes()
	#fq = np.zeros([Fq.shape[0],Fq.shape[1]+1])
	#fn = np.zeros([noise_data,Fn.shape[1]+1])
	#fq[:,0:24] = Fq[:,:,3]
	#fn[0:noise_data,0:24] = Fn[0:noise_data,:,3]
	#fq[:,24]   = mq
	aggregate = np.concatenate((Xq, Xn[0:noise_data,:,:]))
	np.random.shuffle(aggregate)
	print Xq.shape
	print Xn.shape
	print aggregate.shape
	return aggregate

shuffle_waveform(Xq,Xn)
