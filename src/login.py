import streamlit as st
import streamlit.components.v1 as components

def create_login_screen():
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .block-container {padding-top: 0; padding-bottom: 0;}
            body {
                background-color: #001214;
                color: #39FFE1;
                font-family: "Courier New", monospace;
            }
        </style>
    """, unsafe_allow_html=True)

    html = """
    <div class="login-overlay">
        <div class="login-container">
            <div class="login-box">
                <div class="lumon-logo">
                    <svg width="200" height="60" viewBox="0 0 200 60">
                        <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" 
                              fill="#39FFE1" font-family="Courier New" font-size="24" font-weight="bold">
                            LUMON
                        </text>
                    </svg>
                </div>
                <div class="login-form">
                    <div class="input-group">
                        <label>EMPLOYEE ID</label>
                        <input type="text" id="employee-id" class="retro-input" placeholder="MDR-XXXX">
                    </div>
                    <div class="input-group">
                        <label>PASSWORD</label>
                        <input type="password" id="password" class="retro-input" placeholder="********">
                    </div>
                    <button class="login-button" onclick="handleLogin()">LOGIN</button>
                </div>
                <div class="login-footer">
                    <p>MACRODATA REFINEMENT</p>
                    <p class="version">v1.0.0</p>
                </div>
            </div>
        </div>
    </div>

    <style>
        .login-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(0, 18, 20, 0.95);
            backdrop-filter: blur(10px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }

        .login-container {
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        .login-container::before {
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
        }

        .login-box {
            background-color: rgba(0, 18, 20, 0.9);
            border: 1px solid #39FFE1;
            padding: 40px;
            width: 400px;
            box-shadow: 0 0 20px rgba(57, 255, 225, 0.2);
            animation: fadeIn 0.5s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .lumon-logo {
            text-align: center;
            margin-bottom: 40px;
        }

        .input-group {
            margin-bottom: 20px;
        }

        .input-group label {
            display: block;
            margin-bottom: 5px;
            font-size: 14px;
            color: #39FFE1;
        }

        .retro-input {
            width: 100%;
            padding: 10px;
            background-color: #001214;
            border: 1px solid #39FFE1;
            color: #39FFE1;
            font-family: "Courier New", monospace;
            font-size: 16px;
        }

        .retro-input::placeholder {
            color: rgba(57, 255, 225, 0.3);
        }

        .retro-input:focus {
            outline: none;
            box-shadow: 0 0 10px rgba(57, 255, 225, 0.5);
        }

        .login-button {
            width: 100%;
            padding: 12px;
            background-color: #001214;
            border: 1px solid #39FFE1;
            color: #39FFE1;
            font-family: "Courier New", monospace;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .login-button:hover {
            background-color: #39FFE1;
            color: #001214;
        }

        .login-footer {
            margin-top: 40px;
            text-align: center;
            font-size: 12px;
            color: #39FFE1;
        }

        .version {
            opacity: 0.5;
            margin-top: 5px;
        }

        @keyframes scanline {
            0% { background-position: 0 0; }
            100% { background-position: 0 100%; }
        }
    </style>

    <script>
        function handleLogin() {
            const employeeId = document.getElementById('employee-id').value;
            const password = document.getElementById('password').value;
            
            if (employeeId && password) {
                // Send message to Streamlit
                window.parent.postMessage({
                    type: 'streamlit:setComponentValue',
                    value: {
                        employee_id: employeeId,
                        password: password
                    }
                }, '*');
            }
        }

        // Handle Enter key
        document.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                handleLogin();
            }
        });
    </script>
    """

    components.html(html, height=600)

def main():
    create_login_screen()

if __name__ == "__main__":
    main() 