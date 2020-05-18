year <- c(2000 ,   2001  ,  2002  ,  2003 ,   2004)
rate <- c(9.34 ,   8.50  ,  7.62  ,  6.93  ,  6.60)
plot(year, rate,
  main="Commercial Banks Interest Rate for 4 Year Car Loan", 
  sub="http://www.federalreserve.gov/releases/g19/20050805/")

print('Find the correlation between the year and the average interest rate')
cor_year_interest_rate <- cor(year,rate)
print(cor_year_interest_rate)

print('Least squares regression:')
fit <- lm(rate ~ year)
print(fit)

print('Least squares regression attributes:')
attributes(fit)

plot(year, rate, 
     main="Commercial Banks Interest Rate for 4 Year Car Loan", 
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
abline(fit)

print('Results of various model fitting functions:')
summary(fit)