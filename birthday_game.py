import streamlit as st
import random
import time
from datetime import datetime

# Page config
st.set_page_config(page_title="🎂 Happy Birthday My Love!", page_icon="🎮", layout="wide")

# Initialize session state
if 'game_stage' not in st.session_state:
    st.session_state.game_stage = 'intro'
    st.session_state.score = 0
    st.session_state.questions_answered = 0
    st.session_state.jellyfish_collected = 0
    st.session_state.love_level = 0
    st.session_state.combo = 0
    st.session_state.clicked_heart = False

# Enhanced CSS with creative animations and interactions
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-30px) rotate(5deg); }
        66% { transform: translateY(-15px) rotate(-5deg); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.15); }
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        10%, 30% { transform: scale(1.1); }
        20%, 40% { transform: scale(1.15); }
    }
    
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(255,107,107,0.5), 0 0 40px rgba(78,205,196,0.3); }
        50% { box-shadow: 0 0 40px rgba(255,107,107,0.8), 0 0 80px rgba(78,205,196,0.6); }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes wiggle {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(10deg); }
        75% { transform: rotate(-10deg); }
    }
    
    @keyframes fall {
        0% { 
            transform: translateY(-100px) rotate(0deg); 
            opacity: 1; 
        }
        100% { 
            transform: translateY(calc(100vh + 100px)) rotate(720deg); 
            opacity: 0.3; 
        }
    }
    
    @keyframes sparkleExpand {
        0% { 
            opacity: 0; 
            transform: scale(0) rotate(0deg); 
        }
        50% { 
            opacity: 1; 
            transform: scale(1.5) rotate(180deg); 
        }
        100% { 
            opacity: 0; 
            transform: scale(0) rotate(360deg); 
        }
    }
    
    @keyframes shockwave {
        0% {
            transform: scale(0);
            opacity: 1;
        }
        100% {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background gradient animation */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Sparkle cursor trail */
    .sparkle {
        position: fixed;
        pointer-events: none;
        animation: sparkleExpand 1s ease-out;
        font-size: 24px;
        z-index: 9999;
        text-shadow: 0 0 10px rgba(255,255,255,0.8);
    }
    
    /* Click shockwave effect */
    .shockwave {
        position: fixed;
        pointer-events: none;
        width: 30px;
        height: 30px;
        border: 3px solid rgba(255, 255, 255, 0.8);
        border-radius: 50%;
        animation: shockwave 0.8s ease-out;
        z-index: 9998;
    }
    
    /* Falling elements */
    .falling-symbol {
        position: fixed;
        pointer-events: none;
        animation: fall linear;
        font-size: 35px;
        z-index: 1;
        filter: drop-shadow(0 0 8px rgba(255,255,255,0.5));
    }
    
    /* Title styles */
    .big-title {
        font-size: 5em;
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #f9ca24, #ff6b6b);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        margin: 30px 0;
        animation: rainbow 3s linear infinite, pulse 2s ease-in-out infinite;
        text-shadow: 2px 2px 20px rgba(0,0,0,0.3);
        letter-spacing: 3px;
    }
    
    /* Animated celebration */
    .celebration {
        text-align: center;
        font-size: 4em;
        margin: 20px 0;
        animation: bounce 1s ease-in-out infinite;
    }
    
    /* Score box with glow */
    .score-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
        padding: 30px;
        border-radius: 25px;
        color: white;
        text-align: center;
        font-size: 1.8em;
        margin: 30px 0;
        box-shadow: 0 15px 50px rgba(0,0,0,0.4);
        animation: glow 2s ease-in-out infinite;
        border: 3px solid rgba(255,255,255,0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Glassmorphism cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        animation: slideInLeft 0.8s ease-out;
    }
    
    /* Interactive heart */
    .floating-heart {
        position: fixed;
        bottom: 30px;
        right: 30px;
        font-size: 60px;
        cursor: pointer;
        animation: heartbeat 1.5s ease-in-out infinite;
        z-index: 9997;
        filter: drop-shadow(0 0 20px rgba(255,107,107,0.8));
        transition: transform 0.2s;
    }
    
    .floating-heart:hover {
        transform: scale(1.3) rotate(15deg);
    }
    
    /* Distance bridge animation */
    .distance-bridge {
        text-align: center;
        font-size: 2.5em;
        margin: 20px 0;
        animation: slideInRight 1s ease-out;
    }
    
    /* Combo counter */
    .combo-display {
        position: fixed;
        top: 20px;
        right: 20px;
        font-size: 2em;
        background: rgba(255,215,0,0.9);
        padding: 15px 25px;
        border-radius: 15px;
        animation: wiggle 0.5s ease-in-out, pulse 1s ease-in-out infinite;
        z-index: 9996;
        box-shadow: 0 5px 25px rgba(255,215,0,0.5);
        border: 3px solid white;
        font-weight: bold;
    }
    
    /* Progress bar enhancement */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #f9ca24);
        background-size: 200% 100%;
        animation: rainbow 2s linear infinite;
    }
    
    /* Button enhancements */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 1.2em;
        font-weight: 600;
        border-radius: 15px;
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.6);
    }
    
    /* Metric enhancements */
    [data-testid="stMetricValue"] {
        font-size: 2.5em;
        font-weight: 800;
        color: #fff;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }
</style>

<script>
let mouseX = 0, mouseY = 0;
let sparkleTypes = ['✨', '⭐', '💫', '🌟', '💖', '💝', '💗', '🎆'];
let heartClicks = 0;

// Enhanced sparkle cursor trail
document.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    
    if (Math.random() > 0.7) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.innerHTML = sparkleTypes[Math.floor(Math.random() * sparkleTypes.length)];
        sparkle.style.left = (e.pageX - 12) + 'px';
        sparkle.style.top = (e.pageY - 12) + 'px';
        document.body.appendChild(sparkle);
        
        setTimeout(() => sparkle.remove(), 1000);
    }
});

