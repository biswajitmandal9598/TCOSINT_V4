# TCOSINT_V4
TCOSINT_V4 is an advanced Open Source Intelligence (OSINT) toolkit designed for research, analysis, and information gathering from publicly available sources



# 1. Clone repository
    git clone https://github.com/biswa-yt/TCOSINT.git
    cd TCOSINT

# 2. Run setup
     chmod +x setup.sh
     ./setup.sh

# 3. Install dependencies
    pip install -r requirements.txt

# 4. Launch TCOSINT
     python tcosint.py









 # Linux installation 

     sudo apt update && sudo apt install python3 python3-pip git -y
    git clone https://github.com/biswa-yt/TCOSINT.git
       cd TCOSINT
    pip3 install -r requirements.txt



       python3 tcosint.py




       
---

# 📄 5. LICENSE

```markdown
# EDUCATIONAL USE ONLY LICENSE

Copyright (c) 2024 @biswa_yt 🔥🔥

## TERMS AND CONDITIONS

### 1. EDUCATIONAL PURPOSE ONLY
This software is provided SOLELY for educational and security research purposes. 
The primary intent is to demonstrate OSINT techniques and promote cybersecurity awareness.

### 2. PROHIBITED USES
You may NOT use this software for:
- ❌ Stalking, harassment, or intimidation
- ❌ Unauthorized surveillance or monitoring
- ❌ Identity theft or fraud
- ❌ Any illegal activity under any jurisdiction
- ❌ Commercial purposes without explicit permission
- ❌ Violating Truecaller's Terms of Service

### 3. USER RESPONSIBILITY
By using this software, you acknowledge and agree that:
- You are SOLELY responsible for your actions
- You will comply with all applicable laws
- You have obtained necessary permissions
- The developer assumes NO LIABILITY

### 4. LEGAL WARNINGS
This tool may be illegal in some jurisdictions including but not limited to:
- 🇧🇩 Bangladesh: Digital Security Act 2018
- 🇺🇸 USA: Computer Fraud and Abuse Act
- 🇪🇺 EU: GDPR Regulations
- 🌏 Other countries with privacy laws

### 5. NO WARRANTY
This software is provided "AS IS" without any warranty, express or implied.
The developer does not guarantee accuracy, reliability, or completeness of data.

### 6. TERMINATION
Violation of any term automatically terminates your right to use this software.

### 7. ATTRIBUTION
Any redistribution must retain:
- Original copyright notice
- Developer credit to @biswa_yt 🔥🔥
- This license text

---

## ⚠️ READ BEFORE USING





---

## 📊 MODE 4: GENERATE REPORT

### **Description:**
Generate professional reports from previous scans.

### **Options:**
- **TXT Format** - Detailed text report
- **JSON Format** - Raw data export
- **CSV Format** - Spreadsheet compatible

### **Report Location:**
All reports are saved in: `outputs/reports/`

### **Filename Format:**
`TCOSINT_<PHONE>_<TIMESTAMP>.txt`

---

## ⚙️ MODE 5: CONFIGURE TRUECALLER API

### **Description:**
Configure Truecaller API settings for enhanced data extraction.

### **Demo Mode (Default):**
- No configuration needed
- Simulated data for educational purposes
- Works immediately

### **Advanced Configuration:**
1. Obtain Truecaller API credentials
2. Enter Install ID
3. Enter Access Token
4. Test connection

---

## 📚 MODE 6: VIEW SCAN HISTORY

### **Description:**
View and manage previously saved scan reports.

### **Features:**
- List all previous scans
- View report details
- Delete old reports
- Export to different formats

---

## 🎯 COMMAND LINE ARGUMENTS

```bash
# Quick scan from terminal
python tcosint.py --scan 01712345678

# Bulk scan from file
python tcosint.py --bulk numbers.txt

# Export to JSON
python tcosint.py --scan 01712345678 --format json

# Help
python tcosint.py --help
