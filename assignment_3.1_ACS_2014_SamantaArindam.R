<<<<<<< HEAD
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
#1. The dataset contains American Community Survey data. It shows 1 year of data 
# for the counties and states the High School and Bachelor's Degree as percent 
# of the Total population
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


=======
# Assignment: ASSIGNMENT 3.1 2014 American Community Survey

# Name: SAMANTA, ARINDAM

# Date: 22 DECEMBER 2019

# TASK 3.1
rm(list = ls())
# Load the libraries needed
library(ggplot2)
library(tidyr)
library(readr)
library(pastecs)


# Reading the file into a dataframe:acs
# The dataset contains 8 variables with 136 observations
# The elements are ID, Id2, Geography,PopGroupID, POPGROUP.display-label`, RacesReported,
# HSDegree and BachDegree.
# The data types are shown in the output of str()

acs <- read_csv("acs-14-1yr-s0201.csv")
## -- sink("assignment_3.1.1_ACS_2014_SamantaArindam.txt")

# Viewing a sample of the data from the data frame
## --print(head(acs))
head(acs)

#2. Structure of the dataframe
## -- print(str(acs))
str(acs)

#2. No. of observations/rows
nrow(acs)

#2. No of variables/columns 
## print(ncol(acs))
ncol(acs)
## sink()

# Counting the No of rows having the HS Degree between 85% and 95%
# This is just to ensure that the histogram count is showing properly
nrow(subset(acs, HSDegree > 85 & HSDegree < 95))

## pdf("assignment_3.1.1_Histogram_SamantaArindam.pdf")
#3. Histogram with HSDegree variable
# Using gghist as the object I have plotted a simple histogram 
# binwidth is set to 5 which shows an outlier 
gghist <- ggplot(acs, aes( x = HSDegree)) +
  geom_histogram( binwidth = 5, alpha = 0.6) +
  labs(title = "Histogram using ggplot2",
       x = "HS Degree %", y = "Count")
# Plot the histogram
gghist

# This second histogram we have asked for density plot as we want to plot the normal curve
# 4 The data distribution from the frequency histogram shows that it is bimodal as we have 2 towers.
# -------------------------------------------------------------------------------------------------
ggdens <- ggplot(acs, aes( x = HSDegree)) +
  geom_histogram(aes(y = ..density.. ), binwidth = 1, color = "black", fill = "white") +
  labs(title = "Histogram using ggplot2",
       x = "HS Degree %", y = "Density")
# print the plot
ggdens

# Adding another layer to the chart - normal curve
# Adding another layer stat_function() to the histogram object ggdens
# The curve shows that the distribution is not symmetrical/normal. It is not bell-shaped.
# It is negatively skewed as the higher frequency values are towards the tail
# No this data cannot be represented as a normal model.
ggdens + stat_function(fun = dnorm, args = list(mean = mean(acs$HSDegree, na.rm = TRUE), 
                                                sd = sd(acs$HSDegree, na.rm = TRUE)), 
                       color = "red", size = 1 )

# Drawing a Q-Q plot
# This is another way to inspect and see if a distribution is normal
ggplot(acs, aes(sample = acs$HSDegree)) + stat_qq() 
 ## As the QQ plot also shows as it does not have all the points on the diagonal so the distribution is not normal.

## graphics.off()

## sink("assignment_3.1.2_ACS_2014_SamantaArindam.txt")
# 7 Using stat.desc function from the package pastecs
# # as per the graph showing the skewness we see that it is 
## negatively skewed as the frequency of the density is
## towards the higher end.
## kurtosis measures the pointyness of the distribution.
## Here in this case we see the kutosis is positive, so
## it implies that it is leptokurtic which implies
## a heavy tailed distribution.

## Also we see form the histogram that if we remove the 
## outliers from the lower value then we might end up with
## normal distribution.
## print(stat.desc(acs$HSDegree, basic = FALSE, norm = TRUE))

stat.desc(acs$HSDegree, basic = FALSE, norm = TRUE)

## sink()


>>>>>>> e9bdb86d44af5fae92b3766508fa8177796e82ac