// Click shockwave effect
document.addEventListener('click', function(e) {
    for(let i = 0; i < 3; i++) {
        setTimeout(() => {
            const wave = document.createElement('div');
            wave.className = 'shockwave';
            wave.style.left = (e.pageX - 15) + 'px';
            wave.style.top = (e.pageY - 15) + 'px';
            document.body.appendChild(wave);
            
            setTimeout(() => wave.remove(), 800);
        }, i * 100);
    }
});

// Create falling symbols with variety
function createFallingSymbols() {
    const symbols = [
        '🦁', '🏙️', '🌺', '🌸', '❄️', '⭐', '💎', '🎋', 
        '🏝️', '🌴', '🪼', '🦀', '🐚', '🌊', '💙', '💜',
        '🎮', '🎯', '🎨', '🎭', '🎪', '🎢', '🇮🇳', '🇸🇬',
        '✈️', '💌', '📱', '💻', '🌏', '🗺️', '🧭', '🎂',
        '🎁', '🎈', '🎉', '🎊', '🎆', '🎇', '✨'
    ];
    
    setInterval(() => {
        if (Math.random() > 0.4) {
            const symbol = document.createElement('div');
            symbol.className = 'falling-symbol';
            symbol.innerHTML = symbols[Math.floor(Math.random() * symbols.length)];
            symbol.style.left = Math.random() * 100 + '%';
            symbol.style.animationDuration = (Math.random() * 4 + 3) + 's';
            symbol.style.fontSize = (Math.random() * 20 + 25) + 'px';
            document.body.appendChild(symbol);
            
            setTimeout(() => symbol.remove(), 8000);
        }
    }, 200);
}

// Burst effect for correct answers
function createBurst(x, y) {
    const burstEmojis = ['🎉', '✨', '🌟', '💫', '⭐', '💖'];
    for(let i = 0; i < 12; i++) {
        setTimeout(() => {
            const burst = document.createElement('div');
            burst.className = 'sparkle';
            burst.innerHTML = burstEmojis[Math.floor(Math.random() * burstEmojis.length)];
            burst.style.left = x + 'px';
            burst.style.top = y + 'px';
            burst.style.fontSize = '30px';
            document.body.appendChild(burst);
            
            setTimeout(() => burst.remove(), 1000);
        }, i * 50);
    }
}

