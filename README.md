# Team-9_interim_prototype

# Virus on a Network

## §A. Overview of the phenomenon
The COVID-19 pandemic caused a surge of misinformation on social media, especially on platforms like Twitterm where bots played a major role in amplifying false content. These misinformation bots engaged in coordinated actions - liking, sharing, retweeting and commenting to boost the visibility and perceived credibility of misinformation. This created self-reinforcing fake news loop, intensifying public confusion during the so-called "infodemic". Studies have shown as significant portion of pandemic-related tweets contained unverifiable information with bots responsible for a notable share of the spread. This project aims to discover how media ecosystem can be overwhelmed during crisis and derive key findings from it.

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

## §C. Key findings
Fake news loops on social media are sustained primarily by users, with bots initiating the spread of misinformation and misinformed users becoming the main factors that reinforce and prolong these cycles. Misinformation strains shape distinct narrative clusters, influencing nearby users and forming echo chambers that are resistant to external corrections or interventions. Additionally, we have discovered that the spread of misinformation follows a cyclical pattern, where the network oscillates between periods of misinformation propagation and fact-checking responses. However, as long as users remain active within networks that contain infectious bots, the possibility of the fake news loop resurfacing persists. Moreover, misinformation bots act as catalysts, not only triggering the initial spread but also reviving the fake news cycle when they begin to slow down. While intervention entities such as fact-checkers can help control the spread, they are still insufficient to completely eliminate misinformation from the media ecosystem.
