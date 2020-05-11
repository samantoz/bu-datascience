# Assignment: 6.1: GSS 2016 Survey Data

# Name: SAMANTA, ARINDAM

# Date: 4 JANUARY 2020

# TASK 6.1
rm(list = ls())
# Load the libraries needed
library(ggplot2)
##library(tidyr)
library(readr)
## library(pastecs)


# Reading the file into a dataframe:acs


gss2016 <- read_csv("C:/Users/saman/Documents/GitHub/BU-DSC/dataset/gss-2016.csv")
problem(gss2016)

# Viewing a sample of the data from the data frame

gss2016.sub <- gss2016[, c("SIBS","CHILDS","SEX")]

head(gss2016.sub)


#2. Structure of the dataframe

str(gss2016.sub)

# Calculate correlation between the variables SIBS and CHILDS

  cor(gss2016.sub$CHILDS,gss2016.sub$SIBS, use = "pairwise.complete.obs")
  
ggplot(data = gss2016.sub, aes(x = SIBS, y = CHILDS)) +
  geom_point(position = "jitter")



ggplot(data = gss2016.sub, aes(x = SIBS, y = CHILDS)) +
  geom_point(position = "jitter") + 
  geom_abline()

ggplot(data = gss2016.sub, aes(x = SIBS, y = CHILDS)) +
  geom_jitter(width = 0.05, height = 0.05) + 
  geom_smooth()

ggplot(data = gss2016.sub, aes(x = SIBS, y = CHILDS)) +
  geom_jitter(width = 0.05, height = 0.05) + 
  geom_smooth(method = "glm", method.args = list(family = 'poisson'))



#2. No. of observations/rows
## nrow(survey_data)

#2. No of variables/columns 

## ncol(survey_data)