setTimeout(createFallingSymbols, 500);
</script>
""", unsafe_allow_html=True)

# Questions with more variety
geography_questions = [
    {
        "question": "🌏 How many kilometers apart are India and Singapore approximately?",
        "options": ["2,800 km", "3,200 km", "4,100 km", "5,000 km"],
        "answer": "4,100 km",
        "fact": "That's about 5 hours by flight - but our hearts are always connected! 💙✈️"
    },
    {
        "question": "🪼 Which phylum do jellyfish belong to?",
        "options": ["Arthropoda", "Cnidaria", "Mollusca", "Echinodermata"],
        "answer": "Cnidaria",
        "fact": "Jellyfish have been around for over 500 million years - just like our love will last forever! 🪼💕"
    },
    {
        "question": "🦀 How many legs do most arthropods have?",
        "options": ["4 legs", "6 legs", "8 legs", "Varies by species"],
        "answer": "Varies by species",
        "fact": "Insects: 6, Spiders: 8, Crabs: 10! Each one is unique, just like you! 🦀"
    },
    {
        "question": "🇸🇬 What year did Singapore gain independence?",
        "options": ["1959", "1963", "1965", "1971"],
        "answer": "1965",
        "fact": "August 9, 1965 - The start of an amazing nation where my love lives! 🦁🇸🇬"
    },
    {
        "question": "🌊 What percentage of Earth is covered by oceans?",
        "options": ["50%", "61%", "71%", "81%"],
        "answer": "71%",
        "fact": "Even oceans can't separate us! We're connected across the waters! 🌊💙"
    },
    {
        "question": "🦑 Which is the largest arthropod in the world?",
        "options": ["Japanese Spider Crab", "Goliath Beetle", "Giant Centipede", "Coconut Crab"],
        "answer": "Japanese Spider Crab",
        "fact": "Leg span up to 3.7 meters! But nothing spans as far as my love for you! 🦀💕"
    },
    {
        "question": "🇮🇳 Which ocean connects India and Singapore?",
        "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
        "answer": "Indian Ocean",
        "fact": "The Indian Ocean connects our countries - just like our love connects our hearts! 🌊💙"
    },
    {
        "question": "🪸 Do jellyfish have brains?",
        "options": ["Yes, tiny brains", "No, but have nerve nets", "Yes, complex brains", "Only some species"],
        "answer": "No, but have nerve nets",
        "fact": "No brains needed - they just float and vibe, like us on lazy Sundays! 🪼😄"
    },
    {
        "question": "🎮 Which arthropod group includes scorpions?",
        "options": ["Insects", "Arachnids", "Crustaceans", "Myriapods"],
        "answer": "Arachnids",
        "fact": "Scorpions are arachnids with 8 legs - perfect for hugging you when we meet! 🦂💕"
    },
    {
        "question": "💙 Time zone difference: India to Singapore?",
        "options": ["1.5 hours", "2.5 hours", "3.5 hours", "4.5 hours"],
        "answer": "2.5 hours",
        "fact": "2.5 hours apart in time, but 0 hours apart in my heart! 💙⏰"
    }
]

# Intro Stage - Enhanced
if st.session_state.game_stage == 'intro':
    st.markdown('<div class="big-title">🎮 EPIC BIRTHDAY ADVENTURE 🎂</div>', unsafe_allow_html=True)
    st.markdown('<div class="celebration">🎉 🎊 🎁 🎈 🎆 🎇 ✨</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="distance-bridge">🇮🇳 ✈️ 💙 ✈️ 🇸🇬</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div class="glass-card">
        <h2 style='text-align: center; color: white; text-shadow: 2px 2px 10px rgba(0,0,0,0.5);'>
        💙 Happy 2nd Anniversary & Birthday! 💙
        </h2>
        
        <p style='font-size: 1.2em; color: white; text-shadow: 1px 1px 5px rgba(0,0,0,0.5);'>
        <strong>To My Amazing Boyfriend,</strong><br><br>
        
        From India 🇮🇳 to Singapore 🇸🇬...<br>
        Across 4,100 kilometers...<br>
        Through different time zones...<br>
        <strong>But ZERO distance in our hearts! 💙</strong><br><br>
        
        <strong>Today we celebrate YOU!</strong> 🌟<br><br>
        
        Get ready for an EPIC quest featuring:<br>
        🗺️ <strong>Geography</strong> (our connection across the globe)<br>
        🦀 <strong>Arthropoda</strong> (your favorite reading!)<br>
        🪼 <strong>Jellyfish</strong> (those beautiful creatures you love)<br>
        🎮 <strong>Gaming fun</strong> (our favorite pastime together!)<br>
        💙 <strong>Long-distance love</strong> (stronger than ever!)<br><br>
        
        <em>Mission: Collect jellyfish 🪼, answer questions, unlock your surprise!</em><br><br>
        
        <strong>✨ Move your mouse for magic sparkles!</strong><br>
        <strong>💖 Click anywhere for shockwave effects!</strong><br>
        <strong>🎯 Watch the falling symbols rain down!</strong>
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("")
        st.markdown('<div style="text-align: center; font-size: 3em;" class="floating">🎮 🪼 🦀 💙</div>', unsafe_allow_html=True)
        st.markdown("")
        
        if st.button("🚀 START THE BIRTHDAY QUEST!", use_container_width=True, type="primary"):
            st.session_state.game_stage = 'game'
            st.balloons()
            st.rerun()

# Game Stage - Enhanced
elif st.session_state.game_stage == 'game':
    # Combo display
    if st.session_state.combo > 0:
        st.markdown(f'<div class="combo-display">🔥 COMBO x{st.session_state.combo}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="big-title">🪼 OCEAN KNOWLEDGE QUEST 🌊</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; font-size: 1.5em; color: white; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); margin-bottom: 20px;">🇮🇳 💙 India ↔ Singapore 💙 🇸🇬</div>', unsafe_allow_html=True)
    
    # Enhanced score display
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎯 Score", f"{st.session_state.score} pts")
    with col2:
        st.metric("❓ Progress", f"{st.session_state.questions_answered}/10")
    with col3:
        st.metric("🪼 Jellyfish", st.session_state.jellyfish_collected)
    with col4:
        st.metric("💙 Love Level", f"{min(st.session_state.love_level, 100)}%")
    
    st.markdown("---")
    
    if st.session_state.questions_answered >= 10:
        st.session_state.game_stage = 'finale'
        st.rerun()
    
    current_q = geography_questions[st.session_state.questions_answered]
    
    st.markdown(f"""
    <div class="glass-card">
    <h3 style='color: white; text-shadow: 2px 2px 8px rgba(0,0,0,0.5);'>
    Question {st.session_state.questions_answered + 1} of 10:
    </h3>
    <h2 style='color: white; font-size: 2em; text-shadow: 2px 2px 8px rgba(0,0,0,0.5);'>
    {current_q['question']}
    </h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    cols = st.columns(2)
    for idx, option in enumerate(current_q['options']):
        with cols[idx % 2]:
            if st.button(f"🎮 {option}", key=f"opt_{idx}", use_container_width=True):
                if option == current_q['answer']:
                    st.success(f"🎉 PERFECT! {current_q['fact']}")
                    points = 100 + (st.session_state.combo * 25)
                    st.session_state.score += points
                    st.session_state.jellyfish_collected += 1
                    st.session_state.combo += 1
                    st.session_state.love_level += 10
                    st.balloons()
                    st.markdown(f'<div style="text-align: center; font-size: 3em;">🎊 +{points} pts! ✨</div>', unsafe_allow_html=True)
                else:
                    st.error(f"💔 Almost! The answer is: **{current_q['answer']}**")
                    st.info(current_q['fact'])
                    st.session_state.score += 25
                    st.session_state.combo = 0
                    st.session_state.love_level += 5
                
                st.session_state.questions_answered += 1
                time.sleep(3)
                st.rerun()
    
    # Visual progress
    st.markdown("---")
    progress = st.session_state.questions_answered / 10
    st.progress(progress)
    
    jellyfish_display = "🪼 " * (st.session_state.jellyfish_collected + 1)
    st.markdown(f'<div style="text-align: center; font-size: 2.5em;" class="floating">{jellyfish_display}</div>', unsafe_allow_html=True)
    
    symbols = "🇮🇳 ✈️ 💙 🌊 🦀 🪼 ✈️ 🇸🇬"
    st.markdown(f'<div style="text-align: center; font-size: 1.8em; opacity: 0.8;">{symbols}</div>', unsafe_allow_html=True)

