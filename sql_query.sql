-- Query to generate dataset
SELECT 
tvivienda.AP1_1 AS 'HousingClass', -- Tipo de vivienda / Housing type
thogar.TOT_PER AS 'PeopleHousehold', -- Número de personas viviendo en la vivienda / Number of people living in the home
tsdem.PAREN AS 'Kinship', -- Parentesco con el jefe del hogar /  Relationship with the head of the household
tsdem.NIV AS 'Education', -- Educación / Education
tsdem.AP3_8 AS 'Activity', -- Actividad / Activity
tsdem.AP3_10 AS 'Job', -- Trabajo / Job
tmod_vic.BPCOD AS 'Crime', -- Tipo de delito / Type of crime
tmod_vic.SEXO AS 'Sex', -- Género / Sex
tmod_vic.EDAD AS 'Age', -- Edad / Age
tmod_vic.AREAM_OCU AS 'MetroArea', -- Area metropolitana de ocurrencia del delito / Metropolitan area of occurrence of the crime
tmod_vic.BP1_1 AS 'Month', -- Mes de ocurrencia del delito / Month of occurrence of the crime
tmod_vic.BP1_2C AS 'State', -- Estado de ocurrencia del delito / State of occurrence of the crime
tmod_vic.BP1_3C AS 'Municipality', -- Municipio de ocurrencia del delito / Municipality of occurrence of the crime
tmod_vic.BP1_4 AS 'Hour', -- Hora de ocurrencia del delito / Crime occurrence time
tmod_vic.BP1_5 AS 'Place', -- Lugar de ocurrencia del delito / Place of occurrence of the crime
tmod_vic.DOMINIO AS 'Category', -- Urbano/Rural / Urban/Rural
tmod_vic.ESTRATO AS 'SocialClass', -- Estrato socioeconómico / Socioeconomic stratum
tper_vic1.AP4_1 AS 'InhabitingTime', -- Tiempo habitando en la vivienda / Time living in the house
tper_vic1.AP4_10_01 AS 'StopGoingOutNight', -- Dejar de salir de noche por temor a ser víctima / Stop going out at night for fear of being a victim
tper_vic1.AP4_10_02 AS 'StopChildrenAlone', -- Dejar de permitir a menores salir solos por temor a ser víctima / Stop allowing minors to go out alone for fear of being a victim
tper_vic1.AP4_10_03 AS 'StopVisitingFamily', -- Dejar de visitar parientes o amigos por temor a ser víctima / Stop visiting relatives or friends for fear of being a victim
tper_vic1.AP4_10_04 AS 'StopTakingTaxis', -- Dejar de tomar taxi por temor a ser víctima / Stop taking a taxi for fear of being a victim
tper_vic1.AP4_10_05 AS 'StopTakingPublicTransit', -- Dejar de usar transporte público por temor a ser víctima / Stop using public transport for fear of being a victim
tper_vic1.AP4_10_06 AS 'StopCarryingCash', -- Dejar de llevar dinero en efectivo por temor a ser víctima / Stop carrying cash for fear of being a victim
tper_vic1.AP4_10_07 AS 'StopGoingSchool', -- Dejar de ir a la escuela por temor a ser víctima / Stop going to school for fear of being a victim
tper_vic1.AP4_10_08 AS 'StopGoingCinema', -- Dejar de ir al cine o teatro por temor a ser víctima / Stop going to the movies or theater for fear of being a victim
tper_vic1.AP4_10_09 AS 'StopWalking', -- Dejar de salir a caminar por temor a ser víctima / Stop going for a walk for fear of being a victim
tper_vic1.AP4_10_10 AS 'StopWearingJewels', -- Dejar de usar joyas por temor a ser víctima / Stop wearing jewelry for fear of being a victim
tper_vic1.AP4_10_11 AS 'StopEatingOut', -- Dejar de salir a comer o cenar por temor a ser víctima / Stop going out for lunch or dinner for fear of being a victim
tper_vic1.AP4_10_12 AS 'StopCreditCard', -- Dejar de llevar tarjeta de crédito o débito por temor a ser víctima / Stop carrying a credit or debit card for fear of being a victim
tper_vic1.AP4_10_13 AS 'StopStadium', -- Dejar de ir al estadio por temor a ser víctima / Stop going to the stadium for fear of being a victim
tper_vic1.AP4_10_14 AS 'StopSupermart', -- Dejar de frecuentar centros comerciales por temor a ser víctima / Stop going to shopping malls for fear of being a victim
tper_vic1.AP4_10_15 AS 'StopHighways', -- Dejar de viajar por carretera por temor a ser víctima / Stop traveling by road for fear of being a victim
tper_vic1.AP4_10_16 AS 'StopMobilePhones', -- Dejar de llevar teléfono móvil o celular por temor a ser víctima / Stop carrying a mobile or cell phone for fear of being a victim
tper_vic1.AP4_11_01 AS 'ProtectionDoorsWindows', -- Medidas de protección contra delincuencia: cambiar puertas o ventanas / Crime protection measures: changing doors or windows
tper_vic1.AP4_11_02 AS 'ProtectionLocks', -- Medidas de protección contra delincuencia: cambiar o colocar cerraduras y/o candados / Crime Protection Measures: change or place locks and/or padlocks
tper_vic1.AP4_11_03 AS 'ProtectionFences', -- Medidas de protección contra delincuencia: colocar o reforzar rejas o bardas / Crime Protection Measures: place or reinforce bars or fences
tper_vic1.AP4_11_04 AS 'ProtectionAlarmsVideo', -- Medidas de protección contra delincuencia: instalar alarmas y/o videocámaras de vigilancia / Crime Protection Measures: install alarms and/or surveillance video cameras
tper_vic1.AP4_11_05 AS 'ProtectionPrivateSurveillance', -- Medidas de protección contra delincuencia: contratar vigilancia privada en la calle o colonia / Crime Protection Measures: hire private surveillance in the street or neighborhood
tper_vic1.AP4_11_06 AS 'ProtectionNeighbors',	-- Medidas de protección contra delincuencia: realizar acciones conjuntas con sus vecinos / Crime Protection Measures: carry out joint actions with your neighbors
tper_vic1.AP4_11_07 AS 'ProtectionInsurance', -- Medidas de protección contra delincuencia: contratar seguros / Crime Protection Measures: take out insurance
tper_vic1.AP4_11_08 AS 'ProtectionDog', -- Medidas de protección contra delincuencia: comprar un perro guardián / Crime Protection Measures: Buying a Watchdog
tper_vic1.AP4_11_09 AS 'ProtectionWeapons', -- Medidas de protección contra delincuencia: adquirir armas de fuego / Crime Protection Measures: acquiring firearms
tper_vic1.AP4_11_10 AS 'ProtectionMoving', -- Medidas de protección contra delincuencia: cambiarse de vivienda o lugar de residencia / Crime Protection Measures: changing your home or place of residence
tper_vic1.AP4_11_11 AS 'ProtectionOther', -- Medidas de protección contra delincuencia: Otra medida / Crime Protection Measures: Other measure
tper_vic1.AP4_12 AS 'ProtectionExpenses', -- Gastos en protección contra delincuencia / Expenses in protection against crime
tper_vic2.AP6_1_1 AS 'Automobiles', -- Hogar propietario de automóvil, camioneta o camión / Car, van or truck owner household
tper_vic2.AP6_1_2 AS 'NumberAutomobiles', -- Número de vehículos (automóviles, camionetas o camiones) propiedad del hogar / Number of vehicles (cars, vans, or trucks) owned by the household
tper_vic2.AP6_4_01 AS 'CrimeVehicleTheft', -- Hogar víctima de robo total de vehículo / Home victim of total vehicle theft
tper_vic2.AP6_6_01 AS 'NumberVehicleThefts', -- Número de veces hogar víctima de robo total vehículo / Number of times home victim of total vehicle theft
tper_vic2.AP6_4_02 AS 'CrimePartialVehicleTheft', -- Hogar víctima de robo parcial de vehículo / Home victim of partial vehicle theft
tper_vic2.AP6_6_02 AS 'NumberPartialVehicleThefts', -- Número de veces hogar víctima de robo parcial vehículo / Number of times home victim of partial vehicle theft
tper_vic2.AP6_4_03 AS 'CrimeVandalism', -- Hogar víctima de grafiti o vandalismo / Home victim of graffiti or vandalism
tper_vic2.AP6_6_03 AS 'NumberVandalisms', -- Número de veces hogar víctima de grafiti o vandalismo / Number of times home victim of graffiti or vandalism
tper_vic2.AP6_4_04 AS 'CrimeBurglary', -- Hogar víctima de robo a casa-habitación / Home victim of home-room robbery
tper_vic2.AP6_6_04 AS 'NumberBurglaries', -- Número de veces hogar víctima de robo a casa-habitación / Number of times home victim of burglary
-- tper_vic2.AP6_9 AS 'CrimeKidnappingPrior2021', -- Hogar víctima de secuestro antes de 2021 / Household victim of kidnapping before 2021
-- tper_vic2.AP6_10_1 AS 'CrimeKidnapping2021',  -- Hogar víctima de secuestro 2021 / Home Victim of Kidnapping 2021
IF(tper_vic2.AP6_9 = 1 OR tper_vic2.AP6_10_1 = 1, 1, 2) AS 'CrimeHouseholdKidnapping', -- Hogar víctima de secuestro / Household victim of kidnapping
tper_vic2.AP6_10_2 AS 'NumberFamilyKidnappings', -- Número de integrantes víctimas de secuestro / Number of members victims of kidnapping
-- tper_vic2.AP6_14 AS 'CrimeEnforcedDisappearancePrior2021', -- Hogar víctima de desaparición forzada antes de 2021 / Household victim of enforced disappearance before 2021
-- tper_vic2.AP6_15_1 AS 'CrimeEnforcedDisappearance2021', -- Hogar víctima de desaparición forzada 2021 / Household victim of enforced disappearance 2021
IF(tper_vic2.AP6_14 = 1 OR tper_vic2.AP6_15_1 = 1, 1, 2) AS 'CrimeHouseholdEnforcedDisappearance', -- Hogar víctima de desaparición forzada / Household victim of enforced disappearance
tper_vic2.AP6_15_2 AS 'NumberFamilyEnforcedDisappearances', -- Número de integrantes víctimas de desaparición forzada / Number of members victims of forced disappearance
-- tper_vic2.AP6_19 AS 'CrimeMurderPrior2021', -- Hogar víctima de homicidio antes de 2021 / Household victim of homicide before 2021
-- tper_vic2.AP6_20_1 AS 'CrimeMurder2021', -- Hogar víctima de homicidio 2021 / Household victim of homicide 2021
IF(tper_vic2.AP6_19 = 1 OR tper_vic2.AP6_20_1 = 1, 1, 2) AS 'CrimeHouseholdMurder', -- Hogar víctima de homicidio / Household victim of homicide
tper_vic2.AP6_20_2 AS 'NumberMurders', -- Número de integrantes víctimas de homicidio / Number of members victims of homicide
tper_vic2.AP7_3_05 AS 'CrimeTheft', -- Víctima de robo o asalto / Robbery or assault victim
tper_vic2.AP7_4_05 AS 'NumberThefts', -- Número de veces víctima de robo o asalto / Number of times victim of robbery or assault
tper_vic2.AP7_3_06 AS 'CrimeOtherTheft', -- Víctima de robo en forma distinta / Robbery victim in a different form
tper_vic2.AP7_4_06 AS 'NumberOtherThefts', -- Número de veces víctima de robo en forma distinta / Number of times victim of robbery in a different way
tper_vic2.AP7_3_07 AS 'CrimeBankFraud', -- Víctima de fraude bancario / Bank fraud victim
tper_vic2.AP7_4_07 AS 'NumberBankFrauds', -- Número de veces víctima de fraude / Number of times victim of fraud
tper_vic2.AP7_3_08 AS 'CrimeFraud', -- Víctima de fraude al consumidor / Consumer Fraud Victim
tper_vic2.AP7_4_08 AS 'NumberFrauds', -- Número de veces víctima de fraude al consumidor / Number of times victim of consumer fraud
tper_vic2.AP7_3_09 AS 'CrimeExtortion', -- Víctima de extorsión / Extortion victim
tper_vic2.AP7_4_09 AS 'NumberExtortions', -- Número de veces víctima de extorsión / Number of times extortion victim
tper_vic2.AP7_3_10 AS 'CrimeThreats', -- Víctima de amenazas / Victim of threats
tper_vic2.AP7_4_10 AS 'NumberThreats', -- Número de veces víctima de amenazas / Number of times victim of threats
tper_vic2.AP7_3_11 AS 'CrimeInjuries', -- Víctima de lesiones / Injury victim
tper_vic2.AP7_4_11 AS 'NumberInjuries', -- Número de veces víctima de lesiones / Number of times victim of injuries
tper_vic2.AP7_3_12 AS 'CrimeKidnapping', -- Víctima de secuestro / Kidnapping victim
tper_vic2.AP7_4_12 AS 'NumberKidnappings', -- Número de veces víctima de secuestro / Number of times kidnapped
tper_vic2.AP7_3_13 AS 'CrimeAssault', -- Víctima de hostigamiento o intimidación sexual, manoseo, exhibicionismo, intento de violación / Victim of sexual harassment or intimidation, groping, indecent exposure, attempted rape
tper_vic2.AP7_4_13 AS 'NumberAssaults', -- Número de veces víctima de hostigamiento o intimidación sexual, manoseo, exhibicionismo, intento de violación / Number of times victim of sexual harassment or intimidation, groping, exhibitionism, attempted rape
tper_vic2.AP7_3_14 AS 'CrimeRape', -- Víctima de violación sexual / Rape victim
tper_vic2.AP7_4_14 AS 'NumberRapes', -- Número de veces víctima de violación sexual / Number of times rape victim
tper_vic2.AP7_3_15 AS 'CrimeOther', -- Víctima de otros delitos / Victim of other crimes
tper_vic2.AP7_4_15 AS 'NumberOther' -- Número de veces víctima de otros delitos / Number of times victim of other crimes

FROM 
tvivienda

INNER JOIN thogar ON tvivienda.ID_VIV = thogar.ID_VIV
INNER JOIN tsdem ON tvivienda.ID_VIV = tsdem.ID_VIV
INNER JOIN tmod_vic ON tvivienda.ID_VIV = tmod_vic.ID_VIV
INNER JOIN tper_vic1 ON tvivienda.ID_VIV = tper_vic1.ID_VIV
INNER JOIN tper_vic2 ON tvivienda.ID_VIV = tper_vic2.ID_VIV
;
