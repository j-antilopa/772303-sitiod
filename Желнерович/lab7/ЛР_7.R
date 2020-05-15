#-исходные данные
year <- c(2000 ,   2001  ,  2002  ,  2003 ,   2004)
rate <- c(9.34 ,   8.50  ,  7.62  ,  6.93  ,  6.60)

#-точечный график
plot(year,rate,main="Commercial Banks Interest Rate for 4 Year Car Loan",sub="http://www.federalreserve.gov/releases/g19/20050805/")            

#-коррел€ци€ между годом и средней процентной ставки:
cor(year,rate)          

#-команда дл€ выполнени€ регрессии наименьших квадратов €вл€етс€ команда lm
fit <- lm(rate ~ year)
fit
attributes(fit)
fit$coefficients[1]
fit$coefficients[[1]]
fit$coefficients[2]
fit$coefficients[[2]]

#-оценка процентной ставки в 2015
fit$coefficients[[2]]*2015+fit$coefficients[[1]] 

#-формула дл€ вычислени€ остатков
res <- rate - (fit$coefficients[[2]]*year+fit$coefficients[[1]]) 
res
plot(year,res)

#-график линии регрессии на том же участке, как точечной график
plot(year,rate,
     main="Commercial Banks Interest Rate for 4 Year Car Loan",
     sub="http://www.federalreserve.gov/releases/g19/20050805/")
abline(fit)

#-результаты F-теста и других тестов вызвав функцию summary():
summary(fit)

