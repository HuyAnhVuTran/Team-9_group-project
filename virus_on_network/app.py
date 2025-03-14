import math
import solara

from model import (
    State,
    VirusOnNetwork,
    number_misinformed,
    number_susceptible,
    number_resistant,
    number_fact_checkers,
    number_userInfected,
    number_botInfected,
)


from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    # make_space_component,
)

from localmesa.visualization import (
    # Slider,
    # SolaraViz,
    # make_plot_component,
    make_space_component,
)


def agent_portrayal(agent):
    node_color_dict = {
        State.MISINFORMATION_BOT: "#FF0000",  # Red for first strain
        State.MISINFORMATION_BOT_2: "#CC0000", # Darker red for second strain
        State.MISINFORMATION_BOT_3: "#990000", # Even darker red for third strain
        State.MISINFORMED_USER: "#FFD700",    # Yellow for misinformed users
        State.SUSCEPTIBLE: "#008000",         # Green for susceptible users
        State.RESISTANT: "#808080",           # Gray for resistant users
        State.FACT_CHECKER: "#0000FF",        # Blue for fact-checkers
    }

    portrayal = {
        "color": node_color_dict[agent.state],
        "size": 10,
    }

    # Make all misinformation bot strains squares
    if agent.state in [State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3]:
        portrayal["shape"] = "square"
        portrayal["marker"] = "s"  # Square marker for misinformation bots
        portrayal["size"] = 20

    return portrayal





model_params = {
    "num_nodes": Slider(label="Number of agents", value=50, min=10, max=200, step=1),
    "avg_node_degree": Slider(label="Avg Node Degree", value=3, min=1, max=10, step=1),
    "initial_misinformation_bots": Slider(label="Number of Misinformation Bots", value=1, min=1, max=10, step=1),
    # "initial_fact_checkers": Slider(label="Number of Fact Checkers", value=1, min=1, max=10, step=1),
    "fact_checker_ratio": Slider(label="Fact Checker Ratio", value=0.011, min=0.01, max=0.1, step=0.01),
    "virus_spread_chance": Slider(label="Misinformation Spread Chance", value=0.4, min=0.0, max=1.0, step=0.1),
    "virus_check_frequency": Slider(label="Fact Check Frequency", value=0.4, min=0.0, max=1.0, step=0.1),
    # "recovery_chance": Slider(label="Recovery Chance", value=0.3, min=0.0, max=1.0, step=0.1),
    # "gain_resistance_chance": Slider(label="Gain Resistance Chance", value=0.5, min=0.0, max=1.0, step=0.1),
    "resistance_duration": Slider(label="Resistance Duration", value=6, min=1, max=10, step=1),
}


SpacePlot = make_space_component(agent_portrayal)
StatePlot = make_plot_component(
    {
        "Misinformation Bots (Strain 1)": "#FF0000",  # Red
        "Misinformation Bots (Strain 2)": "#CC0000",  # Darker Red
        "Misinformation Bots (Strain 3)": "#990000",  # Even Darker Red
        "Misinformed": "#FFD700",          # Yellow
        "Susceptible": "#008000",          # Green
        "Resistant": "#808080",            # Gray
        "Fact Checkers": "#0000FF",        # Blue
    }
)

InfectionPlot = make_plot_component(
    {
        "User Misinformation Reproduction Rate": "#FFD700",  # Yellow
        "Bot Misinformation Reproduction Rate": "#FF0000",   # Red
    }
)

model = VirusOnNetwork()


page = SolaraViz(
    model,
    components=[SpacePlot, StatePlot, InfectionPlot],
    model_params=model_params,
    name="Misinformation Model",
)