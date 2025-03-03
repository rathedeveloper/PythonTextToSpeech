# Import the gTTS module for text-to-speech conversion
from gtts import gTTS

# Import the PdfReader module from the PyPDF2 library for reading pdf files
from PyPDF2 import PdfReader

# Define a function for converting text to speech and saving it to a file
def text_to_speech(text, filename):

    # Create a gTTS object with the text and set the language to English
    speech = gTTS(text=text, lang="en", slow=False)

    # Save the speech to a file with the specified filename
    speech.save(filename)

# Main function to be executed only when the file is run as the main script
if __name__ == "__main__":

    # Initialize an empty string to store the text from the pdf file
    text = ""

    # Specify the name of the pdf file to be converted
    file = "AutoRecovery save of SEA Steps.pdf"

    # Open the pdf file in binary mode for reading
    with open(file, "rb") as file:

        # Create a PdfReader object to read the contents of the pdf file
        reader = PdfReader(file)

        # Get the number of pages in the pdf file
        number_of_pages = len(reader.pages)

        # Loop through each page of the pdf file and extract the text
        for page in range(number_of_pages):
            text += reader.pages[page].extract_text()

    # Call the text_to_speech function to convert the text to speech and save it to an mp3 file
    text_to_speech(text, "audio.mp3")