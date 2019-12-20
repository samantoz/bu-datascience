# Assignment: ASSIGNMENT 3.1 2014 American Community Survey

# Name: SAMANTA, ARINDAM

# Date: 22 DECEMBER 2019

# TASK 3.1
rm(list = ls())
# Load the libraries needed
library(ggplot2)
library(tidyr)
library(readr)

# Reading the file into a dataframe:acs
# The dataset contains 
acs <- read_csv("acs-14-1yr-s0201.csv")

#2. Structure of the dataframe
str(acs)

#2. No. of observations/rows
nrow(acs)

#2. No of variables/columns 
ncol(acs)

# Viewing a sample of the data from the data frame
head(acs)

# Counting the No of rows having the HS Degree between 85% and 95%
# This is just to ensure that the histogram count is showing properly
nrow(subset(acs, HSDegree > 85 & HSDegree < 95))

#3. Histogram with HSDegree variable
# Using gghist as the object
gghist <- ggplot(acs, aes( x = HSDegree)) +
  geom_histogram( binwidth = 3, alpha = 0.6) +
  labs(title = "Histogram using ggplot2",
       x = "HS Degree %", y = "Count")
# Plot the histogram
gghist
# This histogram we have asked for density plot as we want to plot the normal curve
ggdens <- ggplot(acs, aes( x = HSDegree)) +
  geom_histogram(aes(y = ..density.. ), binwidth = 1, color = "black", fill = "white") +
  labs(title = "Histogram using ggplot2",
       x = "HS Degree %", y = "Density")
# print the plot
ggdens

# Adding another layer to the chart - normal curve
# Adding another layer stat_function() to the histogram object ggdens

ggdens + stat_function(fun = dnorm, args = list(mean = mean(acs$HSDegree, na.rm = TRUE), 
                                                sd = sd(acs$HSDegree, na.rm = TRUE)), 
                       color = "red", size = 1 )

# Drawing a Q-Q plot
qplot(sample = acs$HSDegree, stat = "qq")


