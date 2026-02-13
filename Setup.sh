#!/data/data/com.termux/files/usr/bin/bash
# 🔥 TCOSINT v4.0 - TERMUX SETUP SCRIPT 🔥
# DEVELOPED BY: @biswa_yt 🔥🔥

clear

# Colors
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
BLUE='\033[94m'
MAGENTA='\033[95m'
CYAN='\033[96m'
WHITE='\033[97m'
RESET='\033[0m'
BOLD='\033[1m'

echo -e "${RED}${BOLD}"
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║              🔥 TCOSINT v4.0 - TERMUX SETUP 🔥                   ║"
echo "║              ULTIMATE TRUECALLER OSINT FRAMEWORK                  ║"
echo "║                    DEVELOPED BY @biswa_yt 🔥🔥                    ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"

echo -e "${YELLOW}[+] Updating Termux packages...${RESET}"
pkg update -y && pkg upgrade -y

echo -e "${YELLOW}[+] Installing core dependencies...${RESET}"
pkg install python -y
pkg install python-pip -y
pkg install git -y
pkg install nano -y
pkg install wget -y
pkg install curl -y

echo -e "${YELLOW}[+] Installing Python libraries...${RESET}"
pip install --upgrade pip
pip install cryptography
pip install phonenumbers
pip install requests
pip install colorama
pip install pillow
pip install urllib3

echo -e "${YELLOW}[+] Creating TCOSINT directory structure...${RESET}"
mkdir -p TCOSINT_V4
cd TCOSINT_V4

mkdir -p modules
mkdir -p data
mkdir -p outputs/reports
mkdir -p outputs/exports
mkdir -p config

echo -e "${YELLOW}[+] Creating operator database...${RESET}"
cat > data/bd_operators.db << 'EOF'
{
  "operators": {
    "017": {"name": "Grameenphone", "type": "GSM", "launched": 1997, "4g": true},
    "018": {"name": "Robi", "type": "GSM", "launched": 1997, "4g": true},
    "019": {"name": "Banglalink", "type": "GSM", "launched": 2005, "4g": true},
    "016": {"name": "Airtel", "type": "GSM", "launched": 2007, "4g": true},
    "015": {"name": "Teletalk", "type": "GSM", "launched": 2005, "4g": true},
    "013": {"name": "Grameenphone", "type": "4G", "launched": 2018, "4g": true},
    "014": {"name": "Banglalink", "type": "4G", "launched": 2018, "4g": true}
  }
}
EOF

echo -e "${YELLOW}[+] Creating search patterns database...${RESET}"
cat > data/patterns.json << 'EOF'
{
  "email_patterns": [
    "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
  ],
  "phone_patterns": [
    "01[3-9]\\d{8}",
    "8801[3-9]\\d{8}"
  ],
  "social_patterns": {
    "facebook": "facebook\\.com/[a-zA-Z0-9.]+",
    "instagram": "instagram\\.com/[a-zA-Z0-9_]+",
    "twitter": "twitter\\.com/[a-zA-Z0-9_]+"
  }
}
EOF

echo -e "${YELLOW}[+] Creating config file...${RESET}"
cat > config/config.json << 'EOF'
{
  "version": "4.0",
  "developer": "@biswa_yt 🔥🔥",
  "truecaller_api": "demo_mode",
  "install_id": "",
  "access_token": "",
  "settings": {
    "auto_save": true,
    "show_demo_data": true,
    "color_output": true
  }
}
EOF

echo -e "${YELLOW}[+] Creating requirements.txt...${RESET}"
cat > requirements.txt << 'EOF'
cryptography>=3.4.8
phonenumbers>=8.12.0
requests>=2.25.1
colorama>=0.4.4
pillow>=8.3.1
urllib3>=1.26.0
EOF

echo -e "${YELLOW}[+] Creating main script file...${RESET}"
echo -e "${CYAN}[i] Please create tcosint.py and paste the main code${RESET}"

echo -e "${GREEN}${BOLD}"
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║                    SETUP COMPLETE! 🔥                            ║"
echo "╠═══════════════════════════════════════════════════════════════════╣"
echo "║                                                                   ║"
echo "║  📁 Project: TCOSINT_V4/                                         ║"
echo "║  🐍 Script:  tcosint.py                                          ║"
echo "║                                                                   ║"
echo "║  ▶️  Next steps:                                                  ║"
echo "║     1. cd TCOSINT_V4                                            ║"
echo "║     2. nano tcosint.py  # Paste the main code                   ║"
echo "║     3. python tcosint.py # Run the tool                         ║"
echo "║                                                                   ║"
echo "║  📊 Output directory: outputs/reports/                           ║"
echo "║                                                                   ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"
echo -e "${MAGENTA}[ @biswa_yt 🔥🔥] TCOSINT v4.0 READY FOR DEPLOYMENT${RESET}"
