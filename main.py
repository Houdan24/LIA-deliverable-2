#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 14:20:37 2025

@author: danyhourani garrishrasiah
"""

import numpy as np

# --- Load dataset (CSV) with NumPy ---
# skiprows=1  → skips the header row
# delimiter=','  → separates the columns
# dtype=str  → keeps everything as text so we can convert later
# quotechar='"'  → removes quotation marks around the numbers
data = np.loadtxt("exams.csv", delimiter=",", skiprows=1, dtype=str, quotechar='"')

# --- Display basic info to confirm it worked ---
print("Dataset loaded successfully!")
print("Shape of dataset:", data.shape)
print("First 5 rows:")
print(data[:5])

# --- Split into one array per column (Part 2 requirement) ---
# Order of columns in the dataset:
# 0 gender | 1 race/ethnicity | 2 parental level of education | 3 lunch
# 4 test preparation course | 5 math score | 6 reading score | 7 writing score
gender    = data[:, 0]
race      = data[:, 1]
parent_ed = data[:, 2]
lunch     = data[:, 3]
prep      = data[:, 4]

# --- Convert numeric columns from string → float ---
# (we strip quotes just in case)
math    = np.char.strip(data[:, 5], '"').astype(float)
reading = np.char.strip(data[:, 6], '"').astype(float)
writing = np.char.strip(data[:, 7], '"').astype(float)

# --- Quick verification (simple prints) ---
print("\nColumn previews:")
print("Gender:", gender[:5])
print("Test prep:", prep[:5])
print("Math (first 5):", math[:5])

# --- Basic statistics ---
print("\nAverage scores:")
print("Math:", round(math.mean(), 2))
print("Reading:", round(reading.mean(), 2))
print("Writing:", round(writing.mean(), 2))
