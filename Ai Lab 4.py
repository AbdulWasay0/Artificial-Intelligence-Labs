'''
#TASK 1
def diagnose():
    print("=== Simple Reflex Medical Diagnosis System ===")
    print("Please answer the following questions with yes/no.\n")

    #Common Symptoms
    fever = input("Do you have fever? ").lower()
    cough = input("Do you have cough? ").lower()

    #Questions if you have cough
    sputum = "no"
    if cough == "yes":
        sputum = input("Is the cough with sputum (productive)? ").lower()

    #Other Symptoms
    pain_abdomen = input("Do you have pain in abdomen (especially iliac fossa)? ").lower()
    vomiting = input("Do you have vomiting? ").lower()
    chest_pain = input("Do you have chest pain? ").lower()
    throat_red = input("Are tonsils red and enlarged? ").lower()
    throat_pus = input("Is there pus in tonsils? ").lower()
    xray_patch = input("Does chest X-ray show pneumonic patch? ").lower()

    #Result
    tlc = input("Is TLC (Total leukocyte count) high? ").lower()
    neutrophils = input("Are neutrophils high? ").lower()
    esr = input("Is ESR high? ").lower()

    if fever == "yes":
        #Acute Appendicitis
        if (pain_abdomen == "yes" and vomiting == "yes" and
            tlc == "yes" and neutrophils == "yes" and esr == "yes"):
            print("\nDiagnosis: Acute Appendicitis")
            print("Treatment: Surgery")

        #Pneumonia
        elif (cough == "yes" and sputum == "yes" and chest_pain == "yes" and
              tlc == "yes" and neutrophils == "yes" and esr == "yes"):
            print("\nDiagnosis: Pneumonia")
            if xray_patch == "yes":
                print("X-ray confirms pneumonic patch.")
            print("Treatment: Antibiotics")

        #Acute Tonsillitis
        elif (cough == "yes" and (throat_red == "yes" or throat_pus == "yes")):
            print("\nDiagnosis: Acute Tonsillitis")
            print("Treatment: Anti-allergic + Paracetamol")
            print("If not improved → add antibiotics orally, then IV if still not improved.")

        else:
            print("\nDiagnosis: Not clear from given symptoms/tests.")
            print("Please consult a doctor for further evaluation.")
    else:
        print("\nDiagnosis: No fever → rules don’t match the target diseases.")
        print("Consult a doctor for further evaluation.")

    print("\n=== End of Diagnosis ===")

if __name__ == "__main__":
    diagnose()

'''

'''
#MAM TASK 2
import random

class ModelBasedWumpusAgent:
    def __init__(self, world):
        self.world = world
        self.n = len(world)
        self.m = len(world[0])
        self.x = self.n - 1   # start row (bottom-left)
        self.y = 0            # start col
        self.start = (self.x, self.y)

        # Agent's knowledge (model of the world)
        self.visited = set()
        self.safe = set([self.start])  # start is always safe
        self.danger = set()
        self.path = []  # for returning safely
        self.has_gold = False
        self.max_steps = 50
        self.steps_taken = 0

    def get_adjacent(self, x, y):
        """Return adjacent cells (up, down, left, right)."""
        moves = []
        if x > 0: moves.append(("up", x-1, y))
        if x < self.n-1: moves.append(("down", x+1, y))
        if y > 0: moves.append(("left", x, y-1))
        if y < self.m-1: moves.append(("right", x, y+1))
        random.shuffle(moves)  # random exploration order
        return moves

    def perceive(self, x, y):
        """Perceive the content of current cell."""
        return self.world[x][y]

    def update_model(self, x, y, percept):
        """Update internal state with new percepts."""
        self.visited.add((x, y))
        if percept in ["Pit", "Wumpus"]:
            self.danger.add((x, y))
        else:
            self.safe.add((x, y))

    def choose_action(self):
        """Decide next action based on model."""
        current_percept = self.perceive(self.x, self.y)

        # If gold is here → grab
        if current_percept == "Gold":
            return "grab"

        # Explore adjacent safe, unvisited cells
        for direction, nx, ny in self.get_adjacent(self.x, self.y):
            if (nx, ny) not in self.visited and (nx, ny) not in self.danger:
                return direction

        # If no safe moves → stop
        return "do_nothing"

    def act(self, action):
        """Perform the chosen action."""
        if action == "grab":
            self.has_gold = True
            print("💰 Gold grabbed at:", (self.x, self.y))
            return True

        elif action == "do_nothing":
            print("❌ No safe moves left → FAILURE.")
            return False

        else:
            # move: store current (old) position first
            old_pos = (self.x, self.y)
            if action == "up": self.x -= 1
            elif action == "down": self.x += 1
            elif action == "left": self.y -= 1
            elif action == "right": self.y += 1
            self.path.append(old_pos)
            return True

    def return_to_start(self):
        """Backtrack safely to starting position."""
        print("\nReturning to start safely...")
        while self.path:
            self.x, self.y = self.path.pop()  # reverse steps
            print(f"↩️ Agent moved back to: ({self.x},{self.y})")
        if (self.x, self.y) == self.start:
            print("✅ Returned to start safely. SUCCESS!")
        else:
            print("❌ Could not return to start.")

    def run(self):
        while self.steps_taken < self.max_steps:
            percept = self.perceive(self.x, self.y)
            self.update_model(self.x, self.y, percept)

            print(f"\nStep {self.steps_taken+1}: Agent at ({self.x},{self.y})")
            print("Percept here:", percept)
            print("Visited:", self.visited)
            print("Safe:", self.safe)
            print("Danger:", self.danger)

            action = self.choose_action()
            print("Chosen Action:", action)

            if not self.act(action):
                break

            self.steps_taken += 1

            if self.has_gold:
                self.return_to_start()
                break

            input("Press Enter for next step...")  # pause for viewing


# Example World (4x4) [same as your previous one]
world = [
    ["Empty", "Pit",   "Empty", "Wumpus"],
    ["Empty", "Empty", "Gold",  "Empty"],
    ["Empty", "Pit",   "Empty", "Empty"],
    ["Start", "Empty", "Empty", "Empty"]
]

agent = ModelBasedWumpusAgent(world)
agent.run()

'''

