import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi_diz = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        testo = replaceChars(txtIn)
        path = "resources/" + language[0].upper() + language[1:].replace(" ", "") + ".txt"
        frase_separata = testo.split() #divido in lista di parole da analizzare e cercare sul multidizionario
        print(f"la frase separata è: \n{frase_separata}")
        self.multi_diz.aggiungiLingua(language, path)
        # self.multi_diz.printDic(language) prova stampa dizionario associato alla lingua
        print("Ricerca classica attraverso 'in': ")
        inizio_timer = time.perf_counter()
        parole = self.multi_diz.searchWord(frase_separata, language)
        fine_timer = time.perf_counter()
        tempo_contains = fine_timer - inizio_timer
        # print(self.multi_diz.dizionarioLingue.keys()) prova per vedere se dizionario registra le chiavi
        print("Parole sbagliate:")
        for p in parole:
            if not p.corretta:
                print(p)
        print(f"\nTempo impiegato con logica contains: {tempo_contains:.5f}\n\n")

        #caso selezione lineare
        print("Ricerca di tipo lineare: ")
        sbagliate = self.multi_diz.searchWordLinear(frase_separata, language)
        fine_timer = time.perf_counter()
        tempo_lineare = fine_timer - inizio_timer
        print("Parole sbagliate:")
        for p in sbagliate:
            if not p.corretta:
                print(p)
        print(f"\nTempo impiegato con logica lineare: {tempo_lineare:.5f}\n\n")

        #caso selezione dicotomica
        print("Ricerca di tipo dicotomica: ")
        sbagliate = self.multi_diz.searchWordDichotomic(frase_separata, language)
        fine_timer = time.perf_counter()
        tempo_dicotomica = fine_timer - inizio_timer
        print("Parole sbagliate:")
        for p in sbagliate:
            if not p.corretta:
                print(p)
        print(f"\nTempo impiegato con logica contains: {tempo_dicotomica:.5f}\n\n")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text): #per sostituire i caratteri che non c'entrano un cazzo con la frase sulla quale cicla per ottenere le parole da analizzare rispetto al dizionario
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~?°"
    for c in chars:
        text = text.replace(c, "")
    return text.lower()





#questi vengono usati solo per i test, ovvero provare i metodi di questa classe in loco
def test_spell():
    testo = replaceChars("Gold + fig., amndr!^?")

    print(testo.split())

if __name__ == "__main__":
    test_spell()
    lin = "italian"
    path = "resources/" + lin[0].upper() + lin[1:].replace(" ", "") + ".txt"
    print(path)