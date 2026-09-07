# YTDownPY

YTDownPY | YouTube video downloader desktop app made using Python, featuring a GUI interface built with Custom Tkinter, and media extraction done using yt-dlp library as a backend. Uses multi-threading to make sure the GUI doesn't just freeze

## Features

Query Search: searches and retrieves the top 5 YouTube videos matching the query keywords
Responsive GUI: uses a background thread to process tasks
Progress indicators: CustomTkinter progress indicator
Error handling: Stops users from submitting an empty query

## Project Structure

Main.py is the frontend that mainly handles the GUI and download.py is for: you guessed it... Downloading.

## Installation / Usage

### Prerequisites

* **Python 3.8+**
* **FFmpeg** installed and added to your system PATH (required by `yt-dlp` for video and audio processing)

### Setup

1. Clone or download the repo into your local machine, and open up a terminal in the downloaded directory.

```bash
git clone https://github.com/arch-devnix/YTDownPY.git
cd YTDownPY

```

2. Create a virtual environment inside the directory

```bash
python -m venv venv

```

3. Activate the virtual environment

* **Linux / macOS:**
```bash
source venv/bin/activate

```


* **Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat

```


* **Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1

```



4. Install the dependencies

```bash
pip install -r requirements.txt

```

5. Run the program

```bash
python main.py

```

## Showcase
<p align="center">   
  <img width="400" alt="YTDownPy Interface" src="https://github.com/user-attachments/assets/29babbe8-3469-4690-9df6-035b6c323364" />   
  <img width="421" alt="YTDownPy Demo" src="https://github.com/user-attachments/assets/3be38115-3cb2-4142-b89c-79e282b6cc00" /> 
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/76a94acc-e0ae-43cd-8fad-4328974bc445" />
  
## License

This project uses the MIT License, refer to `LICENSE` for more details.

## Note

I won't be maintaining this since this was just a fun weekend project. Don't expect anything crazy. This was built in Arch Linux therefore, it might not work on other operating systems (Although i'm 99% sure it does work)

yes, that was just for me to say "I use Arch BTW"
