# Prediction of the Probability of Suffering Different Crimes in Mexico
# Author: Daniel Eduardo López
# Github: https://github.com/DanielEduardoLopez
# LinkedIn: https://www.linkedin.com/in/daniel-eduardo-lopez
# Date: 2023/06/03

"""
Project's Brief Description:
Multi-label classification model for predicting the probability of suffering different crimes in Mexico based on the
National Survey of Victimization and Perception of Public Safety (INEGI, 2021).
"""

# Libraries importation
import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
import keras

# Attribute Dictionaries
# Housing Class Attribute Dictionary
housing_class_dict = {
    1: "Stand-alone house",
    2: "Apartment in building",
    3: "Vecindad",
    4: "Rooftop room housing",
    5: "Premises not built for housing"
}

# Kinship Attribute Dictionary
kinship_dict = {
    1: "Household head",
    2: "Spouse",
    3: "Child",
    4: "Parent",
    5: "Other relationship",
    6: "No relationship"
}

# Education Attribute Dictionary
education_dict = {
    0: "None",
    1: "Preschool",
    2: "Elementary",
    3: "Secondary",
    4: "Technical career with finished secondary school",
    5: "Basic normal (with background in secondary)",
    6: "High School",
    7: "Technical career with finished high school",
    8: "Bachelor or professional",
    9: "Master's or PhD",
    99: "Not specified"
}

# Activity Attribute Dictionary
activity_dict = {
    1: "Worker",
    2: "Had a job, but didn't work",
    3: "Looking for a job",
    4: "Student",
    5: "Housekeeper",
    6: "Retired or pensioner",
    7: "Permanently disabled from working",
    8: "Didn't work",
    9: "Not specified",
}

# Job Attribute Dictionary
job_dict = {
    1: "Laborer or pawn",
    2: "Employee or worker",
    3: "Self-employed worker (does not hire workers)",
    4: "Boss or employer (hires workers)",
    5: "Unpaid worker"
}

# Sex Attribute Dictionary
sex_dict = {
    1: "Male",
    2: "Female"
}

# Metropolitan Area Dictionary
metro_area_dict = {
    0:"Not applicable",
    1:"Ciudad de México",
    2:"Guadalajara",
    3:"Monterrey",
    4:"Puebla",
    5:"León",
    6:"La Laguna",
    7:"San Luis Potosí",
    8:"Mérida",
    9:"Chihuahua",
    10:"Tampico",
    12:"Veracruz",
    13:"Acapulco",
    14:"Aguascalientes",
    15:"Morelia",
    16:"Toluca",
    17:"Saltillo",
    18:"Villahermosa",
    19:"Tuxtla Gutiérrez",
    21:"Tijuana",
    24:"Culiacán",
    25:"Hermosillo",
    26:"Durango",
    27:"Tepic",
    28:"Campeche",
    29:"Cuernavaca",
    31:"Oaxaca",
    32:"Zacatecas",
    33:"Colima",
    36:"Querétaro",
    39:"Tlaxcala",
    40:"La Paz",
    41:"Cancún",
    43:"Pachuca"
}

# State Attribute Dictionary
state_dict = {
    1: "Aguascalientes",
    2: "Baja California",
    3: "Baja California Sur",
    4: "Campeche",
    5: "Coahuila",
    6: "Colima",
    7: "Chiapas",
    8: "Chihuahua",
    9: "Ciudad de México",
    10: "Durango",
    11: "Guanajuato",
    12: "Guerrero",
    13: "Hidalgo",
    14: "Jalisco",
    15: "Estado de México",
    16: "Michoacán",
    17: "Morelos",
    18: "Nayarit",
    19: "Nuevo León",
    20: "Oaxaca",
    21: "Puebla",
    22: "Querétaro",
    23: "Quintana Roo",
    24: "San Luis Potosí",
    25: "Sinaloa",
    26: "Sonora",
    27: "Tabasco",
    28: "Tamaulipas",
    29: "Tlaxcala",
    30: "Veracruz",
    31: "Yucatán",
    32: "Zacatecas",
    99: "Not specified"
}

# Month Attribute Dictionary
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "Octocer",
    11: "November",
    12: "December",
    99: "Not specified"
}

# Hour Attribute Dictionary
hour_dict = {
    1: "Morning",
    2: "Afternoon",
    3: "Night",
    4: "Early morning",
    9: "Not specified"
}

