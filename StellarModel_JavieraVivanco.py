#import libraries
import numpy as np
import matplotlib.pyplot as plt

#IMF
def kroupa(m):
    if m < 0.08:
        return m**-0.3
    elif 0.08 <= m < 0.5:
        return 0.08**-0.3 * (m/0.08)**-1.3
    elif 0.5 <= m < 1:
        return 0.08**-0.3 * (0.5/0.08)**-1.3 * (m/0.5)**-2.3
    elif m >= 1:
        return 0.08**-0.3 * (0.5/0.08)**-1.3 * (1/0.5)**-2.3 * (m/1)**-2.3

#stellar population generation
sample = 350000000 #<--- number of tested stars
simulated=1000000 #<--- size of the population
m0 = np.random.uniform(low=0.08, high=100, size=sample)
p0 = np.random.uniform(low=0,high=1, size=sample)
P0 = []
M0 = []
n=0
for M in m0:
    if p0[n]<kroupa(M) and len(M0)<simulated:
        P0.append(p0[n])
        M0.append(M)
    n+=1


#to plot the function line
mass_values = np.logspace(-2, 2, 400)
imf_values = [kroupa(m) for m in mass_values]

#plot of the function with the masses
plt.figure(figsize=(6, 6))
plt.plot(mass_values,imf_values,'--', linewidth=1,color='k')
plt.scatter(M0,P0,color='grey', s=0.001)
plt.yscale('log')
plt.xscale('log') 
plt.xlim(0.08, 100)
plt.ylim(1e-3, 1)
plt.xlabel('Mass (Solar Mass)')
plt.ylabel(r'$\xi$(m)')
plt.show()

#assign age of birth and calculates MS lifetime
birth_times = [np.random.uniform(0, 10**10) for m in M0] #year
TMS_values = [10**10 / (mass**2.5) for mass in M0] #year
ages = [10**10 - year for year in birth_times] #year


#classify into remnants and MS stars
remnant = []
age_rem = []
MS=[]
age_ms = []
for i in range(0,len(ages)):
    if ages[i] > TMS_values[i]:
        remnant.append(M0[i])
        age_rem.append(ages[i])
    else:
        MS.append(M0[i])
        age_ms.append(ages[i])
    
#classify into WD, BH Y NS
BH=[]
age_BH = []
NS=[]
age_NS = []
WD=[]
age_WD = []
shared=[]
age_shared=[]

for i in range(0,len(remnant)):
    if remnant[i] < 9:
        WD.append(remnant[i])
        age_WD.append(age_rem[i])
    if remnant[i] >= 9 and remnant[i] <15:
        NS.append(remnant[i])
        age_NS.append(age_rem[i])
    if remnant[i] >= 27.5 and remnant[i] <= 120:
        BH.append(remnant[i])
        age_BH.append(age_rem[i])
    if remnant[i] >= 15 and remnant[i] < 27.5:
        shared.append(remnant[i])
        age_shared.append(age_rem[i])
    if remnant[i] >= 60 and remnant[i] <= 120:
        shared.append(remnant[i])
        age_shared.append(age_rem[i])


for i in range(0,len(shared)):
    prob = np.random.uniform(0,1)
    if prob > 0.5:
        NS.append(shared[i])
        #print("ns",shared[i])
        age_NS.append(age_shared[i])
    elif prob < 0.5:
        BH.append(shared[i])
        #print("bh",shared[i])
        age_BH.append(age_shared[i])

#final WD mass
def WD_func(mass):
    if mass < 9:
        M_WD = (0.109 * mass) + 0.394
    return M_WD

#final NS mass
def NS_func(mass):
    if 9 <= mass <= 13:
        M_NS = 2.24 + 0.508*(mass-14.75) + 0.125*(mass - 14.75)**2 + 0.011*(mass-14.75)**3
    elif 13 < mass < 15:
        M_NS = 0.123 + 0.112*mass
    elif 15 <= mass < 17.8:
        M_NS = 0.996 + 0.0384 * mass
    elif 17.8 <= mass < 18.5:
        M_NS = -0.020 + 0.10 * mass
    elif 18.5 <= mass < 21.7:
        M_NS = np.random.normal(1.6, 0.158)
    elif 25.2 <= mass < 27.5:
        M_NS = 3232.29 - 409.429 * (mass - 2.619) + 17.2867 * (mass - 2.619) ** 2 - 0.24315 * (mass - 2.619)**3
    elif 60 <= mass <= 120:
        M_NS = np.random.normal(1.78, 0.02)
    else:
        return None
    return M_NS

#final BH mass
def BH_func(mass):
    if 15 <= mass <= 40:
        M_BH_core_low = -2.049 + 0.4140 * mass
        M_BH_all = 15.52 - 0.3294 * (mass - 25.97) - 0.02121 * (mass - 25.97) ** 2 + 0.003120 * (mass - 25.97) ** 3
        M_BH = 0.9 * M_BH_core_low + (1 - 0.9) * M_BH_all
    elif 45 <= mass <= 120:
        M_BH = 5.697 + 7.8598 * 10 ** 8 * (mass) ** -4.858
    else:
        return None
    return M_BH


final_mass_WD = [WD_func(m) for m in WD]
final_mass_BH = [BH_func(m) for m in BH]
final_mass_NS = [NS_func(m) for m in NS]

#not null values
final_mass_WD = [mass for mass in final_mass_WD if mass is not None]
final_mass_NS = [mass for mass in final_mass_NS if mass is not None]
final_mass_BH = [mass for mass in final_mass_BH if mass is not None]

#fraction of stellar bodies
frac_BH = len(BH)/len(M0)
frac_WD = len(WD)/len(M0)
frac_NS = len(NS)/len(M0)
frac_MS = len(MS)/len(M0)

print('MS:', len(MS), '; Fraction MS: ', frac_MS)
print('WD:', len(WD), '; Fraction WD: ', frac_WD)
print('NS:', len(NS), '; Fraction NS: ', frac_NS)
print('BH:', len(BH), '; Fraction BH: ', frac_BH)

#normalized histogram for final masses
plt.hist(MS, bins=100, histtype='step',density=True, color='blue', alpha=0.5, label='Main Sequence')
plt.hist(final_mass_WD, bins=25,histtype='step', density=True, color='red', alpha=0.5, label='White Dwarf')
plt.hist(final_mass_NS, bins=25,histtype='step', density=True, color='green', alpha=0.5, label='Neutron Star')
plt.hist(final_mass_BH, bins=10, histtype='step',density=True, color='purple', alpha=0.5, label='Black Hole')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Final Mass (Solar Mass)')
plt.ylabel('Counts')
plt.legend(loc='best', prop={'size': 6.5})
plt.show()

#normalized histogram for ages
plt.hist(age_ms, bins=30,  histtype='step', density=True, color='blue', alpha=0.5, label='Main Sequence')
plt.hist(age_WD, bins=30, histtype='step',density=True, color='red', alpha=0.5, label='White Dwarf')
plt.hist(age_NS, bins=30, histtype='step',density=True, color='green', alpha=0.5, label='Neutron Star')
plt.hist(age_BH, bins=30, histtype='step', density=True, color='purple', alpha=0.5, label='Black Hole')
plt.xlabel('Age [year]')
plt.ylabel('Counts')
plt.yscale('log')
plt.xscale('log')
plt.legend(loc='best', prop={'size': 6.5})
plt.show()
