import streamlit as st
import random
import time
from datetime import datetime

# Page config
st.set_page_config(page_title="🎂 Happy Birthday Adventure!", page_icon="🎮", layout="wide")

# Initialize session state
if 'game_stage' not in st.session_state:
    st.session_state.game_stage = 'intro'
    st.session_state.score = 0
    st.session_state.questions_answered = 0
    st.session_state.jellyfish_collected = 0

# Custom CSS for animations, sparkles, and Singapore symbols
st.markdown("""
<style>
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes fall {
        0% { transform: translateY(-100px) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0.8; }
    }
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    .pulsing {
        animation: pulse 2s ease-in-out infinite;
    }
    .rainbow {
        animation: rainbow 3s linear infinite;
    }
    .spinning {
        animation: spin 4s linear infinite;
    }
    
    .big-title {
        font-size: 4em;
        text-align: center;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #f9ca24);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin: 20px 0;
    }
    .celebration {
        text-align: center;
        font-size: 3em;
        margin: 20px 0;
    }
    .score-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 1.5em;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Sparkle cursor trail */
    .sparkle {
        position: fixed;
        pointer-events: none;
        animation: sparkle 0.8s ease-out;
        font-size: 20px;
        z-index: 9999;
    }
    
    /* Falling Singapore symbols */
    .falling-symbol {
        position: fixed;
        pointer-events: none;
        animation: fall linear;
        font-size: 30px;
        z-index: 1;
    }
    
    /* Background particles */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
    }
</style>

<script>
// Sparkle cursor trail
document.addEventListener('mousemove', function(e) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    sparkle.innerHTML = ['✨', '⭐', '💫', '🌟'][Math.floor(Math.random() * 4)];
    sparkle.style.left = e.pageX + 'px';
    sparkle.style.top = e.pageY + 'px';
    document.body.appendChild(sparkle);
    
    setTimeout(() => sparkle.remove(), 800);
});

// Create falling Singapore symbols and snowflakes
function createFallingSymbols() {
    const symbols = ['🦁', '🏙️', '🌺', '🌸', '❄️', '⭐', '💎', '🎋', '🏝️', '🌴'];
    
    setInterval(() => {
        const symbol = document.createElement('div');
        symbol.className = 'falling-symbol';
        symbol.innerHTML = symbols[Math.floor(Math.random() * symbols.length)];
        symbol.style.left = Math.random() * 100 + '%';
        symbol.style.animationDuration = (Math.random() * 3 + 4) + 's';
        document.body.appendChild(symbol);
        
        setTimeout(() => symbol.remove(), 7000);
    }, 300);
}

// Start falling symbols after a short delay
setTimeout(createFallingSymbols, 500);
</script>
""", unsafe_allow_html=True)

# Geography & Arthropoda Questions
geography_questions = [
    {
        "question": "Which strait connects Malaysia and Singapore?",
        "options": ["Strait of Malacca", "Johor Strait", "Singapore Strait", "Sunda Strait"],
        "answer": "Johor Strait",
        "fact": "The Johor Strait is only about 1km wide at its narrowest point! 🌊"
    },
    {
        "question": "Which phylum do jellyfish belong to?",
        "options": ["Arthropoda", "Cnidaria", "Mollusca", "Echinodermata"],
        "answer": "Cnidaria",
        "fact": "Jellyfish have been around for over 500 million years - older than dinosaurs! 🪼"
    },
    {
        "question": "How many body segments do arthropods typically have?",
        "options": ["2", "3", "4", "Varies by species"],
        "answer": "Varies by species",
        "fact": "Insects have 3 segments, arachnids have 2, and crustaceans can have many! 🦀"
    },
    {
        "question": "What percentage of Earth's surface is covered by oceans?",
        "options": ["50%", "61%", "71%", "81%"],
        "answer": "71%",
        "fact": "We've only explored about 5% of the ocean - so much mystery awaits! 🌊"
    },
    {
        "question": "Which is the largest arthropod?",
        "options": ["Japanese Spider Crab", "Goliath Beetle", "Giant Centipede", "Coconut Crab"],
        "answer": "Japanese Spider Crab",
        "fact": "Its leg span can reach up to 3.7 meters (12 feet)! 🦀"
    },
    {
        "question": "Singapore lies approximately how many degrees north of the equator?",
        "options": ["0.5°", "1.3°", "3.1°", "5.2°"],
        "answer": "1.3°",
        "fact": "This makes it one of the closest countries to the equator! 🇸🇬"
    },
    {
        "question": "What is Singapore's national flower?",
        "options": ["Orchid (Vanda Miss Joaquim)", "Hibiscus", "Jasmine", "Rose"],
        "answer": "Orchid (Vanda Miss Joaquim)",
        "fact": "It's a hybrid orchid that blooms all year round, symbolizing Singapore's resilience! 🌺"
    },
    {
        "question": "Which ocean creature has blue blood?",
        "options": ["Sharks", "Horseshoe Crabs", "Dolphins", "Jellyfish"],
        "answer": "Horseshoe Crabs",
        "fact": "Their blood contains copper instead of iron, making it blue! And they're arthropods! 🦀💙"
    }
]

