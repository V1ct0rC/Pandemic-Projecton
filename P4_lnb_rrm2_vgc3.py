#Necessary imports
import numpy as np  #Needed to use linspace() function
from scipy.integrate import odeint  #Needed to solve a system of differential equations
from scipy.integrate import simps  #Needed to get the total number of infecteds
import matplotlib.pyplot as plt  #Needed to plot the results


inf_total = 0;  #A global variable to receive the total number of infecteds individuals

def derivatives(y, t, beta, gamma, sigma, alfa):  #Function that returns the derivatives of each class function
    S, E, I, R, D = y;  #y is a vector which contains the functions of each class

    dSdt = -beta * S * I;  #Suscetible
    dEdt = beta * S * I - sigma * E;  #Exposed
    dIdt = sigma * E - gamma * I - alfa * I;  #Infected
    dRdt = gamma * I;  #Recovered
    dDdt = alfa * I;  #Dead

    return dSdt, dEdt, dIdt, dRdt, dDdt;


def plot_projection(ret, t, string):  #Function that plots the progression of each class throughout time
    y1, y2, y3, y4, y5 = ret.T;

    fig, axs = plt.subplots(2, 3, figsize=(30,15), facecolor='lightgray')

    #ax = fig.add_subplot(111, facecolor='#ffffff', axisbelow=True);
    axs[0, 0].plot(t, y1, 'b', alpha=0.5, lw=2, label='Susceptible');  #b stands for blue
    axs[0, 0].plot(t, y2, 'r', alpha=0.5, lw=2, label='Exposed');  #r stands for red
    axs[0, 0].plot(t, y3, 'g', alpha=0.5, lw=2, label='Infected');  #g stands for green
    axs[0, 0].plot(t, y4, 'y', alpha=0.5, lw=2, label='Recovered');  #y stands for yellow
    axs[0, 0].plot(t, y5, 'm', alpha=0.5, lw=2, label='Death');  #m stands for magenta
    axs[0, 0].set_title(string);
    axs[0, 0].set_xlabel('t');
    axs[0, 0].set_ylabel('y(t)');
    
    legend = axs[0, 0].legend();
    legend.get_frame().set_alpha(0.5);
    for spine in ('top', 'right', 'bottom', 'left'):
        axs[0, 0].spines[spine].set_visible(False);

    axs[0, 0].grid(True, 'major', 'both', color='lightgray');

    #Plotting "Death" class alone, so it will be more visible
    axs[1, 0].plot(t, y5, 'm', alpha=0.5, lw=2, label='Death');
    axs[1, 0].set_title("Focusing the deaths progression");
    axs[1, 0].set_xlabel('t');
    axs[1, 0].set_ylabel('y(t)');
    legend = axs[1, 0].legend();
    legend.get_frame().set_alpha(0.5);
    for spine in ('top', 'right', 'bottom', 'left'):
        axs[1, 0].spines[spine].set_visible(False);

    axs[1, 0].grid(True, 'major', 'both', color='lightgray');

    #Plotting "Infected" class alone, so it will be more visible
    axs[0, 1].plot(t, y3, 'g', alpha=0.5, lw=2, label='Infecteds');
    axs[0, 1].set_title("Focusing the infecteds progression");
    axs[0, 1].set_xlabel('t');
    axs[0, 1].set_ylabel('y(t)');
    legend = axs[0, 1].legend();
    legend.get_frame().set_alpha(0.5);
    for spine in ('top', 'right', 'bottom', 'left'):
        axs[0, 1].spines[spine].set_visible(False);

    axs[0, 1].grid(True, 'major', 'both', color='lightgray');

    #Plotting "recovered" class alone, so it will be more visible
    axs[1, 1].plot(t, y4, 'y', alpha=0.5, lw=2, label='Recovered');
    axs[1, 1].set_title("Focusing the Recovereds progression");
    axs[1, 1].set_xlabel('t');
    axs[1, 1].set_ylabel('y(t)');
    legend = axs[1, 1].legend();
    legend.get_frame().set_alpha(0.5);
    for spine in ('top', 'right', 'bottom', 'left'):
        axs[1, 1].spines[spine].set_visible(False);

    axs[1, 1].grid(True, 'major', 'both', color='lightgray');

    #Plotting "Exposed" class alone, so it will be more visible
    axs[0, 2].plot(t, y2, 'r', alpha=0.5, lw=2, label='Exposed');
    axs[0, 2].set_title("Focusing the exposeds progression");
    axs[0, 2].set_xlabel('t');
    axs[0, 2].set_ylabel('y(t)');
    legend = axs[0, 2].legend();
    legend.get_frame().set_alpha(0.5);
    for spine in ('top', 'right', 'bottom', 'left'):
        axs[0, 2].spines[spine].set_visible(False);

    axs[0, 2].grid(True, 'major', 'both', color='lightgray');

    #Plotting "Susceptible" class alone, so it will be more visible
    axs[1, 2].plot(t, y1, 'b', alpha=0.5, lw=2, label='Susceptible');
    axs[1, 2].set_title("Focusing the susceptibles progression");
    axs[1, 2].set_xlabel('t');
    axs[1, 2].set_ylabel('y(t)');
    legend = axs[1, 2].legend();
    legend.get_frame().set_alpha(0.5);
    for spine in ('top', 'right', 'bottom', 'left'):
        axs[1, 2].spines[spine].set_visible(False);

    axs[1, 2].grid(True, 'major', 'both', color='lightgray');

    global inf_total
    inf_total = simps(y3, t)  #Calculating the total number of infecteds


