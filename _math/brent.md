---
layout: post
title: "Optimization (Brent-Dekker, Brent's method)"
---

<sub> _Optimization's_ core goal is to find the "best" solution w.r.t some criteria.  <sub>

1. TOC
{:toc}

---
# Optimization 

Optimization problems often directly translated into minization problem.
It is because many problems are naturally framed as minimization
(e.g. cost reduction, error minimization, e.t.c.).

Even if a problem is initially framed as maximizing something, it can easily be 
transformed into a minimization problem via inverse:

$$ max(f(x)) = min(-f(x));$$

**Caveat**: not every opt. problem is a min. problem; for example
multicriteria optimization and finding any feasible solutions.

# Convergence rate

Used interchangeably with _order of convergence_ within _numerical analysis_. This term describes how quickly a sequence of approximations approaches a true solution. A higher rate of convergence means that the error between the estimated $x^*$ and true $x$ decreases more rapidly.

$$ \lim_{k\to\infty} \frac{x_{k+1} - x^*}{(x_k - x^*)^p} = C,$$

where $ p $ is the convergence rate.

Examples of convergence:

* Linear: error decreases at a const. factor on each iter.
* Quadratic: error is roughly squared with each iter.
* Superlinear: faster then linear (not necessarily with fixed order e.g. 1.5, 1.8)


# Brent's minimization

Not to be confused with the Brent-Dekkers method, which is also called _Brent method_.

First of all, it is an algorithm for minimization without derivatives. Also, it is by far the best in comparison with all other search techniques (Ternary, Dichotomous, Fibonacci, e.t.c). 

Brent's method uses **Golden-section search** and **Succesive Parabolic Interpolation** (SPI), because the first one has guarantee to find minimum (_converge_), while SPI will not guarantee the convergence, however, if it does converge, it will do it quickly. Convergence in a reasonable number of steps is guaranteed for any function.


| | Zeros| Extrema|
| ----------- | ----------- |-----------  |
| Linear convergence      | Bisection       | Golden section search | 
| Superlinear convergence | Successive linear interpolation         | SPI| 

Usually, Brent's method starts with GSS (2 iterations) and then uses SPI only. It is a commonly met case when Brent's method finds an answer on the 1st iteration, but it doesn't know that because of the significant interval.

<h3 style="text-align: center;"> p = 1.325   (worst case p = 1) </h3>

In Python scipy

# Brent-
