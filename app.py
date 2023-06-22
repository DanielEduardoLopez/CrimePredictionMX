# Prediction of the Probability of Suffering Different Crimes in Mexico
# Author: Daniel Eduardo López
# Github: https://github.com/DanielEduardoLopez
# LinkedIn: https://www.linkedin.com/in/daniel-eduardo-lopez
# Date: 2023/06/17

"""
Project's Brief Description:
Multi-label classification model for predicting the probability of suffering different crimes in Mexico based on the
National Survey of Victimization and Perception of Public Safety (INEGI, 2021) using Python and Tensorflow.
"""

# Libraries importation
import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import streamlit as st
from tensorflow.keras.models import model_from_json
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Crime Predictor",
    page_icon="🇲🇽",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/daniel-eduardo-lopez',
        'Report a bug': "https://www.linkedin.com/in/daniel-eduardo-lopez",
        'About': "Multi-label classification model in Python for predicting the probability of suffering different crimes in Mexico."
    }
)

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
    4: "Technical with secondary school",
    5: "Basic normal",
    6: "High School",
    7: "Technical with high school",
    8: "Bachelor or professional",
    9: "Master's or PhD",
    99: "Not specified"
}

# Activity Attribute Dictionary
activity_dict = {
    1: "Worker",
    2: "Had a job but didn't work",
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
    3: "Self-employed worker",
    4: "Boss or employer",
    5: "Unpaid worker",
    9: "Not specified",
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

# Function to select metropolitan area
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

# Function to load the municipalities from serialized file
@st.cache_data
def get_municipalities():
    """
    Function to load the Mexican municipalities catalogue from the JSON file.
    :return:

    municipalities_df (Pandas dataframe): Dataframe with the Mexican municipalities and their IDs.
    """

    municipalities_df = (pd.read_json("MexicanMunicipalitiesCatalogue.json", orient='index', typ='frame',
                                  convert_axes=False, convert_dates=False).
                      reset_index().rename(columns={"index":"Key", 0:"MunState"}))

    municipalities_df = (pd.concat([municipalities_df, municipalities_df.MunState.str.split(', ', expand=True)], axis=1).
                         rename(columns={0: "Municipality", 1: "State"}).
                         drop(columns=["MunState", 2]).set_index("Key"))

    return municipalities_df

# Function to select the municipality
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

    mun_cat = get_municipalities()

    mun_dict = (mun_cat[mun_cat.State == state].
                         drop(columns=['State']).
                         to_dict(orient='dict')
                         )

    return mun_dict['Municipality']

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

# Function to load the encoders states from serialized file
@st.cache_data
def get_encoders():
    """
    Function to retrieve and load the encoders states into the app from the JSON file.
    :return:
    encoders (Python dict): Dictionary with the ordered categories arrays for each predictor.
    """

    # Retrieval of the encoders states

    with open("Encoders.json", "r") as read_file:
        encoders = json.load(read_file)

    return encoders

# Function to load the scalers max values from serialized file
@st.cache_data
def get_scalers():
    """
    Function to retrieve and load the scalers maximum values into the app from the JSON file.
    :return:
    scalers (Python dict): Dictionary with the maximum values for each predictor.
    """

    with open("Scalers.json", "r") as read_file:
        scalers = json.load(read_file)

    return scalers

# Function to craft the input array for the model
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

    # Scaling of numerical predictors
    scalers = get_scalers()

    people_household_sc = people_household / scalers["people_housing"]
    age_sc = age / scalers["age"]

    # Encoded values list
    new_row = np.array([people_household_sc,
                       age_sc,
                       housing_class_encoded,
                       kinship_encoded,
                       education_encoded,
                       activity_encoded,
                       job_encoded,
                       sex_encoded,
                       metro_area_encoded,
                       month_encoded,
                       state_encoded,
                       municipality_encoded,
                       hour_encoded,
                       place_encoded,
                       category_encoded,
                       social_class_encoded,
                       ]).reshape(1, 16)


    encoders = get_encoders()

    encoder_housing_class = OneHotEncoder(categories=encoders["housing_class"], handle_unknown="ignore", sparse_output=False)
    encoder_kinship = OneHotEncoder(categories=encoders["kinship"], handle_unknown="ignore", sparse_output=False)
    encoder_education = OneHotEncoder(categories=encoders["education"], handle_unknown="ignore", sparse_output=False)
    encoder_activity = OneHotEncoder(categories=encoders["activity"], handle_unknown="ignore", sparse_output=False)
    encoder_job = OneHotEncoder(categories=encoders["job"], handle_unknown="ignore", sparse_output=False)
    encoder_sex = OneHotEncoder(categories=encoders["sex"], handle_unknown="ignore", sparse_output=False)
    encoder_metro_area = OneHotEncoder(categories=encoders["metro_area"], handle_unknown="ignore", sparse_output=False)
    encoder_month = OneHotEncoder(categories=encoders["month"], handle_unknown="ignore", sparse_output=False)
    encoder_state = OneHotEncoder(categories=encoders["state"], handle_unknown="ignore", sparse_output=False)
    encoder_municipality = OneHotEncoder(categories=encoders["municipality"], handle_unknown="ignore", sparse_output=False)
    encoder_hour = OneHotEncoder(categories=encoders["hour"], handle_unknown="ignore", sparse_output=False)
    encoder_category = OneHotEncoder(categories=encoders["place"], handle_unknown="ignore", sparse_output=False)
    encoder_place = OneHotEncoder(categories=encoders["category"], handle_unknown="ignore", sparse_output=False)
    encoder_social_class = OneHotEncoder(categories=encoders["social_class"], handle_unknown="ignore", sparse_output=False)

    ct = ColumnTransformer(
        [('pass0', 'passthrough', [0]),
         ('pass1', 'passthrough', [1]),
         ('encoder_housing_class', encoder_housing_class, [2]),
         ('encoder_kinship', encoder_kinship, [3]),
         ('encoder_education', encoder_education, [4]),
         ('encoder_activity', encoder_activity, [5]),
         ('encoder_job', encoder_job, [6]),
         ('encoder_sex', encoder_sex, [7]),
         ('encoder_metro_area', encoder_metro_area, [8]),
         ('encoder_month', encoder_month, [9]),
         ('encoder_state', encoder_state, [10]),
         ('encoder_municipality', encoder_municipality, [11]),
         ('encoder_hour', encoder_hour, [12]),
         ('encoder_category', encoder_place, [13]),
         ('encoder_place', encoder_category, [14]),
         ('encoder_social_class', encoder_social_class, [15])
         ],
        remainder='passthrough'
    )

    input_array = ct.fit_transform(new_row).astype(np.float64)

    return input_array

# Function to load the model into the app from the serialized files
@st.cache_resource
def get_model():
    """
    Function to load the trained model from serialized files.

    :return:
    model (Keras object): Trained model ready for making predictions
    """

    with open('CrimePredictorConfig.json') as json_file:
        json_config = json_file.read()
    model = model_from_json(json_config)
    model.load_weights('CrimePredictorWeights.h5')

    return model

# Function to convert the output array from the model into a pandas dataframe
def get_df(array):
    """
    Function to cast the output array from the multi-layer perceptron model into a Pandas dataframe.

    :parameter:
    array (tensor): Output probabilities array from the multi-layer perceptron model.

    :return:
    df (Pandas dataframe): Dataframe with the probabilities and complement of suffering a crime in Mexico.
    """
    # Labels names
    labels = ["Total Vehicle Theft",
            "Partial Vehicle Theft",
            "Vandalism",
            "Burglary",
            "Kidnapping",
            "Enforced Disappearance",
            "Murder",
            "Theft",
            "Other Theft",
            "Bank Fraud",
            "Consumer Fraud",
            "Extortion",
            "Threats",
            "Injuries",
            "Kidnapping",
            "Assault",
            "Rape",
            "Other",
            "Overall"]

    df = pd.DataFrame(np.array(array).reshape(1, 19), columns=labels)

    df = pd.melt(df, var_name="Crime", value_name="Suffer a Crime")

    df["Not Suffer a Crime"] = 1 - df["Suffer a Crime"]

    df = pd.melt(df, id_vars="Crime", var_name="Event", value_name="Value")

    return df

# Function to plot a donut chart
def plot_pie_chart(df):
    """
    Function to plot the overall probability of suffering any crime in Mexico.

    :parameter:
    df (Pandas dataframe): Dataframe with the probabilities and the complement of suffering crimes in Mexico.

    :return:
    pie_chart (Plotly object): Plotly pie chart.
    """
    font_size = 16
    title_font_size = 20

    pie_colors = ['#5fbbff', 'silver']

    pie_chart = px.pie(df[df['Crime'] == 'Overall'].sort_values(by="Event", ascending=False),
                       values='Value',
                       names='Event',
                       color='Event',
                       hole=0.7,
                       opacity=0.9,
                       color_discrete_sequence=px.colors.sequential.Blues_r,
                       #title='Probability of Suffering Any Crime',
                       width=550,
                       )
    pie_chart.update_traces(hoverinfo='label+percent+name', textinfo='percent', textfont_size=font_size,
                            marker=dict(colors=pie_colors, line=dict(color="rgba(0,0,0,0)", width=4)))
    pie_chart.update_layout(#title_x=0.2, title_y=0.99,
                            margin={"b": 5},
                            paper_bgcolor="rgba(0,0,0,0)",
                            plot_bgcolor="rgba(0,0,0,0)",
                            autosize=True,
                            dragmode=False,
                            #title=dict(font_color='white', font_size=title_font_size),
                            legend=dict(font_color='white',
                                        font_size=font_size,
                                        yanchor="top",
                                        y=1.28,
                                        xanchor="left",
                                        x=0.01
                                        )
                            )

    return pie_chart

# Function to plot a bar chart
def plot_bar_chart(df):
    """
    Function to plot the probabilities of suffering different crimes in Mexico.

    :parameter:
    df (Pandas dataframe): Dataframe with the probabilities and the complement of suffering crimes in Mexico.

    :return:
    bar_chart (Plotly object): Plotly bar chart.
    """
    font_size = 15
    title_font_size = 20

    bar_colors = ['silver',] * 20
    bar_colors.insert(17, '#5fbbff')

    df['Value'] = df['Value'] * 100

    bar_chart = px.bar(df[(df['Crime'] != "Overall") & (df["Event"] == "Suffer a Crime")].sort_values(by = "Value", ascending=True),
                        x='Value', y='Crime',
                        height=450,
                        width=450,
                        color='Value', color_continuous_scale=bar_colors,
                        #title='Probability of Suffering Different Crimes',
                        opacity=0.9,
                        )
    bar_chart.update_traces(marker_color=bar_colors, marker_line_color='#06477D', textfont_size=16, textangle=0,
                                    textposition="outside", cliponaxis=False, hovertemplate=None)
    bar_chart.update_layout(#title_x=0.1,
                            margin={"r": 0, "t": 0, "l": 0, "b": 0},
                            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                            xaxis_ticksuffix="%", autosize=True,
                            dragmode=False,
                            yaxis=dict(tickfont=dict(size=font_size),
                                       ),
                            xaxis=dict(tickfont=dict(size=font_size),
                                       showgrid=True),
                            font=dict(
                                size=font_size
                                      ),
                            yaxis_title=None,
                            #title=dict(font_color='white', font_size=title_font_size),
                            legend=dict(font_color='white',
                                        font_size=font_size),

                            )
    bar_chart.update_xaxes(title="Probability", title_font_size=font_size+1)
    bar_chart.update_yaxes(title_font_size=font_size+1)

    return bar_chart


# Creating of the Municipality Dictionary
mun_cat = get_municipalities()
municipality_dict = mun_cat.drop(columns=['State']).to_dict(orient='dict')['Municipality']


# Disabling fullscreen view for images in app
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)

