import streamlit as st
from datetime import datetime
import urllib.request
import urllib.parse

# --- إعدادات البوت والصفحة ---
st.set_page_config(page_title="هدية خاصة لـ إيلاف ✨", page_icon="🎁", layout="centered")

TELEGRAM_TOKEN = "8623658853:AAFo5okW0IZF-5sFYEiQ7-7T9GWOkzlUghI"
# ✏️ ضع الـ Chat ID الخاص بك هنا لتصلك الرسائل على تليجرام:
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

# --- إدارة الحالة (Session State) ---
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

# --- تصميم الصفحة والألوان ---
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        text-align: center;
        border-top: 8px solid #fbbf24;
    }
    .title-text { color: #e11d48; font-size: 32px; font-weight: bold; margin-bottom: 5px; }
    .sub-text { color: #0f172a; font-size: 22px; margin-bottom: 25px; }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- الشاشة الأولى ---
if st.session_state.page == "first":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>🎁</h1>", unsafe_allow_html=True)
    st.markdown('<div class="title-text">هدية خاصة لكي 🙂</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">هل تقبليها مني 😊</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("نعم 💖", type="primary"):
            st.session_state.page = "options"
            st.rerun()
    with col2:
        if st.button("لا ❌"):
            st.session_state.no_count += 1
            st.warning("الزر يهرب! اضغطي نعم 😊")
    st.markdown('</div>', unsafe_allow_html=True)

# --- الشاشة الثانية (الخيارات) ---
elif st.session_state.page == "options":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title-text" style="color:#be185d;">اختر هديتك 🎁✨</div>', unsafe_allow_html=True)
    
    now_str = datetime.now().strftime("%I:%M:%S %p")

    # الخيار الأول: آيفون
    if not st.session_state.disabled_opts["iphone"]:
        if st.button("📱  آيفون 18 برو ماكس"):
            st.session_state.disabled_opts["iphone"] = True
            st.session_state.choices_history.append(f"📱 آيفون 18 برو ماكس ({now_str})")
            st.info("شسوين بي انتِ تلفونج أغلى واندر لن انتِ تستخدمي♥😊")
    else:
        st.button("📱  آيفون 18 برو ماكس (تم الاختيار ✔️)", disabled=True)

    # الخيار الثاني: ذهب
    if not st.session_state.disabled_opts["gold"]:
        if st.button("💎  ذهب خالص"):
            st.session_state.disabled_opts["gold"] = True
            st.session_state.choices_history.append(f"💎 ذهب ({now_str})")
            st.info("انتِ اغلى من الذهب وعيونج اغلى من الألماس ✨")
    else:
        st.button("💎  ذهب خالص (تم الاختيار ✔️)", disabled=True)

    # الخيار الثالث: أوروبا
    if not st.session_state.disabled_opts["europe"]:
        if st.button("✈️  سفرة الى أوروبا"):
            st.session_state.disabled_opts["europe"] = True
            st.session_state.choices_history.append(f"✈️ سفرة الى أوروبا ({now_str})")
            st.info("والله يا إيلاف والدولار صاعد 180😕 والوضعية ما ساعد، وانتِ وحدج سافر بيج الجمال💖")
    else:
        st.button("✈️  سفرة الى أوروبا (تم الاختيار ✔️)", disabled=True)

    # الخيار الرابع: أنت هديتي
    if st.button("💖  انت هديتي", type="primary"):
        st.session_state.choices_history.append(f"💖 انت هديتي ({now_str})")
        st.session_state.page = "celebration"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- الشاشة الثالثة (الاحتفال والتقرير) ---
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

    st.markdown('<div class="card" style="background-color: #020617; color: white;">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>🎂</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #fbbf24;'>🎉 كل عام وأنتِ بألف خير يا إيلاف! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #f43f5e;'>أنتِ أجمل هدية ❤️✨</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; color: #e2e8f0;'>أتمنى لكِ سنة مليئة بالسعادة، النجاح والراحة 🌸💖</p>", unsafe_allow_html=True)
    
    if st.button("الرجوع للقائمة 🔄"):
        st.session_state.page = "options"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
