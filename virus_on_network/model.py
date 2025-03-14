import math
import networkx as nx
import mesa
from mesa import Model
from agents import State, VirusAgent

# Function to count agents in a specific state
def number_state(model, state):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state == state)

# Restore `number_userInfected` and `number_botInfected`
def number_userInfected(model):
    return model.userInfected

def number_botInfected(model):
    return model.botInfected

# Restore `number_misinformed` to count all misinformed users
def number_misinformed(model):
    return number_state(model, State.MISINFORMED_USER)

# Count misinformed users **by strain**
def number_misinformed_strain_1(model):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state == State.MISINFORMED_USER and a.infecting_strain == State.MISINFORMATION_BOT)

def number_misinformed_strain_2(model):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state == State.MISINFORMED_USER and a.infecting_strain == State.MISINFORMATION_BOT_2)

def number_misinformed_strain_3(model):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state == State.MISINFORMED_USER and a.infecting_strain == State.MISINFORMATION_BOT_3)

# Other count functions
def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)

def number_resistant(model):
    return number_state(model, State.RESISTANT)

def number_fact_checkers(model):
    return number_state(model, State.FACT_CHECKER)

def number_misinformation_bots(model):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state in [State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3])

# Define Virus Model
class VirusOnNetwork(Model):
    """A misinformation spread model with all agent types."""

    def __init__(
        self,
        num_nodes=10,
        avg_node_degree=3,
        initial_misinformation_bots=1,
        virus_spread_chance=0.4,
        virus_check_frequency=0.4,
        resistance_duration=6,
        fact_checker_ratio=0.1,
        seed=None,
    ):
        super().__init__(seed=seed)
        self.num_nodes = num_nodes
        prob = avg_node_degree / self.num_nodes
        self.userInfected = 0
        self.botInfected = 0
        self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)

        while not nx.is_connected(self.G):
            self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)

        self.grid = mesa.space.NetworkGrid(self.G)

        # **Updated Data Collector with All Misinformed Counts**
        self.datacollector = mesa.DataCollector(
            {
                "Misinformation Bots (Strain 1)": lambda m: number_state(m, State.MISINFORMATION_BOT),
                "Misinformation Bots (Strain 2)": lambda m: number_state(m, State.MISINFORMATION_BOT_2),
                "Misinformation Bots (Strain 3)": lambda m: number_state(m, State.MISINFORMATION_BOT_3),
                "Misinformed": number_misinformed,  # Total misinformed count
                "Misinformed (Strain 1)": number_misinformed_strain_1,
                "Misinformed (Strain 2)": number_misinformed_strain_2,
                "Misinformed (Strain 3)": number_misinformed_strain_3,
                "Susceptible": number_susceptible,
                "Resistant": number_resistant,
                "Fact Checkers": number_fact_checkers,
                "User Misinformation Reproduction Rate": number_userInfected,  # Restored function
                "Bot Misinformation Reproduction Rate": number_botInfected,  # Restored function
            }
        )

        # Calculate the number of fact checkers based on the ratio, ensuring at least one
        initial_fact_checkers = max(1, int(fact_checker_ratio * self.num_nodes))

        # Ensure at least one misinformation bot and one fact checker
        nodes = list(self.G.nodes())
        self.random.shuffle(nodes)

        misinformation_bot_count = 0
        fact_checker_count = 0

        # Add three named misinformed users with different strains
        for i in range(3):
            misinformed_agent = VirusAgent(
                self, 
                State.MISINFORMED_USER, 
                virus_spread_chance, 
                virus_check_frequency, 
                resistance_duration,
                name=f"Misinformed User {i+1}"
            )
            misinformed_agent.infecting_strain = [State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3][i]
            self.grid.place_agent(misinformed_agent, nodes.pop())

        # Assign other agents
        for i, node in enumerate(nodes):
            if misinformation_bot_count < initial_misinformation_bots:
                if misinformation_bot_count % 3 == 0:
                    state = State.MISINFORMATION_BOT
                elif misinformation_bot_count % 3 == 1:
                    state = State.MISINFORMATION_BOT_2
                else:
                    state = State.MISINFORMATION_BOT_3
                misinformation_bot_count += 1
            elif fact_checker_count < initial_fact_checkers:
                state = State.FACT_CHECKER
                fact_checker_count += 1
            else:
                state = State.SUSCEPTIBLE

            agent = VirusAgent(
                self,
                state,
                virus_spread_chance,
                virus_check_frequency,
                resistance_duration,
            )
            self.grid.place_agent(agent, node)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        """Advance the model by one step."""
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
