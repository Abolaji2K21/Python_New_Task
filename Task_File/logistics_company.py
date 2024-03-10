from Exception.invalid_deliveries_exception import InvalidDeliveriesException


class logistics_company:
    def __init__(self):
        self.base_salary = 5000
        self.commission_rate = 0
        self.amount_per_parcel = 0

    def validate_deliveries(self, successful_deliveries):
        if successful_deliveries < 0:
            raise InvalidDeliveriesException
        elif successful_deliveries < 50:
            self.amount_per_parcel = 160
        elif successful_deliveries < 60:
            self.amount_per_parcel = 200
        elif successful_deliveries < 70:
            self.amount_per_parcel = 250
        elif successful_deliveries < 100:
            self.amount_per_parcel = 500
        else:
            raise InvalidDeliveriesException

    def calculate_commission(self, successful_deliveries):
        self.validate_deliveries(successful_deliveries)
        self.commission_rate = (successful_deliveries * self.amount_per_parcel) + self.base_salary

        return self.commission_rate
