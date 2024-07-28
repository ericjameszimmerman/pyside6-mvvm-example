import pyside6_mvvm.model as model


class ItemListViewModel:
    def __init__(self, models):
        self._models = models
        self._list_model = model.ListModel(models)

    @property
    def list_model(self):
        return self._list_model

    def get_item_model(self, index):
        if 0 <= index < len(self._models):
            return self._models[index]
        return None
