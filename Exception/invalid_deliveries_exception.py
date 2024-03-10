
class InvalidDeliveriesException(Exception):
    def __init__(self, message="Invalid deliveries"):
        self.message = message
        super().__init__(self.message)

