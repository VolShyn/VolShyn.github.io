import numpy as np
import matplotlib.pyplot as plt

def secant_method(f, x0, x1, tol=1e-10, max_iter=100):
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


if __name__ == "__main__":
    f_x = lambda x: x**3 - x**2 - x - 1
    x0, x1 = 1.0, 2.0  # Initial guesses
    root, points = secant_method(f_x, x0, x1)
    print(f"root: {root}")

    x_values = np.linspace(min(points) - 3, max(points) + 3, 400)
    y_values = f_x(x_values)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values)
    plt.scatter(points[:3], 
                [f_x(p) for p in points[:3]], color='red')  
    for i, point in enumerate(points[:3]):
        plt.annotate(f'x_{i+1}', (point, f_x(point)), 
                     textcoords="offset points", 
                     xytext=(0,10), ha='center')
    

    # draw line [x1,x2]:[y1,y2]
    plt.plot([1, 2], [-2, 1], 'k-', alpha=0.5) 
    plt.plot([points[2], points[2]], [-0.8, 0], 'k-', alpha = 0.3)
    plt.axis([-3,3,-3,3])
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    plt.savefig('Secant.png', transparent=True)
    plt.show()
