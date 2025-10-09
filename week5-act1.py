# Parent class
class Tanzania:
    def __init__(self, population, president, capital):
        self.population = population
        self.president = president
        self.capital = capital


    def display_info(self):
        print(f"The population is {self.population} million people")
        print(f"The president is {self.president}")
        print(f"The capital is {self.capital}")

    # Applying polymorphism
    def describe(self):
        print("Tanzania is a beautiful country in East Africa!!!")

# Child class 1
class DarEsSalaam(Tanzania):  # Fixed class name from Dodoma to DarEsSalaam to match usage
    def __init__(self, population, president, capital, main_industry):  # Removed extra parameter
        super().__init__(population, president, capital)
        self.population = population
        self.main_industry = main_industry

    # Overriding the describe() method
    def describe(self):
        print("Dar es Salaam is Tanzania's largest city and main commercial hub")

    # New method unique to class
    def city_activity(self):
        print(f"The main industry in Dar es Salaam is {self.main_industry}")

# Child class 2
class Arusha(Tanzania):
    def __init__(self, population, president, capital, tourism_sites):
        super().__init__(population, president, capital)
        self.population = population
        self.tourism_sites = tourism_sites

    # Overriding the describe() method
    def describe(self):
        print("Arusha is known as the safari capital of Tanzania and a gateway to Mount Kilimanjaro.")

    # New method unique to Arusha
    def tourism_info(self):
        print("Top tourism sites in Arusha include:")
        for site in self.tourism_sites:
            print(f"- {site}")

# Creating objects
tanzania = Tanzania(65, "Samia Suluhu Hassan", "Dodoma")
dar = DarEsSalaam(65, "Samia Suluhu Hassan", "Dodoma", "Trade and Port Services")  # Fixed parameters
arusha = Arusha(65, "Samia Suluhu Hassan", "Dodoma", ["Serengeti", "Mount Meru", "Ngorongoro Crater"])  # Fixed parameters

# Calling methods
tanzania.display_info()
tanzania.describe()

print("\n--- Dar es Salaam ---")
dar.display_info()
dar.describe()
dar.city_activity()

print("\n--- Arusha ---")
arusha.display_info()
arusha.describe()
arusha.tourism_info()