# M605 Advanced Databases - Individual Project

**Student Name:** Jagruti Ramesh Girase  
**Student ID:** GH1057897  
**Module:** M605 Advanced Databases  
**Domain:** KWS Agricultural Operations (Seed Production & Field Trials)  

---

## Project Overview
This project implements a **hybrid three-tier database architecture** combining a relational SQL database, a non-relational NoSQL database, and an application integration layer built in Python. 

* **Relational Tier (MySQL):** Stores structured operational data such as customer profiles (`clients`) and sales transactions (`orders`) with strict ACID compliance and foreign key constraints.
* **Non-Relational Tier (MongoDB):** Stores semi-structured, flexible documents containing environmental sensor data and agronomic metrics (`field_trial_logs`).
* **Application Layer (Python):** Acts as the bridge connecting both database systems, automating record generation (100+ volume scale) and executing functional queries, joins, and aggregations.

---

## Repository Structure
```text
ADVANCE_DATABASES_PROJECT/
│
├── init_kws_advanced.py    # Script to setup databases and generate 100+ records
├── queries_kws.py          # Script to execute functional SQL JOINs and MongoDB aggregations
└── README.md               # Project documentation and setup guide