# Assignment: ASSIGNMENT 1

# Name: SAMANTA, ARINDAM

# Date: 08 DECEMBER 2019

# TASK 1
# The below code is just for a sample to test the export
setwd("~/GitHub/BU-DSC")
rm(list = ls())
scores <- read.csv("scores.csv", header = TRUE)

sink("assignment_1_SamantaArindam.txt")
print(names(scores))
print(summary(scores))
sink()

jpeg("histogram.jpg")
pdf("histogram.pdf")
# Code 

graphics.off()
