Lingvistica italiana II. Modulo A

Relazione di fine modulo

Dialogo DGmtA01F del corpus CLIPS
Città: Firenze

La trascrizione con **Dragon** e' ottenuto con applicazione Dragon NaturallySpeaking versione 13.

La trascrizione con **Google API** è ottenuta usando libreria 

[SpeachRecognition](https://github.com/Uberi/speech_recognition)
la quale presta l'interfacia di communicazione con diversi API, Google Speech Recognition compreso.
E' stato usato script examples/audio_transcribe.py, il quale usa ogni frammento di audio spezzetato
in parti da 10 secondi come payload della richiesta al Google Speech recognition API.

[Sclite](https://www.nist.gov/itl/iad/mig/tools)

ftp://jaguar.ncsl.nist.gov/pub/sctk-2.4.10-20151007-1312Z.tar.bz2
~/project/sctk-2.4.10/bin

http://www1.icsi.berkeley.edu/Speech/docs/sctk-1.2/sclite.htm
http://www1.icsi.berkeley.edu/Speech/docs/sctk-1.2/options.htm
http://mariangemarcano.blogspot.it/2012/09/speech-recognition-setting-up-sclite.html

scilite reports: http://www1.icsi.berkeley.edu/Speech/docs/sctk-1.2/outputs.htm#output_reports_name_0

./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o dtl


./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o dtl
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o dtl
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o lur
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o lur
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o pralign
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o pralign
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o prf
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o prf
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o rsum
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o rsum
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o sgml
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o sgml
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o spk
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o spk
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o snt
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o snt
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/dragon.txt" -i rm -o sum
./sclite -r "/home/valeriya/project/LingITII/trn/clips.txt" -h "/home/valeriya/project/LingITII/trn/google.txt" -i rm -o sum
