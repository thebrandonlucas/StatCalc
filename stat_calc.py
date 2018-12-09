import PySimpleGUI as sg
from stat_functions import *

main_form = sg.FlexForm('Statistics Calculator', default_element_size=(40, 1))

layout = [
	[sg.Text("Mean", size=(30, 1), font=("Times", 20)),  
	 sg.InputText(size=(30, 1), font=("Times", 20)), 
	], 
	[sg.Submit("Calculate Mean", size=(30, 1), font=("Times", 20))],
	[sg.Text("Least Squares Estimates", size=(30, 1), font=("Times", 20))],  
	[sg.Text("X", size=(30, 1), font=("Times", 20)), 
	 sg.InputText(size=(30, 1), font=("Times", 20)), 
	], 
	[sg.Text("Y", size=(30, 1), font=("Times", 20)), 
	 sg.InputText(size=(30, 1), font=("Times", 20)), 
	], 
	[sg.Submit("Calculate Least Squares Estimates", size=(30, 1), font=("Times", 20))], 
	[sg.Text("Least Squares Line", size=(30, 1), font=("Times", 20)), 
	 sg.InputText(size=(30, 1), font=("Times", 20)), 
	],  
	[sg.Submit("Calculate Least Squares Line", size=(30, 1), font=("Times", 20))]
]

main_form = main_form.Layout(layout)

while True: 
	button, values = main_form.Read()
	if button is None: 
		break
	if button == 'Calculate Mean': 
		xdata = floatlist(values[0])
		#xdata = list(map(float, values[0].split(",")))
		sg.Popup(mean(xdata))
		
	if button == 'Calculate Least Squares Estimates': 
		xdata = list(map(float, values[1].split(",")))
		ydata = list(map(float, values[2].split(",")))
		b = least_squares_estimates(xdata, ydata)
		sg.Popup("b0: " + str(b['beta_naught_0']) + "\n" + "b1: " + str(b['beta_naught_1']))
	if button == 'Calculate Least Squares Line': 
		break
