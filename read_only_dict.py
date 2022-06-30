import collections
import copy


class ReadOnlyDictWrapper(collections.abc.Mapping):
    def __init__(self, data: dict):
        if not isinstance(data, dict):
            raise Exception(f"{dict} expected . Got {type(data)}")
        self._data = copy.deepcopy(data)

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return str(self._data)
