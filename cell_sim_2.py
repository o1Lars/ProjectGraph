from __future__ import annotations         # To adjust the Python version to be default (3.10)
import random                            # import the built-in random module
import ui                                   # import ui module provided by the instructor
from model_ph1 import Cell, Patch               # from model file import the classes Cell and patch
from visualiser import Visualiser           # from visualiser import the class visualiser


def main():
    """Main function of program, directing the three stages of execution."""
    config = Configuration()
    while True:
        try:
            config.menu()               # stage 1, configuration
            sim = Simulation(config)    # stage 2, simulation
            ui.wait()                   # stage 3, reporting
        except KeyboardInterrupt:
            ui.wait("Simulation aborted.")


class Configuration:
    """Defines and configures parameters for simulation."""

    def __init__(self:Configuration):
        """Set default/base config attributes."""
        # [name, input function, min val, max val, default val]
        self._config_base = [
            ['Grid rows', int, 5, 150, 15],
            ['Grid columns', int, 5, 250, 25],
            ['Initial population', int, 1, 100, 2],
            ['Age limit', int, 1, 1000, 10],
            ['Division limit', int, 1, 1000, 2],
            ['Division probability', float, 0.0, 1.0, 0.2],
            ['Division cooldown', int, 0, 1000, 2],
            ['Time limit', int, 1, 1000, 100]
        ]
        self._visual = True
        self._current = 'Default'
        self.set_from_list([b[4] for b in self._config_base])

    
    def menu(self:Configuration):
        """Display main menu."""

        done = False

        while not done:

            s = 'Enabled' if self._visual else 'Disabled'
            c = self._current
            items = {
                'Run simulation': lambda: True,
                'Toggle visualisation (status: %s)' % (s): self.change_visual,
                'Change configuration (current: %s)' % (c): self.change_config,
                'Display configuration details': self.display_config
            }

            ui.title("Please select action:")
            try:
                done = items[ui.select(items.keys(), "exit")]()
            except KeyboardInterrupt:
                ui.goodbye()


    def change_visual(self:Configuration):
        """Toggle visualisation boolean."""
        self._visual = not self._visual


    def change_config(self:Configuration):
        """Change configuration template."""

        while True:

            # config templates
            configs = {
                'Default': [b[4] for b in self._config_base],
                'Custom': None,
                'Dying crawlers': [150, 250, 100, 1, 1, .9, 0, 100],
                'Enochlophobia': [100, 100, 1, 1000, 1000, 1.0, 0, 75],
                'Forever lonely': [150, 250, 1, 1, 1, 1.0, 0, 1000],
                'Surprise me!': [
                    random.randrange(b[2] * 10, b[3] * 10 + 1, b[3]) / 10
                    for b in self._config_base
                ]
            }

            # select config
            ui.title("Please select configuration:")
            try:
                self._current = ui.select(
                    dict(zip(configs.keys(), [
                        "(current)" if k == self._current else ""
                        for k in configs.keys()
                    ]))
                )
                if self._current == 'Custom':
                    self.custom_config()
                else:
                    self.set_from_list(configs[self._current])
            except KeyboardInterrupt:
                return


    def display_config(self:Configuration):
        """Display current configuration values."""
        ui.title("Configuration: %s" % (self._current))
        ui.table(self._config.keys(), self._config.values(),
                 right_align = [0, 1])
        ui.wait()


    def custom_config(self:Configuration):
        """Display custom menu for user defined configuration."""
        while True:
            ui.title("Please select value to customize:")
            try:
                self.custom_config_item(ui.select(self._config))
            except KeyboardInterrupt:
                return


    def custom_config_item(self:Configuration, item):
        """Edit configuration item/value based on user input."""
        base = [base for base in self._config_base if base[0] == item][0]
        try:
            value = ui.valid_input(
                base[1],
                lambda x: base[2] <= x <= base[3],
                "a number between %s and %s" % (base[2], base[3]),
                "Enter new value [%s - %s]:" % (base[2], base[3])
            )
            self._config[item] = value
        except KeyboardInterrupt:
            return


    def set_from_list(self:Configuration, config:list):
        """Sets configuration from ordered list."""
        config = dict(zip(
            [base[0] for base in self._config_base],
            [self._config_base[i][1](config[i]) for i in range(0, len(config))]
        ))
        self._config = config


    def set_from_dict(self:Configuration, config:dict):
        """Sets configuration from dictionary."""
        self._config |= config


    def get(self:Configuration, key:str):
        """Returns configuration value."""
        return self._config[key] if key != 'Visualisation' else self._visual


