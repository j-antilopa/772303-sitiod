year <- c(2010 ,   2011  ,  2012  ,  2013 ,   2014)
rate <- c(9.27 ,   8.40  ,  7.65  ,  6.73  ,  6.50)
plot(year,rate,main="ѕример на основе анализа лет и кредитных ставок",sub="Ћаб работа 7")            
cor(year,rate)
#y=kx+b
#
fit <- lm(rate ~ year)
fit
#строим пр€мую
abline(fit)

fit$coefficients[1]
fit$coefficients[[1]]
fit$coefficients[2]

#ћинимальное рассто€ние от пр€мой до каждой из точек
residuals(fit)

#как измен€ютс€ остатки по времени
plot(year,fit$residuals)

#получение оценки процентной ставки в 2010 году
fit$coefficients[[2]]*2010+fit$coefficients[[1]] 
res <- rate - (fit$coefficients[[2]]*year+fit$coefficients[[1]]) 
res


#то же самое что и plot(year,fit$residuals)
plot(year,res)
plot(year,rate,main="ѕример на основе анализа лет и кредитных ставок",sub="Ћаб работа 7")    

summary(fit)