# Place Attribute Dictionary
place_dict = {
    1: "In the street",
    2: "At home",
    3: "In the workplace",
    4: "In a business or establishment",
    5: "In a public place",
    6: "In the public transportation",
    7: "In a highway",
    8: "Other",
    9: "Not specified",
}

# Category Attribute Dictionary
category_dict = {
    "U": "Urban",
    "C": "Urban complement",
    "R": "Rural"
}

# Social Class Atribute Dictionary
social_class_dict = {
    1: "Low income",
    2: "Lower middle income",
    3: "Higher middle income",
    4: "High income"
}

# Other Attributes dictionary
other_dict = {
    1: "Yes",
    2: "No",
    3: "Not applicable",
    9: "Not specified"
}

# Functions

def select_metro_area(state):
    """
    Function to return the appropriate metropolitan area according to the input Mexican state.
    :parameter:
    state (String): Input Mexican State

    :returns:
    met_area (String): Metropolitan area
    """

    sel_metro_area_dict = {
        "Ciudad de México":["Ciudad de México", "Not applicable"],
        "Jalisco":["Guadalajara", "Not applicable"],
        "Nuevo León":["Monterrey", "Not applicable"],
        "Puebla":["Puebla", "Not applicable"],
        "Guanajuato":["León", "Not applicable"],
        "Coahuila":["La Laguna","Saltillo", "Not applicable"],
        "San Luis Potosí":["San Luis Potosí", "Not applicable"],
        "Yucatán":["Mérida", "Not applicable"],
        "Chihuahua":["Chihuahua", "Not applicable"],
        "Tamaulipas":["Tampico", "Not applicable"],
        "Veracruz":["Veracruz", "Not applicable"],
        "Guerrero":["Acapulco", "Not applicable"],
        "Aguascalientes":["Aguascalientes", "Not applicable"],
        "Michoacán":["Morelia", "Not applicable"],
        "Estado de México":["Toluca", "Not applicable"],
        "Tabasco":["Villahermosa", "Not applicable"],
        "Chiapas":["Tuxtla Gutiérrez", "Not applicable"],
        "Baja California":["Tijuana", "Not applicable"],
        "Sinaloa":["Culiacán", "Not applicable"],
        "Sonora":["Hermosillo", "Not applicable"],
        "Durango":["Durango", "Not applicable"],
        "Nayarit":["Tepic", "Not applicable"],
        "Campeche":["Campeche", "Not applicable"],
        "Morelos":["Cuernavaca", "Not applicable"],
        "Oaxaca":["Oaxaca", "Not applicable"],
        "Zacatecas":["Zacatecas", "Not applicable"],
        "Colima":["Colima", "Not applicable"],
        "Querétaro":["Querétaro", "Not applicable"],
        "Tlaxcala":["Tlaxcala", "Not applicable"],
        "Baja California Sur":["La Paz", "Not applicable"],
        "Quintana Roo":["Cancún", "Not applicable"],
        "Hidalgo":["Pachuca", "Not applicable"]
    }

    metro_area = sel_metro_area_dict[state]

    return metro_area

def select_mun(state):
    """
    Function to return the appropriate municipality dictionary according to the input Mexican state.

    :parameter:
    state (String): Input Mexican State

    :returns:
    mun_dict (Python dictionary): Dictionary with the municipalities for the input Mexican state
    """

    exc_mun_catalogue_dict = {
        "Ciudad de México":"Ciudad de Mexico",
        "Coahuila":"Coahuila de Zaragoza",
        "Estado de México":"Mexico",
        "Michoacán":"Michoacan de Ocampo",
        "Nuevo León":"Nuevo Leon",
        "San Luis Potosí":"San Luis Potosi",
        "Veracruz":"Veracruz de Ignacio de la Llave",
        "Yucatán":"Yucatan"
    }

    try:
        state = exc_mun_catalogue_dict[state]
    except:
        state = state

    mun_cat = pd.read_csv(
        "https://raw.githubusercontent.com/DanielEduardoLopez/CrimePredictionMX/main/MunicipalitiesCatalogue.csv")

    mun_cat = mun_cat[['NOM_ENT', 'CVE_ENT_MUN', 'NOM_MUN']]

    mun_dict = (mun_cat[mun_cat.NOM_ENT == state].
                         drop(columns=['NOM_ENT']).
                         set_index('CVE_ENT_MUN').
                         to_dict(orient='dict')
                         )

    return mun_dict['NOM_MUN']

