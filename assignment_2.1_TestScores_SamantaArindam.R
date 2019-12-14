# Assignment: ASSIGNMENT 2.1 Test SCores

# Name: SAMANTA, ARINDAM

# Date: 04 DECEMBER 2019

# TASK 1. What are the observational units in this study?
rm(list = ls())
# install.packages("data.table")
# library(data.table)
# scores <- fread("scores.csv")

scores <- read.csv("scores.csv", header = TRUE)
scores$Course <- as.factor(toString(scores$Count))
attach(scores)

# sink("assignment_2.1_TestScores_SamantaArindam.txt")
# listing the names of the obervational units in my data set
names(scores)

# determine which variables are categorical and which are quantitative
str(scores)

# variable to hold subset of the dataset that contains only Regular section

regular_data <- subset(scores, subset = scores$Section == "Regular")
summary(regular_data$Count)

# variable to hold subset of the dataset that contains only Sport section
sports_data <- subset(scores, subset = scores$Section == "Sports")
sports_data

x <- regular_data$Count
y <- regular_data$Score

plot(x,y)

# sink()
