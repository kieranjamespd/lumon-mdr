import streamlit as st
import streamlit.components.v1 as components
import random
from datetime import datetime
import time

# Configure the page
st.set_page_config(
    page_title="Lumon MDR",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding-top: 0; padding-bottom: 0;}
    </style>
""", unsafe_allow_html=True)

def create_login_screen():
    login_html = """
    <div class="login-screen">
        <div class="terminal">
            <div class="terminal-header">
                <span class="terminal-title">LUMON MDR TERMINAL</span>
                <span class="terminal-time"></span>
            </div>
            <div class="terminal-content">
                <div class="login-prompt">LOGIN REQUIRED</div>
                <div class="login-form">
                    <div class="input-line">
                        <span class="prompt">EMPLOYEE ID:</span>
                        <input type="text" id="employee-id" class="terminal-input" placeholder="MDR-XXXX" maxlength="7">
                    </div>
                    <div class="input-line">
                        <span class="prompt">PASSWORD:</span>
                        <input type="password" id="password" class="terminal-input" placeholder="********">
                    </div>
                    <div class="login-status"></div>
                </div>
            </div>
        </div>
    </div>

    <style>
        .login-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #001214;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 10000;
        }

        .terminal {
            width: 80%;
            max-width: 800px;
            background-color: #001214;
            border: 1px solid #39FFE1;
            padding: 20px;
            font-family: "Courier New", monospace;
            color: #39FFE1;
            box-shadow: 0 0 20px rgba(57, 255, 225, 0.2);
        }

        .terminal-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #39FFE1;
        }

        .terminal-title {
            font-size: 18px;
            font-weight: bold;
        }

        .terminal-time {
            opacity: 0.7;
        }

        .terminal-content {
            font-size: 16px;
            line-height: 1.5;
        }

        .login-prompt {
            font-size: 20px;
            margin-bottom: 20px;
            text-align: center;
            animation: blink 1s infinite;
        }

        .login-form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .input-line {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .prompt {
            min-width: 120px;
        }

        .terminal-input {
            background: transparent;
            border: none;
            border-bottom: 1px solid #39FFE1;
            color: #39FFE1;
            font-family: "Courier New", monospace;
            font-size: 16px;
            padding: 5px;
            outline: none;
            width: 200px;
        }

        .terminal-input::placeholder {
            color: rgba(57, 255, 225, 0.3);
        }

        .login-status {
            margin-top: 10px;
            min-height: 20px;
            color: #FF3939;
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .login-screen.fade-out {
            animation: fadeOut 1s forwards;
        }
    </style>

    <script>
        function updateTime() {
            const now = new Date();
            const timeString = now.toLocaleTimeString();
            document.querySelector('.terminal-time').textContent = timeString;
        }
        
        updateTime();
        setInterval(updateTime, 1000);

        // Handle login
        const employeeIdInput = document.getElementById('employee-id');
        const passwordInput = document.getElementById('password');
        const loginStatus = document.querySelector('.login-status');
        const loginScreen = document.querySelector('.login-screen');

        function handleLogin() {
            const employeeId = employeeIdInput.value.trim();
            const password = passwordInput.value;

            if (employeeId && password) {
                loginStatus.textContent = 'AUTHENTICATING...';
                loginStatus.style.color = '#39FFE1';
                
                // Simulate authentication delay - reduced from 1500ms to 1000ms
                setTimeout(() => {
                    loginScreen.classList.add('fade-out');
                    
                    // Trigger loading screen after login fades out - reduced from 1000ms to 500ms
                    setTimeout(() => {
                        const loadingScreen = document.querySelector('.loading-screen');
                        loadingScreen.style.display = 'flex';
                        loadingScreen.style.zIndex = '10000';
                        
                        // Force a reflow to ensure the transition works
                        void loadingScreen.offsetWidth;
                        
                        loadingScreen.style.opacity = '1';
                        
                        // Update the employee ID in the main interface
                        document.querySelector('.employee-id').textContent = `EMPLOYEE: ${employeeId}`;
                    }, 500);
                }, 1000);
            } else {
                loginStatus.textContent = 'INVALID CREDENTIALS';
                loginStatus.style.color = '#FF3939';
            }
        }

        // Handle Enter key
        passwordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                handleLogin();
            }
        });

        // Auto-focus employee ID input
        employeeIdInput.focus();
    </script>
    """
    return login_html

def create_loading_animation():
    loading_html = """
    <div class="loading-screen" style="display: none; z-index: 10000; opacity: 0;">
        <div class="terminal">
            <div class="terminal-header">
                <span class="terminal-title">LUMON MDR TERMINAL</span>
                <span class="terminal-time"></span>
            </div>
            <div class="terminal-content">
                <div class="line">INITIALIZING MACRODATA REFINEMENT SYSTEM...</div>
                <div class="line">LOADING CORE COMPONENTS...</div>
                <div class="line">ESTABLISHING SECURE CONNECTION...</div>
                <div class="line">CALIBRATING NUMBER GRID...</div>
                <div class="line">INITIALIZING BIN ARRAYS...</div>
                <div class="line">SYSTEM READY.</div>
            </div>
        </div>
    </div>

    <style>
        .loading-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #001214;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 10000;
            opacity: 0;
            transition: opacity 0.5s ease;
        }

        .terminal {
            width: 80%;
            max-width: 800px;
            background-color: #001214;
            border: 1px solid #39FFE1;
            padding: 20px;
            font-family: "Courier New", monospace;
            color: #39FFE1;
            box-shadow: 0 0 20px rgba(57, 255, 225, 0.2);
        }

        .terminal-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 1px solid #39FFE1;
        }

        .terminal-title {
            font-size: 18px;
            font-weight: bold;
        }

        .terminal-time {
            opacity: 0.7;
        }

        .terminal-content {
            font-size: 16px;
            line-height: 1.5;
        }

        .line {
            opacity: 0;
            transform: translateY(10px);
            animation: typeIn 0.5s forwards;
        }

        .line:nth-child(1) { animation-delay: 0.5s; }
        .line:nth-child(2) { animation-delay: 1.0s; }
        .line:nth-child(3) { animation-delay: 1.5s; }
        .line:nth-child(4) { animation-delay: 2.0s; }
        .line:nth-child(5) { animation-delay: 2.5s; }
        .line:nth-child(6) { animation-delay: 3.0s; }

        @keyframes typeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .loading-screen.fade-out {
            animation: fadeOut 1s forwards;
        }

        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; visibility: hidden; }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>

    <script>
        // Ensure loading screen is properly initialized
        document.addEventListener('DOMContentLoaded', function() {
            const loadingScreen = document.querySelector('.loading-screen');
            if (loadingScreen) {
                loadingScreen.style.display = 'none';
                loadingScreen.style.opacity = '0';
            }
        });
        
        function updateTime() {
            const now = new Date();
            const timeString = now.toLocaleTimeString();
            document.querySelector('.terminal-time').textContent = timeString;
        }
        
        updateTime();
        setInterval(updateTime, 1000);

        // Hide loading screen after animation completes
        setTimeout(() => {
            const loadingScreen = document.querySelector('.loading-screen');
            loadingScreen.classList.add('fade-out');
            
            // Ensure the loading screen is completely hidden after fade out
            setTimeout(() => {
                loadingScreen.style.display = 'none';
                
                // Make sure the main interface is visible
                const mainInterface = document.querySelector('.mdr-interface');
                if (mainInterface) {
                    mainInterface.style.opacity = '1';
                }
            }, 1000);
        }, 5500); // Total loading animation time (6 lines × 0.5s delay each + buffer)
    </script>
    """
    return loading_html

def create_mdr_interface():
    # Generate random numbers for the grid
    numbers = [random.randint(0, 9) for _ in range(250)]
    numbers_html = ''.join([f'<div class="number-cell" data-value="{n}">{n}</div>' for n in numbers])
    
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Get the login screen and loading animation HTML
    login_html = create_login_screen()
    loading_html = create_loading_animation()
    
    # Create the HTML content with proper string formatting
    html_content = f"""
    {login_html}
    {loading_html}
    <div class="mdr-interface" style="opacity: 0; animation: fadeIn 1s forwards 6.5s;">
        <div class="file-header">
            <div class="header-left">
                <span class="employee-id">EMPLOYEE: MDR-XXXX</span>
                <span class="current-time">{current_time}</span>
            </div>
            <span class="completion">4% Complete</span>
            <div class="header-right">
                <span class="lumon-logo">LUMON</span>
                <span class="department">MACRODATA REFINEMENT</span>
            </div>
        </div>
        
        <div class="number-grid" id="numberGrid">
            {numbers_html}
        </div>
        
        <div class="bins-container">
            <div class="bin" id="bin-scary">
                <div class="bin-lid"></div>
                <div class="bin-label">01</div>
                <div class="bin-progress">
                    <div class="progress-bar"></div>
                    <div class="progress-text">24%</div>
                </div>
                <div class="bin-hex">0x137056 : 0x00632E</div>
            </div>
            <div class="bin" id="bin-happy">
                <div class="bin-lid"></div>
                <div class="bin-label">02</div>
                <div class="bin-progress">
                    <div class="progress-bar"></div>
                    <div class="progress-text">12%</div>
                </div>
                <div class="bin-hex">0x137056 : 0x00632E</div>
            </div>
            <div class="bin" id="bin-sad">
                <div class="bin-lid"></div>
                <div class="bin-label">03</div>
                <div class="bin-progress">
                    <div class="progress-bar"></div>
                    <div class="progress-text">39%</div>
                </div>
                <div class="bin-hex">0x137056 : 0x00632E</div>
            </div>
            <div class="bin" id="bin-angry">
                <div class="bin-lid"></div>
                <div class="bin-label">04</div>
                <div class="bin-progress">
                    <div class="progress-bar"></div>
                    <div class="progress-text">54%</div>
                </div>
                <div class="bin-hex">0x137056 : 0x00632E</div>
            </div>
            <div class="bin" id="bin-unknown">
                <div class="bin-lid"></div>
                <div class="bin-label">05</div>
                <div class="bin-progress">
                    <div class="progress-bar"></div>
                    <div class="progress-text">0%</div>
                </div>
                <div class="bin-hex">0x137056 : 0x00632E</div>
            </div>
        </div>
        
        <div class="status-bar">
            <span class="status-text">READY</span>
            <span class="status-time">{current_time}</span>
        </div>
    </div>

    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #001214;
            color: #39FFE1;
            font-family: "Courier New", monospace;
            overflow: hidden;
            position: relative;
        }}

        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                linear-gradient(rgba(57, 255, 225, 0.03) 50%, transparent 50%),
                linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            background-size: 100% 2px, 3px 100%;
            pointer-events: none;
            animation: scanline 10s linear infinite;
            z-index: 2147483647;
        }}

        @keyframes scanline {{
            0% {{ background-position: 0 0; }}
            100% {{ background-position: 0 100%; }}
        }}

        .mdr-interface {{
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            padding: 20px;
            box-sizing: border-box;
            background-color: #001214;
            position: relative;
            box-shadow: inset 0 0 150px rgba(57, 255, 225, 0.1);
            filter: blur(0px);
            transition: filter 0.3s ease;
        }}

        .mdr-interface.blurred {{
            filter: blur(10px);
        }}

        .file-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            border: 1px solid #39FFE1;
            margin-bottom: 20px;
            font-size: 24px;
            text-transform: uppercase;
            position: relative;
        }}

        .completion {{
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            font-size: 20px;
            opacity: 0.8;
        }}

        .lumon-logo {{
            margin-left: auto;
            opacity: 0.5;
        }}

        .number-grid {{
            display: grid;
            grid-template-columns: repeat(25, 1fr);
            grid-template-rows: repeat(10, 1fr);
            gap: 8px;
            padding: 20px;
            border-top: 1px solid #39FFE1;
            border-bottom: 1px solid #39FFE1;
            margin-bottom: 20px;
            min-height: 60vh;
            transition: gap 0.3s ease;
        }}

        .number-grid.expanded {{
            gap: 12px;
        }}

        .number-cell {{
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.5rem;
            color: #39FFE1;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            animation: float 4s ease-in-out infinite;
            user-select: none;
            position: relative;
            will-change: transform;
        }}
        
        .number-cell:hover {{
            transform: scale(2.0);
            text-shadow: 0 0 20px #39FFE1;
            z-index: 2;
        }}
        
        .number-cell:active {{
            transform: scale(1.2);
        }}
        
        @keyframes float {{
            0% {{ transform: translate(0, 0) rotate(0deg); }}
            25% {{ transform: translate(2px, 2px) rotate(1deg); }}
            75% {{ transform: translate(-2px, -2px) rotate(-1deg); }}
            100% {{ transform: translate(0, 0) rotate(0deg); }}
        }}
        
        @keyframes vibrate {{
            0% {{ transform: translate(0, 0) rotate(0deg) scale(1); }}
            25% {{ transform: translate(2px, 2px) rotate(2deg) scale(1.1); }}
            75% {{ transform: translate(-2px, -2px) rotate(-2deg) scale(1.1); }}
            100% {{ transform: translate(0, 0) rotate(0deg) scale(1); }}
        }}
        
        .number-cell.active {{
            animation: vibrate 0.8s ease-in-out infinite;
            color: #39FFE1;
        }}

        .number-cell.selected {{
            color: #39FFE1;
            text-shadow: 0 0 30px #39FFE1;
            transform: scale(1.5);
            z-index: 10;
            animation: pulse 0.5s infinite alternate;
        }}

        .number-cell.removed {{
            opacity: 0;
            transform: scale(0);
        }}

        .number-cell.new {{
            animation: fadeIn 0.5s ease-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .number-cell.animating-to-bin {{
            position: fixed;
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
            pointer-events: none;
            z-index: 1000;
            opacity: 1 !important;
        }}

        .bins-container {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 20px;
            padding: 20px;
            margin-top: auto;
            border-top: 2px solid #39FFE1;
            background: rgba(57, 255, 225, 0.05);
            perspective: 800px;
        }}

        .bin {{
            border: 2px solid #39FFE1;
            padding: 15px;
            min-height: 80px;
            display: flex;
            flex-direction: column;
            align-items: stretch;
            transition: all 0.3s ease;
            background: #001214;
            position: relative;
            overflow: visible;
            box-shadow: 0 0 15px rgba(57, 255, 225, 0.1);
            padding-top: 25px;
            transform-style: preserve-3d;
            background-color: rgba(0, 18, 20, 0.8);
            border: 1px solid rgba(57, 255, 225, 0.3);
            border-radius: 2px;
        }}

        .bin:hover {{
            border-color: #39FFE1;
            box-shadow: 0 0 10px rgba(57, 255, 225, 0.3);
        }}

        .bin-lid {{
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            height: 25px;
            background: #001214;
            border: 2px solid #39FFE1;
            border-bottom: none;
            transform-origin: 0% 100%;
            transform: rotateX(0deg) translateZ(1px);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            backface-visibility: hidden;
            transform-style: preserve-3d;
            z-index: 1;
        }}

        .bin.highlight {{
            border-color: #39FFE1;
            box-shadow: 0 0 30px rgba(57, 255, 225, 0.3);
        }}

        .bin.highlight .bin-lid {{
            transform: rotateX(-70deg) translateZ(1px);
            border-color: #39FFE1;
            box-shadow: 0 0 15px rgba(57, 255, 225, 0.3);
        }}

        .bin::after {{
            content: '';
            position: absolute;
            top: 25px;
            left: 0;
            right: 0;
            height: 20px;
            background: linear-gradient(to bottom, rgba(57, 255, 225, 0.2), transparent);
            opacity: 0;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }}

        .bin.highlight::after {{
            opacity: 1;
        }}

        .bin-label {{
            font-size: 12px;
            margin-bottom: 15px;
            opacity: 0.9;
            font-weight: bold;
            text-align: left;
            margin-top: 5px;
            text-transform: uppercase;
            margin-bottom: 5px;
            color: #39FFE1;
            position: relative;
            z-index: 2;
            padding-top: 5px;
        }}

        .bin-progress {{
            position: relative;
            height: 20px;
            background: rgba(57, 255, 225, 0.1);
            margin-bottom: 10px;
        }}

        .progress-bar {{
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            background: #39FFE1;
            opacity: 0.3;
            width: var(--progress, 0%);
        }}

        .progress-text {{
            position: absolute;
            right: 5px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 14px;
            opacity: 0.8;
        }}

        .bin-hex {{
            font-size: 12px;
            opacity: 0.6;
            text-align: center;
            margin-top: 5px;
            font-family: monospace;
        }}

        .selection-box {{
            position: fixed;
            border: 1px solid #39FFE1;
            background: rgba(57, 255, 225, 0.1);
            pointer-events: none;
            z-index: 1000;
            box-shadow: 0 0 15px rgba(57, 255, 225, 0.2);
            backdrop-filter: brightness(1.2);
        }}

        .header-left, .header-right {{
            display: flex;
            align-items: center;
            gap: 20px;
        }}

        .employee-id, .current-time, .department {{
            font-size: 14px;
            opacity: 0.8;
        }}

        .status-bar {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 30px;
            background-color: #001214;
            border-top: 1px solid #39FFE1;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
            font-size: 14px;
        }}
    </style>

    <script>
        const grid = document.querySelector('.number-grid');
        const numbers = document.querySelectorAll('.number-cell');
        const bins = document.querySelectorAll('.bin');
        let isDragging = false;
        let selectedNumbers = new Set();
        const ACTIVATION_RADIUS = 120;
        const INNER_RADIUS = 50;
        const MIDDLE_RADIUS = 85;
        let mouseStartX = 0;
        let mouseStartY = 0;
        let lastMouseX = 0;
        let lastMouseY = 0;
        let animationFrame = null;
        let selectionBox = null;
        let currentHighlightedBin = null;

        function getDistance(x1, y1, x2, y2) {{
            return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        }}

        function selectRandomBin() {{
            const randomBinIndex = Math.floor(Math.random() * bins.length);
            bins.forEach((bin, index) => {{
                if (index === randomBinIndex) {{
                    bin.classList.add('highlight');
                    currentHighlightedBin = bin;
                }} else {{
                    bin.classList.remove('highlight');
                }}
            }});
            return bins[randomBinIndex];
        }}

        function createSelectionBox(x, y) {{
            const box = document.createElement('div');
            box.classList.add('selection-box');
            document.body.appendChild(box);
            return box;
        }}

        function updateSelectionBox(box, startX, startY, currentX, currentY) {{
            const left = Math.min(startX, currentX);
            const top = Math.min(startY, currentY);
            const width = Math.abs(currentX - startX);
            const height = Math.abs(currentY - startY);
            
            box.style.left = left + 'px';
            box.style.top = top + 'px';
            box.style.width = width + 'px';
            box.style.height = height + 'px';

            if (selectedNumbers.size > 0 && !currentHighlightedBin) {{
                selectRandomBin();
            }}
        }}

        function isInSelectionBox(element, box) {{
            const rect = element.getBoundingClientRect();
            const boxRect = box.getBoundingClientRect();
            
            return !(rect.right < boxRect.left || 
                    rect.left > boxRect.right || 
                    rect.bottom < boxRect.top || 
                    rect.top > boxRect.bottom);
        }}

        function replaceNumber(number) {{
            const newValue = Math.floor(Math.random() * 10);
            const newNumber = document.createElement('div');
            newNumber.className = 'number-cell new';
            newNumber.setAttribute('data-value', newValue);
            newNumber.textContent = newValue;
            
            number.classList.add('removed');
            
            setTimeout(() => {{
                number.parentNode.insertBefore(newNumber, number);
                number.remove();
            }}, 600);
        }}

        function updateBinProgress(bin, newNumbers) {{
            const currentProgress = parseInt(bin.querySelector('.progress-text').textContent);
            const progressBar = bin.querySelector('.progress-bar');
            const progressText = bin.querySelector('.progress-text');
            
            const additionalProgress = newNumbers * 0.4;
            const newProgress = Math.min(100, currentProgress + additionalProgress);
            
            progressBar.style.setProperty('--progress', `${{newProgress}}%`);
            progressText.textContent = `${{Math.round(newProgress)}}%`;

            updateTotalCompletion();
        }}

        function updateTotalCompletion() {{
            const totalProgress = Array.from(bins).reduce((sum, bin) => {{
                const progress = parseInt(bin.querySelector('.progress-text').textContent);
                return sum + progress;
            }}, 0) / bins.length;

            document.querySelector('.completion').textContent = 
                `${{Math.round(totalProgress)}}% Complete`;
        }}

        function animateNumberToBin(number, bin, delay = 0) {{
            const numberRect = number.getBoundingClientRect();
            const binRect = bin.getBoundingClientRect();
            const clone = number.cloneNode(true);
            
            clone.style.animation = 'pulse 0.5s infinite alternate';
            clone.style.position = 'fixed';
            clone.style.left = numberRect.left + 'px';
            clone.style.top = numberRect.top + 'px';
            clone.style.width = numberRect.width + 'px';
            clone.style.height = numberRect.height + 'px';
            clone.classList.add('animating-to-bin');
            
            const randomX = (Math.random() - 0.5) * 50;
            const randomRotation = (Math.random() - 0.5) * 720;
            
            clone.style.transition = 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1) ' + delay + 's';
            document.body.appendChild(clone);

            bin.classList.add('highlight');
            
            requestAnimationFrame(() => {{
                clone.style.left = (binRect.left + binRect.width/2 - numberRect.width/2 + randomX) + 'px';
                clone.style.top = (binRect.top + 20) + 'px';
                clone.style.transform = 'scale(0.5) rotate(' + randomRotation + 'deg)';
                clone.style.opacity = '0';
            }});

            setTimeout(() => {{
                clone.remove();
                replaceNumber(number);
                setTimeout(() => {{
                    bin.classList.remove('highlight');
                }}, 100);
            }}, (delay + 0.25) * 1000);
        }}

        function updateNumbersAnimation(mouseX, mouseY) {{
            numbers.forEach(num => {{
                if (num.classList.contains('selected')) return;
                
                const rect = num.getBoundingClientRect();
                const numCenterX = rect.left + rect.width / 2;
                const numCenterY = rect.top + rect.height / 2;
                const distance = getDistance(mouseX, mouseY, numCenterX, numCenterY);
                
                if (distance < ACTIVATION_RADIUS) {{
                    const intensity = Math.pow(1 - (distance / ACTIVATION_RADIUS), 1.5);
                    const blur = 5 + (intensity * 30);
                    
                    if (!num.matches(':hover')) {{
                        num.style.setProperty('--scale', 1);
                        num.style.transform = 'scale(1)';
                    }}
                    num.style.textShadow = '0 0 ' + blur + 'px #39FFE1';
                    num.classList.add('active');
                }} else {{
                    if (!num.classList.contains('selected')) {{
                        if (!num.matches(':hover')) {{
                            num.style.setProperty('--scale', 1);
                            num.style.transform = 'scale(1)';
                        }}
                        num.style.textShadow = '0 0 5px #39FFE1';
                        num.classList.remove('active');
                    }}
                }}
            }});

            const gridRect = grid.getBoundingClientRect();
            const gridCenterX = gridRect.left + gridRect.width / 2;
            const gridCenterY = gridRect.top + gridRect.height / 2;
            const distanceToCenter = getDistance(mouseX, mouseY, gridCenterX, gridCenterY);
            const maxDistance = gridRect.width / 2;
            
            if (distanceToCenter < maxDistance) {{
                const expansionIntensity = Math.pow(1 - (distanceToCenter / maxDistance), 1.5);
                const gapSize = 8 + (expansionIntensity * 12);
                grid.style.gap = `${{gapSize}}px`;
            }} else {{
                grid.style.gap = '8px';
            }}

            lastMouseX = mouseX;
            lastMouseY = mouseY;
            animationFrame = requestAnimationFrame(() => updateNumbersAnimation(mouseX, mouseY));
        }}

        document.addEventListener('mousemove', (e) => {{
            if (animationFrame) {{
                cancelAnimationFrame(animationFrame);
            }}
            updateNumbersAnimation(e.clientX, e.clientY);

            if (isDragging && selectionBox) {{
                updateSelectionBox(selectionBox, mouseStartX, mouseStartY, e.clientX, e.clientY);
                
                numbers.forEach(num => {{
                    if (isInSelectionBox(num, selectionBox)) {{
                        if (!selectedNumbers.has(num)) {{
                            num.classList.add('selected');
                            selectedNumbers.add(num);
                            num.style.transform = 'scale(2.0)';
                        }}
                    }} else {{
                        if (!isDragging) {{
                            num.classList.remove('selected');
                            selectedNumbers.delete(num);
                            num.style.transform = 'scale(1)';
                        }}
                    }}
                }});
            }}
        }});

        document.addEventListener('mousedown', (e) => {{
            mouseStartX = e.clientX;
            mouseStartY = e.clientY;
            isDragging = true;
            selectedNumbers.clear();
            currentHighlightedBin = null;
            bins.forEach(bin => bin.classList.remove('highlight'));
            selectionBox = createSelectionBox(e.clientX, e.clientY);
        }});

        document.addEventListener('mouseup', (e) => {{
            if (isDragging) {{
                isDragging = false;
                
                if (selectionBox) {{
                    selectionBox.remove();
                    selectionBox = null;
                }}

                if (selectedNumbers.size > 0 && currentHighlightedBin) {{
                    currentHighlightedBin.classList.add('highlight');
                    
                    let delay = 0;
                    const numSelected = selectedNumbers.size;
                    selectedNumbers.forEach(num => {{
                        animateNumberToBin(num, currentHighlightedBin, delay);
                        delay += 0.05;
                    }});

                    updateBinProgress(currentHighlightedBin, numSelected);
                }}
                
                selectedNumbers.clear();
                currentHighlightedBin = null;
            }}
        }});

        updateNumbersAnimation(0, 0);

        document.querySelectorAll('.bin').forEach((bin, index) => {{
            const progressValues = [24, 12, 39, 54, 0];
            const progressBar = bin.querySelector('.progress-bar');
            progressBar.style.setProperty('--progress', `${{progressValues[index]}}%`);
        }});

        function applyRandomMovement(number) {{
            const randomX = (Math.random() - 0.5) * 4;
            const randomY = (Math.random() - 0.5) * 4;
            const randomRotate = (Math.random() - 0.5) * 2;
            number.style.transform = "translate(" + randomX + "px, " + randomY + "px) rotate(" + randomRotate + "deg)";
        }}
        
        setInterval(() => {{
            numbers.forEach(num => {{
                if (Math.random() < 0.1) {{
                    applyRandomMovement(num);
                }}
            }});
        }}, 2000);
        
        setInterval(() => {{
            numbers.forEach(num => {{
                if (!num.classList.contains('active')) {{
                    num.style.transform = '';
                }}
            }});
        }}, 3000);
        
        setInterval(() => {{
            numbers.forEach(num => {{
                if (Math.random() < 0.1) {{
                    num.classList.toggle('active');
                }}
            }});
        }}, 2000);
    </script>
    """
    
    # Render the interface
    components.html(html_content, height=800)

def main():
    # Set up the base styles
    st.markdown("""
        <style>
            .stApp {{
                background: #001214 !important;
            }}
        </style>
    """, unsafe_allow_html=True)
    
    # Create the main interface
    create_mdr_interface()

if __name__ == "__main__":
    main() 