''' 
#Wampus Game with fixed Spawn Point

class WumpusGame:
    def __init__(self, world):
        self.world = world
        self.size = len(world)
        self.x, self.y = self.size - 1, 0
        self.has_gold = False
        self.game_over = False

    def print_world(self):
        print("\nWorld State:")
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i, j) == (self.x, self.y):
                    row.append("A")  # Agent
                elif self.world[i][j] == "Empty":
                    row.append(".")
                elif self.world[i][j] == "Pit":
                    row.append("P")
                elif self.world[i][j] == "Wumpus":
                    row.append("W")
                elif self.world[i][j] == "Gold":
                    row.append("G")
            print(" ".join(row))
        print()

    def move(self, direction):
        new_x, new_y = self.x, self.y
        if direction == "up":
            new_x -= 1
        elif direction == "down":
            new_x += 1
        elif direction == "left":
            new_y -= 1
        elif direction == "right":
            new_y += 1
        else:
            print("Invalid move! Use up/down/left/right.")
            return

        #Check board limits
        if new_x < 0 or new_x >= self.size or new_y < 0 or new_y >= self.size:
            print("Can't move outside the world!")
            return

        self.x, self.y = new_x, new_y
        self.check_cell()

    def check_cell(self):
        cell = self.world[self.x][self.y]
        if cell == "Pit":
            print("☠ Fell into a Pit! Game Over.")
            self.game_over = True
        elif cell == "Wumpus":
            print("Eaten by the Wumpus! Game Over.")
            self.game_over = True
        elif cell == "Gold":
            print("You found the Gold! Now return to Start (bottom-left) to win.")
            self.has_gold = True
            self.world[self.x][self.y] = "Empty"
        elif cell == "Empty":
            print("Safe move.")

        #Check winning condition
        if self.has_gold and (self.x, self.y) == (self.size - 1, 0):
            print("You returned to Start with the Gold. YOU WIN!")
            self.game_over = True

    def play(self):
        print("=== Welcome to Wumpus World ===")
        self.print_world()

        while not self.game_over:
            move = input("Your move (up/down/left/right): ").strip().lower()
            self.move(move)
            self.print_world()


#World Defined
world = [
    ["Pit",   "Empty",  "Empty",  "Pit"],
    ["Empty", "Gold",   "Empty",  "Empty"],
    ["Empty", "Empty",  "Wumpus", "Pit"],
    ["Start", "Pit",    "Empty",  "Empty"]
]

game = WumpusGame(world)
game.play()

'''

