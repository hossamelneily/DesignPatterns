# SRP SOC Single responsibility principle

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entrt(self, text):
        self.count += 1
        self.entries.append(f'{self.count}:{text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    ## the comming functions are seconadry functions
    #N.B we don't want to overload our class with the following functions
    # we need to separate them in persistance class
    # def save(self, filename):
    #     pass
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass

#the folloiwng class is like the model manager in django
class PersistanceManager:
    @staticmethod
    #static method won't take self
    def save(journal, filename):
        print(journal)
    @staticmethod
    def load(filename):
        pass

    def low_from_web(uri):
        pass


j = Journal()
j.add_entrt('yes i can')
j.add_entrt('no no ')

print(j)
filename = 'test.txt'
PersistanceManager.save(j,filename)
