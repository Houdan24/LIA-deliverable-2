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

# ===== PART 3: Manipulating your data =====

# Create empty lists to store the filtered data
gender_f, race_f, parent_ed_f, lunch_f, prep_f = [], [], [], [], []
math_f, reading_f, writing_f = [], [], []

# Loop through each student (each row in the dataset)
for i in range(len(prep)):
    # Check if the student completed the test preparation course
    if prep[i] == "completed":
        # Keep this student's data in all arrays
        gender_f.append(gender[i])
        race_f.append(race[i])
        parent_ed_f.append(parent_ed[i])
        lunch_f.append(lunch[i])
        prep_f.append(prep[i])
        math_f.append(math[i])
        reading_f.append(reading[i])
        writing_f.append(writing[i])

# Convert lists back to NumPy arrays
gender_f   = np.array(gender_f)
race_f     = np.array(race_f)
parent_ed_f= np.array(parent_ed_f)
lunch_f    = np.array(lunch_f)
prep_f     = np.array(prep_f)
math_f     = np.array(math_f)
reading_f  = np.array(reading_f)
writing_f  = np.array(writing_f)

# --- Print a short summary to confirm ---
print("\nPART 3: Filtering Results")
print("Original number of students:", len(prep))
print("Students who completed test prep:", len(prep_f))
print("Average math score (completed):", round(math_f.mean(), 2))

# ===== PART 4: Plotting your data =====

import matplotlib.pyplot as plt
import numpy as np

# 1) Scatter plot – relation between Math and Reading scores
plt.scatter(math, reading)
plt.title("Scatter: Math vs Reading")
plt.xlabel("Math score")
plt.ylabel("Reading score")
plt.show()

# 2) Bar plot – average Math score by test preparation course
prep_labels, prep_counts = np.unique(prep, return_counts=True)
avg_math_completed = math[prep == "completed"].mean()
avg_math_none = math[prep == "none"].mean()
plt.bar(["Completed", "None"], [avg_math_completed, avg_math_none])
plt.title("Average Math Score by Test Prep Status")
plt.xlabel("Test Prep")
plt.ylabel("Average Math Score")
plt.show()

# 3) Histogram – distribution of Writing scores (shows how scores spread)
plt.hist(writing, bins=10, color="lightblue")
plt.title("Histogram: Writing Score Distribution")
plt.xlabel("Writing score")
plt.ylabel("Number of students")
plt.show()

# 4) Pie chart – percentage of students by test prep status
plt.pie(prep_counts, labels=prep_labels, autopct="%1.1f%%")
plt.title("Pie Chart: Test Prep Status")
plt.show()

# 5) Multi-array line plot – compare averages for students with/without test prep
subjects = ["Math", "Reading", "Writing"]
avg_completed = [math[prep == "completed"].mean(),
                 reading[prep == "completed"].mean(),
                 writing[prep == "completed"].mean()]
avg_none = [math[prep == "none"].mean(),
            reading[prep == "none"].mean(),
            writing[prep == "none"].mean()]
plt.plot(subjects, avg_completed, "b--", label="Completed")
plt.plot(subjects, avg_none, "r:", label="None")
plt.title("Average Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average score")
plt.legend()
plt.show()

# 6) Plot with grid – simple line plot of average scores overall
overall_avg = [math.mean(), reading.mean(), writing.mean()]
plt.plot(subjects, overall_avg, marker="o")
plt.title("Overall Average Scores (with grid)")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.grid(True)
plt.show()

# 7) Two subplots side by side – Math score distributions for both groups
plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)
plt.hist(math[prep == "completed"], bins=10, color="green")
plt.title("Math – Completed")
plt.xlabel("Score")
plt.ylabel("Count")

plt.subplot(1, 2, 2)
plt.hist(math[prep == "none"], bins=10, color="orange")
plt.title("Math – None")
plt.xlabel("Score")
plt.ylabel("Count")

plt.suptitle("Math Scores by Test Prep (Two Subplots)")
plt.tight_layout()
plt.show()

