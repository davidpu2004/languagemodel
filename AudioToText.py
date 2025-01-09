import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import time
import os


class AudioToText:
    def __init__(self, model_id="openai/whisper-large-v3"):
        device = "cuda:0" if torch.cuda.is_available() else "cpu"  # If you have GPU else it will use cpu
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        # model_id = "openai/whisper-large-v3"  # define the model
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True)
        model.to(device)
        processor = AutoProcessor.from_pretrained(model_id)

        # create the pipeline
        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            torch_dtype=torch_dtype,
            device=device,
        )

        self.generate_kwargs = {
            "max_new_tokens": 448,
            "num_beams": 1,
            "condition_on_prev_tokens": False,
            "compression_ratio_threshold": 1.35,  # zlib compression ratio threshold (in token space)
            "temperature": (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
            "logprob_threshold": -1.0,
            "no_speech_threshold": 0.6,
            "return_timestamps": True,
        }

    def get_transcript(self, audio_file):
        result = self.pipe(audio_file, generate_kwargs=self.generate_kwargs)
        result = result["text"]
        return result

    def save_as_file(self, output_path, file_name, text):
        output_file = os.path.join(output_path, file_name)
        with open(output_file, 'w') as file:
            file.write(text)


def main():
    start_time = time.time()
    audio_to_text = AudioToText()
    # the audio file ,from which we need to get transcript
    audio_file = "speech.mp3"
    transcript = audio_to_text.get_transcript(audio_file)
    end_time = time.time()
    execution_time = end_time - start_time
    print("*****OpenAI Whisper Model***** \n\n")
    print(f"Processing audio to text takes time: {execution_time:.6f} seconds")
    print("*****the audio transcript***** \n\n", transcript)
    audio_to_text.save_as_file(".","speech.txt",transcript)


if __name__ == "__main__":
    main()
