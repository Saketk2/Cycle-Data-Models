import pandas as pd
import matplotlib.pyplot as plt

jan_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\January.csv", usecols=[4])

# Initialize counters
strandedTotal = 0
nonStrandedTotal = 0
strandedJan = 0
nonStrandedJan = 0

# Iterate through the column and count empty and non-empty slots
for value in jan_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedJan += 1
        strandedTotal += 1
    else:
        nonStrandedJan += 1
        nonStrandedTotal += 1

feb_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\February.csv", usecols=[4])

# Initialize counters
strandedFeb = 0
nonStrandedFeb = 0

# Iterate through the column and count empty and non-empty slots
for value in feb_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedFeb += 1
        strandedTotal += 1
    else:
        nonStrandedFeb += 1
        nonStrandedTotal += 1


Mar_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\March.csv", usecols=[4])

# Initialize counters
strandedMar = 0
nonStrandedMar = 0

# Iterate through the column and count empty and non-empty slots
for value in Mar_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedMar += 1
        strandedTotal += 1
    else:
        nonStrandedMar+= 1
        nonStrandedTotal += 1


Apr_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\April.csv", usecols=[4])

# Initialize counters
strandedApr = 0
nonStrandedApr = 0

# Iterate through the column and count empty and non-empty slots
for value in Apr_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedApr += 1
        strandedTotal += 1
    else:
        nonStrandedApr += 1
        nonStrandedTotal += 1


May_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\May.csv", usecols=[4])

# Initialize counters
strandedMay = 0
nonStrandedMay = 0

# Iterate through the column and count empty and non-empty slots
for value in May_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedMay += 1
        strandedTotal += 1
    else:
        nonStrandedMay += 1
        nonStrandedTotal += 1


June_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\June.csv", usecols=[4])

# Initialize counters
strandedJune = 0
nonStrandedJune = 0

# Iterate through the column and count empty and non-empty slots
for value in June_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedJune += 1
        strandedTotal += 1
    else:
        nonStrandedJune += 1
        nonStrandedTotal += 1


July_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\July.csv", usecols=[4])

# Initialize counters
strandedJuly = 0
nonStrandedJuly = 0

# Iterate through the column and count empty and non-empty slots
for value in July_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedJuly += 1
        strandedTotal += 1
    else:
        nonStrandedJuly += 1
        nonStrandedTotal += 1


Aug_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\August.csv", usecols=[4])

# Initialize counters
strandedAug = 0
nonStrandedAug = 0

# Iterate through the column and count empty and non-empty slots
for value in Aug_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedAug += 1
        strandedTotal += 1
    else:
        nonStrandedAug += 1
        nonStrandedTotal += 1


Sep_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\September.csv", usecols=[4])

# Initialize counters
strandedSep = 0
nonStrandedSep = 0

# Iterate through the column and count empty and non-empty slots
for value in Sep_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedSep += 1
        strandedTotal += 1
    else:
        nonStrandedSep += 1
        nonStrandedTotal += 1


Oct_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\October.csv", usecols=[4])

# Initialize counters
strandedOct = 0
nonStrandedOct = 0

# Iterate through the column and count empty and non-empty slots
for value in Oct_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedOct += 1
        strandedTotal += 1
    else:
        nonStrandedOct += 1
        nonStrandedTotal += 1


Nov_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\November.csv", usecols=[4])

# Initialize counters
strandedNov = 0
nonStrandedNov = 0

# Iterate through the column and count empty and non-empty slots
for value in Nov_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedNov += 1
        strandedTotal += 1
    else:
        nonStrandedNov += 1
        nonStrandedTotal += 1


Dec_data = pd.read_csv(r"C:\Users\Tony\Documents\BigData\Data\December.csv", usecols=[4])

# Initialize counters
strandedDec = 0
nonStrandedDec = 0

# Iterate through the column and count empty and non-empty slots
for value in Dec_data['start_station_name']:
    if pd.isnull(value):  # Check if value is NaN
        strandedDec += 1
        strandedTotal += 1
    else:
        nonStrandedDec += 1
        nonStrandedTotal += 1
    

# Summer data
strandedSummer = strandedJune + strandedJuly + strandedAug
nonStrandedSummer = nonStrandedJune + nonStrandedJuly + nonStrandedAug

# Create data
categories_summer = ['Stranded Bikes', 'Non-Stranded Bikes']
counts_summer = [strandedSummer, nonStrandedSummer]
colors = ['blue', 'red']

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts_summer, labels=categories_summer, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color': "white"})
plt.title('Station Status in the Summer')
plt.show()

# Fall data
strandedFall = strandedSep + strandedOct + strandedNov
nonStrandedFall = nonStrandedSep + nonStrandedOct + nonStrandedNov

# Create data
categories_fall = ['Stranded Bikes', 'Non-Stranded Bikes']
counts_fall = [strandedFall, nonStrandedFall]

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts_fall, labels=categories_fall, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color': "white"})
plt.title('Station Status in Fall')
plt.show()

# Winter data
strandedWinter = strandedDec + strandedJan + strandedFeb
nonStrandedWinter = nonStrandedDec + nonStrandedJan + nonStrandedFeb

# Create data
categories_winter = ['Stranded Bikes', 'Non-Stranded Bikes']
counts_winter = [strandedWinter, nonStrandedWinter]

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts_winter, labels=categories_winter, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color': "white"})
plt.title('Station Status in Winter')
plt.show()

# Spring data
strandedSpring = strandedMar + strandedApr + strandedMay
nonStrandedSpring = nonStrandedMar + nonStrandedApr + nonStrandedMay

# Create data
categories_spring = ['Stranded Bikes', 'Non-Stranded Bikes']
counts_spring = [strandedSpring, nonStrandedSpring]

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(counts_spring, labels=categories_spring, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color': "white"})
plt.title('Station Status in Spring')
plt.show()