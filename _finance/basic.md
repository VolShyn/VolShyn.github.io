---
layout: post
title: "Necessary concepts for quantitative finance"
---

# Explanation

This basic concepts are necessary for further learning of financial modelling, e.g. Hull-White, Black-Karasinski, Nelson Siegel models, etc. 

All financial assets can be described in some way, either with words, or you can describe them with parameters (mathematically).

## Interest rate

Is a percent of borrowed money, that you have to pay. (e.g. If you save money in a bank account, they might pay you _interest_). Usually, interest rate is annualized, and can change over time based on some factors.  

There are nominal and real interest rates:

1. Nominal - with no adjustment for inflation
2. Real - measures loan plus interest, taking inflation to account:

$$ r = \frac{1 + i}{1 + p} - 1,$$

where $ p $ is the inflation rate, and for short periods of time the linear approximation would be $ r \approx i - p $.

<sub> _Inflation_ corresponds to a reduction in the purchasing power of money, i.e. a general increase in the prices of goods and services.<sub>

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

$$ \sigma_{T} = \sigma_d \sqrt{PT}, $$

<sub> P = 250, assuming there are P trading days. <sub>

Since real price changes exhibit non-Gaussian behavior, alternatives are used, like Lévy distribution or log-returns.

## Bonds 

It's easy to think that bonds are like IOU (I owe you), but for money and in bigger scale.

In my opinion, it is better to give a quick example, that will create a better understanding :


* You need money to buy a new oven to bake more goodies
* Instead of asking the bank, you decide to issue "bread bonds"
* People can buy these bonds for, say, $100 each.
* In return, you promise to pay them back:
   * $100 when the bond matures in 5 years (like getting your money back with interest).
   * And also, $5 every year as interest (like getting a thank-you slice of cake each year).

Bonds are different from stocks:

* Bonds don't give you ownership of the issuer, like stocks do. You're just a lender.
* Bonds are generally considered less risky than stocks, but the payoff is also usually lower.

**Clean price**: Base price of the bond, pure value based on what you'll get in the future (payments and payback)

**Black/Model price**: Estimated price of a bond derived using a math model (e.g. Black-Scholes model)

### Yield 

Is essentially the annualized return you get on your investment in a bond. It tells you how much money you can expect to make each year from the bond, factoring in both the interest payments and any change in the bond's price at maturity.

<sub> _Yield Rate_ is just another way to say "yield". So, "bond yield rate" and "yield to maturity" are essentially the same thing. <sub>