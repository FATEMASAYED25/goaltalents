# creating talent opject using a constructor


class Talent:
    def __int__ (self ,  full_name, email, phone, position, birth_year, club, experience):
        self.full_name =full_name.strip()
        self.email=email
        self.phone= int(phone)
        self.position = position
        self.birth_year =int(birth_year)
        self.club = club
        self.experience =int(experience)

    def to_dict(self):
        return self.__dict__

    def is_valid(self):
        return self.full_name != "" and self.email != ""