<p align="center">
	<img src="Images/Header.png?raw=true" width=80% height=80%>
</p>

# Prediction of the Probability of Suffering Different Crimes in Mexico
#### By Daniel Eduardo López

**30/04/2023**

**[LinkedIn](https://www.linkedin.com/in/daniel-eduardo-lopez)**

**[Github](https://github.com/DanielEduardoLopez)**

____
### **Contents**

1. [Introduction](#intro)<br>
2. [General Objective](#objective)<br>
3. [Research Question](#question)<br>
4. [Hypothesis](#hypothesis)<br>
5. [Abridged Methodology](#methodology)<br>
6. [Results](#results)<br>
	6.1 [Data Collection](#collection)<br>
	6.2 [Data Exploration](#eda)<br>
	6.3 [Data Preparation](#preparation)<br>
	6.4 [Data Modeling](#modeling)<br>
	6.5 [Evaluation](#evaluation)<br>
7. [App](#app)<br>
8. [Conclusions](#conclusions)<br>
9. [Bibliography](#bibliography)<br>
10. [Description of Files in Repository](#files)<br>

____
<a class="anchor" id="intro"></a>
### **1. Introduction**

Since the 2000's, Mexico has experienced a sustained increase in crime and violence due to both criminal organizations and common criminals. In this sense, crime has become the top concern for the overall population [(Calderón, Heinle, Kuckertz, Rodríguez-Ferreira & Shirk, 2021)](#calderon). 

Some of the reasons for such a spread of crime and violence are the purposeful fragmentation of the criminal groups by the Mexican government, the consequent increase on competition and diversification among criminal organizations, a rampant corruption within the Mexican institutions, ineffective socio-economic policies, widespread impunity and low effective prosecution rates, and the alienation of local populations to criminals [(Felbab-Brown, 2019)](#calderon). 

In this context, it has been estimated that the crime rate was of 94.1 per 100,000 inhabitants before the COVID-19 lockdown in Mexico [(Balmori de la Miyar, Hoehn‑Velasco & Silverio‑Murillo, 2021)](#balmori).

However, the distribution of crime and violence is uneven accross the country. Thus, it is desirable to know how likely is suffering a crime based on the demographic and socio-economic profile of a given household/person, rather than just sticking to national or regional averages. 

Even though official crime data exists within the country, it has been estimated that the percentage of unreported crimes was of about 93.3% in 2020 [(Mexico Violence Resource Project, 2022)](#resource). In order to address this issue, the **National Survey of Victimization and Perception of Public Safety** (ENVIPE, by its acronym in Spanish) has been develop as a tool to gather representative data about the levels of crime incidence and unreported crimes -*cifra negra*- [(INEGI, 2021)](#inegi). 

Therefore, the ENVIPE data was used to train several classification models for the following crimes:
1. Total vehicle theft
2. Partial vehicle theft
3. Vandalism
4. Burglary
5. Kidnapping
6. Enforced disappearance
7. Murder
8. Theft
9. Other thefts
10. Bank fraud
11. Other frauds
12. Extortion
13. Threats
14. Injuries
15. Assault
16. Rape
17. Other crimes

This, in order to have a more accurate estimation of the probability of suffering different crimes in Mexico, according to an specific demographic and socio-economic profile.

___
<a class="anchor" id="objective"></a>
## **2. General Objective**

To predict the probability of suffering different crimes in Mexico based on demographic and socio-economic data.


___
<a class="anchor" id="question"></a>
## **3. Research Question**

What is the probability of suffering different crimes in Mexico based on demographic and socio-economic data?

___
<a class="anchor" id="hypothesis"></a>
## **4. Hypothesis**

The overall probability of suffering a crime in Mexico is about **0.094%** [(Balmori de la Miyar, Hoehn‑Velasco & Silverio‑Murillo, 2021)](#balmori). However, such probability is different according to the socioeconomic and demographic profile, with the low-income profiles having a higher probability of suffering crimes than the high-income profiles.

___
<a class="anchor" id="methodology"></a>
## **5. Abridged Methodology**

The methodology of the present study is based on Rollin’s *Foundational Methodology for Data Science* [(Rollins, 2015)](#rollins):

1. **Analytical approach**: Building and evaluation of classification models.
2. **Data requirements**: Data about the incidence of the following crimes: Total vehicle theft, Partial vehicle theft, Vandalism, Burglary, Kidnapping, Enforced Disappearance, Murder, Theft, Other thefts, Bank fraud, Other frauds, Extortion, Threats, Injuries, Assault, Rape, and Other crimes; as well as data about the demographics and socio-economic conditions of the households/persons affected by those crimes.
3. **Data collection**: Data from ENVIPE was retrieved from the <a href="https://www.inegi.org.mx/programas/envipe/2022/#Datos_abiertos">INEGI's website</a>. Then, the different tables from ENVIPE were used to build a database in MySQL 8.0.32.0 (see the corresponding SQL script <a href="https://raw.githubusercontent.com/DanielEduardoLopez/PublicSafetyMX/main/sql_script.sql">here</a>). After that, said database was queried to gather only the relevant data and build the dataset to be used in the next steps (see the SQL query used <a href="https://raw.githubusercontent.com/DanielEduardoLopez/PublicSafetyMX/main/sql_query.sql">here</a>).
4. **Data exploration**: Data was explored with Python 3 and its libraries Numpy, Pandas, Matplotlib and Seaborn.
5. **Data preparation**: Data was cleaned and prepared with Python 3 and its libraries Numpy and Pandas.
6. **Data modeling**: The dataset was split in training, validation and testing sets. Then, Logistic Regression, K-Nearest Neighbors, Support Vector Machines, Naive Bayes, Decision Trees, Random Forests, and XGBoost were used to build the classification models. The hyperparameters for each model were tunned using GridSearchCV or RandomizedSearchCV. After that, Platt scaling was used over the scores of the best classification models for estimating the probability of suffering different crimes based on the input data. Python 3 and its libraries Numpy, Pandas, and Sklearn were utilized for all the modeling steps.
7. **Evaluation**: The algorithms predictions were primarily evaluated through the accuracy rate, the area under the ROC curve (AUC ROC), and the root-mean-square error (RMSE). However, other metrics and tools such as confusion matrices, classification reports, AUC ROC plots, precision, negative predictive value (NPV), sensitivity, specificity, and the F1 score were also used.
8. **Implementation**: An app was built and deployed with Streamlit.

___
<a class="anchor" id="results"></a>
## **6. Results**

### **6.1 Data Collection** <a class="anchor" id="collection"></a>

First, data from ENVIPE was retrieved from the <a href="https://www.inegi.org.mx/programas/envipe/2022/#Datos_abiertos">INEGI's website</a>, in form of several CSV files. 

Then, the encoding of the different original CSV files from INEGI were transformed to **UTF-8** using a <a href="https://github.com/DanielEduardoLopez/PublicSafetyMX/blob/45d5bae551ed9be40e30cd1a9578e45ddf3c69c0/CleanCSV.ipynb">previous notebook</a>. Furthermore, the datatypes of the different atributes were also adjusted.

Later, a database was built in MySQL 8.0.32.0 (see the corresponding SQL script <a href="https://raw.githubusercontent.com/DanielEduardoLopez/PublicSafetyMX/main/sql_script.sql">here</a>), comprising the following tables:
* tvivienda
* thogar 
* tsdem
* tmod_vic
* tper_vic1
* tper_vic2

The naming conventions from the original ENVIPE scheme were respected. 

The **ER Diagram** of the built database is as follows (obtained through the *Reverse Engineer* feature in MySQL Workbench):

<p align="center">
	<img src="Images/db_diagram.png?raw=true" width=70% height=60%>
</p>

After that, the UTF-8-encoded CSV files with all the survey observations were loaded to their correspondent tables in the database.

Finally, after a thorough review of all the atributes in each of the tables of the schema, the database was queried to gather only the relevant data and build the dataset to be used in this notebook (see the SQL query used <a href="https://raw.githubusercontent.com/DanielEduardoLopez/PublicSafetyMX/main/sql_query.sql">here</a>).


### **6.2 Data Exploration** <a class="anchor" id="eda"></a>

Pending...


___
<a class="anchor" id="app"></a>
## **7. App**

Pending...

___
<a class="anchor" id="conclusions"></a>
## **8. Conclusions**

Pending...

___
<a class="anchor" id="bibliography"></a>
## **9. Bibliography**

* <a class="anchor" id="balmori"></a> **Balmori de la Miyar, J. R., Hoehn‑Velasco, L. & Silverio‑Murillo, A. (2021).** The U‑shaped crime recovery during COVID‑19 evidence from national crime rates in Mexico. *Crime Science*. 10:14. https://doi.org/10.1186/s40163-021-00147-8
* <a class="anchor" id="calderon"></a> **Calderón, L. Y., Heinle, K., Kuckertz, R. E., Rodríguez-Ferreira, O. & Shirk, D. A. (eds.) (2021).** *Organized Crime and Violence in Mexico: 2021 Special Report*. Justice in Mexico, University of San Diego. https://justiceinmexico.org/wp-content/uploads/2021/10/OCVM-21.pdf 
* <a class="anchor" id="felbab"></a> **Felbab-Brown, V. (2019).** *Mexico’s out-of-control criminal market*. Brookings Institution. https://www.brookings.edu/wp-content/uploads/2019/03/FP_20190322_mexico_crime-2.pdf 
* <a class="anchor" id="inegi"></a> **INEGI (2022).** *Encuesta Nacional de Victimización y Percepción sobre Seguridad Pública (ENVIPE) 2022*. https://www.inegi.org.mx/programas/envipe/2022/
* <a class="anchor" id="resource"></a> **Mexico Violence Resource Project (2022).** *Essential Numbers*. UC San Diego’s Center for U.S.-Mexican Studies. https://www.mexicoviolence.org/essential-numbers
* <a class="anchor" id="rollins"></a> **Rollins, J. B. (2015)**. *Metodología Fundamental para la Ciencia de Datos. Somers: IBM Corporation.* https://www.ibm.com/downloads/cas/WKK9DX51

___
<a class="anchor" id="files"></a>
## **10. Description of files in repository**
File | Description 
--- | --- 
CleanCSV.ipynb | Notebook with the Python code for encoding the original CSV files from INEGI into UTF-8.
PublicSafetyMX.ipynb | Notebook with the Python code for exploring, wrangling, modeling, and evaluating the crime data.
dataset.csv.csv | Queried data retrieved from the database with the data from ENVIPE.
sql_query.sql | SQL code for generating the dataset.
sql_script.sql| SQL script to build database with the data from ENVIPE.
