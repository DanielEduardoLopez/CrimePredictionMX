# Prediction of the Probability of Suffering Different Crimes in Mexico
# Author: Daniel Eduardo López
# Github: https://github.com/DanielEduardoLopez
# LinkedIn: https://www.linkedin.com/in/daniel-eduardo-lopez
# Date: 2023/05/29

"""
Project's Brief Description:
Multi-label classification model for predicting the probability of suffering different crimes in Mexico based on the
National Survey of Victimization and Perception of Public Safety (INEGI, 2021).
"""

# Libraries importation
import numpy as np
import pandas as pd
import streamlit as st
#import keras
#import tensorflow as tf

st.title("Prediction of the Probability of Suffering Different Crimes in Mexico")

page = st.sidebar.selectbox("Choose a page", ["Homepage", "Predict"])

if page == "Homepage":
    st.image("https://github.com/DanielEduardoLopez/CrimePredictionMX/blob/main/Images/picture.jpg?raw=true")
    html_picture = '<p style="font-size: 12px">Image Credit: <a href="https://pixabay.com/photos/police-line-yellow-crime-cemetery-3953745/">ValynPi14</a></p>'
    st.markdown(html_picture, unsafe_allow_html=True)
    st.markdown("#### By Daniel Eduardo López (2023/05/31)")
    url_github = "https://github.com/DanielEduardoLopez"
    url_linkedin = "https://www.linkedin.com/in/daniel-eduardo-lopez"
    st.write("[LinkedIn](%s)" % url_linkedin)
    st.write("[GitHub](%s)" % url_github)
    st.header("Welcome!")
    st.markdown("Since the 2000's, Mexico has experienced a sustained increase in crime and violence due to both criminal organizations and common criminals. In this sense, crime has become **the top concern for the overall population** (Calderón, Heinle, Kuckertz, Rodríguez-Ferreira & Shirk, 2021).")
    st.markdown("Some of the reasons for such a spread of crime and violence are the purposeful fragmentation of the criminal groups by the Mexican government, the consequent increase on competition and diversification among criminal organizations, a rampant corruption within the Mexican institutions, ineffective socio-economic policies, widespread impunity and low effective prosecution rates, and the alienation of local populations to criminals (Felbab-Brown, 2019).")
    st.markdown("In this context, it has been estimated that the crime rate was of 94.1 per 100,000 inhabitants before the COVID-19 lockdown in Mexico (Balmori de la Miyar, Hoehn‑Velasco & Silverio‑Murillo, 2021).")
    st.markdown("However, the distribution of crime and violence is **uneven accross the country**. Thus, it is desirable to know how likely is suffering a crime based on the **demographic and socio-economic profile of a given household/person**, rather than just sticking to national or regional averages.")
    st.markdown("Even though official crime data exists within the country, it has been estimated that the percentage of unreported crimes was of about 93.3% in 2020 (Mexico Violence Resource Project, 2022). In order to address this issue, the :blue[**National Survey of Victimization and Perception of Public Safety**] (ENVIPE, by its acronym in Spanish) has been develop as a tool to gather **representative data** about the levels of crime incidence and unreported crimes -the so-called *cifra negra*- (INEGI, 2021).")
    st.markdown("Therefore, the ENVIPE data was used to train **a multi-label classification model** (Babych, 2023; Brownlee, 2020; Tsoumakas & Katakis, 2007) for the following crimes:")
    st.markdown("1. Total vehicle theft\n2. Partial vehicle theft\n3. Vandalism\n4. Burglary\n5. Kidnapping\n6. Enforced disappearance\n7. Murder\n8. Theft\n9. Other thefts\n10. Bank fraud\n11. Other frauds\n12. Extortion\n13. Threats\n14. Injuries\n15. Assault\n16. Rape\n17. Other crimes\n18. Any crime")
    st.markdown("This, in order to have **a more accurate estimation of the probability of suffering different crimes** in Mexico, according to :blue[**specific demographic and socio-economic profiles**].")
    st.markdown('Please go the page :orange[**"Predict"**] to play with the model. :blush:')
    st.markdown("")
    st.subheader("References:")
    st.markdown("* **Babych, O. (2023)**. *Multi-label NLP: An Analysis of Class Imbalance and Loss Function Approaches*. https://www.kdnuggets.com/2023/03/multilabel-nlp-analysis-class-imbalance-loss-function-approaches.html")
    st.markdown("* **Balmori de la Miyar, J. R., Hoehn‑Velasco, L. & Silverio‑Murillo, A. (2021).** The U‑shaped crime recovery during COVID‑19 evidence from national crime rates in Mexico. *Crime Science*. 10:14. https://doi.org/10.1186/s40163-021-00147-8")
    st.markdown("* **Brownlee, J. (2019)**. *A Gentle Introduction to Cross-Entropy for Machine Learning*. https://machinelearningmastery.com/cross-entropy-for-machine-learning/")
    st.markdown("* **Brownlee, J. (2020).** *Multi-Label Classification with Deep Learning*. https://machinelearningmastery.com/multi-label-classification-with-deep-learning/ ")
    st.markdown("* **Calderón, L. Y., Heinle, K., Kuckertz, R. E., Rodríguez-Ferreira, O. & Shirk, D. A. (eds.) (2021).** *Organized Crime and Violence in Mexico: 2021 Special Report*. Justice in Mexico, University of San Diego. https://justiceinmexico.org/wp-content/uploads/2021/10/OCVM-21.pdf ")
    st.markdown("* **de Carvalho, A.C.P.L.F., Freitas, A.A. (2009)**. A Tutorial on Multi-label Classification Techniques. In: Abraham, A., Hassanien, AE., Snášel, V. (eds) Foundations of Computational Intelligence Volume 5. *Studies in Computational Intelligence*, vol 205. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-01536-6_8")
    st.markdown("* **Felbab-Brown, V. (2019).** *Mexico’s out-of-control criminal market*. Brookings Institution. https://www.brookings.edu/wp-content/uploads/2019/03/FP_20190322_mexico_crime-2.pdf ")
    st.markdown("* **INEGI (2022).** *Encuesta Nacional de Victimización y Percepción sobre Seguridad Pública (ENVIPE) 2022*. https://www.inegi.org.mx/programas/envipe/2022/")
    st.markdown("* **INEGI (2023).** *Catálogo Único de Claves de Áreas Geoestadísticas Estatales, Municipales y Localidades*. https://www.inegi.org.mx/app/ageeml")
    st.markdown("* **Mexico Violence Resource Project (2022).** *Essential Numbers*. UC San Diego’s Center for U.S.-Mexican Studies. https://www.mexicoviolence.org/essential-numbers")
    st.markdown("* **Rollins, J. B. (2015)**. *Metodología Fundamental para la Ciencia de Datos. Somers: IBM Corporation.* https://www.ibm.com/downloads/cas/WKK9DX51")
    st.markdown("* **Tsoumakas, G., & Katakis, I. (2007)**. Multi-label classification: An overview. *International Journal of Data Warehousing and Mining (IJDWM)*, 3(3), 1-13. ")


elif page == "Predict":
    st.subheader(":blue[Socioeconomic & Demographic Profile]")
    st.markdown("Please fill the following fields with the appropriate information (No data is stored whatsoever):")
    HousingClass = st.selectbox("Housing Class:", ["Stand-alone house", "Apartment in building", "Vecindad", "Rooftop room housing", "Premises not built for housing"])
    Kinship = st.selectbox("Kinship regarding the head of the house:", ["Household head", "Spouse", "Child", "Parent", "Other relationship: uncle, nephew, cousin", "No relationship"])
    
