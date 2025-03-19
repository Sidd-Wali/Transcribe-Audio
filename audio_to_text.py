import whisper
import os

# GLOBAL VARIABLES
model = whisper.load_model("medium") # Load the model

def transcribe_file(audFile):
    result = model.transcribe(audFile, task="translate")
    return result['text']

def transcribe_dir(audDir):
    text = ""
    for filename in os.listdir(audDir):
        if filename.endswith('.m4a'):
            audio_path = os.path.join(audDir, filename)
            text += transcribe_file(audio_path)
    return text

def writeToTextFile(text, outputFile):
    with open(outputFile, 'w') as file:
        file.write(text)

def main():
    text = ""
    dir = input("Do you want to transcribe a directory or a file? (d/f): ")
    if dir == 'd':
        audDir = input("Enter the name of the directory")
        text = transcribe_dir(audDir)
    elif dir == 'f':
        files = input("Enter the names of the files, separated by commas: ")
        if (len(files) == 0):
            print("No files entered.")
            return
        else:
            files = files.split(',')
            for file in files:
                text += transcribe_file(file)
    textfile = input("Enter the name of the output text file")
    writeToTextFile(text, textfile)
    print(f"Transcription saved to {textfile}")


