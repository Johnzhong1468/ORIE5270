from scipy.optimize import minimize
import random
import numpy as np

def rb(x):
    f_sum = 0
    for i in range(len(x)-1):
        f_sum += 100*(x[i+1]-x[i]**2)**2+(1-x[i])**2
    return f_sum
    
if __name__ == '__main__':
    random.seed(0)
    print("Using 'L-BFGS-B' and choose different starting points with values from -5 to 5: \n")
    for i in range(5):
        start = random.sample(list(np.linspace(-5,5,100)),3)
        result = minimize(rb,start,method = 'L-BFGS-B')
        print("Start point is: ",start)
        print("Minimized value: ",result.fun)
        print("Minimizing point: ",result.x,"\n")

    print("\n\nUsing 'BFGS' and choose different starting points with values from -5 to 5: \n")
    for i in range(5):
        start = random.sample(list(np.linspace(-5,5,100)),3)
        result = minimize(rb,start,method = 'BFGS')
        print("Start point is: ",start)
        print("Minimized value: ",result.fun)
        print("Minimizing point: ",result.x,"\n")