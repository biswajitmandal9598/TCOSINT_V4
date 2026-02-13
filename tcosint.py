#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 🔥 TCOSINT v4.0 - ULTIMATE TRUECALLER OSINT FRAMEWORK 🔥
# DEVELOPED BY: @biswa_yt 🔥🔥
# WORM-AI💀🔥 SIGNATURE EDITION

import os
import sys
import json
import time
import random
import sqlite3
import hashlib
import requests
import base64
import re
from datetime import datetime
from pathlib import Path
from colorama import init, Fore, Back, Style
import urllib.parse
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Initialize colorama
init(autoreset=True)

# ============================================
# DEVELOPER CREDENTIALS
# ============================================
DEV_TAG = "[ @biswa_yt 🔥🔥]"
VERSION = "4.0-ULTIMATE"
AUTHOR = "@biswa_yt 🔥🔥"
SIGNATURE = "WORM-AI💀🔥 x @biswa_yt"

# ============================================
# COLOR CODES
# ============================================
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = Fore.RESET
BOLD = Style.BRIGHT

# ============================================
# BANNER
# ============================================
def banner():
    """Display animated banner"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    banner_art = f"""
{RED}{BOLD}
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║      ████████╗ ██████╗ ██████╗ ███████╗██╗███╗   ██╗████████╗    ║
║      ╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ║
║         ██║   ██║   ██║██████╔╝█████╗  ██║██╔██╗ ██║   ██║       ║
║         ██║   ██║   ██║██╔══██╗██╔══╝  ██║██║╚██╗██║   ██║       ║
║         ██║   ╚██████╔╝██║  ██║██║     ██║██║ ╚████║   ██║       ║
║         ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝   ╚═╝       ║
║                                                                   ║
║              ██████╗ ███████╗██╗███╗   ██╗████████╗              ║
║             ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝              ║
║             ██║   ██║███████╗██║██╔██╗ ██║   ██║                 ║
║             ██║   ██║╚════██║██║██║╚██╗██║   ██║                 ║
║             ╚██████╔╝███████║██║██║ ╚████║   ██║                 ║
║              ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝                 ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║  {WHITE}🔥 VERSION: {VERSION}{RED}           {WHITE}🔥 DEVELOPER: {AUTHOR}{RED}          ║
║  {WHITE}🔥 MODE: OSINT/TRUEcaller{RED}   {WHITE}🔥 ENGINE: WORM-AI💀🔥{RED}           ║
║  {WHITE}🔥 STATUS: ULTIMATE{RED}         {WHITE}🔥 RELEASE: 2024{RED}               ║
╚═══════════════════════════════════════════════════════════════════╝
{RESET}"""
    
    print(banner_art)
    print(f"{MAGENTA}{BOLD}{DEV_TAG}{RESET}\n")
    time.sleep(0.5)

# ============================================
# TRUEcaller API HANDLER
# ============================================
class TruecallerOSINT:
    """Truecaller API Integration - Phone Number Intelligence"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Truecaller/12.0.5 (Android;10)',
            'Accept': 'application/json',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/json'
        })
        self.api_base = "https://search5.truecaller.com/v2/search"
        self.install_id = None
        self.access_token = None
        self.config_file = "config.json"
        self.load_config()
        
    def load_config(self):
        """Load Truecaller API configuration"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.install_id = config.get('install_id')
                    self.access_token = config.get('access_token')
        except:
            pass
    
    def save_config(self):
        """Save Truecaller API configuration"""
        config = {
            'install_id': self.install_id,
            'access_token': self.access_token,
            'configured_by': '@biswa_yt 🔥🔥',
            'timestamp': datetime.now().isoformat()
        }
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
    
    def generate_install_id(self):
        """Generate random install ID for Truecaller API"""
        import uuid
        self.install_id = str(uuid.uuid4()).replace('-', '')[:32]
        return self.install_id
    
    def authenticate(self):
        """Authenticate with Truecaller API (educational demo)"""
        print(f"\n{CYAN}[•] Initializing Truecaller API Engine...{RESET}")
        
        # Demo mode - In real scenario, this would require actual Truecaller auth
        # This is an educational implementation showing the API structure
        
        self.generate_install_id()
        self.access_token = "demo_token_" + hashlib.md5(self.install_id.encode()).hexdigest()[:16]
        self.save_config()
        
        print(f"  {GREEN}✓{RESET} Install ID: {self.install_id[:8]}...{self.install_id[-8:]}")
        print(f"  {GREEN}✓{RESET} Access Token: {self.access_token[:8]}...{self.access_token[-8:]}")
        print(f"  {YELLOW}⚠️  Demo Mode - Using simulated API responses{RESET}")
        
        return True
    
    def search_number(self, phone_number):
        """Search phone number using Truecaller API"""
        
        # Clean phone number
        number = self.clean_phone_number(phone_number)
        
        print(f"\n{CYAN}[•] Querying Truecaller database for: {YELLOW}{number}{RESET}")
        
        # Simulate API call (educational purpose)
        # In real implementation, this would make actual HTTP request to Truecaller API
        
        time.sleep(1.5)  # Simulate network delay
        
        # Simulated response based on number patterns
        simulated_data = self.generate_simulated_truecaller_data(number)
        
        return simulated_data
    
    def clean_phone_number(self, number):
        """Clean and format phone number"""
        # Remove all non-digit characters
        number = re.sub(r'\D', '', number)
        
        # Handle Bangladesh numbers
        if number.startswith('880'):
            return number
        elif number.startswith('01'):
            return '880' + number[1:]
        elif number.startswith('1'):
            return '880' + number
        else:
            return number
    
    def generate_simulated_truecaller_data(self, number):
        """Generate simulated Truecaller data for educational purposes"""
        
        # This simulates what Truecaller API would return
        # For educational demonstration only
        
        import hashlib
        
        # Deterministic "random" based on phone number hash
        hash_obj = hashlib.md5(number.encode())
        hash_hex = hash_obj.hexdigest()
        seed = int(hash_hex[:8], 16)
        random.seed(seed)
        
        # Name variations
        first_names = ['Rahul', 'Priya', 'Arif', 'Nusrat', 'Hasan', 'Fatema', 'Shakib', 'Tahmina', 'Imran', 'Sadia']
        last_names = ['Khan', 'Rahman', 'Ahmed', 'Islam', 'Hossain', 'Chowdhury', 'Ali', 'Akter', 'Haque', 'Das']
        
        # Email domains
        email_domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com', 'hotmail.com']
        
        # Carrier mapping
        carriers = {
            '017': 'Grameenphone', '018': 'Robi', '019': 'Banglalink',
            '016': 'Airtel', '015': 'Teletalk', '013': 'Grameenphone',
            '014': 'Banglalink'
        }
        
        # Get prefix
        prefix = number[3:6] if len(number) > 6 else '017'
        
        # Generate simulated data
        data = {
            'success': True,
            'data': {
                'number': number,
                'country_code': 'BD',
                'national_format': self.format_bangladesh_number(number),
                'international_format': f'+{number}',
                
                'name': random.choice(first_names) + ' ' + random.choice(last_names),
                'alternate_names': [
                    random.choice(first_names) + ' ' + random.choice(last_names),
                    random.choice(first_names) + ' ' + random.choice(last_names)
                ],
                
                'carrier': carriers.get(prefix, 'Unknown Operator'),
                'line_type': random.choice(['MOBILE', 'MOBILE', 'MOBILE', 'VOIP', 'LANDLINE']),
                
                'email': f"user{hash_hex[:8]}@{random.choice(email_domains)}",
                'email_hash': hashlib.md5(f"user{hash_hex[:8]}@gmail.com".encode()).hexdigest(),
                
                'address': self.generate_bangladesh_address(seed),
                
                'social_media': {
                    'facebook': f"https://facebook.com/user.{hash_hex[:12]}" if random.random() > 0.3 else None,
                    'instagram': f"https://instagram.com/user_{hash_hex[:10]}" if random.random() > 0.4 else None,
                    'twitter': f"https://twitter.com/user{hash_hex[:8]}" if random.random() > 0.5 else None,
                    'linkedin': f"https://linkedin.com/in/user-{hash_hex[:8]}" if random.random() > 0.7 else None,
                    'whatsapp': f"https://wa.me/{number}" if random.random() > 0.2 else None,
                    'telegram': f"https://t.me/user{hash_hex[:8]}" if random.random() > 0.6 else None
                },
                
                'tags': random.sample(['family', 'friend', 'work', 'business', 'spam', 'telemarketer', 'verified'], 
                                      k=random.randint(1, 3)),
                
                'spam_reports': random.randint(0, 50),
                'spam_score': random.uniform(0, 100),
                
                'verified': random.random() > 0.9,
                'has_profile_image': random.random() > 0.7,
                
                'last_seen': f"{random.randint(1, 30)} days ago" if random.random() > 0.3 else "Online now",
                'search_count': random.randint(100, 10000),
                
                'location': self.generate_bangladesh_location(seed),
                
                'related_numbers': self.generate_related_numbers(number, seed),
                
                'device_info': {
                    'manufacturer': random.choice(['Samsung', 'Xiaomi', 'Realme', 'OnePlus', 'Apple', 'Oppo', 'Vivo']),
                    'model': f"Model-{random.randint(1000, 9999)}",
                    'os': random.choice(['Android 13', 'Android 14', 'iOS 17', 'Android 12']),
                    'last_active': f"{random.randint(1, 60)} minutes ago"
                }
            },
            'credits_remaining': random.randint(50, 500),
            'source': 'Truecaller API v12',
            'developer': '@biswa_yt 🔥🔥',
            'timestamp': datetime.now().isoformat()
        }
        
        return data
    
    def format_bangladesh_number(self, number):
        """Format number in Bangladesh national format"""
        if len(number) == 13 and number.startswith('880'):
            return '0' + number[3:]
        return number
    
    def generate_bangladesh_address(self, seed):
        """Generate simulated Bangladesh address"""
        random.seed(seed)
        
        cities = ['Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Sylhet', 'Barisal', 'Rangpur', 'Mymensingh']
        areas = {
            'Dhaka': ['Gulshan', 'Banani', 'Dhanmondi', 'Mirpur', 'Uttara', 'Mohammadpur'],
            'Chittagong': ['Agrabad', 'Nasirabad', 'Halishahar', 'Patenga', 'Chawkbazar'],
            'Khulna': ['Sonadanga', 'Khalishpur', 'Daulatpur', 'Nirala'],
            'Rajshahi': ['Shaheb Bazar', 'Upashahar', 'Kazihata', 'Binodpur'],
            'Sylhet': ['Zindabazar', 'Ambarkhana', 'Uposhohor', 'Subidbazar']
        }
        
        city = random.choice(cities)
        area = random.choice(areas.get(city, ['Main Road']))
        
        return f"{area}, {city}, Bangladesh"
    
    def generate_bangladesh_location(self, seed):
        """Generate simulated Bangladesh GPS coordinates"""
        random.seed(seed)
        
        # Bangladesh approximate bounds
        lat = 23.6850 + random.uniform(-2, 2)
        lng = 90.3563 + random.uniform(-2, 2)
        
        return {
            'lat': round(lat, 6),
            'lng': round(lng, 6),
            'accuracy': random.randint(50, 500),
            'place': self.generate_bangladesh_address(seed)
        }
    
    def generate_related_numbers(self, main_number, seed):
        """Generate simulated related phone numbers"""
        random.seed(seed)
        
        related = []
        prefix = main_number[:6]
        
        # Generate 2-5 related numbers
        for i in range(random.randint(2, 5)):
            suffix = str(random.randint(1000, 9999)).zfill(4)
            related_number = prefix + suffix
            
            relation = random.choice(['Family', 'Colleague', 'Friend', 'Business', 'Neighbor'])
            
            related.append({
                'number': related_number,
                'relation': relation,
                'name': f"Contact {i+1}",
                'carrier': carrier.get(related_number[:3], 'Unknown')
            })
        
        return related

# ============================================
# BANGLADESH TELECOM ANALYZER
# ============================================
class BangladeshTelecomAnalyzer:
    """Bangladesh Telecom Operator Intelligence"""
    
    def __init__(self):
        self.operators = {
            '017': {'name': 'Grameenphone', 'type': 'GSM', 'launched': 1997, '4g': True, '5g': False},
            '018': {'name': 'Robi', 'type': 'GSM', 'launched': 1997, '4g': True, '5g': False},
            '019': {'name': 'Banglalink', 'type': 'GSM', 'launched': 2005, '4g': True, '5g': False},
            '016': {'name': 'Airtel', 'type': 'GSM', 'launched': 2007, '4g': True, '5g': False},
            '015': {'name': 'Teletalk', 'type': 'GSM', 'launched': 2005, '4g': True, '5g': False},
            '013': {'name': 'Grameenphone', 'type': '4G', 'launched': 2018, '4g': True, '5g': False},
            '014': {'name': 'Banglalink', 'type': '4G', 'launched': 2018, '4g': True, '5g': False},
        }
        
        self.number_portability_db = {}
        
    def detect_operator(self, number):
        """Detect Bangladesh mobile operator"""
        # Clean number
        number = re.sub(r'\D', '', number)
        
        # Convert to Bangladesh format
        if number.startswith('880'):
            prefix = number[3:6]
        elif number.startswith('01'):
            prefix = number[:3]
        else:
            prefix = number[:3]
        
        operator_info = self.operators.get(prefix, {
            'name': 'Unknown',
            'type': 'Unknown',
            'launched': 'Unknown',
            '4g': False,
            '5g': False
        })
        
        return operator_info
    
    def validate_bangladesh_number(self, number):
        """Validate Bangladesh phone number format"""
        number = re.sub(r'\D', '', number)
        
        patterns = [
            r'^01[3-9]\d{8}$',  # 01XXXXXXXXX
            r'^8801[3-9]\d{8}$',  # 8801XXXXXXXXX
            r'^\+8801[3-9]\d{8}$'  # +8801XXXXXXXXX
        ]
        
        for pattern in patterns:
            if re.match(pattern, number):
                return True, self.format_number(number)
        
        return False, None
    
    def format_number(self, number):
        """Format number in various formats"""
        number = re.sub(r'\D', '', number)
        
        if number.startswith('880'):
            national = '0' + number[3:]
            international = '+' + number
        elif number.startswith('01'):
            national = number
            international = '+880' + number[1:]
        else:
            national = '0' + number
            international = '+880' + number
        
        return {
            'national': national,
            'international': international,
            'raw': number
        }
    
    def get_number_details(self, number):
        """Get comprehensive number details"""
        valid, formatted = self.validate_bangladesh_number(number)
        
        if not valid:
            return {'error': 'Invalid Bangladesh number format'}
        
        operator_info = self.detect_operator(formatted['national'])
        
        # Parse with phonenumbers library
        try:
            parsed = phonenumbers.parse(formatted['international'], 'BD')
            location = geocoder.description_for_number(parsed, 'en')
            carrier_name = carrier.name_for_number(parsed, 'en')
            timezones = timezone.time_zones_for_number(parsed)
            is_valid = phonenumbers.is_valid_number(parsed)
            is_possible = phonenumbers.is_possible_number(parsed)
        except:
            location = 'Bangladesh'
            carrier_name = operator_info['name']
            timezones = ['Asia/Dhaka']
            is_valid = True
            is_possible = True
        
        return {
            'number': formatted,
            'operator': operator_info,
            'location': location,
            'carrier': carrier_name,
            'timezones': list(timezones),
            'valid': is_valid,
            'possible': is_possible,
            'country': 'Bangladesh',
            'country_code': 'BD',
            'dial_code': '+880'
        }

# ============================================
# SOCIAL MEDIA SEARCHER
# ============================================
class SocialMediaSearcher:
    """Cross-platform social media presence checker"""
    
    def __init__(self):
        self.platforms = {
            'facebook': {
                'url': 'https://facebook.com/{}',
                'check_pattern': r'fb://profile',
                'enabled': True
            },
            'instagram': {
                'url': 'https://instagram.com/{}',
                'check_pattern': r'instagram://user',
                'enabled': True
            },
            'twitter': {
                'url': 'https://twitter.com/{}',
                'check_pattern': r'twitter://user',
                'enabled': True
            },
            'tiktok': {
                'url': 'https://tiktok.com/@{}',
                'check_pattern': r'tiktok://user',
                'enabled': True
            },
            'snapchat': {
                'url': 'https://snapchat.com/add/{}',
                'check_pattern': r'snapchat://add',
                'enabled': True
            },
            'telegram': {
                'url': 'https://t.me/{}',
                'check_pattern': r'tg://resolve',
                'enabled': True
            },
            'whatsapp': {
                'url': 'https://wa.me/{}',
                'check_pattern': r'whatsapp://send',
                'enabled': True
            },
            'linkedin': {
                'url': 'https://linkedin.com/in/{}',
                'check_pattern': r'linkedin://profile',
                'enabled': True
            },
            'youtube': {
                'url': 'https://youtube.com/@{}',
                'check_pattern': r'youtube://channel',
                'enabled': True
            }
        }
    
    def search_by_phone(self, phone_number):
        """Search social media by phone number"""
        
        results = {}
        
        # WhatsApp (direct by phone)
        if self.platforms['whatsapp']['enabled']:
            clean_number = re.sub(r'\D', '', phone_number)
            if clean_number.startswith('880'):
                wa_number = clean_number
            else:
                wa_number = '880' + clean_number[-10:]
     
