# Stellar-Model-Javiera-Vivanco

## Overview

This code enables users to simulate the evolution of stars within the Milky Way, facilitating the exploration and analysis of its stellar population. The model's relationships and functions are detailed in Vivanco (2023)'s paper. The code follows the structure outlined in the diagram below.

<p align="center">
<img src="https://github.com/javieravivanco/Stellar-Model-Javiera-Vivanco/assets/149679459/43cbda24-ad06-4913-b63e-c6fcf2cda0e2" width="350"/>
</p>


### Initial Mass

In this first part, the code draw randomly initial masses of the stars, combining Monte Carlo, with the Initial Mass Function. You have to choose a number of stars that you want to create for your stellar population ("simulated"), and the number of stars that you want to generate ("tested") to see if they satisfy the initial mass function. Then, the code will store the masses that are bellow this function.

**kroupa (m)**: This function receives the generated mass as input, returning its respective probability, according to the initial mass function.


### Time of birth

Having the initial masses, it assigns a birth time to the stars by randomly
drawing a time from a constant star formation rate over the time, with an uniform distribution.

### Main sequence lifetime

In this part of the code, it calculates the Main Sequence Lifetime of the stars, using the initial masses. Then, it calculates the total age of the stars, with the age of the Milky way minus the age of birth.

### End point

To identify which stars are stellar remnants, the code assesses whether a star's total age exceeds the main sequence (MS) lifetime or if it remains within the MS phase. To determine what type of stellar remnant they are, the code uses three functions, describing initial-to-final-mass-relations, para las enanas blancas, estrellas de neutrones y agujeros negros, clasificando los remanentes en su tipo según los rangos de masas descritos por sus respectivas relaciones.

**WD_func(m)**: This function receives the white dwarf initial mass, returning the final mass, according to the IFMR for white dwarfs.

**NS_func(m)**: This function receives the neutron star initial mass, returning the final mass, according to the IFMR for neutron stars. This function is segmented by mass ranges.

**BH_func(m)**: This function receives the black hole initial mass, returning the final mass, according to the IFMR for black holes. This function is segmented by mass ranges.

## Usage

To run the simulation, follow these steps:

1. Ensure that you have Python 3.7 or a higher version installed.
2. Install the required libraries by running the following command:
```
pip install numpy matplotlib
```
3. Run the code.

## Results and other uses

This code computes the fraction of each stellar body within the entire population. Additionally, it generates histograms for the final masses and ages of the population, categorized by the type of celestial object. You have the flexibility to produce additional histograms, plots, statistics, and more using the stored variables to analyze the data according to your specific needs and preferences.

![image](https://github.com/javieravivanco/Stellar-Model-Javiera-Vivanco/assets/149679459/1b0557c6-b07e-4ef8-af38-2e1b09c170a9)




