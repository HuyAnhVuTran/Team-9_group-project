import math
import solara

from model import (
    State,
    VirusOnNetwork,
    Strain,
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
        State.MISINFORMATION_BOT: "#FF0000",  # Red for misinformation bots
        State.MISINFORMED_USER: "#FFD700",    # Yellow for misinformed users
        State.SUSCEPTIBLE: "#008000",         # Green for susceptible users
        State.RESISTANT: "#808080",           # Gray for resistant users
        State.FACT_CHECKER: "#0000FF",        # Blue for fact-checkers
    }
    # return {"color": node_color_dict[agent.state], "size": 10}

    portrayal = {
        "color": node_color_dict[agent.state],
        "size": 10,
    }

    # Special handling for misinformation bots to use their strain color
    if agent.state == State.MISINFORMATION_BOT:
        # Override with strain color if available
        if hasattr(agent, 'strain'):  # Ensure the bot has a 'strain' attribute
            if agent.strain == Strain.STRAIN_A:
                portrayal["color"] = node_color_dict.get(Strain.STRAIN_A, "#FF4D4D")  # Red for strain A
            elif agent.strain == Strain.STRAIN_B:
                portrayal["color"] = node_color_dict.get(Strain.STRAIN_B, "#FF8C00")  # Orange for strain B
            elif agent.strain == Strain.STRAIN_C:
                portrayal["color"] = node_color_dict.get(Strain.STRAIN_C, "#FF66B2")  # Pink for strain C
        
        portrayal["marker"] = "s"
        portrayal["size"] = 20  # Larger size for misinformation bots

    # Special handling for misinformed users to use their strain color
    if agent.state == State.MISINFORMED_USER:
        # Override with strain color if available
        if hasattr(agent, 'strain'):  # Ensure the user has a 'strain' attribute
            if agent.strain == Strain.STRAIN_A:
                portrayal["color"] = node_color_dict.get(Strain.STRAIN_A, "#FF4D4D")  # Red for strain A
            elif agent.strain == Strain.STRAIN_B:
                portrayal["color"] = node_color_dict.get(Strain.STRAIN_B, "#FF8C00")  # Orange for strain B
            elif agent.strain == Strain.STRAIN_C:
                portrayal["color"] = node_color_dict.get(Strain.STRAIN_C, "#FF66B2")  # Pink for strain C
        

    return portrayal




model_params = {
    "num_nodes": Slider(label="Number of agents", value=50, min=10, max=200, step=1),
    "avg_node_degree": Slider(label="Avg Node Degree", value=3, min=1, max=10, step=1),
    "initial_misinformation_bots": Slider(label="Number of Misinformation Bots", value=1, min=1, max=10, step=1),
    # "initial_fact_checkers": Slider(label="Number of Fact Checkers", value=1, min=1, max=10, step=1),
    "fact_checker_ratio": Slider(label="Fact Checker Ratio", value=0.011, min=0.01, max=0.1, step=0.01),
    "misinformation_spread_chance": Slider(label="Misinformation Spread Chance", value=0.4, min=0.0, max=1.0, step=0.1),
    "fact_check_chance": Slider(label="Fact Check Chance", value=0.4, min=0.0, max=1.0, step=0.1),
    # "recovery_chance": Slider(label="Recovery Chance", value=0.3, min=0.0, max=1.0, step=0.1),
    # "gain_resistance_chance": Slider(label="Gain Resistance Chance", value=0.5, min=0.0, max=1.0, step=0.1),
    "resistance_duration": Slider(label="Resistance Duration", value=6, min=1, max=10, step=1),
}


SpacePlot = make_space_component(agent_portrayal)
StatePlot = make_plot_component(
    {
        "Misinformation Bots": "#FF0000",  # Red
        "Total Misinformation": "#FFD700",          # Yellow
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

StrainPlot = make_plot_component(
    {
        "Misinformed (Strain A)": "#FF4D4D",  # Red
        "Misinformed (Strain B)": "#FF8C00",  # Orange
        "Misinformed (Strain C)": "#FF66B2",  # Pink
    }
)

model = VirusOnNetwork()


# page = SolaraViz(
#     model,
#     components=[SpacePlot, StatePlot, InfectionPlot],
#     model_params=model_params,
#     name="Misinformation Model",
# )

@solara.component
def Page():
    with solara.Column():
        solara.Markdown("## Disclaimer")
        solara.Markdown("- Squares represent bot agents.")
        solara.Markdown("- Circles represent human user agents.")

        solara.Markdown("---") # Add a horizontal line to separate the disclaimer

        page = SolaraViz(
            model,
            components=[SpacePlot, StatePlot, InfectionPlot, StrainPlot],
            model_params=model_params,
            name="Misinformation Model",
        )

# Use the Page component as the main Solara page
Page()


