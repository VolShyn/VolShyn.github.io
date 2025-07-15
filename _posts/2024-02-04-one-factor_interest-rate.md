---
layout: post
title: "Short-rate models"
category: finance
date: 2024-02-04
---


1. TOC
{:toc}

---

# Short-rate models
Refers to the instantaneous interest rate at a specific point in time. It's essentially the rate you'd pay to borrow money for an infinitesimally small period of time.

They specify the behavior of short-term interest rate. They are also can be classified into **equilibrium** (i.e. start with some assumptions about economic variables) and no-arbitrage models.

## One-Factor models

Imply that the future evolution of all interest rates is determined by a _single driving force_, i.e. there is only one feature that is truly significant. 

### Derivatives

We don't actually take derivatives of the interest rate itself in the classical sense of calculus. In this context, interest rate derivatives refer to financial instruments whose value is directly linked to the movement of one or more underlying interest rates (Bonds, Options, e.t.c).

### Hedging

Businesses and investors often face interest rate risk, which means the value of their assets or liabilities can be negatively impacted by unexpected changes in interest rates.
In this sense, "deriving" benefit from interest rate movements comes from strategically positioning oneself in the market based on expectations of future changes.

### Drift

Refers to the average tendency of the short-term interest rate over time. So, it represents the force pulling the rate towards it's long-term level. Drift is also known as **mean-reversion** tendency.

When interest rate ($r$) is high, mean reversion tends to cause it to have a negative _drift_;
When $r$ is low, mean reversion tends to cause positive drift.

It can be estimated by calibrating the models to historical data. 

### SDE

Stochastic differential equation

---

# Vasicek 

Model, that assumes that the interest rate is normally distributed. Predicts where interest rates will end up at the end of a given period of time.

The risk-neutral process for $r$ is:

$$ dr = a(b - r)dt + \sigma dz, $$

where $a$ - speed of the mean reversion, $b$ - mean reversion level, $\sigma$ - volatility, they are constant, $dz$ is a **Wiener process** modeling risk factor. 

 Short rate here pulled is pulled to a lebel $b$ ar rate $a$.


# Hull-White

It is an extension of the _Vasicek_ model.  

# Black-Karasinski

Assumes that the short rate follows a log-normal distribution rather than a normal. This is important because firstly, finances and their derivatives are usually not distributed normally, secondly log-normal distribution ensures that the interest rates are always positive.

SDE:

$$ dr_t = [\theta - a \cdot log(r_t)] dt + \sigma  dW_t, $$

where 

* $d$ - infinitesmall change,
* $r_t$ - short-rate at time $t$,
* $a(t)$ - speed of reversion (how quickly the rate moves towards it's long-run mean), e.g. if $a(t)$ = 0.1, then rate would adjust 10% towards the long-run mean within a year,
* $\theta$ - is time-dependent function that determines mean reversion level,
* $\sigma$ - volatility,
* $dW_t$ - standard brownian motion (small random increment).



# Reading

1. https://medium.com/@polanitzer/va%C5%A1%C3%AD%C4%8Dek-1977-model-in-python-predict-the-bank-of-israel-interest-rate-one-year-ahead-using-62b8890f77ab

2. https://www.econstor.eu/bitstream/10419/50684/1/584765029.pdf