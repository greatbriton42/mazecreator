class mazefactory:
    def __init__(self):
        self.Default = "random"
        self.Choices = ["random"]

    def importmaze(self, algorithm):
        if algorithm == "random":
            import Random
            return ["Random values for the maze", Random.create]