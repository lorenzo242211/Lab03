
class Dictionary:       #devo creare l'oggetto dizionario, al quale posso accedere al suo attributo lista di parole attraverso un apposito metodo
    def __init__(self):
        self.parole = list()

    def loadDictionary(self,path):
        with open(path, 'r', encoding="utf-8") as file:
            righe = file.readlines()
            for parola in righe:
                self.parole.append(parola.strip().lower())

    def printAll(self):
        for p in self.parole:
            print(p)


    @property
    def lista(self):
        return self.parole


def test():
    diz = Dictionary() #ho creato l'oggetto
    diz.loadDictionary("resources/Italian.txt")
    print(len(diz.lista))

if __name__ == "__main__":
    test()