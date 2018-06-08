import sys
import glob
import os
import keras
import numpy as np
import pandas as pd
from scipy import sparse
from keras.models import Sequential
from keras.layers import Dense
#pretty printing dataframe
from tabulate import tabulate

#this is where the files will be read into arrays then the arrays will be put into an array
for input_file in glob.glob("*.npy"):
	data = np.load(input_file)
	column_names = ['Cumulative','Frame ID','Minerals','Vespene','Food Cap','Food Used','Food Army','Food Worker','Idle Worker Count','Army Count','Warp Gate Count','Probe','Zealot','Stalker','Sentry','Adept','High Templar','Dark Templar','Immortal','Colossus','Disruptor','Archon','Observer','Warp Prism','Phoenix','Void Ray','Oracle','Carrier','Tempest','Mothership','Enemy Probe','Enemy Zealot','Enemy Stalker','Enemy Sentry','Enemy Adept','Enemy High Templar','Enemy Dark Templar','Enemy Immortal','Enemy Colossus','Enemy Disruptor','Enemy Archon','Enemy Observer','Enemy Warp Prism','Enemy Phoenix','Enemy Void Ray','Enemy Oracle','Enemy Carrier','Enemy Tempest','Enemy Mothership','Most Beneficial Unit']

	#np.concatenate([column_names,data])
	#process the frames and append onto frame
	df = pd.DataFrame(data, columns = column_names)
	
	msk = np.random.rand(len(df)) < 0.75
	train = df[msk]
	test = df[~msk]
	#print(type(train))
	#print(type(test))
	#print(df.shape)
	#df.to_csv(r'testing.txt', header=True, index=None, sep=' ', mode='a')

	#neural network implementation
	model = Sequential()

	model.add(Dense(49, activation='relu', input_dim=49))
	model.add(Dense(49, activation='relu'))
	model.add(Dense(49, activation='relu'))

	model.add(Dense(1))

	model.compile(loss='mean_squared_error', optimizer='adam', metrics= ['acc'])

	train_arr_x = train.drop(columns=['Most Beneficial Unit']).values
	train_arr_y = train['Most Beneficial Unit'].values

	test_arr_x = test.drop(columns=['Most Beneficial Unit']).values
	test_arr_y = test['Most Beneficial Unit'].values
 
	model.fit(train_arr_x, train_arr_y, batch_size=50, epochs=1000)

	print(model.evaluate(test_arr_x, test_arr_y))

	print(model.predict(test_arr_x))

