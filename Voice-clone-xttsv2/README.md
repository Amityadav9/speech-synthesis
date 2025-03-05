
# Voice Cloning with XTTS-v2

![XTTS-v2 Voice Cloning](https://img.shields.io/badge/AI-Voice%20Cloning-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A powerful and easy-to-use voice cloning application built with the XTTS-v2 model. This tool allows you to clone any voice from a short audio sample and generate new speech in the same voice with your own text.

## ✨ Features

- 🎙️ High-quality voice cloning with minimal training data
- 🌍 Multilingual support (German, English, and many other languages)
- 🖥️ GPU acceleration for faster processing
- 🔊 Real-time audio playback
- 💾 Automatic saving of generated audio
- 🧠 Built on state-of-the-art XTTS-v2 technology

## 📋 Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (for faster processing, though CPU mode is supported)
- Audio samples for voice cloning (WAV or MP3 format)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/Amityadav9/speech-synthesis.git
cd voice-clone-xttsv2
```

2. Install the required packages:

```bash
# Core dependencies
pip install numpy sounddevice scipy

# For GPU acceleration (choose the appropriate version for your CUDA)
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118  # For CUDA 11.8

# Install TTS and other requirements
pip install TTS aiohttp Pillow asyncio
```

### PyTorch GPU Installation Options

Select the appropriate command based on your CUDA version:

- **CUDA 11.8 (recommended):**
  ```bash
  pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```

- **CUDA 12.1:**
  ```bash
  pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
  ```

- **CUDA 11.7:**
  ```bash
  pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu117
  ```

Check your CUDA version with: `nvidia-smi`

## 📁 File Structure

```
voice-cloning/
├── audio/                  # Directory for voice samples (place your .wav files here)
├── output/                 # Generated audio files are saved here
├── voice_cloner.py         # Main voice cloning script
└── README.md               # This file
```

## 🖥️ Usage

1. Add your voice sample(s) to the `audio` directory (WAV or MP3 format)
2. Run the voice cloning script:

```bash
python voice_cloner.py
```

3. The script will:
   - List available voice samples
   - Generate speech based on the example texts
   - Play the generated audio
   - Save the audio files to the `output` directory

### Customizing

To customize the voice cloning process, edit the `voice_cloner.py` file:

- Change the example texts in the `texts` list
- Modify the language parameter (default is German, "de")
- Adjust the file naming for saved outputs

### Command Line Arguments (Planned Feature)

```bash
python voice_cloner.py --voice <voice_file> --text "Your text here" --language en
```

## 🌍 Supported Languages

- German (de)
- English (en)
- French (fr)
- Spanish (es)
- Italian (it)
- Portuguese (pt)
- Polish (pl)
- Turkish (tr)
- Russian (ru)
- Dutch (nl)
- Czech (cs)
- Arabic (ar)
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
- Hungarian (hu)
- Hindi (hi)
- And many more...

## 🔧 Troubleshooting

### Common Issues

1. **"CUDA not available" error**
   - Ensure your GPU drivers are installed correctly
   - Check that the PyTorch version matches your CUDA version

2. **Low quality audio output**
   - Use higher quality voice samples (10-30 seconds of clear speech)
   - Try different voice samples or recordings
   - Ensure minimal background noise in reference audio

3. **Out of memory errors**
   - Reduce batch size or close other GPU-intensive applications
   - Try using CPU mode if your GPU has limited memory

4. **Model download issues**
   - The first run will download the XTTS-v2 model (1.5GB)
   - Ensure a stable internet connection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License 

## 🙏 Acknowledgments

- [Coqui TTS](https://github.com/coqui-ai/TTS) for the XTTS-v2 model
- All open-source contributors making voice synthesis accessible
