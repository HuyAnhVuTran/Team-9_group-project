from enum import Enum
from mesa import Agent

class State(Enum):
    SUSCEPTIBLE = 0            # Users not yet exposed to misinformation
    MISINFORMED_USER = 1        # Users who believe and spread misinformation
    RESISTANT = 2               # Users resistant to misinformation
    FACT_CHECKER = 3            # Users who actively fact-check misinformation
    MISINFORMATION_BOT = 4      # Misinformation bots that primarily spread falsehoods

class Strain(Enum):
    STRAIN_A = 0
    STRAIN_B = 1
    STRAIN_C = 2

class VirusAgent(Agent):
    """Individual Agent definition and its properties/interaction methods."""


    def __init__(
        self,
        model,
        initial_state,
        misinformation_spread_chance,
        fact_check_chance,
        # recovery_chance,
        # gain_resistance_chance,
        resistance_duration,
        initial_strain = None,
        
    ):
        super().__init__(model)
        self.state = initial_state
        self.strain = initial_strain
        self.prev_strain = None
        self.misinformation_spread_chance = misinformation_spread_chance
        self.fact_check_chance = fact_check_chance
        self.influence_chance = fact_check_chance * 0.7
        self.relapse_chance = 0.3
        # self.recovery_chance = recovery_chance
        # self.gain_resistance_chance = gain_resistance_chance
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
            if self.random.random() < self.misinformation_spread_chance:
                a.state = State.MISINFORMED_USER
                a.strain = self.strain
                a.prev_strain = self.strain
                if self.state is State.MISINFORMATION_BOT:
                    self.model.botInfected += 1
                    # print(f"Bot infected: {botInfected}")
                elif self.state is State.MISINFORMED_USER:
                    self.model.userInfected += 1
                    # print(f"User infected: {userInfected}")

    def try_to_infect_resistant(self):
        neighbors_nodes = self.model.grid.get_neighborhood(
            self.pos, include_center=False
        )
        resistant_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.RESISTANT
        ]
        for a in resistant_neighbors:
            if self.random.random() < self.relapse_chance and a.prev_strain != self.strain:
                print(f"Prev: {a.prev_strain}, Bot: {self.strain}")
                a.state = State.MISINFORMED_USER
                a.strain = self.strain
                if self.state is State.MISINFORMATION_BOT:
                    self.model.botInfected += 1
                    # print(f"Bot infected: {botInfected}")
                elif self.state is State.MISINFORMED_USER:
                    self.model.userInfected += 1
                    # print(f"User infected: {userInfected}")


    # def try_gain_resistance(self):
    #     if self.random.random() < self.gain_resistance_chance:
    #         self.state = State.RESISTANT


    # def try_remove_infection(self):
    #     if self.random.random() < self.recovery_chance:
    #         self.state = State.SUSCEPTIBLE
    #         self.try_gain_resistance()
    #     else:
    #         self.state = State.MISINFORMED_USER


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
            temp = self.random.random()
            # print(f"Random: {temp}, Fact check chance: {self.fact_check_chance}")
            if temp < self.fact_check_chance:
                a.state = State.RESISTANT
                a.strain = None
                a.relapse_chance = self.relapse_chance
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
            temp = self.random.random()
            # print(f"Random: {temp}, influence chance: {self.influence_chance}")
            if temp < self.influence_chance:
                a.state = State.RESISTANT
                a.strain = None
                a.relapse_chance = self.relapse_chance
                a.resistance_counter = self.resistance_duration
    
    def switch_strain(self, new_strain):
        # print(f"Bot switched from {self.strain} to {new_strain}")
        self.strain = new_strain

    def step(self):
        if self.state in [State.MISINFORMED_USER, State.MISINFORMATION_BOT]:
            self.try_to_infect_neighbors()
            self.try_to_infect_resistant()
        elif self.state is State.FACT_CHECKER:
            self.try_fact_check()
        elif self.state is State.RESISTANT:
            self.try_influence_misinformed()
            self.resistance_counter -= 1
            if self.resistance_counter <= 0:
                self.state = State.SUSCEPTIBLE
                self.strain = None
        # self.try_check_situation()


    # def try_check_situation(self):
    #     if (self.random.random() < self.fact_check_chance) and (
    #         self.state is State.MISINFORMED_USER
    #     ):
    #         self.try_remove_infection()