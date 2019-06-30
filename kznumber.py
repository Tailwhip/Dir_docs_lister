class kzNumber():

    def __init__(self):
        # making variables
        print("START")
        self.kz = "PPP-NNN"
        self.kz_I = self.kz[0:3]
        self.kz_dash = self.kz[3]
        self.kz_II = self.kz[4:]
        self.kz_fail = True
        self.proj_fail = True
        self.proj_numbers = ["000", "001", "002", "003", "004", "005", "006", "007", "008", "022", "030", "031"]
        self.dash_fail = True
        self.range_fail = True
        self.digits_fail = True
        #self.get_kz()
        print("KZ-{}".format(self.kz))

    # a function for getting a kz number from user
    def get_kz(self):
        print("Wpisz numer KZ zachowując prawidłowy format: PPP-NNN \n"
              "PPP - numer projektu \n"
              "NNN - numer kolejny Karty zmian\n"
              "CTRL + C aby zakończyć")
        self.kz = input()
        self.kz_I = self.kz[0:3]
        self.kz_dash = self.kz[3]
        self.kz_II = self.kz[4:]
        self.exceptions()

    # a function for checking all exceptions during getting kz number
    def exceptions(self):
        # checking if both parts of kz is an int
        while self.kz_fail:
            try:
                int(self.kz_I)
                int(self.kz_II)
                self.kz_fail = False
            except ValueError:
                self.kz_fail = True
                print("Nieprawidłowy numer Karty zmian: użyj cyfr \n")
                self.get_kz()

        # checking if the first part of kz is one of the available project numbers
        while self.proj_fail:
            for number in self.proj_numbers:
                if number == self.kz_I:
                    self.proj_fail = False
                    break
                else: self.proj_fail = True
            if self.proj_fail:
                print("Nieprawidłowy numer Karty zmian: nie ma takiego projektu \n")
                self.get_kz()

        # checking if kz_dash is actually a dash sign
        while self.dash_fail:
            if self.kz_dash != "-":
                print("Nieprawidłowy numer Karty zmian: brak myślnika rozdzielającego \n")
                self.get_kz()
            else: self.dash_fail = False

        # chcecking if range of kz number is within <000, 999>
        while self.range_fail:
            if int(self.kz_II) < 0 or int(self.kz_II) > 999:
                print("Nieprawidłowy numer Karty zmian: numer kolejny KZ ujemny lub zbyt wysoki \n")
                self.get_kz()
            else: self.range_fail = False

        # checking if kz number has 3 digits
        while self.digits_fail:
            if self.kz_II.__len__() < 3:
                print("Nieprawidłowy numer Karty zmian: numer kolejny KZ musi być trzycyfrowy \n")
                self.get_kz()
            else:
                self.digits_fail = False
