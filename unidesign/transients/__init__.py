"""
Transient Dynamics for Neural Processing

Building Blocks
- Network N for the neuroanatomy with nodes representing neurons and edges representing connection weight
- A set of input pattern I extended in time, representing a spatio-temporal entity, thought of as the
activation of a subset of neurons that would be activated by the sensory signal transduction
- Mapping of e.g. odor identity and concentration to activation pattern I

Experimental physiological data
- Activity patterns, spike time events on the network nodes

Temporal Propagation Function (model)
- Fitting experimental activity pattern evolution given input pattern and anatomical connectivity
- Generate transients T using the fitted model for given input patterns

Algorithm:
- Extract the stable heteroclinic channels, i.e. the metastable saddle states
- Implement the Lotka-Voltera equation as model to generate the transients using ne

http://www.scipy.org/Cookbook/LoktaVolterraTutorial?action=show&redirect=LoktaVolterraTutorial


Try:
- extract from space-time object objects with a sliding time-window approach
existing only in a topological space (no distances), using open sets to define nearness
and use it for clustering into metastable states.

"""
