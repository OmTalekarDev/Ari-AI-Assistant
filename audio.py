import numpy as np
import sounddevice as sd


def record_audio(seconds: int = 5, sample_rate: int = 16000) -> np.ndarray:
    """Record mono microphone audio and return float32 samples."""
    print(f"🎙️ Listening for {seconds} seconds...")
    audio = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
    )
    sd.wait()
    return np.squeeze(audio)
