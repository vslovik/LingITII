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
Convert text from IOB into TSV format
Usage examples:
    cat iob_labeled_set.txt | python iob_decoder.py
    python iob_decoder.py iob_labeled_set.txt

    python iob_decoder.py data/it_train_iob > data/it_train_decoded
"""

from __future__ import print_function
import sys, getopt
import codecs
import re

class Reader(object):
    """
    An iterator over examples read from a file in TSV format.
    If the input is from a file, it can be iterated several times.
    """
    def __init__(self, filename=None):
        self.filename = filename

    def __iter__(self):
        if self.filename:
            file = codecs.open(self.filename, 'r', 'utf-8', errors='ignore')
        else:
            file = codecs.getreader('utf-8')(sys.stdin)

        phrases = ''.join([line for line in file]).split('\n\n')
        for ph in phrases:
             # ah, eh, ehm e oh
            ph = ph\
                .replace('<sp>', '')\
                .replace('<lp>','')\
                .replace('<inspiration>','')\
                .replace('<tongue-click>','')\
                .replace('<creacky-voice>','')\
                .replace('<NOISE>','')\
                .replace('[screaming]','')\
                .replace(',','')\
                .replace('!','')\
                .replace('?','')\
                .replace('*','')\
                .replace('{','')\
                .replace('}','')\
                .replace('[whispering]','')\
                .replace('<laugh>','')\
                .replace('#','')\
                .replace('<eeh>','')\
                .replace(u'<mbè>','')\
                .replace('<mh>','')\
                .replace('<laugh>','')\
                .replace('<mhmh>','')\
                .replace('<ahah>',' ')\
                .replace('<ah>','ah')\
                .replace('<eh>','eh')\
                .replace('<ah>','ah')\
                .replace('<ehm>','ehm')\
                .replace('<oh>','oh')\
                .replace('+',' ')\
                .replace('[dialect]',' ')\
                .replace('<oo>',' ')\
                .replace('/',' ')

            ph = re.sub(r'(\s)+', r'\1', ph)
            ph = re.sub(r'(\t)\t+', r'\1', ph)
            yield ph.strip()

class Writer(object):

    @classmethod
    def write(cls, i, line):
        """
        Prints a number - token pair

        :param i: token number
        :param token: token
        """
        print(u'{}\t{}\n\n'.format(i, line).encode('utf-8'))


def main(argv):
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    if len(args):
        it = Reader(args[0])
    else:
        it = Reader()
    writer = Writer()
    for item in it:
        writer.write('---', item)



if __name__ == "__main__":
    main(sys.argv[1:])