'''
#With Random Spawn Location
import random

class WumpusGame:
    def __init__(self, world):
        self.world = world
        self.size = len(world)
        self.x, self.y = self.get_random_safe_spawn()
        self.has_gold = False
        self.game_over = False

    def get_random_safe_spawn(self):
        """Pick a random starting position that is not Pit or Wumpus"""
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.world[x][y] not in ["Pit", "Wumpus"]:
                print(f"Agent spawned at ({x},{y}) safely.")
                return x, y

    def print_world(self):
        print("\nWorld State:")
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i, j) == (self.x, self.y):
                    row.append("A")  # Agent
                elif self.world[i][j] == "Empty":
                    row.append(".")
                elif self.world[i][j] == "Pit":
                    row.append("P")
                elif self.world[i][j] == "Wumpus":
                    row.append("W")
                elif self.world[i][j] == "Gold":
                    row.append("G")
            print(" ".join(row))
        print()

    def move(self, direction):
        new_x, new_y = self.x, self.y
        if direction == "up":
            new_x -= 1
        elif direction == "down":
            new_x += 1
        elif direction == "left":
            new_y -= 1
        elif direction == "right":
            new_y += 1
        else:
            print("Invalid move! Use up/down/left/right.")
            return

        # Check board limits
        if new_x < 0 or new_x >= self.size or new_y < 0 or new_y >= self.size:
            print("Can't move outside the world!")
            return

        self.x, self.y = new_x, new_y
        self.check_cell()

    def check_cell(self):
        cell = self.world[self.x][self.y]
        if cell == "Pit":
            print("☠ Fell into a Pit! Game Over.")
            self.game_over = True
        elif cell == "Wumpus":
            print("Eaten by the Wumpus! Game Over.")
            self.game_over = True
        elif cell == "Gold":
            print("You found the Gold! Now return to Start position to win.")
            self.has_gold = True
            self.world[self.x][self.y] = "Empty"  # remove gold
        elif cell == "Empty":
            print("Safe move.")

        # Winning condition
        if self.has_gold and (self.x, self.y) == (self.spawn_x, self.spawn_y):
            print("You returned to your spawn with the Gold. YOU WIN!")
            self.game_over = True

    def play(self):
        # Remember spawn point for winning condition
        self.spawn_x, self.spawn_y = self.x, self.y
        print("=== Welcome to Wumpus World ===")
        self.print_world()

        while not self.game_over:
            move = input("Your move (up/down/left/right): ").strip().lower()
            self.move(move)
            self.print_world()


# Define the world (same as image)
world = [
    ["Pit",   "Empty",  "Empty",  "Pit"],
    ["Empty", "Gold",   "Empty",  "Empty"],
    ["Empty", "Empty",  "Wumpus", "Pit"],
    ["Empty", "Pit",    "Empty",  "Empty"]
]

game = WumpusGame(world)
game.play()

'''

'''
#TASK 3
class PacmanGame:
    def __init__(self):
        self.size = 4
        # 4x4 grid world (from the figure)
        self.world = [
            ["Pacman", "Cherry", "Food", "Cherry"],
            ["Food", "Ghost", "Empty", "Cherry"],
            ["Cherry", "Food", "Cherry", "Ghost"],
            ["Cherry", "Empty", "Ghost", "Empty"]
        ]
        self.x, self.y = 0, 0  # Pacman starts at cell 0
        self.score = 0
        self.has_power = False
        self.power_steps = 0

    def print_world(self):
        print("\nWorld State:")
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i, j) == (self.x, self.y):
                    row.append("P")  # Pacman position
                elif self.world[i][j] == "Food":
                    row.append(".")
                elif self.world[i][j] == "Cherry":
                    row.append("C")
                elif self.world[i][j] == "Ghost":
                    row.append("G")
                else:
                    row.append(" ")
            print(" | ".join(row))
        print(f"Score: {self.score} | Power: {self.has_power} ({self.power_steps} steps left)")

    def move(self, direction):
        nx, ny = self.x, self.y
        if direction == "up": nx -= 1
        elif direction == "down": nx += 1
        elif direction == "left": ny -= 1
        elif direction == "right": ny += 1

        # Check bounds
        if 0 <= nx < self.size and 0 <= ny < self.size:
            self.x, self.y = nx, ny
            self.consume()
        else:
            print("Wall hit! Can't move there.")

    def consume(self):
        cell = self.world[self.x][self.y]

        if cell == "Food":
            self.score += 10
            print("Ate food! +10 points")
            self.world[self.x][self.y] = "Empty"

        elif cell == "Cherry":
            self.score += 50
            self.has_power = True
            self.power_steps = 5  # power lasts 5 moves
            print("Ate cherry! Ghosts are scared now!")
            self.world[self.x][self.y] = "Empty"

        elif cell == "Ghost":
            if self.has_power:
                self.score += 200
                print("Ghost defeated! +200 points")
                self.world[self.x][self.y] = "Empty"
            else:
                print("Pacman eaten by Ghost! GAME OVER")
                exit()

        # Decrease power steps
        if self.has_power:
            self.power_steps -= 1
            if self.power_steps <= 0:
                self.has_power = False
                print("Power ended. Ghosts are dangerous again.")

    def check_victory(self):
        # Victory if no food or cherry left
        for row in self.world:
            for cell in row:
                if cell in ["Food", "Cherry"]:
                    return False
        return True

    def run(self):
        while True:
            self.print_world()

            if self.check_victory():
                print("\nAll food and cherries eaten! YOU WIN!")
                print(f"Final Score: {self.score}")
                break

            move = input("Move (up/down/left/right): ").lower()
            if move in ["up", "down", "left", "right"]:
                self.move(move)
            else:
                print("Invalid move! Use up/down/left/right.")


# Run the game
if __name__ == "__main__":
    game = PacmanGame()
    game.run()

'''