YTDownPY |  YouTube video downloader desktop app made using Python, featuring a GUI interface built with Custom Tkinter, and media extraction done using yt-dlp library as a backend. Uses multi-threading to make sure the GUI doesn't just freeze

## Features
Query Search: searches and retrieves the top 5 YouTube videos matching the query keywords
Responsive GUI: uses a background thread to process tasks
Progress indicators: CustomTkinter progress indicator
Error handling: Stops users from submitting an empty query

## Project Structure
Main.py is the frontend that mainly handles the GUI and download.py is for. you guessed it... Downloading.

## Installation / Usage

1. Clone or download the repo into your local machine, and open up a terminal in the downloaded directory.
```
cd YTDownPY
```

2. Create a virtual enviroment inside the directory
```
python -m venv venv
```

3. Activate the virtual enviroment
```
source venv/bin/activate
```

4. Install the dependencies
```
pip install -r requirements.txt
```

5. Run the program
```
python main.py
```
## Showcase
<img width="689" height="453" alt="YTDownPy Interface" src="https://github.com/user-attachments/assets/29babbe8-3469-4690-9df6-035b6c323364" />
## License
This project uses the MIT License, refer to `LICENSE` for more details.

## Note
I won't be maintaining this since this was just a fun weekend project. Don't expect anything crazy. This was built in Arch Linux therefore, it might not work on other operating systems (Although i'm 99% sure it does work)

yes, that was just for me to say "I use Arch BTW"
