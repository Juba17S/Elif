import streamlit as st
import urllib.request
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="هدية خاصة لـ إيلاف ✨", page_icon="🎁", layout="centered")

TELEGRAM_TOKEN = "8623658853:AAFo5okW0IZF-5sFYEiQ7-7T9GWOkzlUghI"
# ✏️ ضع الـ CHAT_ID الخاص بك هنا لكي تصلك التقرير على تليجرام:
MY_CHAT_ID = "YOUR_CHAT_ID_HERE"

def send_telegram_report(message_text):
    if MY_CHAT_ID == "YOUR_CHAT_ID_HERE":
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": MY_CHAT_ID, "text": message_text, "parse_mode": "HTML"}
    try:
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data)
        urllib.request.urlopen(req)
    except Exception:
        pass

# --- إدارة الحالة ---
if "page" not in st.session_state:
    st.session_state.page = "first"
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "choices_history" not in st.session_state:
    st.session_state.choices_history = []
if "disabled_opts" not in st.session_state:
    st.session_state.disabled_opts = {"iphone": False, "gold": False, "europe": False}
if "report_sent" not in st.session_state:
    st.session_state.report_sent = False

# --- تصميم CSS احترافي بأزرار 3D لمعة وخلفية فخمة ---
st.markdown("""
<style>
    .stApp { background-color: #0f172a; }
    .card-3d {
        background: #ffffff;
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5), inset 0 2px 0 rgba(255,255,255,0.8);
        border: 4px solid #f43f5e;
        text-align: center;
        position: relative;
    }
    .gold-stripe {
        height: 8px;
        background: #fbbf24;
        border-radius: 10px 10px 0 0;
        margin: -30px -30px 20px -30px;
    }
    .glossy-btn {
        background: linear-gradient(180deg, #f43f5e 0%, #be185d 100%);
        color: white !important;
        font-weight: bold;
        font-size: 18px;
        border-radius: 14px;
        box-shadow: 0 6px 0 #831843, 0 10px 15px rgba(0,0,0,0.3);
        border: none;
        transition: all 0.1s ease;
    }
    .stButton>button {
        border-radius: 14px !important;
        height: 55px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 6px 0 #020617 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- الشاشة الأولى ---
if st.session_state.page == "first":
    st.markdown('''
    <div class="card-3d">
        <div class="gold-stripe"></div>
        <div style="font-size: 80px; margin-bottom: 10px;">🎁</div>
        <h1 style="color: #e11d48; font-size: 32px; font-weight: bold; margin: 0;">هدية خاصة لكي 🙂</h1>
        <p style="color: #0f172a; font-size: 22px; font-weight: bold; margin-top: 5px;">هل تقبليها مني 😊</p>
    </div>
    <br>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("نعم 💖", type="primary", use_container_width=True):
            st.session_state.page = "options"
            st.rerun()
    with col2:
        if st.button("لا ❌", use_container_width=True):
            st.session_state.no_count += 1
            st.warning("الزر يهرب! اضغطي نعم 😊")

# --- الشاشة الثانية (الخيارات) ---
elif st.session_state.page == "options":
    st.markdown('''
    <div class="card-3d">
        <div class="gold-stripe"></div>
        <h1 style="color: #be185d; font-size: 30px; font-weight: bold;">اختر هديتك 🎁✨</h1>
    </div>
    <br>
    ''', unsafe_allow_html=True)

    now_str = datetime.now().strftime("%I:%M:%S %p")

    if not st.session_state.disabled_opts["iphone"]:
        if st.button("📱  آيفون 18 برو ماكس", use_container_width=True):
            st.session_state.disabled_opts["iphone"] = True
            st.session_state.choices_history.append(f"📱 آيفون 18 برو ماكس ({now_str})")
            st.info("شسوين بي انتِ تلفونج أغلى واندر لن انتِ تستخدمي♥😊")
    else:
        st.button("📱  آيفون 18 برو ماكس (تم الاختيار ✔️)", disabled=True, use_container_width=True)

    if not st.session_state.disabled_opts["gold"]:
        if st.button("💎  ذهب خالص", use_container_width=True):
            st.session_state.disabled_opts["gold"] = True
            st.session_state.choices_history.append(f"💎 ذهب ({now_str})")
            st.info("انتِ اغلى من الذهب وعيونج اغلى من الألماس ✨")
    else:
        st.button("💎  ذهب خالص (تم الاختيار ✔️)", disabled=True, use_container_width=True)

    if not st.session_state.disabled_opts["europe"]:
        if st.button("✈️  سفرة الى أوروبا", use_container_width=True):
            st.session_state.disabled_opts["europe"] = True
            st.session_state.choices_history.append(f"✈️ سفرة الى أوروبا ({now_str})")
            st.info("والله يا إيلاف والدولار صاعد 180😕 والوضعية ما ساعد، وانتِ وحدج سافر بيج الجمال💖")
    else:
        st.button("✈️  سفرة الى أوروبا (تم الاختيار ✔️)", disabled=True, use_container_width=True)

    if st.button("💖  انت هديتي", type="primary", use_container_width=True):
        st.session_state.choices_history.append(f"💖 انت هديتي ({now_str})")
        st.session_state.page = "celebration"
        st.rerun()

# --- الشاشة الثالثة (الكيكة والشموع المتحركة بـ HTML Canvas) ---
elif st.session_state.page == "celebration":
    st.balloons()

    if not st.session_state.report_sent:
        now_time = datetime.now().strftime("%Y-%m-%d  |  %I:%M:%S %p")
        history_text = "\n".join([f"   <b>{idx+1}.</b> {choice}" for idx, choice in enumerate(st.session_state.choices_history)])
        msg = (
            f"🎁 <b>تقرير فتح هدية عيد الميلاد!</b> 🎁\n\n"
            f"📅 <b>الوقت:</b> <code>{now_time}</code>\n"
            f"❌ <b>محاولات زر 'لا':</b> <code>{st.session_state.no_count} مرة</code>\n\n"
            f"📜 <b>ترتيب الخيارات:</b>\n{history_text}"
        )
        send_telegram_report(msg)
        st.session_state.report_sent = True

    # رسم الكيكة والشموع المتحركة واقعياً على الويب مباشرة
    st.components.v1.html("""
    <div style="text-align: center; background: #020617; padding: 20px; border-radius: 20px;">
        <canvas id="cakeCanvas" width="350" height="220"></canvas>
        <h2 style="color: #fbbf24; font-family: sans-serif; margin-top: 10px;">🎉 كل عام وأنتِ بألف خير يا إيلاف! 🎉</h2>
        <h3 style="color: #f43f5e; font-family: sans-serif;">أنتِ أجمل هدية ❤️✨</h3>
        <p style="color: #e2e8f0; font-family: sans-serif;">أتمنى لكِ سنة مليئة بالسعادة، النجاح والراحة 🌸💖</p>
    </div>

    <script>
        const canvas = document.getElementById('cakeCanvas');
        const ctx = canvas.getContext('2d');

        function drawCake() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const cx = 175, basey = 200;

            // طبقات الكيكة
            ctx.fillStyle = '#f43f5e'; ctx.fillRect(cx - 90, basey - 40, 180, 40);
            ctx.fillStyle = '#fef08a'; ctx.fillRect(cx - 65, basey - 80, 130, 40);
            ctx.fillStyle = '#78350f'; ctx.fillRect(cx - 40, basey - 110, 80, 30);

            // الشموع
            const pos = [cx - 20, cx, cx + 20];
            const colors = ['#3b82f6', '#ec4899', '#10b981'];

            pos.forEach((x, i) => {
                ctx.fillStyle = colors[i];
                ctx.fillRect(x - 3, basey - 130, 6, 20);
                
                // نار الشمعة المتحركة
                let dx = (Math.random() - 0.5) * 3;
                let dy = (Math.random() - 0.5) * 2;
                
                ctx.beginPath();
                ctx.arc(x + dx, basey - 136 + dy, 6, 0, Math.PI * 2);
                ctx.fillStyle = '#ff6b00'; ctx.fill();
                
                ctx.beginPath();
                ctx.arc(x + dx, basey - 136 + dy, 3, 0, Math.PI * 2);
                ctx.fillStyle = '#ffea00'; ctx.fill();
            });
        }
        setInterval(drawCake, 80);
    </script>
    """, height=420)

    if st.button("الرجوع للقائمة 🔄", use_container_width=True):
        st.session_state.page = "options"
        st.rerun()
