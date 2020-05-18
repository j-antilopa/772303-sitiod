year <- c(2000, 2001, 2002, 2003, 2004)
rate <- c(13.90, 13.22, 12.54, 11.95, 11.89)
# 24-mo. persona
plot(year, rate, main = "Commercial Banks Interest Rate for 4 Year Car Loan", sub = "http://www.federalreserve.gov/releases/g19/20050805/")
cor(year, rate)
fit <- lm(rate ~ year)
fit
res <- residuals(fit)
res
abline(fit)
summary(fit)