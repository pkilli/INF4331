import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys,os,time,glob
"""
program reads from various csv files and makes plot for specified values.

"""
#pd.set_option('display.mpl_style', 'default')
plt.rcParams.get('axes.color_cycle') 
plt.rcParams['figure.figsize'] = (15, 5)

def plot_CO2(start=None, end=None):
	"""
	Reads from the file co2.csv with help from pandas.
	finds carbon emission in the time period specified the parameters.
	@param start First Year specified
	@param end  Last year.
	@return png file for vizualizing
	"""
	co2_stats = pd.read_csv('co2.csv')
	years = []
	carbon = []
	for i in zip(co2_stats['Year'], co2_stats['Carbon']):
		if (i[0] >= start) and (i[0] <= end):
			years.append(i[0])
			carbon.append(i[1])	
	return plot(years,carbon,'carbon emission','carbon')
	
def plot_temperature(start=None, end=None, month=None):
	"""
	Reads from the file temperature.csv with help from pandas.
	finds temperature in the time period specified the parameters.
	@param start First Year specified
	@param end  Last year.
	@param month Month to vizualize the temperature
	@return png file for vizualizing
	"""
	temp_stats = pd.read_csv('temperature.csv')
	years = []
	temp = []
	for i in zip(temp_stats['Year'],temp_stats[month]):
		if (i[0] >= start) and (i[0] <= end):
			years.append(i[0])
			temp.append(i[1])
	description = ('temperature in '  + month)
	return plot(years,temp, description,name='temperature')


def plot_CO2_per_country(year=None, lower=None,upper=None):
	"""
	Reads from the file CO2_by_country.csv with help from pandas.
	finds temperature in the time period specified the parameters.
	@param Year Year specified
	@param lower  Lower threshold of carbon emission emitted per capita
	@param upper Upper threshold of carbon emission emitted per capita
	@return png file for vizualizing
	"""

	co2_per_country_stats = pd.read_csv('CO2_by_country.csv')
	CO2 = np.zeros((co2_per_country_stats.shape[0],co2_per_country_stats.shape[1]-8))
	tmp_col_value = np.zeros((co2_per_country_stats.shape[0],0))
	years = np.zeros(co2_per_country_stats.shape[1]-8)
	country = np.zeros(co2_per_country_stats.shape[0])
	
	i = 0
	for index, value in co2_per_country_stats.iteritems():
		if i == 1:
			country = value
		elif i > 3 and i < co2_per_country_stats.shape[1]-5:
			years[i-4] =int(index) 
			col_value=value
			col_value = [np.nan if x=='' else float(x) for x in col_value]
			CO2[:,i-4] = col_value
		i+=1
	
	year_index = np.where(years==year)[0][0]
	co2 = CO2[:,year_index]
	co2 = np.asarray([ 0.01 if np.isnan(x) else x for x in co2])
	country_index = np.where(np.logical_and(co2 > lower, co2 < upper))[0]
	country_ = []
	for i in country_index:
		country_.append(country[i])
	N 				= len(country_)

	
	description = ('CO2 emissions per capita')
	return plot(co2,country_index,description,'co2_per_cap',country_,N,True)
	
def plot(val1, val2,description=None,name=None,val3=None,val4=None,BAR=False):	 
	"""
	Making a plot with matplotlib with values from methods in program
	@param val1 Value to use in plot
	@param val2  Value to use in plot
	@param description string for title to the plot
	@param name Filename
	@param val3 value to help plot bar
	@param val4 Value to plot bar
	@param bar True if it is supposed to be a bar plot, False otherwise
	@return png file
	"""

	fig = plt.figure()

	if BAR:
		bw = 0.1
		plt.clf()
		ax = fig.add_axes([.1, .4, 0.8, 0.5])
		ax.bar(np.arange(val4)*bw, val1[val2], 0.8*bw, align='center')
		ax.axis([0-bw/2,val4*bw-bw/2,0,1.1*max(val1[val2])])
		plt.xticks(np.arange(0,val4*bw,bw), val3, rotation='vertical')
		plt.ylabel(description)

	else:
		plt.plot(val1,val2)
		plt.title('%s from %g to %g' % (description,val1[0],val1[-1]))
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		# Remove old plot files
		for filename in glob.glob(os.path.join('static', name + '.png')):
			os.remove(filename)
	plotfile = os.path.join('static', name + '.png')
	plt.savefig(plotfile)
	return plotfile

if __name__=="__main__":
	print ('Module file not meant for execution.')






