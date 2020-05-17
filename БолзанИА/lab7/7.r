year <- c(2010 ,   2011  ,  2012  ,  2013 ,   2014)
rate <- c(9.27 ,   8.40  ,  7.65  ,  6.73  ,  6.50)
plot(year,rate,main="������ �� ������ ������� ��� � ��������� ������",sub="��� ������ 7")            
cor(year,rate)
#y=kx+b
#
fit <- lm(rate ~ year)
fit
#������ ������
abline(fit)

fit$coefficients[1]
fit$coefficients[[1]]
fit$coefficients[2]

#����������� ���������� �� ������ �� ������ �� �����
residuals(fit)

#��� ���������� ������� �� �������
plot(year,fit$residuals)

#��������� ������ ���������� ������ � 2010 ����
fit$coefficients[[2]]*2010+fit$coefficients[[1]] 
res <- rate - (fit$coefficients[[2]]*year+fit$coefficients[[1]]) 
res


#�� �� ����� ��� � plot(year,fit$residuals)
plot(year,res)
plot(year,rate,main="������ �� ������ ������� ��� � ��������� ������",sub="��� ������ 7")    

summary(fit)