import math
import solara

from model import (
    State,
    VirusOnNetwork,
    number_misinformed,
    number_susceptible,
    number_resistant,
    number_fact_checkers,
)


from mesa.visualization import (
    Slider,
    SolaraViz,
    make_plot_component,
    make_space_component,
)


def agent_portrayal(agent):
    node_color_dict = {
        State.MISINFORMATION_BOT: "#FF0000",  # Red for misinformation bots
        State.MISINFORMED_USER: "#FFD700",    # Yellow for misinformed users
        State.SUSCEPTIBLE: "#008000",         # Green for susceptible users
        State.RESISTANT: "#808080",           # Gray for resistant users
        State.FACT_CHECKER: "#0000FF",        # Blue for fact-checkers
    }
    return {"color": node_color_dict[agent.state], "size": 10}




model_params = {
    "num_nodes": Slider(label="Number of agents", value=50, min=10, max=200, step=1),
    "avg_node_degree": Slider(label="Avg Node Degree", value=3, min=1, max=10, step=1),
    "initial_outbreak_size": Slider(label="Initial Misinformed Size", value=1, min=1, max=10, step=1),
    "virus_spread_chance": Slider(label="Misinformation Spread Chance", value=0.4, min=0.0, max=1.0, step=0.1),
    "virus_check_frequency": Slider(label="Fact Check Frequency", value=0.4, min=0.0, max=1.0, step=0.1),
    "recovery_chance": Slider(label="Recovery Chance", value=0.3, min=0.0, max=1.0, step=0.1),
    "gain_resistance_chance": Slider(label="Gain Resistance Chance", value=0.5, min=0.0, max=1.0, step=0.1),
    "fact_checker_ratio": Slider(label="Fact Checker Ratio", value=0.1, min=0.0, max=1.0, step=0.1),
}


SpacePlot = make_space_component(agent_portrayal)
StatePlot = make_plot_component(
    {
        "Misinformation Bots": "#FF0000",  # Red
        "Misinformed": "#FFD700",          # Yellow
        "Susceptible": "#008000",          # Green
        "Resistant": "#808080",            # Gray
        "Fact Checkers": "#0000FF",        # Blue
    }
)




model = VirusOnNetwork()


page = SolaraViz(
    model,
    components=[SpacePlot, StatePlot],
    model_params=model_params,
    name="Misinformation Model",
)


