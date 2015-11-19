# Aufgabe 7

library(ggplot2)

png(filename="Gaussian-k-sigma.png")

# Parameters
mu = 3
sigma = 3

step_size = 0.05
k = 10

# Logic
x = seq(from=mu-k*sigma, to=mu+k*sigma, by=step_size)
dens = dnorm(x, mean=mu, sd=sigma)

d <- data.frame(x=x, y=dens)
plot(d, type="lines")

for (k in k:1) {
    print(paste("k=", k, ", P(...)=",
                pnorm(mu+k*sigma, mean=mu, sd=sigma) -
                pnorm(mu-k*sigma, mean=mu, sd=sigma)))

    k1start = mu - k*sigma
    k1end = mu + k*sigma
    cord.x <- c(k1start, seq(k1start, k1end, step_size), k1end)
    cord.y <- c(0,dnorm(seq(k1start, k1end, step_size), mean=mu, sd=sigma),0)
    polygon(cord.x, cord.y, col=rainbow(3)[k])
}

dev.off()