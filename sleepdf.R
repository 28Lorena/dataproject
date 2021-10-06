data()

data("sleep")

str(sleep)
head(sleep)
tail(sleep)
nrow(sleep)
ncol(sleep)

attach(sleep)

v1 <-c(0.7,-1.6,-0.2,-1.2,-0.1,3.4,3.7,0.8,
       0.0,2.0,1.9,0.8,1.1,0.1,-0.1,4.4,5.5,1.6,4.6,3.4)
v2 <- c(1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2)
v3 <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

mylist <- list(v1,v2,v3)

df <- data.frame (ext=v1,ID=v3)

library(ggplot2)

df

ggplot(df,aes(ext,ID)) + geom_point()

ggplot(df,aes(ext,ID)) + geom_line()
