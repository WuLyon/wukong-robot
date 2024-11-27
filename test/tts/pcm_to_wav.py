import wave
import os

def pcm_to_wav(pcm_file, channels=1, sample_rate=44100, sample_width=2):
    """
    Convert a .pcm file to a .wav file.
    
    Args:
        pcm_file (str): Path to the .pcm file.
        wav_file (str): Path to the output .wav file.
        channels (int): Number of audio channels (1 = mono, 2 = stereo).
        sample_rate (int): Sample rate in Hz (e.g., 44100).
        sample_width (int): Sample width in bytes (e.g., 2 for 16-bit audio).
 
       """

    dir_path = os.path.dirname(pcm_file)
    wav_file = dir_path + "/output.wav"

    with open(pcm_file, 'rb') as pcmf:
        pcm_data = pcmf.read()



    with wave.open(wav_file, 'wb') as wavf:
        wavf.setnchannels(channels)
        wavf.setsampwidth(sample_width)
        wavf.setframerate(sample_rate)
        wavf.writeframes(pcm_data)

    # Check if the output file was created
    if os.path.exists(wav_file):
        print(f"Converted {pcm_file} to {wav_file} successfully!")
    else:
        print("Conversion failed.")


# Convert PCM to WAV
if __name__ == "__main__":
    script_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(script_path)
    pcm_file = dir_path + "/demo.pcm"
    pcm_to_wav(pcm_file)