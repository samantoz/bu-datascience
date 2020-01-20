# Checking normality visually

setwd("~/GitHub/BU-DSC/dataset/R/plots")


install.packages("car")
install.packages("ggplot2")
install.packages("psych")
library(pastecs)
library(psych)
library(Rcmdr)
library(ggplot2)

# Load the data
dlf <- read.delim("DownloadFestival.dat", header = TRUE)
# Plot the day1 variable from the dlf dataframe
# plotting a density plot instaed of a frequency plot as we want to plot the normal curve.

hist.day1 <- ggplot(dlf, aes(day1)) +  
  opts(legend.position = "none") + 
  geom_histogram (aes(y = ..density..), color = "black", fill = "white") + 
  labs(x = "Hygiene score for Day 1", y = "Density")
 

hist.day1