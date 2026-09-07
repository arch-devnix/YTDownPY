# YTDownPY

YouTube video downloader desktop app made using Python, featuring a GUI built with **CustomTkinter** and media extraction powered by **yt-dlp**. Uses multi-threading to ensure the interface remains fast and responsive.

---

## Features

* **Query Search:** Searches and retrieves the top 5 YouTube videos matching key terms.
* **Responsive GUI:** Offloads heavy download tasks to background threads to prevent UI freezes.
* **Progress Tracking:** Integrated CustomTkinter progress bar for real-time status updates.
* **Input Validation:** Prevents empty queries and handles network/download errors gracefully.

---

## Project Structure

* **`main.py`**: Handles the CustomTkinter GUI layout, user inputs, and thread management.
* **`download.py`**: Manages backend logic, queries, and media extraction via `yt-dlp`.

---

## Installation & Usage

### Prerequisites

* **Python 3.8+**
* **FFmpeg** installed and added to your system PATH (required by `yt-dlp` for video/audio processing).
* **Linux (Arch):** `sudo pacman -S ffmpeg`
* **Linux (Debian/Ubuntu):** `sudo apt install ffmpeg`
* **macOS:** `brew install ffmpeg`
* **Windows:** Download via [ffmpeg.org](https://ffmpeg.org/download.html) or `winget install FFmpeg`



### Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/YTDownPY.git
cd YTDownPY

```


2. **Create a virtual environment**
```bash
python -m venv venv

```


3. **Activate the virtual environment**
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




4. **Install dependencies**
```bash
pip install -r requirements.txt

```


5. **Run the application**
```bash
python main.py

```



---

## Showcase

---

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## Note

This was a fun weekend project built on Arch Linux (*I use Arch BTW*). It is provided as-is and will not be actively maintained.
