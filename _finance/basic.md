---
layout: post
title: "Necessary concepts for quantitative finance"
---

# Explanation

This basic concepts are necessary for further learning of financial modelling, e.g. Hull-White model, Black-Karasinski, Nelson Siegel, etc. 

All financial assets can be described in some way, either with words, or you can describe them with parameters (mathematically).

## Interest rate

Is a percent of borrowed money, that you have to pay. (e.g. If you save money in a bank account, they might pay you _interest_). Usually, interest rate is annualized, and can change over time based on some factors.  

There are nominal and real interest rates:

1. Nominal - with no adjustment for inflation
2. Real - measures loan plus interest, taking inflation to account:

$$ r = \frac{1 + i}{1 + p} - 1,$$

where $ p $ is the inflation rate, and for short periods of time the linear approximation would be $ r \approx i - p $.

## Maturity 

Or **maturity date**, is the date on which a loan or investment becomes due and the principal amount must be repaid. Longer maturities typically offer higher interest rates but also carry higher risk.

## Returns 

Is the overall gain or loss (negative return) from an investment, expressed as a percentage of the initial investment. 

<sub>Rarely measured in absolute terms (e.g. dollars). <sub>

Typically annualized to compare returns over time periods of different lengths.

$$ R = \frac{V_f - V_i}{V_i},$$

where $V_f$ - final value with dividents and interest, $V_i$ - initial value.

Without reinvestments, return $R$ in some period of time $t$ is called _rate of return_ and denoted as $r$:

$$ r = \frac{R}{t}.$$ 

## Volatility

Intensity and frequency of price fluctuations of asset. So, it's simply a measure of how much prices are measured around their average, measured by the standard deviation $\sigma$ or log-returns.

<sub> Log-returns cancels out exponential growth. <sub>


For instruments described by Gaussian random walks or Wiener processes, the price distribution widens with time. Intuitively, the probability of straying further from the initial price increases as time progresses. However, unlike a linear relationship, volatility grows with the $\sqrt{t}$. This is due to the expected cancellation of some fluctuations, preventing price deviations after twice the time from simply doubling. 

So, the generalized volatility $\sigma_T$ for time horizon $T$ in years is expressed as:

$$ \sigma_{T} = \sigma_a \sqrt{T},$$

where $\sigma_a$ is annual volatility.

$$\sigma_a = \sigma_d \sqrt{P},$$

where $\sigma_d$ is daily volatility.

As a result:

$$ \sigma_{T} = \sigma_d \sqrt{PT} $$

<sub> P = 250, assuming there are P trading days. <sub>

Since real price changes exhibit non-Gaussian behavior, alternatives are used, like Lévy distribution or log-returns.


