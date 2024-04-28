import numpy as np
import matplotlib.pyplot as plt
import time
from typing import Tuple 

def visualize_opt_steps(*, 
                points: list, 
                n: int = 3,
                f,
                show_lines = False,
                save = False) -> None:
    """
    Args:
        points: list of points
        n: number of points to show
        f: function to visualize lines
        show_lines: show lines
        save: Save image without background 

    func to visualize optimization
    """
    x_values = np.linspace(min(points) - 3, max(points) + 3, 100)
    y_values = f(x_values)

    plt.figure(figsize=(10, 6))
    try:
        points[:n]
        plt.plot(x_values, y_values)
        plt.scatter(points[:n], 
                    [f(p) for p in points[:n]], color='red')  
        for i, point in enumerate(points[:n]):
            plt.annotate(f'x_{i+1}', (point, f(point)), 
                        textcoords="offset points", 
                        xytext=(0,10), ha='center')
        
        if show_lines:
            # draw line as [x1,x2]:[y1,y2]
            plt.plot([points[0], points[1]],
                    [f(points[0]), f(points[1])], 'k-', alpha=0.5) 
            plt.plot([points[2], points[2]],
                    [f(points[2]), 0], 'k-', alpha = 0.3)

        plt.axis([-3,3,-3,3])

        # here we draw cartesian coordinate system
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)

        local_time = time.ctime(time.time())[11:].replace(' ', '_')
        if save:
            plt.savefig(f'plot_{local_time}', transparent=True)

        plt.show()

    except IndexError:
        print('n is out of index')


def secant_method(f, 
                  x0: float, 
                  x1: float, 
                  tol=1e-5, 
                  max_iter=100) -> Tuple[float, list]:
    """
    secant method realization
    storing points for further plotting
    """
    points = [x0, x1]  # store the points used in the iterations
    
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        denominator = f_x1 - f_x0
        if abs(denominator) < tol:
            raise ValueError("Denominator too small; \
                             division by zero possible")
        
        x2 = x1 - f_x1 * (x1 - x0) / denominator
        
        points.append(x2)  # new point
        
        if abs(x2 - x1) < tol:
            return x2, points  # root and all points used
        
        x0, x1 = x1, x2

    raise Exception("Secant method did not converge")    
    

def bisection_method(f, 
                     a: float, 
                     b: float,
                     tol=1e-5, 
                     max_iter=100) -> Tuple[float, list]:
    if f(a) * f(b) >= 0:
        raise ValueError("Function has the same sign \
                          at the endpoints a and b")

    points = [a, b]  
    for _ in range(max_iter):
        c = (a + b) / 2
        points.append(c)  # storing the midpoint
        
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, points  
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise Exception("Bisection method did not converge")



if __name__ == "__main__":

    f_x = lambda x: x**3 - x**2 - x - 1 

    ############## Secant method ##############
    x0, x1 = 1.0, 2.0  # initial guesses
    root, points = secant_method(f_x, x0, x1)
    print(f"root: {root}")
    print(points)
    visualize_opt_steps(points=points, f=f_x, show_lines=True)

    ############## Bisection ##############
    a, b = 1.0, 2.0  
    root, points = bisection_method(f_x, a, b)
    visualize_opt_steps(points=points, show_lines = True, 
                        n = 3, f=f_x)

    ############## Dekkers ##############

    



    ############## Brent-dekkers ##############