def get_encoded_value(value, dictionary):
    """
    Function to return the encoded value of a selected variable according to a provided dictionary.

    :param:
    value (String): Selected value.
    dictionary (Python dictionary): Dictionary containing the selected value and its equivalent encoded value.

    :returns:
    encoded_value (Number): Corresponding encoded value for the input variable.
    """
    encoded_value = [k for k, v in dictionary.items() if v == value]

    if encoded_value:
        return encoded_value[0]
    return None

def get_input_array(sex, age, education, activity, job,
                    social_class, category, housing_class,
                    people_household, kinship, state, metro_area,
                    municipality, month, hour, place):
    """
    Function to transform the encoded values into the input array for the multi-label classification model.

    :param:
    sex (Integer): Sex encoded value.
    age (Integer): Age value.
    education (Integer): Education encoded value.
    activity (Integer): Activity encoded value.
    social_class (Integer): Social class encoded value.
    category (Integer): Category encoded value.
    housing_class (Integer): Housing class encoded value.
    people_household (Integer): Number of persons in the household
    kinship (Integer): Kinship encoded value.
    state (Integer): State encoded value.
    metro_area (Integer): Metropolitan area encoded value.
    municipality (Float): Municipality encoded value.
    month (Integer): Month encoded value.
    hour (Integer): Hour encoded value.
    place (Integer): Place encoded value.

    :returns:
    input_array (Numpy array): Input array for the multi-label classification model.
    """

    # Get encoded values
    sex_encoded = get_encoded_value(sex, sex_dict)
    education_encoded = get_encoded_value(education, education_dict)
    activity_encoded = get_encoded_value(activity, activity_dict)
    job_encoded = get_encoded_value(job, job_dict)
    social_class_encoded = get_encoded_value(social_class, social_class_dict)
    category_encoded = get_encoded_value(category, category_dict)
    housing_class_encoded = get_encoded_value(housing_class, housing_class_dict)
    kinship_encoded = get_encoded_value(kinship, kinship_dict)
    state_encoded = get_encoded_value(state, state_dict)
    metro_area_encoded = get_encoded_value(metro_area, metro_area_dict)
    municipality_encoded = get_encoded_value(municipality, municipality_dict)
    month_encoded = get_encoded_value(month, month_dict)
    hour_encoded = get_encoded_value(hour, hour_dict)
    place_encoded = get_encoded_value(place, place_dict)

    # Encoded values list
    new_row_list = [housing_class_encoded,
                   people_household,
                   kinship_encoded,
                   education_encoded,
                   activity_encoded,
                   job_encoded,
                   sex_encoded,
                   age,
                   metro_area_encoded,
                   month_encoded,
                   state_encoded,
                   municipality_encoded,
                   hour_encoded,
                   place_encoded,
                   category_encoded,
                   social_class_encoded
                   ]

    cols = ["HousingClass",
            "PeopleHousehold",
            "Kinship",
            "Education",
            "Activity",
            "Job",
            "Sex",
            "Age",
            "MetroArea",
            "Month",
            "State",
            "Municipality",
            "Hour",
            "Place",
            "Category",
            "SocialClass"
            ]

    # Definition of a new dataframe with the encoded values
    new_row = pd.DataFrame(np.array(new_row_list).reshape(1, 16),
                           index=["X"], columns=cols)

    # Retrieval of the original dataset and appending of the new row
    path = "https://raw.githubusercontent.com/DanielEduardoLopez/CrimePredictionMX/main/dataset.csv"
    df = pd.read_csv(path)
    df = df[cols]
    df = df.append(new_row)

    # Wrangling of the Municipality attribute
    df["MunicipalityUniqueID"] = df["State"].astype(str) + "." + df["Municipality"].astype(str)
    df["MunicipalityUniqueID"] = df["MunicipalityUniqueID"].astype("Float64")
    df = df.drop(columns="Municipality")

    categorical_attributes = ["HousingClass",
                              "Kinship",
                              "Education",
                              "Activity",
                              "Job",
                              "Sex",
                              "MetroArea",
                              "Month",
                              "State",
                              "MunicipalityUniqueID",
                              "Hour",
                              "Place",
                              "Category",
                              "SocialClass"
                              ]

    # Get dummies
    df = pd.get_dummies(df, columns=categorical_attributes, drop_first=True)

    # Keep only the new raw as a Numpy array
    input_array = df.filter(items=["X"], axis=0).values

    return input_array

