# Exploratory-Data-Analysis-Crime-Data
An EDA project for Jovian Data Science Bootcamp

### Data Source
The data is from the 'Crime Data from 2020 to Present' Dataset by Los Angeles Police Department from the Los Angeles Open Data Portal. The data can be found [here](https://data.lacity.org/A-Safe-City/Crime-Data-from-2020-to-Present/2nrs-mtv8). It Contains all crimes reported to the LAPD from 2020 to present and it is updated daily. It contains approximately 700,000 records and 26 columns. Data has been pulled in JSON format through the SODA API using pandas library.





### Data Exploration and Cleaning
- I started by importing the JSON data into a pandas dataframe using the **Pandas Library**.
- I then checked the shape of the data and the data types of the columns.
- I checked the missing values in each column and found that the columns with the most missing values are:
    - **weapon_description** (608 Missing values) - Replaced with 'UNKNOWN WEAPON/OTHER WEAPON' value already found in the column.
    - **weapon_used_code** (608 Missing values) - Redundant column with weapon description. It was dropped as explained below.
    - **vict_sex** (62 Missing values) - Replaced with 'X' value already found in the column which represents unknown sex.
    - **vict_descent** (62 Missing values) - Replaced with 'unknown' which will represents unknown descent.
    - **mocodes, crm_cd_2, cross_street** all have missing values but they will not be used in the analysis so they will be dropped.
- I checked for duplicates and found that there are **no significant duplicates** in the data.
- I checked for outliers and found:
    - The **time_occ(time occured) column** data is supposed to be in 24 hour military format but a lot of those entries are not 4 digit. I am guessing they are missing Zeros at the end or in the front. I will add zeros to the front of the entries that are less than 4 digits. I created functions to clean the data and add zeros to the front of the entries that are less than 4 digits but the data output was coming as string. Thus i had to use pandas to_datetime function to convert the data to datetime format for easier analysis and visualization.
    - The **vict_age**(Victim age) column has outliers i.e. having a value of '0' which is not possible. I will assume that this is a missing value and replace it with the mean age of the victims. It does not matter if mean or mode is used because the mean and mode are very close to each other and hence the data is not skwed.
- I checked for the unique values in each column and found that there are a few redundant columns, Namely:
    -**weapon_used_code** is redundant with weapon_description. Although it may be useful for machine learning purposes, it is not useful for EDA because it is a code and not a description.
    -**status_code** is redundant with status_description. Status description is more descriptive, easier to understand and small in size.
    -**crm_cd_1** is redundant with crm_cd. By definition, crm_cd_1 is the same as crm_cd. I will drop crm_cd_1.

### Data Analysis and Visualization





        
