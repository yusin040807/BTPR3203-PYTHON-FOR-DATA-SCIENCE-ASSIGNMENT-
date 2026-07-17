# River Quality Monitoring System

## BTPR3203 Python for Data Science Assignment

### Student Information

**Name:** DING YU SIN

**Student ID:** B230207C


**Course:** BTPR3203 Python for Data Science

**Semester:** 2026B

---

# Project Overview

The River Quality Monitoring System is developed as part of the BTPR3203 Python for Data Science assignment. The purpose of this system is to help monitor and manage river water quality using the Water Quality Index (WQI).

The system allows users to:

- Manage river monitoring stations
- Classify river water quality
- Record monitoring readings
- Analyse water quality trends
- Save and load river station information using text files

The project is implemented using Python and demonstrates the use of dictionaries, lists, tuples, functions, object-oriented programming, file handling, and exception handling.

---

# Features

## Part 1 – River Station Management

- Store river stations using nested dictionaries
- Display all river stations
- Classify WQI into Class I – Class V
- Add a new river station
- Update an existing river station
- Input validation for station information

---

## Part 2 – Monitoring Reading Log

- Log monitoring readings
- Store readings as tuples
- Automatically update station WQI
- Automatically update river status
- Display monitoring history
- Generate river pollution alerts

---

## Part 3 – Trend Analysis

- RiverStation class
- Display river station summaries
- Calculate average WQI by state
- Analyse WQI trends
- Identify greatest improvement
- Identify greatest decline
- Count stations in each WQI class

---

## Part 4 – File Handling

- Export river station data
- Load river station data
- Input validation
- Exception handling
- Automatic WQI reclassification after loading

---

# Python Concepts Used

This project demonstrates the following Python concepts:

- Variables
- Input and Output
- If-Else Statements
- Loops
- Functions
- Lists
- Tuples
- Dictionaries
- Nested Dictionaries
- Classes and Objects
- File Handling
- Exception Handling
- Datetime Module
- Sorting
- Data Validation

---

# Project Structure

```
River-Quality-Monitoring-System/
│
├── river_quality_monitoring.py
├── river_stations.txt
├── README.md
└── .gitignore
```

---

# File Description

| File | Description |
|------|-------------|
| river_quality_monitoring.py | Main Python program |
| river_stations.txt | Stores exported river station information |
| README.md | Project documentation |
| .gitignore | Ignore unnecessary files when uploading to GitHub |

---

# How to Run

## Step 1

Install Python 3.

Check the installation:

```bash
python --version
```

or

```bash
py --version
```

---

## Step 2

Download or clone this repository.

---

## Step 3

Open the project folder using Visual Studio Code.

---

## Step 4

Run the program.

Using Python:

```bash
python river_quality_monitoring.py
```

or

```bash
py river_quality_monitoring.py
```

---

# Main Menu

When the program starts, the following menu will be displayed:

```
======= Main Menu =======

1. Classify All Stations
2. Add / Update Station
3. Log Monitoring Reading
4. Trend Analysis
5. Export Report
0. Exit
```

---

# Sample River Stations

The program initially contains four monitoring stations.

| Station | State | Initial WQI |
|----------|---------|------------|
| Sungai Klang KL | Selangor | 68.3 |
| Sungai Muar | Johor | 54.1 |
| Sungai Perak | Perak | 84.6 |
| Sungai Pahang | Pahang | 45.8 |

---

# Water Quality Classification

| WQI | Classification |
|------|----------------|
| >92.7 | Class I – Clean |
| 76.5 – 92.7 | Class II – Slightly Polluted |
| 51.9 – 76.5 | Class III – Moderately Polluted |
| 31.0 – 51.9 | Class IV – Polluted |
| ≤31.0 | Class V – Heavily Polluted |

---

# Program Workflow

```
Start Program
      │
      ▼
Display Main Menu
      │
      ├── Part 1
      │      ├── Display Stations
      │      ├── Classify WQI
      │      └── Add / Update Station
      │
      ├── Part 2
      │      ├── Log Reading
      │      ├── View Reading History
      │      └── River Alerts
      │
      ├── Part 3
      │      ├── RiverStation Class
      │      ├── Average WQI
      │      ├── Trend Analysis
      │      └── Class Summary
      │
      ├── Part 4
      │      ├── Export Data
      │      └── Load Data
      │
      ▼
Exit
```

---

# Example Output

## Main Menu

```
======= Main Menu =======

1. Classify All Stations
2. Add / Update Station
3. Log Monitoring Reading
4. Trend Analysis
5. Export Report
0. Exit
```

---

## Station Display

```
Station Name              State          WQI      Status
--------------------------------------------------------------
Sungai Klang KL           Selangor       68.30    Class III
Sungai Muar               Johor          54.10    Class III
Sungai Perak              Perak          84.60    Class II
Sungai Pahang             Pahang         45.80    Class IV
```

---

## Export Example

```
River station report saved successfully.
```

---

# Requirements

- Python 3.x
- Visual Studio Code (recommended)

---

# Author

**Name:** DING YU SIN

**Student ID:** B230207C

Southern University College

BTPR3203 Python for Data Science

2026

---

# License

This project is developed for academic purposes only.

© 2026 DING YU SIN. All rights reserved.