@st.cache_resource
def get_model():
    """
    Function to load trained model.

    :return:
    model (Keras object): Trained model ready for making predictions
    """

    with open('CrimePredictorConfig.json') as json_file:
        json_config = json_file.read()
    model = tf.keras.models.model_from_json(json_config)
    model.load_weights('CrimePredictorWeights.h5')

    return model

# Data Sources

# Creating of Municipality Dictionary
mun_cat = pd.read_csv(
        "https://raw.githubusercontent.com/DanielEduardoLopez/CrimePredictionMX/main/MunicipalitiesCatalogue.csv")

mun_cat = mun_cat[['NOM_ENT', 'CVE_ENT_MUN', 'NOM_MUN']]

municipality_dict = (mun_cat.drop(columns=['NOM_ENT']).
                     set_index('CVE_ENT_MUN').
                     to_dict(orient='dict')['NOM_MUN']
                     )


# App

st.title("Prediction of the Probability of Suffering Different Crimes in Mexico")

page = st.sidebar.selectbox("Choose a page", ["Homepage", "Predict"])

# Hompage
if page == "Homepage":
    st.image("https://github.com/DanielEduardoLopez/CrimePredictionMX/blob/main/Images/picture.jpg?raw=true")
    html_picture = '<p style="font-size: 12px">Image Credit: <a href="https://pixabay.com/photos/police-line-yellow-crime-cemetery-3953745/">ValynPi14</a></p>'
    st.markdown(html_picture, unsafe_allow_html=True)
    st.markdown("#### By Daniel Eduardo López (2023/05/31)")
    url_github = "https://github.com/DanielEduardoLopez"
    url_linkedin = "https://www.linkedin.com/in/daniel-eduardo-lopez"
    st.write("[LinkedIn](%s)" % url_linkedin)
    st.write("[GitHub](%s)" % url_github)
    st.header(":blue[Welcome!]")
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

# Predict Page
elif page == "Predict":
    st.subheader(":blue[Socioeconomic & Demographic Profile]")
    st.markdown("Please fill the following fields with the appropriate information (No data is stored whatsoever):")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        # Select boxes in app
        sex = st.selectbox("Sex:", list(sex_dict.values()))
        age = st.selectbox("Age:", list(range(15, 100)))
        education = st.selectbox("Education:", list(education_dict.values()))
        activity = st.selectbox("Activity:", list(activity_dict.values()))
        job = st.selectbox("Job:", list(job_dict.values()))
        social_class = st.selectbox("Social Class:", list(social_class_dict.values()))
        category = st.selectbox("Geographical Category:", list(category_dict.values()))
        housing_class = st.selectbox("Housing Class:", list(housing_class_dict.values()))


    with col2:
        # Select boxes in app
        people_household = st.selectbox("Number of persons living in the household:", list(range(1, 31)))
        kinship = st.selectbox("Kinship regarding the head of the house:", list(kinship_dict.values()))
        state = st.selectbox("State:", list(state_dict.values()))
        metro_area = st.selectbox("Metropolitan Area:", sorted(select_metro_area(state)))
        municipality = st.selectbox("Municipality:", sorted(list(select_mun(state).values())))
        month = st.selectbox("Month:", list(month_dict.values()))
        hour = st.selectbox("Hour:", list(hour_dict.values()))
        place = st.selectbox("Place:", list(place_dict.values()))


    st.markdown("")
    st.markdown("")
    st.subheader(":blue[Prediction Results]")
    st.markdown("According to the provided socioeconomic and demographic data, the probability of suffering different crimes in Mexico is as follows:")

    if st.button('Predict Probability'):
        # Get input array from user's input
        input_array = get_input_array(sex, age, education, activity, job,
                                social_class, category, housing_class,
                                people_household, kinship, state, metro_area,
                                municipality, month, hour, place)

        # Model
        model = get_model()

        # Prediction
        Y = model.predict(input_array)

        st.success(Y)
