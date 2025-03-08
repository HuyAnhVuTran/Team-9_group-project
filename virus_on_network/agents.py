from enum import Enum
from mesa import Agent


class State(Enum):
    SUSCEPTIBLE = 0            # Users not yet exposed to misinformation
    MISINFORMED_USER = 1        # Users who believe and spread misinformation
    RESISTANT = 2               # Users resistant to misinformation
    FACT_CHECKER = 3            # Users who actively fact-check misinformation
    MISINFORMATION_BOT = 4      # Misinformation bots that primarily spread falsehoods


class VirusAgent(Agent):
    """Individual Agent definition and its properties/interaction methods."""


    def __init__(
        self,
        model,
        initial_state,
        virus_spread_chance,
        virus_check_frequency,
        recovery_chance,
        gain_resistance_chance,
    ):
        super().__init__(model)
        self.state = initial_state
        self.virus_spread_chance = virus_spread_chance
        self.virus_check_frequency = virus_check_frequency
        self.recovery_chance = recovery_chance
        self.gain_resistance_chance = gain_resistance_chance


    def try_to_infect_neighbors(self):
        neighbors_nodes = self.model.grid.get_neighborhood(
            self.pos, include_center=False
        )
        susceptible_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.SUSCEPTIBLE
        ]
        for a in susceptible_neighbors:
            if self.random.random() < self.virus_spread_chance:
                a.state = State.MISINFORMED_USER


    def try_gain_resistance(self):
        if self.random.random() < self.gain_resistance_chance:
            self.state = State.RESISTANT


    def try_remove_infection(self):
        if self.random.random() < self.recovery_chance:
            self.state = State.SUSCEPTIBLE
            self.try_gain_resistance()
        else:
            self.state = State.MISINFORMED_USER


    def try_fact_check(self):
        neighbors_nodes = self.model.grid.get_neighborhood(
            self.pos, include_center=False
        )
        misinformed_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.MISINFORMED_USER
        ]
        for a in misinformed_neighbors:
            if self.random.random() < self.virus_check_frequency:
                a.state = State.RESISTANT


    def step(self):
        if self.state in [State.MISINFORMED_USER, State.MISINFORMATION_BOT]:
            self.try_to_infect_neighbors()
        elif self.state is State.FACT_CHECKER:
            self.try_fact_check()
        self.try_check_situation()


    def try_check_situation(self):
        if (self.random.random() < self.virus_check_frequency) and (
            self.state is State.MISINFORMED_USER
        ):
            self.try_remove_infection()


