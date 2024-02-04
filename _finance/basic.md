---
layout: post
title: "Necessary concepts for quantitative financial modeling"
---

1. TOC
{:toc}

---

Necessary concepts for quantitative financial modeling

# Introduction

These basic concepts are necessary for further learning of financial modeling, e.g. Hull-White, Black-Karasinski, Nelson Siegel models, etc. 

All financial assets can be described in some way, either with words, or you can describe them with parameters (mathematically).

## Interest rate

**Interest** is extra as compensation for lending money. 
While **interest rate** is a percentage of that rate. Usually, interest rate is annualized, and can change over time based on some factors.  

There are nominal and real interest rates:

1. Nominal - with no adjustment for inflation
2. Real - measures loan plus interest, taking inflation to account and measured as:

$$ r = \frac{1 + i}{1 + p} - 1,$$

where $i$ - interest rate, $ p $ - inflation rate.

For short periods of time the linear approximation would be $ r \approx i - p $.

<sub> _Inflation_ corresponds to a reduction in the purchasing power of money, i.e. a general increase in the prices of goods and services.<sub>

## Maturity 

Or **maturity date**, is the date on which a loan or investment becomes due and the principal amount must be repaid. Longer maturities typically offer higher interest rates but also carry higher risk.

## Term-structure

Describes how much you earn for lending money for different durations.

So it is an relationship between interest rates and their corresponding maturities. 

**Short-term** - usually, term that is less than one year. 

**Long-term** - flexible, typically beyond 5 years.

## Returns 

Is the overall gain or loss (negative return) from an investment, expressed as a percentage of the initial investment. 

<sub>Rarely measured in absolute terms (e.g. dollars). <sub>

Typically annualized to compare returns over time periods of different lengths.

$$ R = \frac{V_f - V_i}{V_i},$$

where $V_f$ - final value with dividents and interest, $V_i$ - initial value.

Without reinvestments, return $R$ in some period of time $t$ is called _rate of return_ and denoted as $r$:

$$ r = \frac{R}{t}.$$ 

Basically, it is right to say, that _returns_ are a kind of metric in the financial world.

## Volatility

Intensity and frequency of price fluctuations of an asset. So, it's simply a measure of how much prices are measured around their average, measured by the standard deviation $\sigma$ or log-returns.

<sub> Log-returns cancel out exponential growth. <sub>


For instruments described by Gaussian random walks or Wiener processes, the price distribution widens with time. Intuitively, the probability of straying further from the initial price increases as time progresses. However, unlike a linear relationship, volatility grows with the $\sqrt{t}$. This is due to the expected cancellation of some fluctuations, preventing price deviations after twice the time from simply doubling. 

So, the generalized volatility $\sigma_T$ for time horizon $T$ in years is expressed as:

$$ \sigma_{T} = \sigma_a \sqrt{T},$$

where $\sigma_a$ is annual volatility.

$$\sigma_a = \sigma_d \sqrt{P},$$

where $\sigma_d$ is daily volatility.

As a result:

$$ \sigma_{T} = \sigma_d \sqrt{PT}, $$

<sub> P = 250, assuming there are P trading days. <sub>

Since real price changes exhibit non-Gaussian behavior, alternatives are used, like Lévy distribution or log returns.

## Bonds 

It's easy to think that bonds are like IOU (I owe you), but for money and on a bigger scale.

In my opinion, it is better to give a quick example, that will create a better understanding :


* You need money to buy a new oven to bake more goodies
* Instead of asking the bank, you decide to issue "bread bonds"
* People can buy these bonds for, say, $100 each.
* In return, you promise to pay them back:
   * $100 when the bond matures in 5 years (like getting your money back with interest).
   * And also, $5 every year as interest (like getting a thank-you slice of cake each year).

Bonds vs stocks:
* Bonds don't give you ownership of the issuer, like stocks do. You're just a lender.
* Bonds are generally considered less risky than stocks, but the payoff is also usually lower.

**Zero-coupon bond** (discount bond) - type of bonds without periodic interest payments (so-called _coupons_). 

Tbh, there are many types of bonds, however, we are interested only in the parameters of bonds.

**Clean price**: Base price of the bond, pure value based on what you'll get in the future (payments and payback)

**Black/Model price**: The estimated price of a bond derived using a math model (e.g. Black-Scholes model)

### Yield 

Overall, yield is the return the investor gets from the investment.

In the context of bonds, yield is expressed as:

$$ \gamma = \frac{i}{b_c},  $$

where $ i $ - interest rate, $ b_c$ - current bond price.

<sub> _Yield Rate_ is just another way to say "yield". So, "bond yield rate" and "yield to maturity" are essentially the same thing. <sub>

<sub> _Yield curve_ shows interest rates to maturity. It is also called _redemption yield_ <sub>


## Swaps

A **swap** is a contractual agreement between two parties to exchange cash flows based on different underlying assets.

A **swaption** is an option to enter into a swap contract at a future date. Unlike a swap itself, it grants the holder the right, but not the obligation, to execute the swap under predetermined terms.

|  | Swap | Swaption |
|---|---|---|
| **Commitment** | Two-way commitment to exchange cash flows | One-way right to enter a swap |
| **Initial Cost** | No upfront cost | Buyer pays a premium |
| **Flexibility** | Less flexible (fixed terms) | More flexible (option to choose) |
| **Risk/Reward** | Higher risk and reward potential | Lower risk and reward potential |

**Bermuda swaption** - is like having multiple swaptions bundled together, each with its own pre-defined exercise date throughout the contract's lifespan. This allows large-scale investors to have an option that allows them to change from fixed to floating interest rates on a set schedule.


## Tenor

The length of time ramaining before a financial contract expires
