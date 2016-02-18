import subprocess

# subprocess.call(["./src/sonic-annotator", "-t", "./src/monoNoteOut.n3", "./audio/testAudioLong.wav", "-w", "csv", "--csv-one-file", "./testAudioNoteOut.csv"])
subprocess.call(["./src/sonic-annotator", "-t", "./src/monoNoteOut.n3", "/Users/gong/Documents/MTG document/Jingju arias/aCapella/bcnRecording/audio/005.wav", "-w", "csv", "--csv-stdout"])
