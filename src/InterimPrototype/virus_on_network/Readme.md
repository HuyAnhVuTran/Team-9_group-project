# Team-9_interim_prototype

# Virus on a Network

## §A. Summary of the current implementation state

Our simulation was developed using Mesa, a Python-based agent-based modeling framework. We built it as a modified version of the Virus on a Network model, specifically adapting it to simulate Twitter's information ecosystem. The model uses random activation scheduling, meaning that agents act in random order during each step of the simulation, ensuring that misinformation spreads unpredictably—just like in real-world social media environments. It also utilizes various metrics such as reproduction rates, state counts, and strain distribution to monitor the emerging dynamics between bot and user agents in a network environment like Twitter.

For more information about this model, read the NetLogo's web page: http://ccl.northwestern.edu/netlogo/models/VirusonaNetwork.

JavaScript library used in this example to render the network: [d3.js](https://d3js.org/).

## §B. Installation and Run the simulation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
```
## Before Running the model

Before running the model, you should change the directory to where the model is located, and run the following command

```
    $ cd /path_to_model/
```

## How to Run

To run the model interactively, in this directory, run the following command

```
    $ solara run app.py
```

## Files

* ``model.py``: Contains the agent class, and the overall model class.
* ``agents.py``: Contains the agent class.
* ``app.py``: Contains the code for the interactive Solara visualization.

## §C. Limitations and planned improvements 
One of the most difficult aspects of implementation was ensuring the simulation never reached a stagnant state, where users were not transitioning between states. Implementing a Resistance Duration parameter for the decay of the infection state over time along with additional strains of misinformation created a more dynamic simulation. Utilizing the Resistance Duration parameter showed us that we also need to monitor and update the current strain of a bot or user at each step. To solve this, we implemented a new attribute to handle changes in the current strain of misinformation when infecting an agent on the network. Another difficult aspect of the implementation was representing these changes visually in our network graph, specifically the node behaviours. The node colours remain unchanged to match their current strain along with the graph having too much noise and clutter. For limitations in our simulation, it only emulates a fixed and controlled network where the user defines the number of initial agents and the number of users per agent type (Number of Misinformation Bots and Fact Checker Ratio). This prevents the possibility of representing other unpredictable emergent behaviours.
For our 4th deliverable, we plan to revise the allocation of misinformation strains to Misinformation Bots to address propagation biases. We aim to implement a process for strain switching where bots will switch misinformation strains based on the lowest propagation. Additionally, we also aim to implement new metrics such as clustering coefficients along with dynamic nodes. Clustering coefficients will be useful for analyzing how closely connected are Misinformed Users during the simulation and it provides an understanding of how network structures contribute to the persistence and amplification of misinformation. We also plan on dynamically adding nodes to the initial network because it represents the user population growth over time and if this is not possible we plan to look into how we can change existing user states to add more variability to the simulation.
