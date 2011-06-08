"An endurantist holds that for an object to persist through time is for
it to exist completely at different times (each instance of existence
we can regard as somehow separate from previous and future instances,
though still numerically identical with them).
A perdurantist on the other hand holds that for a thing to exist through
time is for it to exist as a continuous reality, and that when we
consider the thing as a whole we must consider an aggregate of all its
"temporal parts" or instances of existing. "

Cited from http://en.wikipedia.org/wiki/Philosophy_of_space_and_time

Paper
-----
* http://arxiv.org/abs/1103.3300
* http://www.stat.cmu.edu/~gmg/home/index.php/publications.html
* http://www.cscs.umich.edu/~crshalizi/weblog/
* http://cscs.umich.edu/~crshalizi/notebooks/neural-coding.html

Spike Train Metric
------------------
* van Rossum, M. C. W. (2001). A novel spike distance. Neural Comput. 13, 751–763
spike distance metric to evaluate each neuron’s spike discharge pattern. The metric quantifies the distance between
every possible pair of spike trains in the data set for each neuron.

* Python Neo: http://packages.python.org/neo/classes.html (see RecordingPoint for link to spatial)
* OpenElectrophy http://neuralensemble.org/trac/OpenElectrophy/wiki

* Discrete Event System Specification http://en.wikipedia.org/wiki/DEVS
* Hierarchical Time Series http://robjhyndman.com/papers/hierarchical/

Neural Coding / Reconstructions
-------------------------------
* Characterizing the fine structure of a neural sensory code through information distortion
http://www.springerlink.com/content/at610w0480663m00/fulltext.pdf

Packages
--------
* http://code.google.com/p/pandas/

Questions
---------
* DynamicRegion with t dimension. How to transform event and interval?

Examples
--------
Use NetworkX to store coupling parameter for a system of coupled, damped oscillators
http://www.uncg.edu/phy/hellen/Python_Instructions.html
To make a network of such oscillators coupled over the network you could replace those lines with the code:
def damped_osc(u,t,b,G): #defines the system of odes
    n=len(G)
    x=u[:n]
    v=u[n:]
    dx=v
    dv=-x-b*v
    for n in G:   # coupling
        dx[n] += sum( G[n][nbr].get('weight',1)*(x[nbr]-x[n]) for nbr in G[n] )
    return r_[dx,dv]  # this is one of many ways to concatenate numpy arrays
t = arange(0,20,0.1)
u0 = array([1,1.1,0,0])   # initial x for each node and v for each node
G=networkx.complete_graph(2)
b=0.4
u=odeint(damped_osc,u0,t,args=(b,G)) #b is in tuple, needs comma

So, the network is stored in G, and the odeint vector field function can use it to  hold the coupling coefficients between nodes.

