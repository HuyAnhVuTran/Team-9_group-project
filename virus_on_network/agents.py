from enum import Enum
from mesa import Agent

class State(Enum):
    SUSCEPTIBLE = 0            # Users not yet exposed to misinformation
    MISINFORMED_USER = 1        # Users who believe and spread misinformation
    RESISTANT = 2               # Users resistant to misinformation
    FACT_CHECKER = 3            # Users who actively fact-check misinformation
    MISINFORMATION_BOT = 4      # Misinformation bots that primarily spread falsehoods
    MISINFORMATION_BOT_2 = 5    # Second strain of misinformation
    MISINFORMATION_BOT_3 = 6    # Third strain of misinformation


class VirusAgent(Agent):
    """Individual Agent definition and its properties/interaction methods."""

    def __init__(
        self,
        model,
        initial_state,
        virus_spread_chance,
        virus_check_frequency,
        resistance_duration,
    ):
        super().__init__(model)
        self.state = initial_state
        self.virus_spread_chance = virus_spread_chance
        self.virus_check_frequency = virus_check_frequency
        self.influence_chance = virus_check_frequency * 0.7
        self.resistance_duration = resistance_duration
        self.resistance_counter = 0

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
                if self.state == State.MISINFORMATION_BOT:
                    a.state = State.MISINFORMED_USER
                    self.model.botInfected += 1
                elif self.state == State.MISINFORMATION_BOT_2:
                    a.state = State.MISINFORMED_USER
                    self.model.botInfected_2 += 1
                elif self.state == State.MISINFORMATION_BOT_3:
                    a.state = State.MISINFORMED_USER
                    self.model.botInfected_3 += 1
                elif self.state == State.MISINFORMED_USER:
                    self.model.userInfected += 1

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
                a.resistance_counter = self.resistance_duration

    def try_influence_misinformed(self):
        neighbors_nodes = self.model.grid.get_neighborhood(
            self.pos, include_center=False
        )
        misinformed_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.MISINFORMED_USER
        ]
        for a in misinformed_neighbors:
            if self.random.random() < self.influence_chance:
                a.state = State.RESISTANT
                a.resistance_counter = self.resistance_duration

    def step(self):
        if self.state in [State.MISINFORMED_USER, State.MISINFORMATION_BOT, State.MISINFORMATION_BOT_2, State.MISINFORMATION_BOT_3]:
            self.try_to_infect_neighbors()
        elif self.state == State.FACT_CHECKER:
            self.try_fact_check()
        elif self.state == State.RESISTANT:
            self.try_influence_misinformed()
            self.resistance_counter -= 1
            if self.resistance_counter <= 0:
                self.state = State.SUSCEPTIBLE
