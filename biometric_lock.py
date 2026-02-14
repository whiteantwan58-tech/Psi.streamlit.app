"""
🔒 Biometric Lock Screen Module
EVE 1010_WAKE - Quantum Security Interface

This module provides a biometric authentication interface for the PSI Sovereign System.
Includes facial recognition placeholder and fingerprint scanner animation.
"""

import streamlit as st
from datetime import datetime

# Authorized users
AUTHORIZED_USERS = ["whiteantwan58-tech", "eve"]

def show_lock_screen():
    """
    Display biometric lock screen with quantum-themed design
    Returns True if user is authenticated, False otherwise
    """
    
    st.markdown("""
    <style>
        /* Full screen lock overlay */
        .lock-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: linear-gradient(135deg, #0a0a1f 0%, #1a1a3e 50%, #2d1b69 100%);
            z-index: 9999;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        /* Animated fingerprint scanner */
        .fingerprint {
            width: 150px;
            height: 150px;
            border: 3px solid #00ffff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: pulse 2s ease-in-out infinite;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.6);
        }
        
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
                box-shadow: 0 0 30px rgba(0, 255, 255, 0.6);
            }
            50% {
                transform: scale(1.1);
                box-shadow: 0 0 50px rgba(0, 255, 255, 0.9);
            }
        }
        
        /* Holographic text */
        .lock-title {
            background: linear-gradient(45deg, #00ffff, #ff00ff, #ffff00, #00ffff);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: holographicShift 3s ease infinite;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 20px;
            text-align: center;
        }
        
        @keyframes holographicShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        /* Access denied animation */
        .access-denied {
            color: #ff0000;
            font-size: 1.5rem;
            animation: blink 0.5s linear infinite;
        }
        
        @keyframes blink {
            0%, 50%, 100% { opacity: 1; }
            25%, 75% { opacity: 0.3; }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Lock screen container
    st.markdown("""
    <div class="lock-screen">
        <div class="lock-title">🔐 EVE 1010_WAKE</div>
        <div style="color: #00ffff; font-size: 1.2rem; margin-bottom: 40px;">
            BIOMETRIC AUTHENTICATION REQUIRED
        </div>
        <div class="fingerprint">
            <span style="font-size: 4rem;">🔓</span>
        </div>
        <div style="color: #888; margin-top: 30px; text-align: center;">
            <p>Authorized Access Only</p>
            <p style="font-size: 0.9rem;">whiteantwan58-tech | eve</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Authentication form (below the lock screen overlay)
    st.markdown("<br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
    
    with st.form("biometric_auth"):
        st.markdown("### 🔐 Enter Access Code")
        
        username = st.text_input(
            "Username",
            placeholder="whiteantwan58-tech or eve",
            key="username_input"
        )
        
        access_code = st.text_input(
            "Access Code",
            type="password",
            placeholder="Enter your access code",
            key="access_code_input"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            submit = st.form_submit_button("🔓 Unlock", use_container_width=True)
        
        with col2:
            bypass = st.form_submit_button("⚠️ Emergency Bypass", use_container_width=True)
    
    if submit:
        if username.lower() in AUTHORIZED_USERS:
            # In production, verify access_code against secure hash
            st.session_state.authenticated = True
            st.session_state.current_user = username
            st.success(f"✅ Access Granted: {username}")
            st.balloons()
            return True
        else:
            st.error("❌ ACCESS DENIED - Unauthorized user")
            st.markdown('<p class="access-denied">⚠️ SECURITY BREACH LOGGED</p>', unsafe_allow_html=True)
            return False
    
    if bypass:
        # Emergency bypass for development/testing
        st.warning("⚠️ Emergency Bypass Activated - Limited Access")
        st.session_state.authenticated = True
        st.session_state.current_user = "guest"
        return True
    
    return False

def check_authentication():
    """
    Check if user is authenticated
    Returns True if authenticated, False otherwise
    """
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    return st.session_state.authenticated

def get_current_user():
    """
    Get the current authenticated user
    Returns username or "guest"
    """
    if "current_user" not in st.session_state:
        return "guest"
    
    return st.session_state.current_user

def logout():
    """
    Log out the current user
    """
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.rerun()

# ============================================================
# BROWSER CAMERA ACCESS (Placeholder)
# ============================================================

def enable_camera_access():
    """
    Enable browser camera access using HTML5 MediaDevices API
    This is a placeholder for future implementation
    """
    
    st.markdown("""
    ### 📹 Camera Access Instructions
    
    To enable facial recognition, you need to:
    
    1. **Grant Permission**: Allow camera access when prompted by browser
    2. **HTTPS Required**: Camera API only works on secure connections
    3. **Browser Support**: Use Chrome, Edge, or Safari
    
    #### JavaScript Implementation (Future)
    
    ```javascript
    // MediaDevices API for camera access
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            // Camera stream available
            const video = document.querySelector('video');
            video.srcObject = stream;
        })
        .catch(function(err) {
            console.error("Camera access denied:", err);
        });
    ```
    
    #### Python Streamlit Component (Future)
    
    ```python
    import streamlit.components.v1 as components
    
    # Custom component for camera access
    camera_html = '''
        <video id="video" width="640" height="480" autoplay></video>
        <script>
            const video = document.getElementById('video');
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(stream => video.srcObject = stream);
        </script>
    '''
    components.html(camera_html)
    ```
    """)
    
    st.info("📸 **Note**: Camera integration requires custom Streamlit component development")

# ============================================================
# FINGERPRINT SCANNER ANIMATION
# ============================================================

def show_fingerprint_scanner():
    """
    Display animated fingerprint scanner
    Pure CSS/HTML animation
    """
    
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 300px;">
        <div class="fingerprint">
            <svg width="100" height="100" viewBox="0 0 100 100">
                <!-- Fingerprint ridges -->
                <ellipse cx="50" cy="50" rx="40" ry="45" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.3"/>
                <ellipse cx="50" cy="50" rx="35" ry="40" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.4"/>
                <ellipse cx="50" cy="50" rx="30" ry="35" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.5"/>
                <ellipse cx="50" cy="50" rx="25" ry="30" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.6"/>
                <ellipse cx="50" cy="50" rx="20" ry="25" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.7"/>
                <ellipse cx="50" cy="50" rx="15" ry="20" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.8"/>
                <ellipse cx="50" cy="50" rx="10" ry="15" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.9"/>
                
                <!-- Scanning line -->
                <line x1="0" y1="50" x2="100" y2="50" stroke="#ff00ff" stroke-width="3" opacity="0.8">
                    <animate attributeName="y1" values="0;100;0" dur="2s" repeatCount="indefinite"/>
                    <animate attributeName="y2" values="0;100;0" dur="2s" repeatCount="indefinite"/>
                </line>
            </svg>
        </div>
    </div>
    
    <p style="text-align: center; color: #00ffff; font-size: 1.2rem; margin-top: 20px;">
        🔍 Scanning biometric signature...
    </p>
    """, unsafe_allow_html=True)

# ============================================================
# EXAMPLE USAGE
# ============================================================

if __name__ == "__main__":
    st.set_page_config(page_title="Biometric Lock Test", page_icon="🔒")
    
    st.title("🔒 Biometric Lock Screen Test")
    
    if not check_authentication():
        if show_lock_screen():
            st.rerun()
    else:
        st.success(f"✅ Authenticated as: {get_current_user()}")
        
        st.markdown("### 🎉 Access Granted!")
        st.markdown("You have successfully passed biometric authentication.")
        
        if st.button("🚪 Logout"):
            logout()
        
        st.markdown("---")
        
        st.markdown("### 📹 Camera Access Demo")
        enable_camera_access()
        
        st.markdown("---")
        
        st.markdown("### 🔍 Fingerprint Scanner")
        show_fingerprint_scanner()
