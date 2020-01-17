# Assignment: ASSIGNMENT 5.1 Student Survey

# Name: SAMANTA, ARINDAM

# Date: 4 JANUARY 2020

# TASK 3.1
rm(list = ls())
# Load the libraries needed
library(ggplot2)
library(tidyr)
library(readr)
library(pastecs)


# Reading the file into a dataframe:acs


survey_data <- read_csv("C:/Users/saman/Documents/GitHub/BU-DSC/dataset/student-survey.csv")

# Viewing a sample of the data from the data frame

head(survey_data)

#2. Structure of the dataframe

str(survey_data)

#2. No. of observations/rows
nrow(survey_data)

#2. No of variables/columns 

ncol(survey_data)

TimeRead <- survey_data$TimeReading
TimeTV <- survey_data$TimeTV
TimeTV.hrs <- survey_data$TimeTV/60


lm(TimeRead ~ TimeTV)

lm(TimeRead ~ TimeTV.hrs)

survey_data %>%
  ggplot(aes(TimeReading,TimeTV)) + geom_point() + 
  geom_smooth(method = "lm", se = FALSE)

# Creating a scatter plot with the survey data
plot(survey_data$TimeReading, survey_data$TimeTV/60,
     main = "Scatter plot of Tv Time Vs Reading Time",
     xlab = "Reading Time(hrs)",
     ylab = "TV Time (hrs)")

# Call supsmu() to generate a smooth trend curve

trend1 <- supsmu(survey_data$TimeReading, survey_data$TimeTV/60, bass = 10)

lines(trend1)

# Create an empty plot

plot(survey_data$TimeTV/60, survey_data$Happiness,
     type = "n",
     ylab = "Happiness Index",
     xlab = "TVTime(hrs)")

# Adding Point with shapes determined by happiness index
points(survey_data$TimeTV/60, survey_data$Happiness,
       pch = survey_data$Gender)

trend2 <- supsmu(survey_data$TimeTV/60, survey_data$Happiness, bass = 10)

lines(trend2)

#Adding Legend for the Gender
legend("topright", pch = c(0,1),
       legend = c("M","F"))


