import math
import networkx as nx
import mesa
from mesa import Model
from agents import State, VirusAgent


def number_state(model, state):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state is state)


def number_misinformation_bots(model):
    return number_state(model, State.MISINFORMATION_BOT)


def number_misinformed(model):
    return number_state(model, State.MISINFORMED_USER)


def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)


def number_resistant(model):
    return number_state(model, State.RESISTANT)


def number_fact_checkers(model):
    return number_state(model, State.FACT_CHECKER)


class VirusOnNetwork(Model):
    """A misinformation spread model with all agent types including misinformation bots."""


    def __init__(
        self,
        num_nodes=10,
        avg_node_degree=3,
        initial_outbreak_size=1,
        virus_spread_chance=0.4,
        virus_check_frequency=0.4,
        recovery_chance=0.3,
        gain_resistance_chance=0.5,
        fact_checker_ratio=0.1,
        misinformation_bot_ratio=0.1,
        seed=None,
    ):
        super().__init__(seed=seed)
        self.num_nodes = num_nodes
        prob = avg_node_degree / self.num_nodes
        self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
        while not nx.is_connected(self.G):
            self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
       
        self.grid = mesa.space.NetworkGrid(self.G)


        self.datacollector = mesa.DataCollector(
            {
                "Misinformation Bots": number_misinformation_bots,
                "Misinformed": number_misinformed,
                "Susceptible": number_susceptible,
                "Resistant": number_resistant,
                "Fact Checkers": number_fact_checkers,
            }
        )


        for node in self.G.nodes():
            if self.random.random() < fact_checker_ratio:
                state = State.FACT_CHECKER
            elif self.random.random() < misinformation_bot_ratio:
                state = State.MISINFORMATION_BOT
            else:
                state = State.SUSCEPTIBLE


            a = VirusAgent(
                self,
                state,
                virus_spread_chance,
                virus_check_frequency,
                recovery_chance,
                gain_resistance_chance,
            )
            self.grid.place_agent(a, node)


        infected_nodes = self.random.sample(list(self.G), initial_outbreak_size)
        for a in self.grid.get_cell_list_contents(infected_nodes):
            a.state = State.MISINFORMED_USER


        self.running = True
        self.datacollector.collect(self)


    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
