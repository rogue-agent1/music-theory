#!/usr/bin/env python3
"""music_theory - Scales, chords, intervals, and key detection."""
import sys

NOTES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
SCALE_PATTERNS = {
    "major": [2,2,1,2,2,2,1],
    "minor": [2,1,2,2,1,2,2],
    "harmonic_minor": [2,1,2,2,1,3,1],
    "pentatonic": [2,2,3,2,3],
    "blues": [3,2,1,1,3,2],
    "chromatic": [1]*12,
    "dorian": [2,1,2,2,2,1,2],
    "mixolydian": [2,2,1,2,2,1,2],
}
CHORD_PATTERNS = {
    "major": [0,4,7],
    "minor": [0,3,7],
    "dim": [0,3,6],
    "aug": [0,4,8],
    "7": [0,4,7,10],
    "maj7": [0,4,7,11],
    "min7": [0,3,7,10],
}

def note_index(note):
    return NOTES.index(note)

def scale(root, pattern="major"):
    idx = note_index(root)
    intervals = SCALE_PATTERNS[pattern]
    result = [NOTES[idx % 12]]
    for step in intervals[:-1]:
        idx += step
        result.append(NOTES[idx % 12])
    return result

def chord(root, quality="major"):
    idx = note_index(root)
    return [NOTES[(idx + i) % 12] for i in CHORD_PATTERNS[quality]]

def interval_name(semitones):
    names = {0:"unison",1:"min2",2:"maj2",3:"min3",4:"maj3",5:"P4",6:"tritone",7:"P5",8:"min6",9:"maj6",10:"min7",11:"maj7",12:"octave"}
    return names.get(semitones % 12, f"{semitones}st")

def transpose(notes, semitones):
    return [NOTES[(note_index(n) + semitones) % 12] for n in notes]

def test():
    assert scale("C") == ["C","D","E","F","G","A","B"]
    assert scale("A", "minor") == ["A","B","C","D","E","F","G"]
    assert chord("C") == ["C","E","G"]
    assert chord("A", "minor") == ["A","C","E"]
    assert chord("G", "7") == ["G","B","D","F"]
    assert interval_name(7) == "P5"
    assert interval_name(4) == "maj3"
    t = transpose(["C","E","G"], 2)
    assert t == ["D","F#","A"]
    assert scale("D", "pentatonic") == ["D","E","F#","A","B"]
    print("OK: music_theory")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        print("Usage: music_theory.py test")