# Disabling displayModeBar in Plotly Charts
config = {'displayModeBar': False}

# App

st.title("Prediction of the Probability of Suffering Different Crimes in Mexico")

# Defining page to display
if "app_page" not in st.session_state:
    page = "Predict"
else:
    page = st.session_state["app_page"]

# Side bar
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("**About me and this project:**")
col1, col2 = st.sidebar.columns([0.3, 0.7], gap="small")
with col1:
    st.markdown("")
    st.image("Picture.jpg")

with col2:
    st.markdown("Hi! I'm Eduardo, engineer specialized in data science. The thing I enjoy the most is working with data and people.  ")

st.sidebar.markdown("I love learning, and this is a personal project to play with deep learning and model deployment. :computer:")
st.sidebar.markdown("Please don't take the predictions from this app so seriously. This is not intended to provide super accurate results.")

# Homepage
if page == "Homepage":

    # Header information
    col1, col2 = st.columns([0.1, 0.9], gap="small")

    with col1:
        st.image("Picture.jpg")

    with col2:
        st.markdown('##### :blue[Daniel Eduardo López]')
        html_contact = '<a href="https://github.com/DanielEduardoLopez">GitHub</a> | <a href="https://www.linkedin.com/in/daniel-eduardo-lopez">LinkedIn</a>'
        st.caption(html_contact, unsafe_allow_html=True)

    st.markdown("June 21, 2023")
    st.caption("5 min read")
    st.image("police-line-picture.jpg")
    html_picture = '<p style="font-size: 12px" align="center">Image Credit: <a href="https://pixabay.com/photos/police-line-yellow-crime-cemetery-3953745/">ValynPi14</a> from <a href="https://pixabay.com">Pixabay</a>.</p>'
    st.caption(html_picture, unsafe_allow_html=True)

    # Introduction    
    st.header(":blue[Welcome!]")
    st.markdown("Since the 2000's, Mexico has experienced a sustained increase in crime and violence due to both criminal organizations and common criminals. In this sense, crime has become **the top concern for the overall population** (Calderón, Heinle, Kuckertz, Rodríguez-Ferreira & Shirk, 2021).")
    st.markdown("Some of the reasons for such a spread of crime and violence are the purposeful fragmentation of the criminal groups by the Mexican government, the consequent increase on competition and diversification among criminal organizations, a rampant corruption within the Mexican institutions, ineffective socio-economic policies, widespread impunity and low effective prosecution rates, and the alienation of local populations to criminals (Felbab-Brown, 2019).")
    st.markdown("In this context, it has been estimated that the crime rate was of 94.1 per 100,000 inhabitants before the COVID-19 lockdown in Mexico (Balmori de la Miyar, Hoehn‑Velasco & Silverio‑Murillo, 2021).")
    st.markdown("However, the distribution of crime and violence is **uneven accross the country**. Thus, it is desirable to know how likely is suffering a crime based on the **demographic and socio-economic profile of a given household/person**, rather than just sticking to national or regional averages.")
    st.markdown("Even though official crime data exists within the country, it has been estimated that the percentage of unreported crimes was of about 93.3% in 2020 (Mexico Violence Resource Project, 2022). In order to address this issue, the :blue[**National Survey of Victimization and Perception of Public Safety**] (ENVIPE, by its acronym in Spanish) has been develop as a tool to gather **representative data** about the levels of crime incidence and unreported crimes -the so-called *cifra negra*- (INEGI, 2021).")
    st.markdown("Therefore, the ENVIPE data was used to train **a multi-label classification model** (Babych, 2023; Brownlee, 2020; Tsoumakas & Katakis, 2007) for the following crimes:")
    st.markdown("1. Total vehicle theft\n2. Partial vehicle theft\n3. Vandalism\n4. Burglary\n5. Kidnapping\n6. Enforced disappearance\n7. Murder\n8. Theft\n9. Other thefts\n10. Bank fraud\n11. Other frauds\n12. Extortion\n13. Threats\n14. Injuries\n15. Assault\n16. Rape\n17. Other crimes\n18. Any crime")
    st.markdown("This, in order to have **a more accurate estimation of the probability of suffering different crimes** in Mexico, according to :blue[**specific demographic and socio-economic profiles**].")
    st.markdown("")

    # Model brief description
    st.subheader(":blue[Model]")
    st.markdown("Based on all the observations gathered by the ENVIPE, :blue[**a multi-layer perceptron**] was built and trained using Python and Tensorflow, achieving about **67.3%** of **precision**, about **64.9%** of **recall**, a **F1 score** of about **65.8%**, and a **ROC AUC** of about **63.9%**.")
    url_repository = "https://github.com/DanielEduardoLopez/CrimePredictionMX"
    st.write("All the technical details can be found at [GitHub](%s)." % url_repository)
    st.markdown("Thus, the resulting model had an OK performance with some opportunity for improvement though. Please don't take its predictions so seriously :wink:")
    st.markdown("According to the developed model, **the probability of suffering any crime in Mexico was 83.9%**, which was very close to the actual figure of 82.2% from the ENVIPE.")
    st.markdown('Please go the :orange[**_Predict_**] page to play with the model. :blush:')

    bcol1, bcol2, bcol3 = st.columns([1, 1, 1])

    with bcol2:
        if st.button('Go to Predict Page'):
            st.session_state["app_page"] = "Predict"
            st.experimental_rerun()

    st.markdown("")

    # References
    st.subheader(":blue[References]")
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

    # Brief description of the app
    url_repository = "https://github.com/DanielEduardoLopez/CrimePredictionMX"
    st.write('Uses a neural network trained on the <i>National Survey of Victimization and Perception of Public Safety</i> (INEGI, 2022) to predict crime probabilities. Check out the code [here](%s) and more details at the <h style="color:orange;"><i><b>Homepage</b></i></h>. Please do not take the predictions from this app so seriously. 😉' % url_repository, unsafe_allow_html=True)

    bcol1, bcol2, bcol3 = st.columns([1, 1, 1])

    with bcol2:
        if st.button('Go to Homepage'):
            st.session_state["app_page"] = "Homepage"
            st.experimental_rerun()

    # Input data section
    st.markdown("")
    st.subheader(":blue[Socioeconomic & Demographic Profile]")
    st.markdown("Please fill the following fields with the appropriate information (No data is stored :innocent:):")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        # Select boxes in app
        sex = st.selectbox("**Gender:**", list(sex_dict.values()))
        age = st.selectbox("**Age:**", list(range(15, 100)))
        education = st.selectbox("**Education Level:**", list(education_dict.values()))
        activity = st.selectbox("**Current Employment Status:**", list(activity_dict.values()))
        job = st.selectbox("**Job Position:**", list(job_dict.values()), help="If you don't have a job, please select 'Not specified'.")
        social_class = st.selectbox("**Social Class:**", list(social_class_dict.values()), help="Socioeconomic status defined by your income, occupation and expenditure patterns.")
        category = st.selectbox("**Type of Populated Area:**", ['Urban', 'Rural'], help="Urban or Rural.")



    with col2:
        # Select boxes in app
        housing_class = st.selectbox("**Housing Type:**", list(housing_class_dict.values()), help="Description of the building used for living.")
        people_household = st.selectbox("**Number of Persons Living in the Household:**", list(range(1, 31)))
        kinship = st.selectbox("**Kinship Regarding the Head of the Household:**", list(kinship_dict.values()))
        state = st.selectbox("**Mexican State of Residence:**", list(state_dict.values()))
        metro_area = st.selectbox("**Metropolitan Area of Residence:**", sorted(select_metro_area(state)), help="If you don't live in any of the options, please select 'Not applicable'")
        municipality = st.selectbox("**Municipality of Residence:**", sorted(list(select_mun(state).values())))
        #month = st.selectbox("Month:", list(month_dict.values()))
        hour = st.selectbox("**Hour of the Day:**", list(hour_dict.values()))
        #place = st.selectbox("Place:", list(place_dict.values()))
        month = 99
        place = 9


    st.markdown("")
    st.markdown("")

    # Results section

    bcol1, bcol2, bcol3 = st.columns([1, 1, 1])

    st.session_state["flag_charts"] = 1

    with bcol2:
        if st.button('Predict Probability :nerd_face:'):
            # Get input array from user's input
            input_array = get_input_array(sex, age, education, activity, job,
                                        social_class, category, housing_class,
                                        people_household, kinship, state, metro_area,
                                        municipality, month, hour, place)
            # Model
            model = get_model()

            # Prediction
            Y = model.predict(input_array)
            st.success("Success! Please scroll down...")
            st.session_state["flag_charts"] = 2


    if st.session_state["flag_charts"] == 1:
        pass

    elif st.session_state["flag_charts"] == 2:

        # Charts sections
        st.subheader(":blue[Prediction Results]")
        st.markdown("According to the provided socioeconomic and demographic data, the probability of suffering different crimes in Mexico is as follows: :bar_chart:")
        st.markdown("")
        st.markdown("")

        df = get_df(Y)
        pie_chart = plot_pie_chart(df)
        bar_chart = plot_bar_chart(df)

        # Pie chart
        bcol1, bcol2, bcol3 = st.columns([0.1, 0.8, 0.1])
        with bcol2:
            st.markdown('<p style="font-size: 22px" align="center"><b>Overall Probability of Suffering Any Crime in Mexico</b></p>', unsafe_allow_html=True)
            st.plotly_chart(pie_chart, config=config, use_container_width=True)
        st.markdown("Don't freak out if you get 100% or so. Everyone is exposed to suffer a crime in Mexico in their lifetime. Petty crimes most likely.")
        st.markdown("")
        st.markdown("")

        # Bar chart
        bcol1, bcol2, bcol3 = st.columns([0.1, 0.8, 0.1])
        with bcol2:
            st.markdown(
                '<p style="font-size: 22px" align="center"><b>Probability of Suffering Different Crimes in Mexico</b></p>',
                unsafe_allow_html=True)
            st.plotly_chart(bar_chart, config=config, use_container_width=True)

        # Crimes description
        st.markdown("#### **Crimes Description**")
        st.markdown(
            ":blue[**- Assault**:] Sexual harassment or intimidation, groping, indecent exposure, or attempted rape.")
        st.markdown(":blue[**- Bank Fraud:**] Use of illegal means to get money from bank depositors.")
        st.markdown(":blue[**- Burglary**:] Illegal enter into a house to commit theft.")
        st.markdown(":blue[**- Consumer Fraud**:] Intentional deception to secure unfair or unlawful gain.")
        st.markdown(":blue[**- Enforced Disappearance**:] Abduction of a household member with unknown whereabouts.")
        st.markdown(":blue[**- Extortion**:] Practice of obtaining an illegal benefit through coercion.")
        st.markdown(":blue[**- Injury**:] Harm done to a person.")
        st.markdown(":blue[**- Kidnapping**:] Unlawful abduction and confinement of a household member against their will.")
        st.markdown(":blue[**- Murder**:] Unlawful killing without justification of a household member.")
        st.markdown(":blue[**- Other**:] Other crimes.")
        st.markdown(":blue[**- Other Theft**:] Robbery in a different form.")
        st.markdown(":blue[**- Partial Vehicle Theft**:] Criminal act of stealing parts of a motor vehicle.")
        st.markdown(":blue[**- Rape**:] Sexual assault involving sexual intercourse carried out against a person without their consent.")
        st.markdown(":blue[**- Theft**:] Act of taking another person's property without that person's consent.")
        st.markdown(":blue[**- Threats**:] Crime of intentionally putting another person in fear of bodily or mental injury.")
        st.markdown(":blue[**- Vandalism**:] Deliberate destruction of or damage to the household.")
        st.markdown(":blue[**- Vehicle Theft**:] Criminal act of stealing a complete motor vehicle.")
        st.session_state["flag_charts"] = 1
