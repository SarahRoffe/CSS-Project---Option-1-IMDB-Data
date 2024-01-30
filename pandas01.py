#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Created on Mon Jan 29 09:57:12 2024

#@author: user

#just like R ctrl enter runs your script
#Also ctrl F10
#working directory
#import os

#path = os.getcwd()

#print(path)

#work for the day
import pandas

#can you make pretty with your working directory
file = pandas.read_csv("country_data.csv")

print(file)

print(file.info()) 
#like head() in R

print(file.describe())