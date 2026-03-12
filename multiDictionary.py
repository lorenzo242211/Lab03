import dictionary as d
import richWord as rw  #considero le parole come oggetti stringa booleano


class MultiDictionary:

    def __init__(self):
       self.dizionarioLingue = dict()

    def printDic(self, language):
        for parola in self.dizionarioLingue[language]:
            print(parola)

    def searchWord(self, words, language): #words è la lista di parole estratta in spellchecker
        sbagliate = list()
        for w in words:
            parola_bool = rw.RichWord(w)
            if w in self.dizionarioLingue[language]:
                parola_bool.corretta = True
            else:
                parola_bool.corretta = False
            sbagliate.append(parola_bool)
        return sbagliate

    def searchWordLinear(self, words, language):
        sbagliate = list()
        for w in words:
            parola_bool = rw.RichWord(w)
            for p in self.dizionarioLingue[language]:
                if w == p:
                    parola_bool.corretta = True
                    break #questo break esce dal for di ricerca quindi appena trova parola esce e passa a prossima w in words?
            #se arriva al fondo e non l'ha trovata implica parola non c'è, quindi aggiungo a lista sbagliate
            #uso Il trucco del "For... Else"
            else:
                parola_bool.corretta = False
            sbagliate.append(parola_bool) #aggiunge l'oggetto stringaParola Bool
        return sbagliate

    def searchWordDichotomic(self, words, language):
        sbagliate = []
        # Salviamo la lista in una variabile per comodità e pulizia
        dizionario = self.dizionarioLingue[language]

        for w in words:
            inizio = 0
            fine = len(dizionario) - 1
            parola_bool = rw.RichWord(w)
            parola_bool.corretta = True
            while inizio <= fine:
                # Troviamo l'indice centrale.
                # In Python // fa la divisione intera (senza virgola)
                mezzo = (inizio + fine) // 2
                parola_centro = dizionario[mezzo]

                if parola_centro == w:
                    # Trovata! Rompiamo il while
                    break
                elif parola_centro < w:
                    # La parola cercata viene DOPO in ordine alfabetico.
                    # Scartiamo la metà sinistra.
                    inizio = mezzo + 1
                else:
                    # La parola cercata viene PRIMA in ordine alfabetico.
                    # Scartiamo la metà destra.
                    fine = mezzo - 1

            else:
                # Se il while finisce (cioè inizio supera fine) senza beccare il break,
                # significa che abbiamo ristretto il campo a zero e la parola non c'è.
                parola_bool.corretta = False #la parola non c'è, è quindi "sbagliata"
            sbagliate.append(parola_bool)


        return sbagliate

    def aggiungiLingua(self, lingua, path):
        if lingua in self.dizionarioLingue: return
        nuovo_diz = d.Dictionary()
        nuovo_diz.loadDictionary(path)
        self.dizionarioLingue[lingua] = nuovo_diz.lista


