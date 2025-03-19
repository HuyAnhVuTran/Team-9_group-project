# Team-9_interim_prototype

# Virus on a Network

## §A. Summary of the current implementation state

Our simulation was developed using Mesa, a Python-based agent-based modeling framework. We built it as a modified version of the Virus on a Network model, specifically adapting it to simulate Twitter's information ecosystem. The model uses random activation scheduling, which means that agents act in random order during each step of the simulation, ensuring that the spread of misinformation occurs in an unpredictable manner—just like in real-world social media environments. It also utilizes various metrics such as reproduction rates, state counts, and strain distribution to monitor the emerging dynamics between bot and user agents in a network environment like Twitter.

For more information about this model, read the NetLogo's web page: http://ccl.northwestern.edu/netlogo/models/VirusonaNetwork.

JavaScript library used in this example to render the network: [d3.js](https://d3js.org/).

## §B. Installation and Run the simulation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
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
In this deliverable, one of the most difficult aspects of implementing the simulation was ensuring that the model did not become stagnant, where users were not transitioning between states. To address this issue we implemented a Resistance Duration parameter and we implemented multiple strains of misinformation to diversify and also makes the model more dynamic. When doing so, we realized that we also need a mechanism to monitor the current strain of a bot or user and update it for each step. To sovlve this, we implemented a new attribute to handle changes in the current strain of misinformation that was infecting an agent on the network. For this, we find it quite difficult to represent these changes visually in our network graph. To be more specific, we faced multiple setbacks where nodes would not change color to match their current strain or the graph would be cluttered by up to 9 different user state. Another limitation is that our current simulation is only capable of simulating in a closed, fixed network where the user defines the number of initial agents and the number of users per agent type (Number of Misinformation Bots and Fact Checker Ratio). For future improvements, we plan to revise the allocation of misinformation strains to Misinformation Bots in order to address bias in misinformation strain propagation we aim to implement a process for strain switching where bots will switch misinformation strain based on lowest propagation. Additionally, we also aim to implement new metrics such as the clustering coefficient will be useful for analyzing how tightly connected Misinformed Users are. This metric will complement our existing data by providing an understanding of how network structures contribute to the persistence and amplification of misinformation. Another improvements is the  a method for dynamically adding more nodes to the initial network ( reflecting social media growth as there are new users joinig every seconds) and if this is not possible we plan to look into how we can change existing user states to add more variability to the simulation.
