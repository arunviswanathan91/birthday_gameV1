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

# Custom CSS for animations and styling
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
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    .pulsing {
        animation: pulse 2s ease-in-out infinite;
    }
    .rainbow {
        animation: rainbow 3s linear infinite;
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
    }
</style>
""", unsafe_allow_html=True)

# Geography & Arthropoda Questions
geography_questions = [
    {
        "question": "Which strait connects Malaysia and Singapore?",
        "options": ["Strait of Malacca", "Johor Strait", "Singapore Strait", "Sunda Strait"],
        "answer": "Johor Strait",
        "fact": "The Johor Strait is only about 1km wide at its narrowest point!"
    },
    {
        "question": "Which phylum do jellyfish belong to?",
        "options": ["Arthropoda", "Cnidaria", "Mollusca", "Echinodermata"],
        "answer": "Cnidaria",
        "fact": "Jellyfish have been around for over 500 million years - older than dinosaurs!"
    },
    {
        "question": "How many body segments do arthropods typically have?",
        "options": ["2", "3", "4", "Varies by species"],
        "answer": "Varies by species",
        "fact": "Insects have 3 segments, arachnids have 2, and crustaceans can have many!"
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
        "fact": "Its leg span can reach up to 3.7 meters (12 feet)!"
    },
    {
        "question": "Singapore lies approximately how many degrees north of the equator?",
        "options": ["0.5°", "1.3°", "3.1°", "5.2°"],
        "answer": "1.3°",
        "fact": "This makes it one of the closest countries to the equator!"
    }
]

# Intro Stage
if st.session_state.game_stage == 'intro':
    st.markdown('<div class="big-title floating">🎮 BIRTHDAY QUEST 2024 🎂</div>', unsafe_allow_html=True)
    st.markdown('<div class="celebration">🎉 🎊 🎁 🎈 🎆 🎇 ✨</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### 💙 Happy 2nd Anniversary & Birthday! 💙
        
        **Dear Amazing Boyfriend,**
        
        From Malaysia to Singapore, across 2 years of adventures...
        Today we celebrate YOU! 🌟
        
        Get ready for an epic birthday quest combining:
        - 🗺️ Geography challenges
        - 🦀 Arthropoda trivia  
        - 🪼 Jellyfish facts
        - 🎮 Gaming fun!
        
        **Your mission:** Collect jellyfish and answer questions to unlock your birthday surprise!
        """)
        
        st.markdown("---")
        
        if st.button("🚀 START THE ADVENTURE!", use_container_width=True):
            st.session_state.game_stage = 'game'
            st.rerun()

# Game Stage
elif st.session_state.game_stage == 'game':
    # Header
    st.markdown('<div class="big-title pulsing">🪼 Ocean Knowledge Quest 🌊</div>', unsafe_allow_html=True)
    
    # Score display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 Score", st.session_state.score)
    with col2:
        st.metric("❓ Questions", f"{st.session_state.questions_answered}/6")
    with col3:
        st.metric("🪼 Jellyfish", st.session_state.jellyfish_collected)
    
    st.markdown("---")
    
    # Check if all questions answered
    if st.session_state.questions_answered >= 6:
        st.session_state.game_stage = 'finale'
        st.rerun()
    
    # Display current question
    current_q = geography_questions[st.session_state.questions_answered]
    
    st.markdown(f"### Question {st.session_state.questions_answered + 1}:")
    st.markdown(f"## {current_q['question']}")
    
    st.markdown("")
    
    # Answer options
    cols = st.columns(2)
    for idx, option in enumerate(current_q['options']):
        with cols[idx % 2]:
            if st.button(option, key=f"opt_{idx}", use_container_width=True):
                if option == current_q['answer']:
                    st.success(f"🎉 Correct! {current_q['fact']}")
                    st.session_state.score += 100
                    st.session_state.jellyfish_collected += 1
                    st.balloons()
                else:
                    st.error(f"❌ Not quite! The answer is: {current_q['answer']}")
                    st.info(current_q['fact'])
                    st.session_state.score += 25
                
                st.session_state.questions_answered += 1
                time.sleep(2)
                st.rerun()
    
    # Jellyfish animation area
    st.markdown("---")
    jellyfish_display = "🪼 " * (st.session_state.jellyfish_collected + 1)
    st.markdown(f'<div style="text-align: center; font-size: 3em;" class="floating">{jellyfish_display}</div>', unsafe_allow_html=True)

# Finale Stage
elif st.session_state.game_stage == 'finale':
    st.balloons()
    
    st.markdown('<div class="big-title rainbow">🎂 HAPPY BIRTHDAY! 🎉</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="score-box pulsing">
        🏆 FINAL SCORE: {st.session_state.score} points! 🏆
        <br>
        🪼 Jellyfish Collected: {st.session_state.jellyfish_collected} 🪼
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### 💝 A Special Message 💝
        
        **To my incredible boyfriend,**
        
        🌏 From the moment we met, you've made every day an adventure.
        
        📚 Your love for learning (geography, arthropods, jellyfish!) inspires me every single day.
        
        🎮 Whether we're gaming together or exploring new places, you make everything more fun.
        
        🇲🇾 ➡️ 🇸🇬 Malaysia to Singapore, our love knows no borders.
        
        **2 years together** and it feels like we're just getting started! 
        
        Here's to many more birthdays, adventures, and jellyfish facts together! 🪼✨
        
        **I love you so much! Happy Birthday, Sayang! 💙**
        
        ---
        
        *P.S. - Your birthday gift is waiting for you... but first, enjoy this moment! 🎁*
        
        🎮 Game Over? Never! Our adventure continues! 🎮
        """)
        
        st.markdown('<div style="text-align: center; font-size: 4em;">💙🎂🎉🎈🎁🪼🎮✨</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        if st.button("🔄 Play Again!", use_container_width=True):
            st.session_state.game_stage = 'intro'
            st.session_state.score = 0
            st.session_state.questions_answered = 0
            st.session_state.jellyfish_collected = 0
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 20px;'>
    💝 Made with love on December 16, 2025 💝<br>
    🎮 Celebrating 2 years of love & adventure 🎮
</div>
""", unsafe_allow_html=True)