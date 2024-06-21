"""
    This file generates figures, based on the generated data files.
    Results are located in /Data (After you run the program)
"""

import numpy             as np
import matplotlib.pyplot as plt

import matplotlib.patheffects as PathEffects

from matplotlib.lines   import Line2D
from matplotlib.patches import Patch


sizes  = ["mini","small","medium","large"]
sizes2 = ["n100", "n1000", "n10_000", "n100_000"]
sizes3 = ["100","1000","10,000","100,000"]

xs     = np.array([1,2,3,4])

densities = ["sparse","dense"]
measures  = ["modularity", "zahn_condorcet"]

colors  = [(.6,.3,.9),(.3,.6,.9),'r','c','m','y','k','w']
colors2 = plt.cm.hsv(np.linspace(0, 1, len(measures)))

s = len(sizes)
d = len(densities)
m = len(measures)

allData = np.zeros((d,s,m,27))   # 2: sparse or dense; 
                                 # 4: mini, small, medium, large; 
                                 # 2: modularity, deviation_to_uniformity; 
                                 # 5: measures: avg + sigma + nmi + sigma each, + avg run time


legend_elements = []

for i_m, measure in enumerate(measures):
    legend_elements.append(Patch(facecolor=colors[i_m], edgecolor='k',
                         label=measure))



for i_d, density in enumerate(densities):
    for i_s, size in enumerate(sizes2):
        for i_m, measure in enumerate(measures):
            rows = np.genfromtxt("data/{}_{}_graphs_{}.csv".format(size, density, measure), delimiter = ",")
            
            measureList    = rows[1:,12]
            avg_measure = np.mean(measureList)
            sig_measure = np.std(measureList)
            
            nmis        = rows[1:,13]
            avg_nmi     = np.mean(nmis)
            sig_nmi     = np.std(nmis)
            
            runtimes    = rows[1:,14]
            avg_runtime = np.mean(runtimes)
            
            adding = np.array([avg_measure, sig_measure, avg_nmi, sig_nmi, avg_runtime])
            adding2 = np.append(nmis, avg_measure)
            adding2 = np.append(adding2, avg_runtime)
            
            allData[i_d,i_s,i_m,:] = adding2

if len(measures) == 1:
    offsets = np.array([0])
else:
    offsets = np.linspace(-.18,.18,len(measures))
    
width = .5 / (len(measures))


#PLOT THE NMI SCORES AS SHOWN IN PAPER:
for i_d, density in enumerate(densities):
    plt.figure()
    
    for i_m, measure in enumerate(measures):
        plt.plot(xs, allData[i_d,:,i_m,-1],label="{}".format(measure))
    
    plt.yscale("log")
    plt.xticks(xs, sizes3)
    plt.grid()
    
    plt.xlabel("Network size $n$")
    plt.ylabel("Computation time [s]")
    
    plt.legend(loc="lower right")
    plt.savefig("data/runtime_{}.pdf".format(density))


#PLOT THE COMPUTATION TIMES AS SHOWN IN PAPER:
for i_d, density in enumerate(densities):
    fig, ax = plt.subplots()
    
    for i_m, measure in enumerate(measures):
        
        bplot = ax.boxplot(np.transpose(allData[i_d,:,i_m,:-2]), positions = xs + offsets[i_m], patch_artist = True, widths = width, boxprops = dict(facecolor = colors[i_m]))
        
        for i, median in enumerate(bplot['medians']):
                
                sizeIndex    = i % len(sizes)
                measureIndex = i // len(sizes)
                
                txt = plt.text(median.get_xdata()[0] + .01, median.get_ydata()[0] - 0.05, '$Q = {}$'.format(np.round(allData[i_d,sizeIndex,i_m,-2], 2)), color='black', va='bottom', fontweight = 'bold', fontsize = 7)
                txt.set_path_effects([PathEffects.withStroke(linewidth=3, foreground = 'w')])
                
                plt.draw()
                
    plt.xticks(xs, sizes3)
    plt.yticks(np.arange(0,1.05,.1))
    plt.grid(which='both',linestyle="--")
    
    
    plt.minorticks_on()
    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(.05))
    plt.grid(which='minor', linestyle=":")
    plt.grid(False, axis='x')
    
    for tick in xs[:-1]:
        plt.axvline(tick+.5, color='gray', linestyle = '--', linewidth=.5)
    plt.tick_params(bottom=False)
    
    plt.ylim(.4,1.05)
    
    plt.xlabel("Network size $n$")
    plt.ylabel("NMI score")

    plt.savefig("data/nmi_{}.pdf".format(density))           