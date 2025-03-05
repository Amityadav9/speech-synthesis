import os
import torch
import asyncio
import sounddevice as sd
import numpy as np
from TTS.api import TTS
from scipy.io.wavfile import write as write_wav


class VoiceCloner:
    def __init__(self):
        print("🎙️ Initialisiere XTTS-v2 Modell für Stimmklonen...")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tts = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2",
            progress_bar=False,
            gpu=True if torch.cuda.is_available() else False,
        )

        # Erstelle Verzeichnis für Stimmen, falls es nicht existiert
        self.voices_dir = os.path.join(os.getcwd(), "audio")
        os.makedirs(self.voices_dir, exist_ok=True)

        # Erstelle Ausgabeverzeichnis
        self.output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(self.output_dir, exist_ok=True)

        print(f"✅ Stimmkloner initialisiert auf {self.device}")

    def list_available_voices(self):
        """Liste alle verfügbaren Stimmbeispiele im Audio-Verzeichnis auf"""
        voice_files = [
            f for f in os.listdir(self.voices_dir) if f.endswith((".wav", ".mp3"))
        ]
        print(f"Verfügbare Stimmreferenzen ({len(voice_files)}):")
        for i, file in enumerate(voice_files):
            print(f"{i + 1}. {file}")
        return voice_files

    async def clone_voice(self, text, voice_file, language="de"):
        """Generiere Sprache mit der angegebenen Stimmreferenz und Text"""
        print(f"🔊 Klone Stimme von: {voice_file}")
        print(f"🗣️ Generiere Sprache für: '{text}'")

        speaker_wav = os.path.join(self.voices_dir, voice_file)
        if not os.path.exists(speaker_wav):
            print(f"❌ Stimmreferenzdatei nicht gefunden: {speaker_wav}")
            return False

        try:
            # Verwende run_in_executor, um Event Loop nicht zu blockieren
            loop = asyncio.get_event_loop()
            wav = await loop.run_in_executor(
                None,
                lambda: self.tts.tts(
                    text=text,
                    language=language,
                    speaker_wav=speaker_wav,
                ),
            )

            # Normalisiere Audio
            wav = np.array(wav, dtype=np.float32)
            wav = wav / np.max(np.abs(wav))

            # Spiele die generierte Audio ab
            sd.play(wav, 24000)
            sd.wait()

            # Speichere die generierte Audio
            output_filename = (
                f"kloned_{voice_file.split('.')[0]}_{text[:20].replace(' ', '_')}.wav"
            )
            output_path = os.path.join(self.output_dir, output_filename)

            # Konvertiere zu int16 für WAV-Speicherung
            wav_int = np.int16(wav * 32767)
            write_wav(output_path, 24000, wav_int)
            print(f"✅ Geklonte Stimme gespeichert unter: {output_path}")

            return True

        except Exception as e:
            print(f"❌ Fehler beim Stimmklonen: {e}")
            return False


async def main():
    cloner = VoiceCloner()

    # Liste verfügbare Stimmreferenzen auf
    voices = cloner.list_available_voices()
    if not voices:
        print("Keine Stimmreferenzdateien im 'audio'-Verzeichnis gefunden.")
        print(
            "Bitte fügen Sie .wav-Dateien zu diesem Verzeichnis hinzu und starten Sie erneut."
        )
        return

    # Wähle eine Stimme aus (Standard ist die erste oder lasse den Benutzer wählen)
    selected_voice = voices[0]

    # Beispieltexte, die mit der geklonten Stimme generiert werden sollen
    texts = [
        "Ich begrüße Sie herzlich im Gläsernen Palast, einem Ort voller Geschichte und Schönheit",
        "Wir bewegen uns nun zu einem besonderen Aussichtspunkt innerhalb des Gläsernen Palastes.",
        "Hier sind wir an einem wunderbaren Aussichtspunkt angekommen. Bitte schauen Sie zuerst nach draußen und genießen Sie die atemberaubende Aussicht.",
    ]

    # Sprachauswahl (Standard Deutsch)
    language = "de"

    # Generiere Sprache für jeden Beispieltext
    for text in texts:
        await cloner.clone_voice(text, selected_voice, language)
        await asyncio.sleep(1)  # Pause zwischen den Beispielen


if __name__ == "__main__":
    asyncio.run(main())
