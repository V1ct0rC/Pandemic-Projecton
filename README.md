# Pandemic-Projecton
Implementation of an pandemic projection in Recife - Brasil, following SEIRD equation model. Project proposed by our Numerical Methods course. 

## Universidade Federal de Pernambuco
### Computer Engineering - Informatics Center
### Numerical Methods (MNC - 2021.1)
Lucas Nascimento Brandão (lnb)
Rodrigo Rocha Moura (rrm2)
Victor Gabriel de Carvalho (vgc3)

## Abstract
Almost two years ago, the first cases of what would posteriorly become a global pandemic started to show up in Asia. Currently, the virus is widely spread across the world and, despite the relative control that many countries already exhibit, it is still crucial to understand and predict the course of this disease. It is in this context that mathematical progression models gain great importance, because they are able to model previous and future events with certain detail and precision. Therefore, the model we used was a modification of the SIR model: SEIRD, which stands for suscetible (S), exposed (E), infected (I), recovered (R) and dead (D) individuals. With its results, a clear relation can be seen between reality and our projection in some aspects, however, due to the simplicity of our model, we could not archieve great precision and fidelity. Nevertheless, we cannot rule out the educational relevance of our project regarding the application of differential equations.

## Introduction and Objectives
The coronavirus pandemic has had a great impact on the Brazilian population, physically and mentally, that waits with so much anxiety and desire for the end of this isolation times. Meanwhile, a question remains: When is it really safe to decree the end of a viral outbreak? In order to contribute to this question, our study explains the development of COVID-19 pandemic from 01/02/2021 to 31/01/2022 in Pernambuco and predicts the course of the epidemiological situation until 31/07/2022. Throughout the study, we consider the symptoms of the disease and its stages, specified as five classes of individuals: Suscetible, Exposed, Infected, Recovered and Dead. This SEIRD model uses some parameters, which are decisicve in Pernambuco's pandemic reality. An example is the presence of Influenza A H3N2 subtype, because patients affected by the coronavirus may have a symptoms recovery rate extended by the new disease. In addition, there are others effects that are present in our daily lives such as the use of a mask, the presence of the vaccine, social isolation and seasonal rains.

## Objectives
>Predict the progression of the coronavirus epidemic in Pernambuco.

>Learn about the possibilities to face the upcoming pandemic situation.

>Estimate the damage caused by our atitudes and government decisions.

>Model the data acquired in order to use the tools provided by differential equations methods.

>Understand the impact of easing the rules of coexistence in the midst of COVID-19 and Influenza.

>Discuss the validity of the SEIRD model in the Pernambuco context.

## Methods
The general implementation of our project will be done through the Python programming language (more specifically the scientific libraries Numpy, Scipy and Matplotlib) and documented in the form of a Jupyter Notebook. We used Scipy's Integrate module because there are functions needed to solve systems of differential equations and main calculations. In the end, the results and graphic progression of the pandemic in our state will be presented through the Matplotlib library, in order to facilitate the interpretation of the results obtained.

In this model, we consider that: the number of the total population N is fixed; when a person is infected, soon or later the symptoms will show up; the duration of the symptoms is the duration of the disease; the population is homogeneous.

Equations for each class of individuals:

>dS/dt = -β * S * I

>dE/dt = β * S * I - σ * E

>dIdt = σ * E - γ * I - α * I

>dR/dt = γ * I

>dD/dt = α * I

Parameters β, σ, γ and α:

>Beta -> effective contact rate (when a contact to a infected person result in contracting the virus); β = (1/days of disease)/N.

>Sigma -> mean latent period rate (1/sigma is the mean period of time between contracting the virus and showing up symptoms).

>Gamma -> mean recuperation rate (1/days of disease).

>Alfa -> fatality rate (number of deaths from disease/total population).

Each parameter will be calibrated considering the effects below.

These are the impacts of each effect:

>Vaccine: It increases gamma (recuperation decreases because of the vaccine) and decreases both beta (taking the vaccine curbs the number of effective contacts) and alfa (one that takes a vaccine is less likely to die because of the disease). Present in both past and future models.

