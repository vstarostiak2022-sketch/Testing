class Figure:
    FIGURES = ["triangle", "square", "rectangle"]

    def __init__(self, type, length):
        assert length > 0, "Length must be greater than 0"
        assert type in self.FIGURES, f"Allowed figures: {', '.join(self.FIGURES)}"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length  # виправлено помилку

    @property
    def get_angles(self):
        if self.type in ["square", "rectangle"]:
            return 4
        if self.type == "triangle":
            return 3
