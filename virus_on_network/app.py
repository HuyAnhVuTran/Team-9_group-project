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
)

from localmesa.visualization import (
    make_space_component,
)

def agent_portrayal(agent):
    """Defines how agents are visualized based on their state."""
    
    node_color_dict = {
        State.MISINFORMATION_BOT: "#FF0000",  # Red for first strain
        State.MISINFORMATION_BOT_2: "#CC0000",  # Darker red for second strain
        State.MISINFORMATION_BOT_3: "#990000",  # Even darker red for third strain
        State.SUSCEPTIBLE: "#008000",  # Green for susceptible users
        State.RESISTANT: "#808080",  # Gray for resistant users
        State.FACT_CHECKER: "#0000FF",  # Blue for fact-checkers
    }

    # Assign misinformed users **shades of pink** based on the infecting strain
    if agent.state == State.MISINFORMED_USER:
        if agent.infecting_strain == State.MISINFORMATION_BOT:
            color = "#FFB6C1"  # Light Pink for strain 1
        elif agent.infecting_strain == State.MISINFORMATION_BOT_2:
            color = "#FF69B4"  # Hot Pink for strain 2
        elif agent.infecting_strain == State.MISINFORMATION_BOT_3:
            color = "#C71585"  # Deep Pink for strain 3
        else:
            color = "#FFB6C1"  # Default to Light Pink if untracked
    else:
        color = node_color_dict.get(agent.state, "#FFFFFF")  # Default white if undefined

    portrayal = {
        "color": color,
        "size": 10,
    }

    # Make misinformation bots squares
    if agent.state in [State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3]:
        portrayal["shape"] = "square"
        portrayal["marker"] = "s"  # Square marker for misinformation bots
        portrayal["size"] = 20

    return portrayal


# Define model parameters with sliders
model_params = {
    "num_nodes": Slider(label="Number of agents", value=50, min=10, max=200, step=1),
    "avg_node_degree": Slider(label="Avg Node Degree", value=3, min=1, max=10, step=1),
    "initial_misinformation_bots": Slider(label="Number of Misinformation Bots", value=1, min=1, max=10, step=1),
    "fact_checker_ratio": Slider(label="Fact Checker Ratio", value=0.011, min=0.01, max=0.1, step=0.01),
    "virus_spread_chance": Slider(label="Misinformation Spread Chance", value=0.4, min=0.0, max=1.0, step=0.1),
    "virus_check_frequency": Slider(label="Fact Check Frequency", value=0.4, min=0.0, max=1.0, step=0.1),
    "resistance_duration": Slider(label="Resistance Duration", value=6, min=1, max=10, step=1),
}


# Space Visualization
SpacePlot = make_space_component(agent_portrayal)

# State Plot: Tracks the number of different agent types
StatePlot = make_plot_component(
    {
        "Misinformation Bots (Strain 1)": "#FF0000",  # Red
        "Misinformation Bots (Strain 2)": "#CC0000",  # Darker Red
        "Misinformation Bots (Strain 3)": "#990000",  # Even Darker Red
        "Misinformed (Strain 1)": "#FFB6C1",  # Light Pink
        "Misinformed (Strain 2)": "#FF69B4",  # Hot Pink
        "Misinformed (Strain 3)": "#C71585",  # Deep Pink
        "Susceptible": "#008000",  # Green
        "Resistant": "#808080",  # Gray
        "Fact Checkers": "#0000FF",  # Blue
    }
)

# Infection Rate Plot: Tracks spread rate of misinformation
InfectionPlot = make_plot_component(
    {
        "User Misinformation Reproduction Rate": "#FF69B4",  # Matches hot pink
        "Bot Misinformation Reproduction Rate": "#990000",  # Dark red
    }
)

# Initialize the Model
model = VirusOnNetwork()

@solara.component
def Page():
    with solara.Column():
        solara.Markdown("## Disclaimer")
        solara.Markdown("- Squares represent bot agents.")
        solara.Markdown("- Circles represent human user agents.")

        solara.Markdown("---") # Add a horizontal line to separate the disclaimer

        page = SolaraViz(
            model,
            components=[SpacePlot, StatePlot, InfectionPlot],
            model_params=model_params,
            name="Misinformation Model",
        )

# Use the Page component as the main Solara page
Page()