>Social distancing easing: We consider this increases beta (if the number of contacts between people increases, so does the number of effective contacts). Present only in the future model.

>Easing the use of mask: It increases beta (as a physical barrier against the spread of the virus, without masks people are more likely to spread it). Present only in the future model.

>Influenza A H3N2 subtype: It decreases gamma (Some symptoms of this subtype are similar to covid's. So, this subtype increases the days of recuperation when a person with covid symptoms contracts the subtype, so it will extend some of the already present symptoms of covid). Only present in the future model.

>Seasonal rains: It increases beta (As we get closer to Pernambuco's winter season, the number of rains increases throughout the state. So, indoor spaces will be more frequented). Present only in the future model.

## Parameters calibration
Past simulation values from: https://www.cievspe.com/_files/ugd/3293a8_10cba904d4404df69a626b8793e63f1e.pdf .
Future simulation values from: https://www.cievspe.com/_files/ugd/3293a8_bf9c9315a4704fe7bb7ac44c08738b35.pdf .
### Beta (β):
Past: At https://coronavirus.ceara.gov.br/project/guia-de-vigilancia-epidemiologica-ministerio-da-saude-versao-3/ there is a section called "Período de transmissibilidade", which is the period that someone can transmit the virus. Our simulation considers that the duration of the symptoms is the duration of the disease. This survellaince report show that the contagious period is about 14 days. Then beta = ((1/14)/N).

Future: Source: https://www.gov.br/saude/pt-br/coronavirus/publicacoes-tecnicas/guias-e-planos/guia-de-vigilancia-epidemiologica-covid-19/view .Throughout this report we can see one effect of the vaccine: there is a recommendation of a 10 days quarantine, a short period compared to the old one. But taking the effects of social distancing and mask usage easing, seasonal rains and Influenza A H3N2 subtype, we'll use a 12 days disease period. Then beta = ((1/12)/N).

### Sigma (σ):
Past and Future: At both < https://www.gov.br/saude/pt-br/coronavirus/publicacoes-tecnicas/guias-e-planos/guia-de-vigilancia-epidemiologica-covid-19/view > and < https://coronavirus.ceara.gov.br/project/guia-de-vigilancia-epidemiologica-ministerio-da-saude-versao-3/ > there is a section called "Período de incubação", which is the period between contracting the virus and showing up symptoms. These survellaince reports show that this latency period lasts for about 5 days. Then sigma = 1/5.

### Gamma (γ):
Past: At https://coronavirus.ceara.gov.br/project/guia-de-vigilancia-epidemiologica-ministerio-da-saude-versao-3/ there is a section called "Período de transmissibilidade", which is the period of transmitting the virus. Our simulation considers that the duration of the symptoms is the duration of the disease. This survellaince report show that the contagious period is about 14 days. Then gamma = 1/14.

Future: Source: https://www.gov.br/saude/pt-br/coronavirus/publicacoes-tecnicas/guias-e-planos/guia-de-vigilancia-epidemiologica-covid-19/view .Throughout this report we can see one effect of the vaccine: there is a recommendation of a 10 days quarantine, a short period compared to the old one. But taking the effects of social distancing easing, easing the use of mask, seasonal rains and Influenza A H3N2 subtype, we'll use a 12 days disease period. Then gamma = 1/12.

Notice that we can use Gamma to calculate Beta (β = γ/N), due to their close relation.

### Alfa (α):
Past: At https://www.britannica.com/science/case-fatality-rate is shown that fatality rate = number of deaths from a specified disease over a defined period of time/the number of individuals diagnosed with the disease during that time. Then, in order to find a correct alfa, we need to use the number of deaths from 31/01/2022: Alfa = 20643/698267 which is approximately 0.03.

Future: At https://www.britannica.com/science/case-fatality-rate is shown that fatality rate = number of deaths from a specified disease over a defined period of time/the number of individuals diagnosed with the disease during that time. Then, in order to find a correct alfa, we need to use the number of deaths from 31/07/2022, but this is impossible. So, we can use the newest number of deaths, which is from 11/05/2022: Alfa = 21648/929090 = 0.02. Source: https://www.cievspe.com/_files/ugd/3293a8_c05a80efe0f04a82b18f15cfcb455c46.pdf .

## Implementation of the past and the future
Implementation shown on our .ipynb or .py files.

## Results and Discussions
Analyzing the graphs and values presented above and comparing them with reality, we can note a certain relation between our projection and what actually happened.

About the number of deaths:

>About the past: The epidemiological report from 31/01/2022 (used in parameters calibration section) shows that the total number of deaths in Pernambuco was 20,643. On our first graphs set the total number of deaths is approximately 20,000. That gives us an satisfatory precision.

>About the future with security measures and immunization: Today's data (https://www.cievspe.com/_files/ugd/3293a8_c05a80efe0f04a82b18f15cfcb455c46.pdf) shows that the total number of deaths in Pernambuco is 21,648, which isn't close to 50,000, shown on our projection (indicated on our second graphs set).

About the number of recovereds:

>About the past: The epidemiological report from 31/01/2022 (used in parameters calibration section) shows that the total number of recovereds in Pernambuco was 597,803. On our first graphs set the total number of recovereds is approximately 245,000. This difference probably happened because our model assumed less infecteds for that period, resulting in less recovereds.

>About the future with security measures and immunization: Today's data (https://www.cievspe.com/_files/ugd/3293a8_c05a80efe0f04a82b18f15cfcb455c46.pdf) shows that the total number of recovereds in Pernambuco is 794,785. On our second graphs set the total number of recovereds is approximately 720,000.

About the number of infecteds:

>About the past: The epidemiological report from 31/01/2022 (used in parameters calibration section) shows that the total number of infecteds in Pernambuco was 698,267. On our first graphs set the total number of infecteds is approximately 348,308.

>About the future: Today's data (https://www.cievspe.com/_files/ugd/3293a8_c05a80efe0f04a82b18f15cfcb455c46.pdf) shows that the total number of infecteds in Pernambuco is 929,090. On our second graphs set the total number of infecteds is approximately 348,307 + 1,480,134 = 1,828,441.

However, analyzing this group can be tricky, due to the fact that COVID-19 usually causes mild symptoms that can easily be confused with other diseases, underreporting of cases certainly happened in Pernambuco. Such aspects, combined with the low incentive for testing, may have delayed the real number of infecteds.

As we can see, some of our projections shows discrepant numbers compared to reality. Two reasons for that difference may be:

unadopted less relevant parameters that, when joined, can impact the final results;

the SEIRD model isn't completely valid for the progression of coronavirus pandemic in Pernambuco.

All graphs shows the herd immunity, because the functions enter in a stable state. This scenario hasn't actually happened yet and we believe that it would not happen that soon, as our projection sugests. There are several unpredictable factors that coult delay the shown steady state.

Still analyzing the projections, we can testify the effectiveness of immunization and distancing rules, which played an important role in slowing down the growth of cases and deaths curve, compared to a projection without such policies. We can see an increase of around 5000 deaths at the end of our estimation with fewer sanitary restrictions, followed by fewer recovered individuals.

Given the complexity of our model and project, it it impossible to fully describe real scenarios, however, we can still converse about several pandemic aspects in our state.

Our project still has great relevance in the actual scenario, considering that, despite the current decrement in cases, it is essential to have some idea about what should happen in the future. Thus, we will be able to judge our current attitudes towards preventive measures and propose new behaviors that would potentially prevent greater consequences. It is also important to point out the educational and academic significance of our model, allowing us to apply differential equations in real world issues.

## Conclusion
Finally, we can conclude that the SEIRD model, as we used it, is not very applicable for Pernambuco's pandemic projection. Due to our model's simplicity and the unpredictability of COVID-19, we had to face some discrepancies between what happened and what was esrimated. Nevertheless, this project has shown that dealing with a global calamity is not something simple and that there is a large number of variables interfering in calculating the future. However, we can make estimates for future contexts based on previous behaviors. The attitude of each individual may be too difficult to estimate, but the attitude of a large group is not impossible.

This kind of work is essential these days, mainly because to learn how to deal with something new and unexpected, like a pandemic. It is also crucial to use our data to improve governmental response during crisis, in order to avoid worst consequences and to improve population's quality of life.