# Finale Stage - MEGA Enhanced
elif st.session_state.game_stage == 'finale':
    # Triple celebration effects
    st.balloons()
    time.sleep(0.3)
    st.snow()
    time.sleep(0.3)
    st.balloons()
    
    st.markdown('<div class="big-title">🎂 HAPPY BIRTHDAY MY LOVE! 🎉</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="celebration">🎊 🎁 🎈 🎆 🎇 ✨ 💙 🪼 🦁 🌸</div>', unsafe_allow_html=True)
    
    # Calculate achievements
    perfect_score = st.session_state.score >= 1000
    jellyfish_master = st.session_state.jellyfish_collected >= 8
    combo_king = st.session_state.combo >= 5
    
    st.markdown(f"""
    <div class="score-box">
        🏆 FINAL SCORE: {st.session_state.score} POINTS! 🏆<br>
        🪼 Jellyfish Collected: {st.session_state.jellyfish_collected}/10 🪼<br>
        🔥 Max Combo: {st.session_state.combo}x 🔥<br>
        💙 Love Level: {min(st.session_state.love_level, 100)}% (MAX!) 💙<br><br>
        {'⭐ PERFECT SCORE ACHIEVED! ⭐<br>' if perfect_score else ''}
        {'🪼 JELLYFISH MASTER! 🪼<br>' if jellyfish_master else ''}
        {'🔥 COMBO KING! 🔥<br>' if combo_king else ''}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div class="glass-card" style="animation: slideInLeft 1s ease-out;">
        <h2 style='text-align: center; color: white; text-shadow: 2px 2px 10px rgba(0,0,0,0.5);'>
        💝 A Love Letter Across the Ocean 💝
        </h2>
        
        <p style='font-size: 1.3em; color: white; text-shadow: 1px 1px 5px rgba(0,0,0,0.5); line-height: 1.8;'>
        <strong>My Dearest Love,</strong><br><br>
        
        🌏 <strong>4,100 kilometers.</strong> That's the distance between India and Singapore.<br>
        ⏰ <strong>2.5 hours.</strong> That's our time zone difference.<br>
        📱 <strong>Countless video calls.</strong> That's how we see each other's smiles.<br>
        💙 <strong>ZERO distance in our hearts.</strong> That's what truly matters.<br><br>
        
        For <strong>2 YEARS</strong>, you've been my:<br>
        🎮 <strong>Gaming partner</strong> - conquering worlds together<br>
        🗺️ <strong>Geography buddy</strong> - exploring the world's wonders<br>
        🦀 <strong>Arthropoda enthusiast</strong> - sharing fascinating facts<br>
        🪼 <strong>Jellyfish appreciator</strong> - marveling at ocean beauty<br>
        📚 <strong>Fellow learner</strong> - growing together every day<br>
        💙 <strong>Best friend</strong> - understanding me like no one else<br>
        ✨ <strong>Soulmate</strong> - completing my world<br><br>
        
        Every day you inspire me with your:<br>
        🌟 Curiosity about the world<br>
        💪 Strength in pursuing your dreams<br>
        😄 Ability to make me laugh across screens<br>
        💖 Unconditional love that knows no borders<br><br>
        
        <strong>Long distance?</strong> More like <strong>STRONG distance!</strong> 💪💙<br>
        Every kilometer between us makes our love stronger.<br>
        Every time zone makes our "good morning" more special.<br>
        Every video call makes my heart skip a beat.<br><br>
        
        From Thiruvananthapuram 🇮