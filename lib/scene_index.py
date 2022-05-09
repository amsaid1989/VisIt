class SceneIndex:
    _index = 0

    @staticmethod
    def create_index():
        current = SceneIndex._index

        SceneIndex._index += 1

        return current