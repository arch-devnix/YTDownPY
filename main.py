import customtkinter as ctk
from PIL import Image
from downloader import YoutubeManager
from pathlib import Path
import threading

ASSETS_DIR = Path(__file__).resolve().parent / 'assets'

class YoutubeGUI:
    def __init__(self, root):
        self.ytd = YoutubeManager()
        self.root = root

        ctk.set_default_color_theme('blue')
        ctk.set_appearance_mode('dark')

        self.root.geometry('600x500')
        self.root.title('YTDown Project')
        
        # == Title Frame ==
        self.title_frame = ctk.CTkFrame(self.root, fg_color='#ffffff', border_color='#cccccc', border_width=2)
        self.title_frame.pack(pady=(20, 10))

        # ====Load Image asset====
        try:
            img = Image.open(ASSETS_DIR / 'logo.png')
            logo_image = ctk.CTkImage(light_image=img, dark_image=img, size=(36, 36))
            self.icon_label = ctk.CTkLabel(self.title_frame, text="", image=logo_image)
            self.icon_label.pack(side="left", padx=10, pady=5)
        except Exception:
            pass
            
        # == Title ==
        self.title = ctk.CTkLabel(self.title_frame, text='YTDownPY', text_color='black', font=('Roboto', 24, 'bold'))
        self.title.pack(side='left', padx=(0, 10), pady=5)
        
        # == Query Box ==
        self.query_entry = ctk.CTkEntry(self.root, placeholder_text='Search....', width=400)
        self.query_entry.pack(pady=5)
        
        # == Search Btn ==
        self.search_btn = ctk.CTkButton(self.root, text='Search', fg_color='grey', hover_color='#9c9c9c', command=self.run_search)
        self.search_btn.pack(pady=5)
        
        # == Scrollable Frame ==
        self.results_frame = ctk.CTkScrollableFrame(
            self.root, 
            width=530,
            height=250, 
            fg_color='#474747', 
            border_color='black',
            border_width=2
        )
        self.results_frame.pack(pady=10)

    def run_search(self):
        self.query = self.query_entry.get().strip()
        print(f'User entry: {self.query}')
        

        if not self.query:
            self.query_entry.configure(placeholder_text="⚠️ Please type a search term!")
            return


        self.query_entry.delete(0, "end")
        self.query_entry.configure(placeholder_text="Search....")
        
        for widget in self.results_frame.winfo_children():
            widget.destroy()


        self.loading_bar = ctk.CTkProgressBar(self.results_frame, orientation="horizontal")
        self.loading_bar.pack(pady=50, padx=20, fill="x")
        

        self.loading_bar.configure(mode="indeterminate")
        self.loading_bar.start()

        threading.Thread(target=self.display_vids, daemon=True).start()

    def display_vids(self):
        try:
            videos = self.ytd.getvids(self.query)

            if hasattr(self, 'loading_bar'):
                self.loading_bar.destroy()

            for vid in videos:
                self.video_text = f"{vid['title']} | By: {vid['uploader']} ({vid['duration']})"
                text_label = ctk.CTkLabel(
                    master=self.results_frame, 
                    text=self.video_text,
                    text_color="white",
                    font=('Roboto', 14)
                )
                text_label.pack(pady=5, anchor="w", padx=10, fill='x')
                text_label.bind(
                    '<Button-1>',
                    lambda event,
                    url=vid['url']: 
                    threading.Thread(
                        target=self.on_video_click, args=(url,), daemon=True
                    ).start()
                )
        except Exception as e:
            print(f"Error fetching videos: {e}")
            if hasattr(self, 'loading_bar'):
                self.loading_bar.destroy()

    def on_video_click(self, url):
        self.query_entry.configure(placeholder_text='Search....')
        try:
            print(f'User clicked: {url}')
            for widget in self.results_frame.winfo_children():
                widget.destroy()

            self.loading_bar = ctk.CTkProgressBar(self.results_frame, orientation="horizontal")
            self.loading_bar.pack(pady=50, padx=20, fill="x")
            

            self.loading_bar.configure(mode="indeterminate")
            self.loading_bar.start()

            self.ytd.download_video(url)

            completion_label = ctk.CTkLabel(self.results_frame, text="✅ Download Complete!", text_color="green", font=('Roboto', 16, 'bold'))
            completion_label.pack(pady=50)


        except Exception as e:
            completion_label = ctk.CTkLabel(self.results_frame, text=f"❌ Error: {e}", text_color="red", font=('Roboto', 16, 'bold'))
            completion_label.pack(pady=50)

        finally:
            if hasattr(self, 'loading_bar'):
                    self.loading_bar.destroy()

if __name__ == "__main__":
    new_window = ctk.CTk()
    ytdown = YoutubeGUI(new_window)
    new_window.mainloop()