"""
PROJECTION ABOUT THE PAST
- Starting at 01/02/2021
- Until 31/01/2022
"""
#Initial values from 01/02/2021: https://www.cievspe.com/_files/ugd/3293a8_10cba904d4404df69a626b8793e63f1e.pdf
#From https://coronavirus.ceara.gov.br/project/guia-de-vigilancia-epidemiologica-ministerio-da-saude-versao-3/
#We got the days of disease (14) and latency period (5).

N = 9674793;  #Estimated Pernambuco population: www.ibge.gov.br/cidades-e-estados/pe.html
E0 = 1852;  #Individuals exposed in the latency period (0.2 * I0)
D0 = 10364;  #Individuals killed by covid
I0, R0 = 9258, 222929;  #Initial number of infected and recovered individuals
#I0: 9258, at https://dados.seplag.pe.gov.br/apps/corona.html page 3
#8376 is the number of confirmed cases in the 6st week of 2021 (01/02/2021)
S0 = N - I0 - R0 - D0 - E0;  #Everyone else, S0, is susceptible to infection initially.
beta, gamma = (1/14)/N, 1/14;  #Contact rate, beta (in 1/days/#Individuals), and mean recovery rate, gamma, (in 1/days).
sigma, alfa = 0.2, 0.03;

t = np.linspace(0, 395, 396)  #An array of equally spaced points. In this case, t is a period of days
#395 days: 01/02/2021 -> 31/01/2022

y0 = S0, E0, I0, R0, D0;  #Initial values vector

ret = odeint(derivatives, y0, t, args = (beta, gamma, sigma, alfa));

string = "Pandemic projection about the past"
plot_projection(ret, t, string);  #Note that the y axis has a 1 * 10^6 scale in the graph with all functions and the one focusing S group


"""
PROJECTION ABOUT THE FUTURE
- With all the effects chosen
- Starting at 31/01/2022
"""
#Initial values from 31/01/2022: https://www.cievspe.com/_files/ugd/3293a8_bf9c9315a4704fe7bb7ac44c08738b35.pdf

N = 9674793;  #Estimated Pernambuco population: www.ibge.gov.br/cidades-e-estados/pe.html
E0 = 6685;  #Individuals exposed in the latency period (0.2 * I0)
D0 = 20643;  #Individuals killed by covid
I0, R0 = 33424, 597803;  #Initial number of infected and recovered individuals
#I0: 33424, at https://dados.seplag.pe.gov.br/apps/corona.html page 3
#33424 is the number of confirmed cases in the 6th week of 2022 (31/01/2022)
S0 = N - I0 - R0 - D0 - E0;  #Everyone else, S0, is susceptible to infection initially.
beta, gamma = (1/12)/N, 1/12;  #Contact rate, beta (in 1/days/#Individuals), and mean recovery rate, gamma, (in 1/days).
sigma, alfa = 0.2, 0.02;