# Intro Stage
if st.session_state.game_stage == 'intro':
    st.markdown('<div class="big-title floating">🎮 EPIC BIRTHDAY QUEST 2024 🎂</div>', unsafe_allow_html=True)
    st.markdown('<div class="celebration pulsing">🎉 🎊 🎁 🎈 🎆 🎇 ✨ 🦁 🏙️ ❄️</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### 💙 Happy 2nd Anniversary & Birthday! 💙
        
        **Dear Amazing Boyfriend,**
        
        From Malaysia 🇲🇾 to Singapore 🇸🇬, across 2 years of adventures...
        Today we celebrate YOU! 🌟
        
        Get ready for an EPIC birthday quest combining:
        - 🗺️ **Geography challenges**
        - 🦀 **Arthropoda trivia**  
        - 🪼 **Jellyfish facts**
        - 🎮 **Gaming fun!**
        - 🦁 **Singapore magic!**
        
        **Your mission:** Collect jellyfish, answer questions, and unlock your birthday surprise!
        
        *(Move your mouse around for sparkles! ✨)*
        """)
        
        st.markdown("---")
        
        # Fun animated button area
        st.markdown('<div style="text-align: center; font-size: 2.5em;" class="spinning">🎮</div>', unsafe_allow_html=True)
        
        if st.button("🚀 START THE ADVENTURE!", use_container_width=True, type="primary"):
            st.session_state.game_stage = 'game'
            st.rerun()
        
        st.markdown('<div style="text-align: center; margin-top: 20px;">🪼 🦁 🌸 ❄️ ⭐ 💎 🌴</div>', unsafe_allow_html=True)

# Game Stage
elif st.session_state.game_stage == 'game':
    # Header with animations
    st.markdown('<div class="big-title pulsing">🪼 Ocean Knowledge Quest 🌊</div>', unsafe_allow_html=True)
    
    # Score display with fun animations
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 Score", st.session_state.score)
    with col2:
        st.metric("❓ Questions", f"{st.session_state.questions_answered}/8")
    with col3:
        st.metric("🪼 Jellyfish", st.session_state.jellyfish_collected)
    
    st.markdown("---")
    
    # Check if all questions answered
    if st.session_state.questions_answered >= 8:
        st.session_state.game_stage = 'finale'
        st.rerun()
    
    # Display current question
    current_q = geography_questions[st.session_state.questions_answered]
    
    # Fun question display with emojis
    st.markdown(f"### 🎯 Question {st.session_state.questions_answered + 1}:")
    st.markdown(f"## {current_q['question']}")
    
    st.markdown("")
    
    # Answer options with fun styling
    cols = st.columns(2)
    for idx, option in enumerate(current_q['options']):
        with cols[idx % 2]:
            if st.button(f"🎮 {option}", key=f"opt_{idx}", use_container_width=True):
                if option == current_q['answer']:
                    st.success(f"🎉 CORRECT! {current_q['fact']}")
                    st.session_state.score += 100
                    st.session_state.jellyfish_collected += 1
                    st.balloons()
                    st.markdown('<div style="text-align: center; font-size: 4em;">🎊 ✨ 🌟 💫</div>', unsafe_allow_html=True)
                else:
                    st.error(f"❌ Oops! The answer is: {current_q['answer']}")
                    st.info(current_q['fact'])
                    st.session_state.score += 25
                
                st.session_state.questions_answered += 1
                time.sleep(2.5)
                st.rerun()
    
    # Jellyfish animation area with Singapore symbols
    st.markdown("---")
    jellyfish_display = "🪼 " * (st.session_state.jellyfish_collected + 1)
    singapore_symbols = "🦁 🏙️ 🌺 🌸 🎋 "
    st.markdown(f'<div style="text-align: center; font-size: 3em;" class="floating">{jellyfish_display}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align: center; font-size: 2em; opacity: 0.7;">{singapore_symbols}</div>', unsafe_allow_html=True)
    
    # Progress indicator
    progress = st.session_state.questions_answered / 8
    st.progress(progress)

# Finale Stage
elif st.session_state.game_stage == 'finale':
    # Multiple balloon effects
    st.balloons()
    time.sleep(0.5)
    st.snow()
    
    st.markdown('<div class="big-title rainbow">🎂 HAPPY BIRTHDAY! 🎉</div>', unsafe_allow_html=True)
    
    # Celebration banner
    st.markdown('<div style="text-align: center; font-size: 3em;" class="pulsing">🎊 🎁 🎈 🎆 🎇 ✨ 🦁 🏙️ 🌸 ❄️</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="score-box pulsing">
        🏆 FINAL SCORE: {st.session_state.score} points! 🏆
        <br>
        🪼 Jellyfish Collected: {st.session_state.jellyfish_collected} 🪼
        <br>
        ⭐ Achievement Unlocked: BIRTHDAY CHAMPION! ⭐
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### 💝 A Special Message 💝
        
        **To my incredible boyfriend,**
        
        🌏 From the moment we met, you've made every day an adventure.
        
        📚 Your curiosity about everything - from geography to arthropods to jellyfish - inspires me every single day. Watching you learn and grow is one of my favorite things.
        
        🎮 Whether we're gaming together, exploring new places, or just being silly, you make everything more fun and meaningful.
        
        🇲🇾 ➡️ 🇸🇬 From Malaysia to Singapore, distance means nothing when hearts are this close.
        
        **2 YEARS together** and it feels like we're just getting started! Every day with you is a new level unlocked. 🎮✨
        
        You're my:
        - 🦁 Lion City love
        - 🪼 Jellyfish expert  
        - 🦀 Arthropoda enthusiast
        - 🎮 Gaming partner
        - 💙 Best friend and soulmate
        
        Here's to many more birthdays, adventures, geography facts, and jellyfish discoveries together! 🪼✨
        
        **I love you SO MUCH! Happy Birthday, Sayang! 💙🎂**
        
        ---
        
        *P.S. - Your real birthday gift is waiting for you... but I hope this made you smile! 🎁*
        
        *P.P.S. - Keep moving your mouse for sparkles! ✨*
        
        🎮 Game Over? NEVER! Our adventure continues FOREVER! 🎮
        """)
        
        # Final celebration
        st.markdown('<div style="text-align: center; font-size: 5em;" class="rainbow floating">💙</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; font-size: 3em;">🎂🎉🎈🎁🪼🦁🎮✨🌸❄️🌟💫</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🔄 Play Again!", use_container_width=True, type="primary"):
                st.session_state.game_stage = 'intro'
                st.session_state.score = 0
                st.session_state.questions_answered = 0
                st.session_state.jellyfish_collected = 0
                st.rerun()
        
        with col_b:
            if st.button("🎊 More Celebration!", use_container_width=True):
                st.balloons()
                st.snow()
                st.toast("🎉 HAPPY BIRTHDAY! 🎂", icon="🎈")

# Footer with Singapore symbols
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 20px;'>
    💝 Made with love on December 16, 2025 💝<br>
    🎮 Celebrating 2 years of love & adventure 🎮<br>
    🇲🇾 Malaysia 💙 Singapore 🇸🇬<br>
    🦁 🏙️ 🌺 🌸 🪼 🦀 ❄️ ✨
</div>
""", unsafe_allow_html=True)