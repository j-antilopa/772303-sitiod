t=seq(-10,10,0.1)
y=cos(t)
plot(t,y,type="l", xlab="x", ylab="y",col="green",main='Cos')
diag(x = 1, 5, 5)
my.mat <- matrix(seq(1, 12), nrow = 4, ncol = 4, byrow = TRUE)
dim(my.mat) <- c(2,2,2,2)
my.mat
my.matsum <- my.mat + 6
my.matsum
my.matS1S2 <- my.mat + my.matsum
my.matS1S2
my.matPow <- my.mat^2
my.matPow
my.matMult <- my.mat %*% my.matPow
my.matMult
my.matT <- 1:16
dim(my.matT) <- c(4, 4)
t(my.matT)
A=c(3,-2,2,-1,1,-1,0,1,4)
dim(A)<-c(3,3)
A
B=c(5,0,15)
dim(B)<-c(3,1)
B
x<-solve(A,B)
x


