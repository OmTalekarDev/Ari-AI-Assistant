import json
from pathlib import Path

from faster_whisper import WhisperModel

from audio import record_audio
from commands import handle_command


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.json"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            "config.json not found. Copy config.example.json to config.json first."
        )

    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def main() -> None:
    config = load_config()

    model_name = config.get("whisper_model", "base.en")
    language = config.get("language", "en")
    seconds = int(config.get("record_seconds", 5))

    print(f"🤖 {config.get('assistant_name', 'Ari')} starting...")
    print(f"🧠 Whisper model: {model_name}")

    model = WhisperModel(model_name, device="cpu", compute_type="int8")

    while True:
        audio = record_audio(seconds=seconds)

        segments, _ = model.transcribe(
            audio,
            language=language,
            vad_filter=True,
        )

        text = " ".join(segment.text for segment in segments).strip()

        if text:
            print(f"🗣️ You: {text}")

        if not handle_command(text):
            break


if __name__ == "__main__":
    main()
