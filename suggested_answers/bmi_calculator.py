class BMI:
    def __init__(self, height, weight):
        self._height = height
        self._weight = weight
    def get_bmi(self):
        bmi = self._weight / (self._height * 0.01)**2
        return bmi
    def get_bmi_label(self):
        bmi = self.get_bmi()
        if bmi > 30:
            return 'Obese'
        elif bmi > 25:
            return 'Overweight'
        elif bmi > 18.5:
            return 'Normal weight'
        else:
            return 'Underweight'