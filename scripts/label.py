#!/usr/env python
# -*- coding: utf-8 -*-

# 5. Convertire i file per il controllo con SCLITE
# Per ogni testo, tutti e tre i file di trascrizione (trascrizione originale, trascrizione di Dragon e
# trascrizione di Google) devono essere registrati in formato trn.
# Occorre quindi:
# 
# 
# 
# Eliminare tutto ciò che non rappresenta le parole del parlato (note, segni di interpunzione)
# separare con a capo (newline) ogni enunciazione – tipicamente ogni frase, ma si può anche
# scegliere di usare altre unità
# Inserire a fondo enunciazione un codice tra parentesi tonde con identificativo del parlante,
# trattino basso e numero progressivo: «(a_1)»
# Il codice del parlante deve essere fatto in questo modo: iniziali del parlante, con lettere maiuscole e
# senza punti, seguite da trattino e dal nome della città. Per esempio, si prendano le battute del
# parlante indicato in DGmtB02B.txt come:
# INp1:
# T. S.M., F, 24, Bari, spontaneo, fluente, G>F
# Le battute di questo parlante dovranno essere indicate come “(TSM-Bari_1)” e così via.
# Attenzione! Nei dialoghi, la numerazione è alternata. Al primo parlante viene assegnato il turno 1,
# al secondo il turno 2; quando riprende il primo parlante, il suo è il turno 3 e così via.
# Possono essere per esempio eliminati in automatico:
# <sp> <lp> <inspiration> <tongue-click> <creacky-voice> <NOISE>
# [screaming]
# , ! ? { } * /
# Devono essere eliminati anche gli spazi doppi.
# Devono essere invece mantenute le parti iniziali di parola che terminano con +.
# Sono interiezioni accettate, da inserire nel testo come parole, quelle registrate nel dizionario di De
# Mauro. Quindi vanno accettate ah, eh, ehm e oh, più eventuali altre interiezioni inserite nel
# dizionario, ma vanno cancellate <eeh>, <mbè> e <mh> (anche se De Mauro registra mm). Vanno
# cancellate anche le interiezioni riportate in forma ripetuta (per esempio, <mhmh>), anche quando
# riguardano interiezioni accettate (non va quindi accentata neanche <ahah>).

#!/usr/env python
# -*- coding: utf-8 -*-

"""
Convert transcribed text into trn format
Usage examples:
    python cleaner.py DGmtA01F.txt
"""

from __future__ import print_function
import sys, getopt
import codecs
import re

class Reader(object):
    def __init__(self, filename=None):
        self.filename = filename

    def __iter__(self):
        if self.filename:
            file = codecs.open(self.filename, 'r', 'ISO-8859-1', errors='ignore')
        else:
            file = codecs.getreader('ISO-8859-1')(sys.stdin)
        i = 0
        for line in file:
            i += 1
            if i % 2:
                label = 'LL'
                number = i / 2 + 1
            else:
                label = 'RF'
                number = i / 2
            line = re.sub(r'\([^()]+\)', '', line.strip())
            line = ''.join([line, '(', label, '-Firenze_', str(number), ')'])
            yield line

class Writer(object):
    @classmethod
    def write(cls, line):
        print(u'{}'.format(line).encode('utf-8'))


def main(argv):
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    if len(args):
        it = Reader(args[0])
    else:
        it = Reader()
    writer = Writer()
    for item in it:
        writer.write(item)


if __name__ == "__main__":
    main(sys.argv[1:])