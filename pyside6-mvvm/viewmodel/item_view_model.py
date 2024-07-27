class ItemViewModel:
    def __init__(self, model):
        self.model = model

    def get_name(self):
        return self.model.name

    def get_icon_path(self):
        return self.model.icon_path

    def get_content(self):
        return f"Content for {self.model.name}"
