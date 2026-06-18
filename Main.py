import threading
import random
import time
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
import speech_recognition as sr

class MobileOverlayApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple" 
        
        # App State
        self.current_viewers = 1
        self.max_viewers = 647[cite: 1]
        
        # --- PROCEDURAL CHAT DATA ---
        self.chat_usernames = [
            "GamerX", "StreamSniper", "GlitchFace", "PixelLord", "VibeCheck99", 
            "Shadow_Runs", "CyberPunk", "HyperDrive", "NeonKnight", "KappaClaus",
            "ChillBeans", "ToxicAvenger", "PogChamp_69", "LootGoblin", "WkeySpammer"
        ]
        
        self.chat_templates = [
            "Yo Matthew! What's good?"
"stream is rendering perfectly today ngl"
"bro what are you wearing lmao 💀"
"Sending good vibes for the stream today! ✨"
"drop the playlist link expeditiously"
"actually throwing, uninstall please"
"That play was clean, absolute cinema"
"We eating good with this stream tonight"
"Hello Matthew hope you are having a nice day"
"wait what did I miss? Just tapped in"
"This gameplay is cooked. Absolutely cooked."
"Your layout looks so pretty today! 💜"
"can we get a W in the chat"
"standard Matthew L tbh"
"blaze it up, front row seats to greatness lets gooo"
"bro thinks he’s him 😭"
"Incredible tracking right there!"
"is it just me or is the audio kinda low?"
"Audio is fine for me, check your setup"
"preview of a professional hardstuck player"
"absolute textbook execution right there"
"This stream always clears my bad mood"
"boring. play something else"
"Love the energy today Matthew! 🔥"
"chat is moving so fast wtf"
"peak entertainment right here"
"bro is playing with his eyes closed surely"
"That overlay looks so sleek wow"
"setup is looking highkey fire"
"worst stream on the platform hands down"
"The comeback is going to be legendary"
"bro got zero aura after that play"
"you got this!! don't let the trolls get to you"
"valid strategy honestly"
"my grandmother plays faster than this"
"That was a massive brain move"
"bro is coping so hard right now"
"Let's goooo! Big dubs only!"
"wait is this live or a recording?"
"live chat, we here!"
"missing every shot is crazy work"
"Mod team is working overtime today bless them"
"loving the vibe so much! 🥰"
"you need to adjust your sensitivity fr"
"built different fr fr"
"drop the spec sheet for the PC again?"
"imagine hating in the chat, couldn't be me"
"bro is entirely washed, tragic to see"
"THAT WAS INSANE!!!"
"stealth lurk activated 🥷"
"unlocked a new fear watching that play lol"
"You're doing amazing sweetie! 🐝"
"mid stream, checking out"
"The framerate is buttery smooth today"
"stream schedule update when?"
"bro is frozen in fear lmao"
"Thank you for always streaming, love the content!"
"chat is under collective hypnosis right now"
"L + ratio + fell off"
"blast off! we reaching the milestone tonight!"
"midnight streams just hit different"
"secure the bag Matthew!"
"actual definition of a skill issue right here"
"So wholesome, love this community🌸"
"wait what game is this?"
"bro got deleted out of existence"
"that reaction time was crazy fast"
"unban my boy please he did nothing wrong"
"lowkey the best stream on twitch rn"
"pure garbage gameplay, I'm out"
"This music is so relaxing"
"we up right now!! 📈"
"bro is saltier than the dead sea"
"Keep shining Matthew!"
"clutch or kick let's see it"
"I'm literally falling asleep watching this"
"massive W, we love to see it"
"typing with one hand eating pizza, still better than you"
"This stream is pure comfort content"
"wait for the drop..."
"crying and throwing up over that loss"
"manipulation of the highest order, clean play"
"highkey enjoying this right now"
"system error: streamer brain not found"
"Hope everyone in chat is having a beautiful day!"
"speedy recovery from that blunder"
"definitely using aimbot and still missing lmao"
"been here since day one, love the growth!"
"let's analyze the economic impact of that play"
"who allowed this man to broadcast 💀"
"rizz level is off the charts today"
"so cute! look at the chat go"
"absolute chaos and I am here for it"
"GG, it's over, wrap it up"
"We go again! Back to back wins let's get it"
"everybody in chat needs to relax fr"
"grandpa needs to retire from gaming"
"Such a peaceful stream tonight, thank you"
"absolute peak performance"
"bro vanished from the scoreboard"
"New meme format just dropped"
"Matthew looking sharp today! 😍"
"actual circus going on in this stream"
"commands aren't working for me"
"vibe check passed with flying colors"
"bro is yapping so much today"
"500 IQ play right there, nobody can convince me otherwise"
"You'll get it next time, don't worry!"
"welcome to the hardstuck club Matthew"
"This stream gives me so much life"
"lag? or just bad?"
"love the background setup so much"
"bro thinks he's the main character 😭"
"literal gold content right here"
"PANIC MODE ACTIVATED"
"mod team clean up aisle three please"
"at least you tried, that's what counts!"
"unbothered. moisturized. happy. in my lane."
"actual garbage tier gameplay lmao"
"taking a deep breath after that one"
"stream is completely cooking tonight"
"my little brother plays better than this fr"
"snacking on popcorn watching this drama"
"output looks beautiful today"
"building a house with all them bricks you throwing"
"lucky play but we take those"
"infinite aura points gained"
"hurts to watch but I can't look away"
"setup is looking spicy today Matthew"
"zero hype, dead stream, nothing to see here"
"Absolutely floating after that victory!"
"sharing one collective brain cell with chat right now"
"crying on stream is a crazy look"
"proud of you son"
"bro went into avatar state right there"
"absolute worst content on my feed today"
"Such a chill atmosphere tonight"
"slicing through the competition let's go"
"adding this clip to the cringe compilation"
"The lighting is hitting perfectly right now"
"processing that terrible play... error found"
"Take a break if you need water Matthew! Drink water!"
"chat is absolutely rioting lmao"
"cooked him to a crisp"
"don't listen to the haters, you're doing great"
"skill check: FAILED ❌"
"Love the community here, so welcoming"
"overlay drip is immaculate"
"dude just delete the channel at this point"
"absolutely electric energy right now!"
"wait did the stream just rewind or am I tripping"
"You have the nicest smile Matthew!"
"delete this stream immediately 🗑️"
"music selection is top tier today"
"grind never stops, let's get it"
"bro is typing paragraphs in chat chill out"
"smooth movement, absolutely locked in"
"Hope you're having a wonderful evening!"
"bro skipped the tutorial obviously"
"Literally my favorite streamer right now"
"can you hear us? mic check?"
"typing trash while being down points is wild"
"This stream makes me so happy after a long day"
"alpha energy only in this chat 😤"
"boooooring, do a giveaway or something"
"neon vibes, color palette of the stream is so aesthetic"
"actual 4D chess player right here"
"tragic ending to a beautiful run"
"Sending you lots of love and support!"
"bro is thick-headed as a brick fr"
"defending this chat with my life 🛡️"
"flawless victory incoming"
"clown emoji stream right now"
"Everything about this stream is perfect"
"we moving at hyperspeed now boyzzzz"
"zero talent, pure luck stream"
"visual effects are looking clean"
"Sweetheart you are doing a wonderful job, keep it up!"
"haters are fuming in the comments right now"
"ready for the main event"
"crown slipped, entirely washed"
"perfect stream to fall asleep to (in a good way)"
"Bro's aura is radiating through the screen"
"it's gg, pack it up boys"
"rising from the ashes of that terrible play!"
"chill vibes only, keep the chat positive guys, no negativity"
"dumpster fire of a stream and I love it"
"Setting the gold standard for streaming"
"streamer is experiencing major brain lag rn"
"You brighten up my day Matthew!"
"that flank was actually nasty"
"came here just to drop an L"
"nothing but immaculate vibes in here"
"solid gameplay, ignore the chat backseat driving"
"bro please stop yapping it’s so cringe"
"content is absolute liquid gold tonight"
"We reached the peak of entertainment"
"dude is mad because he lost a pixel game 💀"
"camera quality looks incredible today"
"chat unlocked the secret final boss victory let's gooo!"
        ]
        
        self.chat_fillers = [
            " PogU!!!", " LFG!!!", " Hype!", " lmao", " KekW", " 🔥🔥🔥", " 💀💀💀", 
            " monkaS", " NotLikeThis", " GIGACHAD", " 😂", " check the replay!", " wow."
        ]

        # --- UI LAYOUT ---
        root = MDBoxLayout(
            orientation='vertical', 
            padding="16dp", 
            spacing="16dp",
            md_bg_color=get_color_from_hex("#121212")
        )
        
        # Upper Container: Stats & Mic[cite: 1]
        stats_card = MDCard(
            orientation='vertical',
            padding="16dp",
            spacing="12dp",
            size_hint=(1, 0.35),
            md_bg_color=get_color_from_hex("#1f1f1f"),
            line_color=get_color_from_hex("#9146FF"), # Twitch Purple[cite: 1]
            line_width=2,
            radius=[12, 12, 12, 12]
        )
        
        viewer_layout = MDBoxLayout(orientation='horizontal', size_hint_y=None, height="30dp", spacing="8dp")
        
        self.dot_label = MDLabel(
            text="●", 
            font_style="H5",
            theme_text_color="Custom",
            text_color=get_color_from_hex("#ff4a4a"),
            size_hint_x=None,
            width="24dp"
        )
        
        self.viewer_label = MDLabel(
            text=f"Viewers: {self.current_viewers}",[cite: 1]
            font_style="H6",
            theme_text_color="Primary",
            bold=True
        )
        
        viewer_layout.add_widget(self.dot_label)
        viewer_layout.add_widget(self.viewer_label)
        
        self.speech_label = MDLabel(
            text='"Waiting for you to speak..."',[cite: 1]
            font_style="Subtitle1",
            theme_text_color="Secondary",
            italic=True
        )
        
        stats_card.add_widget(viewer_layout)
        stats_card.add_widget(self.speech_label)
        root.add_widget(stats_card)
        
        # Lower Container: Simulated Streaming Live Chat
        chat_card = MDCard(
            orientation='vertical',
            padding="16dp",
            spacing="8dp",
            size_hint=(1, 0.65),
            md_bg_color=get_color_from_hex("#18181b"), # Darker Twitch Chat Background
            radius=[12, 12, 12, 12]
        )
        
        chat_header = MDLabel(
            text="LIVE STREAM CHAT",
            font_style="Button",
            theme_text_color="Custom",
            text_color=get_color_from_hex("#9146FF"),
            size_hint_y=None,
            height="24dp",
            bold=True
        )
        chat_card.add_widget(chat_header)
        
        # Create 5 labels to act as scrolling chat lines
        self.chat_lines = []
        for _ in range(6):
            lbl = MDLabel(
                text="",
                font_style="Body2",
                theme_text_color="Primary",
                markup=True, # Allows color coding usernames
                size_hint_y=None,
                height="32dp"
            )
            self.chat_lines.append(lbl)
            chat_card.add_widget(lbl)
            
        root.add_widget(chat_card)
        
        # --- START BACKGROUND LOGIC ---
        Clock.schedule_interval(self.animate_live_dot, 0.75)
        
        # Thread 1: Viewer Growth[cite: 1]
        threading.Thread(target=self.viewer_growth_loop, daemon=True).start()[cite: 1]

        # Thread 2: Voice Recognition[cite: 1]
        threading.Thread(target=self.voice_recognition_loop, daemon=True).start()[cite: 1]
        
        # Thread 3: Active Live Chat Simulator
        threading.Thread(target=self.live_chat_loop, daemon=True).start()
        
        return root

    # --- UI UPDATERS ---
    def update_viewer_ui(self, dt):
        self.viewer_label.text = f"Viewers: {self.current_viewers}"[cite: 1]
        
    def update_speech_ui(self, text):
        def set_text(dt):
            self.speech_label.text = f'"{text}"'[cite: 1]
        Clock.schedule_once(set_text)

    def add_chat_message_ui(self, formatted_message):
        """Scrolls the chat messages upward on the screen safely"""
        def update_chat(dt):
            # Shift all text lines up by 1 position
            for i in range(len(self.chat_lines) - 1):
                self.chat_lines[i].text = self.chat_lines[i+1].text
            # Push new message to the bottom row
            self.chat_lines[-1].text = formatted_message
        Clock.schedule_once(update_chat)

    def animate_live_dot(self, dt):
        bright_red = get_color_from_hex("#ff4a4a")[cite: 1]
        dark_red = get_color_from_hex("#a30000")[cite: 1]
        self.dot_label.text_color = dark_red if self.dot_label.text_color == bright_red else bright_red[cite: 1]

    # --- SIMULATED LOOPS ---
    def viewer_growth_loop(self):[cite: 1]
        while True:
            if self.current_viewers < self.max_viewers:[cite: 1]
                remaining = self.max_viewers - self.current_viewers[cite: 1]
                growth_factor = max(1, int(remaining * 0.05))[cite: 1]
                self.current_viewers += random.randint(1, growth_factor)[cite: 1]
                if self.current_viewers > self.max_viewers:[cite: 1]
                    self.current_viewers = self.max_viewers[cite: 1]
                Clock.schedule_once(self.update_viewer_ui)[cite: 1]
            time.sleep(random.randint(5, 15))[cite: 1]

    def live_chat_loop(self):
        """Generates thousands of unique procedural chat messages mentioning 'IQ'"""
        while True:
            # Generate a random colored username
            user = random.choice(self.chat_usernames)
            color = random.choice(["#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#e67e22", "#1abc9c"])
            
            # Construct a unique phrase (thousands of mathematical variations)
            phrase = random.choice(self.chat_templates)
            filler = random.choice(self.chat_fillers) if random.random() > 0.4 else ""
            
            formatted_msg = f"[color={color}][b]{user}:[/b][/color] {phrase}{filler}"
            
            self.add_chat_message_ui(formatted_msg)
            
            # Chat moves faster as viewer count grows[cite: 1]
            speed_modifier = max(0.4, 4.0 - (self.current_viewers / 150.0))
            time.sleep(random.uniform(0.2, speed_modifier))

    def voice_recognition_loop(self):[cite: 1]
        recognizer = sr.Recognizer()[cite: 1]
        try:
            microphone = sr.Microphone()[cite: 1]
            with microphone as source:[cite: 1]
                recognizer.adjust_for_ambient_noise(source, duration=1)[cite: 1]
        except Exception as e:
            self.update_speech_ui(f"Mic Error: {e}")
            return

        while True:
            try:
                with microphone as source:[cite: 1]
                    audio = recognizer.listen(source, phrase_time_limit=5)[cite: 1]
                text = recognizer.recognize_sphinx(audio)[cite: 1]
                if text.strip():[cite: 1]
                    self.update_speech_ui(text)[cite: 1]
            except Exception:
                pass

if __name__ == '__main__':
    MobileOverlayApp().run()
