import math
import networkx as nx
import mesa
from mesa import Model
from agents import State, VirusAgent


def number_state(model, state):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state is state)


def number_misinformation_bots(model):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state in [State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3])

def number_misinformation_bots_2(model):
    return number_state(model, State.MISINFORMATION_BOT_2)

def number_misinformation_bots_3(model):
    return number_state(model, State.MISINFORMATION_BOT_3)
    return number_state(model, State.MISINFORMATION_BOT)


def number_misinformed(model):
    return number_state(model, State.MISINFORMED_USER)


def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)


def number_resistant(model):
    return number_state(model, State.RESISTANT)


def number_fact_checkers(model):
    return number_state(model, State.FACT_CHECKER)


def number_userInfected(model):
    return model.userInfected


def number_botInfected(model):
    return model.botInfected

def reproduction_userInfected(model):
    num_misinformed = number_misinformed(model)
    if num_misinformed == 0:
        return 0  # Return a default value to avoid division by zero
    return model.userInfected / num_misinformed

def reproduction_botInfected(model):
    num_misinformed = number_misinformed(model)
    if num_misinformed == 0:
        return 0  # Return a default value to avoid division by zero
    return model.botInfected / num_misinformed



class VirusOnNetwork(Model):
    """A misinformation spread model with all agent types including misinformation bots."""


    def __init__(
        self,
        num_nodes=10,
        avg_node_degree=3,
        initial_outbreak_size=1,
        initial_misinformation_bots=1,  # Add this parameter
        # initial_fact_checkers=1,        # Add this parameter
        virus_spread_chance=0.4,
        virus_check_frequency=0.4,
        # recovery_chance=0.3,
        # gain_resistance_chance=0.5,
        resistance_duration=6,
        fact_checker_ratio=0.1,
        misinformation_bot_ratio=0.1,
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


        self.datacollector = mesa.DataCollector(
    {
        "Misinformation Bots (Strain 1)": number_misinformation_bots,
        "Misinformation Bots (Strain 2)": number_misinformation_bots_2,
        "Misinformation Bots (Strain 3)": number_misinformation_bots_3,
        "Misinformed": number_misinformed,
        "Susceptible": number_susceptible,
        "Resistant": number_resistant,
        "Fact Checkers": number_fact_checkers,
        "User Misinformation Reproduction Rate": reproduction_userInfected,
        "Bot Misinformation Reproduction Rate": reproduction_botInfected,
    }
    )



        # for node in self.G.nodes():
        #     if self.random.random() < fact_checker_ratio:
        #         state = State.FACT_CHECKER
        #     elif self.random.random() < misinformation_bot_ratio:
        #         state = State.MISINFORMATION_BOT
        #     else:
        #         state = State.SUSCEPTIBLE

        # Calculate the number of fact checkers based on the ratio and ensure at least one
        initial_fact_checkers = max(1, int(fact_checker_ratio * self.num_nodes))

        # Ensure at least one misinformation bot and one fact checker
        nodes = list(self.G.nodes())
        self.random.shuffle(nodes)

        misinformation_bot_count = 0
        fact_checker_count = 0

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

            a = VirusAgent(
                self,
                state,
                virus_spread_chance,
                virus_check_frequency,
                # recovery_chance,
                # gain_resistance_chance,
                resistance_duration,
            )
            self.grid.place_agent(a, node)


        # infected_nodes = self.random.sample(list(self.G), initial_outbreak_size)
        # for a in self.grid.get_cell_list_contents(infected_nodes):
        #     a.state = State.MISINFORMED_USER


        self.running = True
        self.datacollector.collect(self)
        global stepCount
        stepCount = 0


    def step(self):
        global stepCount
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
        # Debugging statements to verify data collection
        print(f"Step {stepCount}: User Infected Rate = {reproduction_userInfected(self):.2%}, Bot Infected Rate = {reproduction_botInfected(self):.2%}")
        self.userInfected = 0
        self.botInfected = 0
        stepCount += 1
