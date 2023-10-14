class School:
    def __init__(self, name, level, number_of_students):
        self._name = name
        self._level = level
        self._number_of_students = number_of_students


    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_number_of_students(self):
        return self._number_of_students

    def set_number_of_student(self, number_of_students):
        self._number_of_students = number_of_students

    def __repr__(self):
        return ("A {level} school {name} with {numberOfStudents} students"
                .format(level=self._level, name=self._name, numberOfStudents=self._number_of_students))


class PrimarySchool(School):
    def __init__(self, name, number_of_students, pickup_policy):
        super().__init__(name, "Primary", number_of_students)
        self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
        return self.pickup_policy

    def __repr__(self):
        school_info = super().__repr__()
        return school_info + ". The pickup policy is: {pickUpPolicy}".format(pickUpPolicy=self.pickup_policy)


class HighSchool(School):
    def __init__(self, name, number_of_students, sport_teams):
        super().__init__(name, "High", number_of_students)
        self.sport_teams = sport_teams

    def get_sport_teams(self):
        return self.sport_teams

    def __repr__(self):
        school_info = super().__repr__()
        return school_info + ". Sport teams of this school include {sportTeams}".format(sportTeams=self.sport_teams)


high_school = HighSchool("NBCC", 2000, ["Football", "Soccer", "Basket Ball", "Tennis"])
print(high_school)
