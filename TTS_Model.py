from elevenlabs import ElevenLabs
import os
import pygame

# Initialize the ElevenLabs API
api = ElevenLabs(api_key="sk_63775d56ff418b7510cf298e3af8156177f3e0bc5d986247")

# Function to perform TTS
def text_to_speech():
    file_path="Model Response.txt" 
    output_audio="output.mp3"
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return

        # Read text from the file
        with open(file_path, "r") as file:
            model_text = file.read().strip()
        
        if not model_text:
            print("Error: The file is empty.")
            return
        
        print("Analysing...")
        
        # Generate audio using the text
        audio_generator = api.generate(
            text=model_text,
            voice="cgSgspJ2msm6clMCkdW9"
        )

        # Consume the generator and combine audio chunks into bytes
        audio_data = b"".join(audio_generator)

        if os.path.exists(output_audio):
            os.remove(output_audio)
        
        # Save the audio to a file
        with open(output_audio, "wb") as audio_file:
            audio_file.write(audio_data)
            
        print("Speaking...")
        
        # Initialize pygame mixer to play audio
        pygame.mixer.init()
        pygame.mixer.music.load(output_audio)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.quit()
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    

