import argparse

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
SCALES = {
    "major": [0,2,4,5,7,9,11],
    "minor": [0,2,3,5,7,8,10],
    "pentatonic": [0,2,4,7,9],
    "blues": [0,3,5,6,7,10],
    "dorian": [0,2,3,5,7,9,10],
    "mixolydian": [0,2,4,5,7,9,10],
    "chromatic": list(range(12)),
}
CHORDS = {
    "maj": [0,4,7], "min": [0,3,7], "dim": [0,3,6], "aug": [0,4,8],
    "7": [0,4,7,10], "maj7": [0,4,7,11], "min7": [0,3,7,10],
    "sus2": [0,2,7], "sus4": [0,5,7],
}
INTERVALS = {0:"unison",1:"m2",2:"M2",3:"m3",4:"M3",5:"P4",6:"tritone",7:"P5",8:"m6",9:"M6",10:"m7",11:"M7",12:"octave"}

def note_idx(name): return NOTES.index(name.upper().replace("♯","#").replace("♭","b"))

def main():
    p = argparse.ArgumentParser(description="Music theory tools")
    sub = p.add_subparsers(dest="cmd")
    s = sub.add_parser("scale")
    s.add_argument("root"); s.add_argument("type", choices=SCALES.keys())
    c = sub.add_parser("chord")
    c.add_argument("root"); c.add_argument("type", choices=CHORDS.keys())
    i = sub.add_parser("interval")
    i.add_argument("note1"); i.add_argument("note2")
    sub.add_parser("circle")
    args = p.parse_args()
    if args.cmd == "scale":
        root = note_idx(args.root)
        notes = [NOTES[(root+s)%12] for s in SCALES[args.type]]
        print(f"{args.root} {args.type}: {' '.join(notes)}")
    elif args.cmd == "chord":
        root = note_idx(args.root)
        notes = [NOTES[(root+s)%12] for s in CHORDS[args.type]]
        print(f"{args.root}{args.type}: {' '.join(notes)}")
    elif args.cmd == "interval":
        n1, n2 = note_idx(args.note1), note_idx(args.note2)
        semitones = (n2 - n1) % 12
        print(f"{args.note1} -> {args.note2}: {semitones} semitones ({INTERVALS.get(semitones, '?')})")
    elif args.cmd == "circle":
        print("Circle of Fifths:")
        idx = 0
        for _ in range(12):
            print(f"  {NOTES[idx % 12]}", end="")
            idx += 7
        print()
    else: p.print_help()

if __name__ == "__main__":
    main()
