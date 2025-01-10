

import numpy as np
import scipy.io.wavfile as wavfile


class AudioByteArray:
    @classmethod
    def wav_to_bytearray(cls,file_path):
        # Read the WAV file
        #sample rate: eg: 44100Hz
        sample_rate, audio_data = wavfile.read(file_path)
        channel = audio_data.shape[1]  #number of channels
        length = audio_data.shape[0] / sample_rate
        print(f"length = {length}s")

        # Convert the audio data to a byte array
        byte_array = np.array(audio_data, dtype=np.int16).tobytes()
        return sample_rate,byte_array,channel

    @classmethod
    def bytearray_to_wav(cls,byte_array, output_wav_file,channel, sample_rate=44100,):
        # Convert the byte array to a NumPy array of int16
        audio_data = np.frombuffer(byte_array, dtype=np.int16)
        data=audio_data.reshape(-1, channel)
        # Write the NumPy array to a WAV file
        wavfile.write(output_wav_file, sample_rate, data)

# Example usage
def main():
    input_wav_file = ".\\audio\\harvard.wav"
    sample_rate, byte_array, channel = AudioByteArray.wav_to_bytearray(input_wav_file)
    print("rate ", sample_rate)
    print("channel ", channel)
    AudioByteArray.bytearray_to_wav(byte_array, ".\\audio\\harvard2.wav", channel, sample_rate)

if __name__ == "__main__":
        main()










