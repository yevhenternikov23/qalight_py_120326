class QuestRoom:
    def __init__(self, name, level_dificulty, player_limit):
        if level_dificulty < 1 or level_dificulty > 5:
            raise ValueError("Difficulty should be between 1 and 5")

        self.name = name
        self.level_dificulty = level_dificulty
        self.player_limit = player_limit
        self.players = []
        self.status = "waiting"
        self.events_log = []

    def add_player(self, name):
        if len(self.players) >= self.player_limit:
            return "No free slots!"
        
        self.players.append(name)
        self.events_log.append(f"Player {name} joined")
        return f"Player {name} joined"

    def remove_player(self, name):
        if name in self.players:
            self.players.remove(name)
            self.events_log.append(f"Player {name} left")
            return f"Player {name} left"
        
        return f"Player not found"

    def is_full(self):
        if len(self.players) >= self.player_limit:
            return True
        else:
            return False

    def free_slots(self):
        return self.player_limit - len(self.players)

    def reset_room(self):
        self.players.clear()
        self.status = "finished"
        self.status = "waiting"
        self.events_log.append("Room reset")
        return "Room reset"

    def players_list(self):
        if len(self.players) == 0:
            return "No players in the room"
        else:
            return self.players

    def start(self):
        if len(self.players) == 0:
            return "Room is empty"
        
        self.status = "active"
        message = f"Quest '{self.name}' started with {len(self.players)} players!"
        self.events_log.append(message)
        return message

    def show_log(self):
        return self.events_log

    def __str__(self):
        return f"QuestRoom: {self.name} | Difficulty: {self.level_dificulty} | Players: {len(self.players)} / {self.player_limit}"

room = QuestRoom("Піратський острів", 3, 4)

print(room.add_player("Олег"))
print(room.add_player("Даша"))
print(room.start())
print(room)
print(room.show_log())