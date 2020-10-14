# config_admin.ini

## Purpose

To hold the JIRA credentials, reporting html page layout, and reporting calculation thresholds or ceilings.

## Description

There are currently 3 sections in config_admin.ini:

1. ADMIN

2. MASTER-LAYOUT

3. REPORTING

### ADMIN section

This section has 2 variables:

user = The JIRA logon user used to authenticate against JIRA when extracting data attached to a JIRA ticket.

passwd = The JIRA logon password.

### MASTER-LAYOUT

This section allows you to format the appearance of each report, such as the size of the font and how big to make the charts.

### REPORTING

log_level is deprecated

outlier_threshold = Using the Z-Score algorithm, how far from the norm do you deviate before we flag you as an anomaly. 

reports_hourly = Number of hours to report on the daily chart, which appears on the right side of each charting row (The big chart).

reports_daily is deprecated
