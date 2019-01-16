class MazeFactory:
    def __init__(self):
        self.Default = "random"
        self.Choices = ["random", "rightpriority"]

    def importmaze(self, algorithm):
        if algorithm == "random":
            import Random
            return ["Random values for the maze", Random.create]
        elif algorithm == "rightpriority":
            import RightPriority
            return ["Prioritorize going right", RightPriority.create]