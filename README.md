# M605 Advanced Databases - Individual Project

**Student Name:** Jagruti Ramesh Girase  
**Student ID:** GH1057897  
**Module:** M605 Advanced Databases  
**Domain:** KWS Agricultural Operations (Seed Production & Field Trials)  
**GitHub Repository:** [Advance Databases Project](https://github.com/username/Advance_Databases_Project)

---

## Project Overview
This project implements a **hybrid database architecture** for KWS Agricultural Operations, combining a relational SQL database for structured financial/client accounts and a non-relational NoSQL database for flexible field trial logs. An automated Python application layer connects both tiers to handle integration data flows, full CRUD operations, and advanced aggregations.

* **Relational Tier (MySQL):** `kws_relational_db` managing structured grower accounts (`clients`) and sales orders (`orders`) with strict ACID compliance, foreign key constraints, and indexing.
* **Non-Relational Tier (MongoDB):** `kws_agricultural_db` managing schema-flexible agronomic sensor and trial data (`field_trial_logs`).
* **Application Layer (Python):** VS Code workspace scripts handling database setup, indexing, cross-database integration, and execution.

---

## Workspace Directory Structure
```text
Advance_Databases_Project/
│
├── init_kws_advanced.py    # Python script to initialize databases, apply indexes, & generate 100+ records
├── queries_kws.py          # Python script to execute functional SQL JOINs, cross-platform flow, CRUD, & aggregations
└── README.md               # Project documentation and setup guide