t = np.linspace(0, 181, 182)  #An array of equally spaced points. In this case, t is a period of days
#181 days: 31/01/2022 -> 31/07/2022

y0 = S0, E0, I0, R0, D0;  #Initial values vector

ret = odeint(derivatives, y0, t, args = (beta, gamma, sigma, alfa));

string = "Future Pandemic projection with security measures and immunization"
plot_projection(ret, t, string);  #Note that the y axis has a 1 * 10^6 scale in the graph with all functions and the one focusing S group


"""
PROJECTION ABOUT THE FUTURE
- Without security measures and immunization
- Starting at 31/01/2022
"""
#Initial values from 31/01/2022: https://www.cievspe.com/_files/ugd/3293a8_bf9c9315a4704fe7bb7ac44c08738b35.pdf

N = 9674793;  #Estimated Pernambuco population: www.ibge.gov.br/cidades-e-estados/pe.html
E0 = 6685;  #Individuals exposed in the latency period (0.2 * I0)
D0 = 20643;  #Individuals killed by covid
I0, R0 = 33424, 597803;  #Initial number of infected and recovered individuals
#I0: 33424, at https://dados.seplag.pe.gov.br/apps/corona.html page 3
#33424 is the number of confirmed cases in the 6th week of 2022 (31/01/2022)
S0 = N - I0 - R0 - D0 - E0;  #Everyone else, S0, is susceptible to infection initially.
beta, gamma = (1/14)/N, 1/14;  #Contact rate, beta (in 1/days/#Individuals), and mean recovery rate, gamma, (in 1/days).
sigma, alfa = 0.2, 0.03;

t = np.linspace(0, 181, 182)  #An array of equally spaced points. In this case, t is a period of days
#181 days: 31/01/2022 -> 31/07/2022

y0 = S0, E0, I0, R0, D0;  #Initial values vector

ret = odeint(derivatives, y0, t, args = (beta, gamma, sigma, alfa));

string = "Future Pandemic projection without security measures and immunization"
plot_projection(ret, t, string);  #Note that the y axis has a 1 * 10^6 scale in the graph with all functions and the one focusing S group


"""
PROJECTION ABOUT THE FUTURE
- Without security measures, immunization and Influenza A H3N2 subtype
- Starting at 31/01/2022
"""
#Initial values from 31/01/2022: https://www.cievspe.com/_files/ugd/3293a8_bf9c9315a4704fe7bb7ac44c08738b35.pdf

N = 9674793;  #Estimated Pernambuco population: www.ibge.gov.br/cidades-e-estados/pe.html
E0 = 6685;  #Individuals exposed in the latency period (0.2 * I0)
D0 = 20643;  #Individuals killed by covid
I0, R0 = 33424, 597803;  #Initial number of infected and recovered individuals
#I0: 33424, at https://dados.seplag.pe.gov.br/apps/corona.html page 3
#33424 is the number of confirmed cases in the 6th week of 2022 (31/01/2022)
S0 = N - I0 - R0 - D0 - E0;  #Everyone else, S0, is susceptible to infection initially.
beta, gamma = (1/10)/N, 1/10;  #Contact rate, beta (in 1/days/#Individuals), and mean recovery rate, gamma, (in 1/days).
sigma, alfa = 0.2, 0.03;

t = np.linspace(0, 181, 182)  #An array of equally spaced points. In this case, t is a period of days
#181 days: 31/01/2022 -> 31/07/2022

y0 = S0, E0, I0, R0, D0;  #Initial values vector

ret = odeint(derivatives, y0, t, args = (beta, gamma, sigma, alfa));

string = "Future Pandemic projection without security measures and immunization"
plot_projection(ret, t, string);  #Note that the y axis has a 1 * 10^6 scale in the graph with all functions and the one focusing S group