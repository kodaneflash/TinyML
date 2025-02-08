# todo: not a central feature, but users should be able to optionally define callbacks that are called
# during the solution search or model training, e.g. to log progress, etc.


# A callback is a function that is called at certain points during the model building process.
class Callback:
    def __init__(self, description: str):
        pass
