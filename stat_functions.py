import re

#Split a string based on input into a list
def splist(string):
#	new_str = ','.join(string.split())
	outlist = re.split(' |,|\n|, |;|; ', string)
	delimeters = [' ',',','\n',';']
	if not any([x in string for x in delimeters]):
		outlist = 'Error: Please use a space, comma, or colon as a delimeter'
	return outlist

def floatlist(data):
	inlist = [float(a) for a in splist(data)]
	return inlist

def least_squares_estimates(xdata, ydata): 
	beta_naught_1 = sxy(xdata, ydata) / sxx(xdata)
	beta_naught_0 = mean(ydata) - beta_naught_1 * mean(xdata)
	return {"beta_naught_0":beta_naught_0, "beta_naught_1":beta_naught_1}
	
def least_squares_line(beta_naught_0, beta_naught_1): 
	y = 0
	return y; 

def sxy(xdata, ydata):
	sxy = 0
	mean_x = mean(xdata)
	mean_y = mean(ydata)
	for i in range(0, len(xdata)): 
		sxy += (xdata[i] - mean_x) * (ydata[i] - mean_y)
	return sxy

def sxx(xdata): 
	sxx = 0
	mean_x = mean(xdata)
	for num in xdata: 
		sxx += (num - mean_x)**2
	return	sxx

def mean(data): 
	sum = 0
	n = len(data)
	for num in data: 
		sum += num
	return sum / n 

