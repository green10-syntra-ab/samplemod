class SwimmingPoolPayDesk:
    def calculate_admission_fee(self, age):
        """ Calulate admission fee

        :param age: age of visitor
        :return: fee for visitor
        """
        if not isinstance(age, (int, float)) : raise TypeError
        if age < 0 : raise ValueError
        elif 0 <= age <= 6 : return 1.00
        elif 6 < age <= 16 : return 2.00
        elif 16 < age <= 65 : return 2.50
        else : return 1.50
