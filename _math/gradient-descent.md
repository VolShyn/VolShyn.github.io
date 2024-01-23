---
layout: post
title: "Gradient Descent"
---

<sub> _Method_ is a general term for a way of doing something, not necessarily tied to strict rules or sequences.  
_Algorithm_ well-defined sequence of steps or instructions for completing a task or solving some problem. <sub>

1. TOC
{:toc}

---


# Gradient Descent

Gradient descent is an iterative algorithm, that finds the extremum of an objective function (e.g. Cost Function).

**Main goal**: finding the best parameters of a model, which will give us the highest accuracy on the training dataset and good generalization.

_Steps_: 

    1. Initializing parameters (randomly, normally/uniformly distributed, etc) 
    2. Compute the gradient ∇ of the objective function w.r.t each parameter
    3. Update parameters by taking step α in the opposite direction of the ∇

## Objective function ($J$):

$$ J(\theta_0, \theta_1) = \frac{1}{2n} \sum_{i=1}^{n}(h_\theta(x_i) - y_i)^2 ,$$

where $\theta_0$, $\theta_1$ are parameters, $ h_\theta(x_i) $ is a hypothesis function (predicted values), and $y_i$ - actual (target) value.

**Input**: $n$ parameters (e.g. $\theta_n$), i.e. for NN's we must consider all weights and biases 

**Output**: 1 number (the cost)

Vector denotation commonly used in NN: 

$$ J(\mathbb{W},\mathbb{B}) = \frac{1}{n} (\hat{Y} - Y)^2.$$

Thus, $\nabla J$ will show the direction of steepest ascent $\vec{d}$, and coefficients in that vector tell which parameter change matters more.

Quick example:


$$ \vec{d} = \begin{bmatrix} \theta_0 \\ \theta_1 \end{bmatrix} = \begin{bmatrix} -95 \\ -1431 \end{bmatrix}$$  


![grad](https://github.com/VolShyn/VolShyn.github.io/assets/78854637/5230a0fc-cb61-45b5-b70b-caa77596c10f)


So, we can see, that $\theta_1$ matters more if we want as fast as possible to get to the minimum of $J$.   

## GD algorithm:

$$ \theta_{n+1} = \theta_n - \alpha \nabla J,  $$

where $\theta_n$ is current value of the parameters, $- \alpha \nabla J$ is a step $\alpha$ (hyperparameter) in the opposite way of $\nabla J$ to get new values $\theta_{n+1}$.

If we want to go deeper in our understanding, we need to know how $\nabla J$ is calculated. The **gradient** of a function at a point $ x $ is the vector of its partial derivatives: 

$$ g = \frac{\partial J}{\partial x} = \nabla J = \begin{bmatrix} \frac{\partial J}{\partial x_1} \\ \vdots \\ \frac{\partial J}{\partial x_n}\end{bmatrix}.$$ 

In context of linear algebra, $\nabla$ maps objective function $ J: \mathbb{R}^n \rightarrow \mathbb{R} $ onto $ \nabla J: \mathbb{R}^n \rightarrow \mathbb{R}^n $.

Thus, $ \nabla J $ is a vector-valued function (**vector field**). In comparison, $J'$ is a **scalar field** (some sort of heatmap if imagine). 

<sub> Vector-valued function takes a vector as an input and gives vector as an output.<sub>

Before we dive into the process of calculating $\nabla$, it is important to point out, that gradient is computed differently among different models.

Let's calculate $\nabla J$ for linear regression model as: 

$$ \nabla J := \frac{\partial}{\partial\theta}J = \frac{\partial}{\partial\theta}\frac{1}{2n} \sum_{i=1}^{n}(h_\theta(x_i) - y_i)^2,  $$

factor of $\frac{1}{2}$ included to simplify the derivative, as it cancels out the exponent.

Now we apply chain rule:

$$\frac{\partial}{\partial\theta}\frac{1}{2n}(h_\theta(x_i) - y_i)^2 = (h_\theta(x_i) - y_i)\frac{\partial}{\partial\theta}(h_\theta(x_i) - y_i), $$

$$h_\theta(x_i) = \theta^T x_i, $$

$$\frac{\partial}{\partial\theta}(\theta^Tx_i - y_i) = x_i. $$


The end result will be:

$$ \alpha \frac{1}{n}\sum_{i=1}^{n}(h_\theta(x_i) - y_i)x_{i}.$$



# Reading

1. https://en.wikipedia.org/wiki/Gradient
2. Kevin P.Murphy (2022) Probabilistic Machine Learning: An Introduction 
