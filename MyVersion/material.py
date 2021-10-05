class Material:
    def __init__(self, color, ambient, diffuse, spectular) -> None:
        self.color = color  # base color used
        self.ambient = ambient  # how much does it reflect back
        self.diffuse = diffuse  # what color it reflects back
        self.spectular = spectular  # what color of spectular light