class Simulation:                              # class for Simulation
    """Contains and executes all simulation logic."""

    def __init__(self:Simulation, config:Configuration):
        """Prepares and runs simulation upon initialization."""
        self._config = config                 # attribute of Class
        self._cells = []                      # an empty list of cells
        self._patches = []                    # an empty list of Patches
        self._stats = {'Total cells': 0, 'Total deaths': 0}
        self._ticks = 0
        self.create_grid()                     # step 1, create the grid
        self.populate()                        # step 2, populate it
        self.run()                             # step 3, run simulation

    
    def create_grid(self:Simulation)->None:   #None means it should only return none
        """Create grid of patches."""
        self._patches = [
            [
                Patch(row, col)
                for col in range(self.cols())
            ]
            for row in range(self.rows())
        ]

    
    def populate(self:Simulation)->None:
        """Create initial population of cells in random patches."""
        k = min(len(p := self.patches()), self.config('Initial population'))
        patches = random.sample(p, k == k)
        for patch in patches:
            self.add_cell(Cell(patch))


    def run(self:Simulation):
        """Ticks for as long as there is live cells and still time."""
        while self.cells():
            tick = self.tick()
            self.report()
            self.visualise()
            if tick >= self.config('Time limit'):
                break


    def tick(self:Simulation):
        """Perform a tick's worth of possible cell actions."""
        # all cells finish each step before next step
        for cell in (cells := [cell for cell in self.cells()]):
            self.attempt_division(cell)
        for cell in cells:
            cell.tick()
        for cell in cells:
            self.correct_overcrowding(cell)
        for cell in self.cells():
            self.trigger_death(cell)
        self._ticks += 1
        return self._ticks

    def attempt_division(self:Simulation, cell:Cell):
        """Attempts division for cell based on given criteria."""

        # fail if no available adjacent patches for 'offspring'
        if not (available := self.available_patches(cell)):
            return

        # fail if division limit reached
        if cell.divisions() >= self.config('Division limit'):
            return

        # fail if cooldown still active from last division
        if (cell.last_division() <= self.config('Division cooldown')
            and cell.divisions() > 0):
            return

        # fail if chance does not permit
        if random.random() > self.config('Division probability'):
            return

        # divide into random available adjacent patch
        self.add_cell(cell.divide(random.choices(available, k = 1)[0]))


    def correct_overcrowding(self:Simulation, cell:Cell):
        """Fix potentially overcrowded neighbourhood by killing random cell."""

        # unnecessary if neighbourhood is not overcrowded
        if self.available_patches(cell):
            return

        # random (age weighted) cell in neighbourhood will be triggered to die
        cells = [patch.cell() for patch in self.neighbourhood(cell.patch())]
        weights = [cell.age() for cell in cells]
        self.trigger_death(
            random.choices(cells, weights = weights, k = 1)[0],
            overcrowding = True
        )


    def trigger_death(self:Simulation, cell:Cell, overcrowding:bool = False):
        """Triggers death of cell if valid cause."""

        # no cause yet
        cause = False

        # age related
        if cell.age() >= self.config('Age limit'):
            cause = self.track('Death by age limit')

        # division exhaustion
        if cell.divisions() >= self.config('Division limit'):
            cause = self.track('Death by division limit')
        
        # victim of overcrowding
        if overcrowding:
            cause = self.track('Death by overcrowding')
        
        if cause:
            cell.die()
            self.remove_cell(cell)


    def config(self:Simulation, key:str):
        """Returns configuration value for given key."""
        return self._config.get(key)

    
    def rows(self:Simulation):
        """Returns configuration value for 'Grid rows'."""
        return self.config('Grid rows')


    def cols(self:Simulation):
        """Returns configuration value for 'Grid columns'."""
        return self.config('Grid columns')


    def patches(self:Simulation)->list[Patch]:
        """Returns flat list of patches in grid."""
        return [patch for rows in self._patches for patch in rows]


    def patch(self:Simulation, row:int, col:int)->Patch:
        """Returns patch at row, col coordinate in grid."""
        return self._patches[row][col]

    
    def add_cell(self:Simulation, cell:Cell):
        """Adds cell to list of live cells."""
        self._cells.append(cell)
        self.track('Total cells')

    
    def remove_cell(self:Simulation, cell:Cell):
        """Removes cell from list of live cells."""
        self._cells.remove(cell)
        self.track('Total deaths')


    def cells(self:Simulation):
        """Returns list of live cells."""
        return self._cells


    def track(self:Simulation, key:str, i:int = 1)->int:
        """Increments stat and returns new value."""
        self._stats[key] = i + (self._stats[key] if key in self._stats else 0)

        return self._stats[key]

    
    def neighbourhood(self:Simulation, patch:Patch)->list[Patch]:
        """Returns list of 3x3 neighbourhood for given patch."""

        # calculate neighbourhood rows
        rows = [patch.row() - 1 if patch.row() > 0 else self.rows() - 1,
                patch.row(),
                patch.row() + 1 if patch.row() + 1 < self.rows() else 0]

        # calculate neighbourhood columns
        cols = [patch.col() - 1 if patch.col() > 0 else self.cols() - 1,
                patch.col(),
                patch.col() + 1 if patch.col() + 1 < self.cols() else 0]

        return [self.patch(row, col) for row in rows for col in cols]


    def available_patches(self:Simulation, cell:Cell)->list[Patch]:
        """Returns list of available patches adjacent to given cell."""
        return [
            patch
            for patch in self.neighbourhood(cell.patch())
            if not patch.has_cell()
        ]


    def report(self:Simulation):
        """Update stats display."""
        tick = self._ticks
        limit = self.config('Time limit')
        percent = round(100 * tick / limit, 1)
        ui.title("Tick progress: %d/%d (%s%%)" % (tick, limit, percent))
        ui.table(self._stats.keys(), self._stats.values())
        ui.ctrlc("abort")


    def visualise(self:Simulation):
        """Create and update Visualiser object if configured."""
        if not self.config('Visualisation'):
            return
        if not hasattr(self, '_visual'):
            self._visual = Visualiser(
                self.patches(),
                self.rows(),
                self.cols(),
                False,
                False
            )
        self._visual.update()


# if cell_sim is the main module, run main()
if __name__ == '__main__':
    main()