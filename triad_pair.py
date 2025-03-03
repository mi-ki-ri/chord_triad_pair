from pychord import Chord
from colorama import init, Fore


def merge_triads(triad):
    c_scale = ["C", "D", "E", "F", "G", "A", "B"]
    basses = ("C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B")
    appendixes = ["", "m", "dim", "aug", "sus4", "sus2"]

    for bass in basses:
        for appendix in appendixes:
            chord = Chord(f"{bass}{appendix}")
            scale = chord.components()
            scale.extend(triad.components())
            scale = list(set(scale))
            scale.sort()
            print(triad.chord, " + ", f"{bass}{appendix}", end=": \n\t")
            for note in scale:
                if note in triad.components():
                    print(Fore.CYAN + note, end=" ")
                elif note in c_scale:
                    print(Fore.BLUE + note, end=" ")
                else:
                    print(Fore.RED + note, end=" ")
            print()
    print("=====================================")


triads = ["C", "Am", "G"]

init(autoreset=True)

for triad in triads:
    merge_triads(Chord(triad))
