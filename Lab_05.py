"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Lab #05
    Created on Wednesday Feb 28 19:30 2024  
    Last Updated Wednesday Feb 28 22:16

    Description: 
        The program uses list comprehension to plot 2 sets of y data, and 1 set of x data
        which is used to plot the sin and cos of the values (x data).
        
    
    Inputs: 
        PlotData(xData, yData, xAxisLab, yAxisLab, title)
        
            xData :
                List of Floats
                - values plugged into the calculation
                
            yData : 
                List of Floats 
                - results of scientific calculations for each value
                
            xAxisLab :
                String
                
            yAxisLab :
                String
                
            title :
                String

    Returns: 
        none
        

    Dependencies: time, mathhplotlib.pyplot, math

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""




#----imports




import time, math
import matplotlib.pyplot as plt




#----function definitions




def PlotData(xData, yData, xAxisLab, yAxisLab, title):
    
    """
    
    Description
    ----------
    The PlotData() func uses a handful of inputs to plot sin and cos values.
    
    Parameters
    ----------
    
        xData : 
            List of Floats
            These are the values 
            
        yData : 
            List of Floats
            These are the sin or cos of the values
            
        xAxisLab : 
            String
            Label for x axis
            
        yAxisLab :
            String
            Label for y axis
            
        title :
            String
            Chart title
        
    Returns
    -------
    None.

    """
    
    plt.title( title )
    plt.xlabel( xAxisLab )
    plt.ylabel( yAxisLab )
    plt.scatter( xData, yData  )
    plt.plot( xData, yData )
    filename = "placeholder"
    # we are using this func for 2 specific reasons, 
    # so the filename will be for the sin chart or the cos chart depending on y axis label
    if( yAxisLab == "Sin" ):
        filename = "Scott_Quashen_Y1.png"
    else:
        filename = "Scott_Quashen_Y2.png"
    plt.savefig(filename, dpi=600)
    plt.show()

# end PlotData




#----main code




# dev name
print( "Scott Quashen..." + time.asctime() )

# step count
N = 21

# divide right bound of range by step count to get step size
stepsSizee =  (( math.pi * 2 ) /  N  )

# each step
steps = [ ( i * stepsSizee) for i in range( N + 1 ) ]

# create a list of the sin values for each step value in our range
Y1 = [ math.sin( ( i - i ) + stepsSizee * i ) for i in range( 0, N + 1 ) ]

# plot sin 
PlotData( steps , Y1 , "Value", "Sin", "Plotting Sin Values" )

# and create the list of cos
Y2 = [ math.cos( ( i - i ) + stepsSizee * i ) for i in range( 0, N + 1 ) ]

# plot cos
PlotData( steps , Y2 , "Value", "Cos", "Plotting Cos Values" )





#----end 















