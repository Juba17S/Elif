import tkinter as tk
import random
from datetime import datetime
import urllib.request
import urllib.parse
import json

# --- إعدادات بوت تليجرام ---
TELEGRAM_TOKEN = "8623658853:AAFo5okW0IZF-5sFYEiQ7-7T9GWOkzlUghI"
# ✏️ ضغ الـ Chat ID الخاص بحسابك هنا لتصلك الرسائل عليه:
MY_CHAT_ID = "8623658853" 

def send_telegram_report(message_text):
    if MY_CHAT_ID == "YOUR_CHAT_ID_HERE":
        print("تنبيه: لم يتم وضع CHAT_ID الخاص بك، لن يتم إرسال الرسالة لتليجرام.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": MY_CHAT_ID,
        "text": message_text,
        "parse_mode": "HTML"
    }
    try:
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data)
        urllib.request.urlopen(req)
        print("تم إرسال التقرير بنجاح إلى تليجرام! 🚀")
    except Exception as e:
        print(f"خطأ في إرسال التقرير: {e}")

class UltraRealisticBirthdayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("هدية خاصة لـ إيلاف ✨")
        self.root.geometry("700x780")
        self.root.configure(bg="#0f172a")
        self.root.resizable(False, False)

        # تتبع الإحصائيات والاختيارات
        self.no_clicks_count = 0  # عدد محاولات الضغط/التحويم على لا
        self.choices_history = []  # سجّل بالخيارات بالترتيب
        self.report_sent = False   # لمنع تكرار إرسال التقرير

        self.disabled_options = {
            "iphone": False,
            "gold": False,
            "europe": False
        }

        self.particles = []
        self.flames = []
        self.animating = False

        self.show_first_screen()

    def clear_screen(self):
        self.animating = False
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_3d_card(self):
        shadow = tk.Frame(self.root, bg="#020617")
        shadow.place(relx=0.505, rely=0.505, anchor="center", width=610, height=700)

        card = tk.Frame(self.root, bg="#ffffff", bd=0, highlightthickness=4, highlightbackground="#f43f5e")
        card.place(relx=0.5, rely=0.5, anchor="center", width=610, height=700)

        gold_stripe = tk.Frame(card, bg="#fbbf24", height=10)
        gold_stripe.pack(fill="x", side="top")

        return card

    def create_custom_button(self, parent, text, command, bg_color, shadow_color, is_disabled=False, width=380, height=60):
        canvas = tk.Canvas(parent, width=width, height=height, bg="#ffffff", highlightthickness=0)
        
        if is_disabled:
            canvas.create_rectangle(5, 5, width-5, height-5, fill="#e2e8f0", outline="#cbd5e1", width=2)
            canvas.create_text(width/2, height/2, text=text + " (تم الاختيار ✔️)", font=("Simplified Arabic", 15, "bold"), fill="#94a3b8")
            return canvas

        shadow_rect = canvas.create_rectangle(6, 8, width-4, height-2, fill=shadow_color, outline="")
        btn_rect = canvas.create_rectangle(4, 4, width-6, height-6, fill=bg_color, outline="")
        
        gloss_light = self.lighten_color(bg_color)
        gloss_polygon = canvas.create_polygon(
            6, 6, 
            width-8, 6, 
            width-18, height/2 - 2, 
            6, height/2 - 2, 
            fill=gloss_light, outline=""
        )

        btn_text = canvas.create_text(width/2, height/2, text=text, font=("Segoe UI Emoji", 15, "bold"), fill="#ffffff")

        def on_enter(e):
            canvas.itemconfig(btn_rect, fill=gloss_light)
            canvas.config(cursor="hand2")

        def on_leave(e):
            canvas.itemconfig(btn_rect, fill=bg_color)

        def on_press(e):
            canvas.move(btn_rect, 0, 3)
            canvas.move(gloss_polygon, 0, 3)
            canvas.move(btn_text, 0, 3)

        def on_release(e):
            canvas.move(btn_rect, 0, -3)
            canvas.move(gloss_polygon, 0, -3)
            canvas.move(btn_text, 0, -3)
            if command:
                command()

        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)
        canvas.bind("<Button-1>", on_press)
        canvas.bind("<ButtonRelease-1>", on_release)

        return canvas

    def lighten_color(self, hex_color):
        color_map = {
            "#be185d": "#f43f5e",
            "#d97706": "#fbbf24",
            "#059669": "#34d399",
            "#e11d48": "#fb7185",
            "#10b981": "#6ee7b7",
            "#f43f5e": "#fda4af",
            "#3b82f6": "#60a5fa"
        }
        return color_map.get(hex_color, "#ffffff")

    # --- الشاشة الأولى ---
    def show_first_screen(self):
        self.clear_screen()

        self.bg_canvas = tk.Canvas(self.root, bg="#0f172a", highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)

        card = self.create_3d_card()

        icon_frame = tk.Frame(card, bg="#ffe4e6", width=120, height=120)
        icon_frame.pack(pady=(40, 15))
        icon_frame.pack_propagate(False)
        lbl_gift = tk.Label(icon_frame, text="🎁", font=("Segoe UI Emoji", 65), bg="#ffe4e6")
        lbl_gift.pack(expand=True)

        lbl_title = tk.Label(
            card,
            text="هدية خاصة لكي 🙂",
            font=("Simplified Arabic", 32, "bold"),
            fg="#e11d48",
            bg="#ffffff"
        )
        lbl_title.pack(pady=(0, 5))

        lbl_sub = tk.Label(
            card,
            text="هل تقبليها مني 😊",
            font=("Arabic Typesetting", 24, "bold"),
            fg="#0f172a",
            bg="#ffffff"
        )
        lbl_sub.pack(pady=(0, 40))

        self.btn_area = tk.Frame(card, bg="#ffffff", width=500, height=130)
        self.btn_area.pack()

        btn_yes = self.create_custom_button(
            self.btn_area,
            "نعم 💖",
            self.show_options_screen,
            bg_color="#10b981",
            shadow_color="#047857",
            width=160,
            height=58
        )
        btn_yes.place(x=70, y=20)

        self.btn_no = self.create_custom_button(
            self.btn_area,
            "لا ❌",
            None,
            bg_color="#f43f5e",
            shadow_color="#be185d",
            width=160,
            height=58
        )
        self.btn_no.place(x=270, y=20)

        self.btn_no.bind("<Enter>", self.escape_no_button)
        self.btn_no.bind("<Button-1>", self.escape_no_button)

        self.init_floating_hearts()
        self.animating = True
        self.animate_hearts()

    def escape_no_button(self, event=None):
        self.no_clicks_count += 1  # تسجيل محاولة الرفض
        new_x = random.randint(10, 310)
        new_y = random.randint(0, 60)
        self.btn_no.place(x=new_x, y=new_y)

    # --- الشاشة الثانية (اختيار الهدايا) ---
    def show_options_screen(self):
        self.clear_screen()

        card = self.create_3d_card()

        lbl_header = tk.Label(
            card,
            text="اختر هديتك 🎁✨",
            font=("Simplified Arabic", 32, "bold"),
            fg="#be185d",
            bg="#ffffff"
        )
        lbl_header.pack(pady=(35, 25))

        options = [
            ("iphone", "📱  آيفون 18 برو ماكس", self.select_iphone, "#be185d", "#831843"),
            ("gold", "💎  ذهب خالص", self.select_gold, "#d97706", "#78350f"),
            ("europe", "✈️  سفرة الى أوروبا", self.select_europe, "#059669", "#064e3b"),
            ("gift", "💖  انت هديتي", self.select_final_gift, "#e11d48", "#881337")
        ]

        for key, text, cmd, bg_col, shadow_col in options:
            is_dis = self.disabled_options.get(key, False)
            btn = self.create_custom_button(
                card,
                text,
                cmd,
                bg_col,
                shadow_col,
                is_disabled=is_dis,
                width=380,
                height=58
            )
            btn.pack(pady=12)

    def record_choice(self, title):
        now_str = datetime.now().strftime("%I:%M:%S %p")
        self.choices_history.append(f"{title} (الساعة {now_str})")

    def select_iphone(self):
        self.disabled_options["iphone"] = True
        self.record_choice("📱 آيفون 18 برو ماكس")
        self.show_styled_popup("📱 آيفون 18 برو ماكس", "شسوين بي انتِ تلفونج أغلى واندر لن انتِ تستخدمي♥😊", "#f43f5e", "📱")

    def select_gold(self):
        self.disabled_options["gold"] = True
        self.record_choice("💎 ذهب")
        self.show_styled_popup("💎 ذهب", "انتِ اغلى من الذهب وعيونج اغلى من الألماس ✨", "#fbbf24", "💎")

    def select_europe(self):
        self.disabled_options["europe"] = True
        self.record_choice("✈️ سفرة الى أوروبا")
        self.show_styled_popup("✈️ سفرة الى أوروبا", "والله يا إيلاف والدولار صاعد 180😕 والوضعية ما ساعد، وانتِ وحدج سافر بيج الجمال💖", "#10b981", "✈️")

    def select_final_gift(self):
        self.record_choice("💖 انت هديتي (الاختيار النهائي)")
        self.show_celebration_screen()

    def show_styled_popup(self, title, message, theme_color, icon_emoji):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("540x300")
        popup.configure(bg="#0f172a")
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()

        popup.geometry(f"+{self.root.winfo_x() + 80}+{self.root.winfo_y() + 210}")

        frame = tk.Frame(popup, bg="#ffffff", highlightthickness=4, highlightbackground=theme_color)
        frame.pack(fill="both", expand=True, padx=12, pady=12)

        lbl_icon = tk.Label(frame, text=icon_emoji, font=("Segoe UI Emoji", 40), bg="#ffffff")
        lbl_icon.pack(pady=(15, 5))

        lbl_msg = tk.Label(
            frame,
            text=message,
            font=("Simplified Arabic", 17, "bold"),
            fg="#1e293b",
            bg="#ffffff",
            wraplength=460,
            justify="center"
        )
        lbl_msg.pack(expand=True, pady=(0, 15))

        def close_and_refresh():
            popup.destroy()
            self.show_options_screen()

        btn_close = self.create_custom_button(
            frame,
            "حسناً اقنعتني 😁 🌸",
            close_and_refresh,
            bg_color=theme_color,
            shadow_color="#be185d",
            width=220,
            height=48
        )
        btn_close.pack(pady=(0, 20))

    def draw_realistic_cake(self, canvas, center_x, base_y):
        canvas.create_rectangle(center_x - 130, base_y - 60, center_x + 130, base_y, fill="#f43f5e", outline="#be185d", width=3)
        for i in range(-120, 130, 30):
            canvas.create_oval(center_x + i - 15, base_y - 68, center_x + i + 15, base_y - 52, fill="#ffffff", outline="#ffe4e6")

        canvas.create_rectangle(center_x - 90, base_y - 120, center_x + 90, base_y - 60, fill="#fef08a", outline="#eab308", width=3)
        for i in range(-80, 90, 25):
            canvas.create_oval(center_x + i - 12, base_y - 126, center_x + i + 12, base_y - 114, fill="#ffffff", outline="#fef3c7")

        canvas.create_rectangle(center_x - 55, base_y - 165, center_x + 55, base_y - 120, fill="#78350f", outline="#451a03", width=3)
        for i in range(-45, 50, 20):
            canvas.create_oval(center_x + i - 10, base_y - 170, center_x + i + 10, base_y - 160, fill="#f472b6", outline="#db2777")

        canvas.create_oval(center_x - 40, base_y - 180, center_x - 26, base_y - 166, fill="#dc2626", outline="#991b1b")
        canvas.create_oval(center_x + 26, base_y - 180, center_x + 40, base_y - 166, fill="#dc2626", outline="#991b1b")

        candle_positions = [center_x - 20, center_x, center_x + 20]
        candle_colors = ["#3b82f6", "#ec4899", "#10b981"]

        self.flames = []
        for idx, cx in enumerate(candle_positions):
            canvas.create_rectangle(cx - 4, base_y - 195, cx + 4, base_y - 165, fill=candle_colors[idx], outline="#ffffff")
            canvas.create_line(cx, base_y - 195, cx, base_y - 200, fill="#000000", width=2)
            
            outer_f = canvas.create_oval(cx - 7, base_y - 216, cx + 7, base_y - 200, fill="#ff6b00", outline="#ff9e00")
            inner_f = canvas.create_oval(cx - 3, base_y - 212, cx + 3, base_y - 202, fill="#ffea00", outline="")
            
            self.flames.append({'cx': cx, 'base_y': base_y - 200, 'outer': outer_f, 'inner': inner_f})

    # --- الشاشة الثالثة وإرسال التقرير لتليجرام ---
    def show_celebration_screen(self):
        self.clear_screen()

        # إرسال التقرير فور الوصول لهذه الشاشة
        if not self.report_sent:
            self.send_final_report()
            self.report_sent = True

        self.canvas = tk.Canvas(self.root, width=700, height=780, bg="#020617", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.draw_realistic_cake(self.canvas, 350, 240)

        self.canvas.create_text(
            350, 290,
            text="🎉 كل عام وأنتِ بألف خير يا إيلاف! 🎉",
            fill="#fbbf24",
            font=("Simplified Arabic", 28, "bold")
        )

        self.canvas.create_text(
            350, 365,
            text="أنتِ أجمل هدية ❤️✨",
            fill="#f43f5e",
            font=("Simplified Arabic", 24, "bold")
        )

        self.canvas.create_text(
            350, 435,
            text="أتمنى لكِ سنة مليئة بالسعادة، النجاح والراحة 🌸💖",
            fill="#e2e8f0",
            font=("Simplified Arabic", 16),
            justify="center"
        )

        btn_back = self.create_custom_button(
            self.root,
            "الرجوع للقائمة 🔄",
            self.show_options_screen,
            bg_color="#1e1b4b",
            shadow_color="#020617",
            width=220,
            height=50
        )
        self.canvas.create_window(350, 560, window=btn_back)

        self.init_gentle_confetti()
        self.animating = True
        self.animate_celebration()

    def send_final_report(self):
        now_time = datetime.now().strftime("%Y-%m-%d  |  %I:%M:%S %p")
        
        history_text = "\n".join([f"   <b>{idx+1}.</b> {choice}" for idx, choice in enumerate(self.choices_history)])
        if not history_text:
            history_text = "   لم يتم تسجيل خيارات."

        msg = (
            f"🎁 <b>تقرير فتح هدية عيد الميلاد!</b> 🎁\n\n"
            f"📅 <b>التاريخ والوقت:</b>\n<code>{now_time}</code>\n\n"
            f"❌ <b>محاولات الضغط على زر 'لا':</b>\n<code>{self.no_clicks_count} مرة</code>\n\n"
            f"شريط الخيارات حسب الترتيب 📜:\n"
            f"{history_text}\n\n"
            f"✨ <i>تم فتح الهدية بنجاح!</i>"
        )
        
        send_telegram_report(msg)

    def animate_celebration(self):
        if not self.animating:
            return

        for f in self.flames:
            cx = f['cx']
            base_y = f['base_y']
            dx = random.uniform(-1.5, 1.5)
            dy = random.uniform(-2, 1)
            
            self.canvas.coords(f['outer'], cx - 7 + dx, base_y - 16 + dy, cx + 7 + dx, base_y)
            self.canvas.coords(f['inner'], cx - 3 + dx, base_y - 12 + dy, cx + 3 + dx, base_y - 2)

        for p in self.particles:
            self.canvas.move(p['id'], 0, p['speed'])
            pos = self.canvas.coords(p['id'])
            
            if pos and pos[1] > 780:
                new_x = random.randint(20, 680)
                new_y = random.randint(-50, -10)
                self.canvas.coords(p['id'], new_x, new_y, new_x + p['size'], new_y + p['size'])

        self.root.after(40, self.animate_celebration)

    def init_floating_hearts(self):
        self.particles = []
        hearts = ["✨", "💖", "🌷", "💕", "🌸", "💎"]
        for _ in range(30):
            x = random.randint(20, 680)
            y = random.randint(0, 760)
            char = random.choice(hearts)
            speed = random.uniform(1.0, 3.0)
            item = self.bg_canvas.create_text(x, y, text=char, font=("Segoe UI Emoji", random.randint(14, 24)))
            self.particles.append([item, speed])

    def animate_hearts(self):
        if not self.animating:
            return
        for p in self.particles:
            item, speed = p[0], p[1]
            self.bg_canvas.move(item, 0, -speed)
            pos = self.bg_canvas.coords(item)
            if pos and pos[1] < -10:
                self.bg_canvas.coords(item, random.randint(20, 680), 780)
        self.root.after(40, self.animate_hearts)

    def init_gentle_confetti(self):
        self.particles = []
        colors = ["#f43f5e", "#ec4899", "#d946ef", "#a855f7", "#3b82f6", "#10b981", "#fbbf24", "#ffffff"]
        
        for _ in range(90):
            x = random.randint(20, 680)
            y = random.randint(-400, 0)
            size = random.randint(6, 12)
            color = random.choice(colors)
            speed = random.uniform(2.5, 5.5)
            
            p_id = self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
            self.particles.append({'id': p_id, 'speed': speed, 'size': size})

if __name__ == "__main__":
    root = tk.Tk()
    app = UltraRealisticBirthdayApp(root)
    root.mainloop()