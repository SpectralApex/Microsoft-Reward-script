import subprocess
import random
import datetime
import os
import time

log_file = "last_run.txt"
today = str(datetime.date.today())

# Check if already run today
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        last_run = f.read().strip()
    if last_run == today:
        print("[MISSION LOG] Already executed today. Skipping.")
        exit()

# --- Your existing script code goes here ---
print("[MISSION LOG] Running daily search mission...")

# Save today's date
with open(log_file, "w") as f:
    f.write(today)

#List of random search topics
topics = [
    "Python programming", "Cybersecurity labs", "Gaming dashboards", "Artificial Intelligence",
    "Space exploration", "Quantum computing", "Machine learning", "Data visualization",
    "Blockchain technology", "Cloud computing", "Augmented reality", "Virtual reality",
    "Digital art", "System automation", "Linux commands", "PowerShell scripting",
    "Web development", "Mobile apps", "Cyber defense", "Ethical hacking",
    "Internet of Things (IoT)", "Smart homes", "Robotics engineering", "Drone technology",
    "Renewable energy", "Solar power innovations", "Electric vehicles", "Self-driving cars",
    "Space telescopes", "Black holes", "Mars colonization", "Exoplanet discovery",
    "Astrobiology", "Nanotechnology", "Genetic engineering", "CRISPR technology",
    "Brain-computer interfaces", "Neural networks", "Deep learning", "Natural language processing",
    "Chatbots", "Voice assistants", "Cyber forensics", "Malware analysis",
    "Phishing detection", "Incident response drills", "Penetration testing", "Zero trust security",
    "Cloud security", "Digital privacy", "Encryption methods", "Quantum cryptography",
    "Passwordless authentication", "Multi-factor authentication", "Social engineering attacks",
    "Cyber law", "Digital currencies", "NFTs (Non-Fungible Tokens)", "Metaverse worlds",
    "Game engines", "Unreal Engine", "Unity development", "Esports tournaments",
    "Game streaming", "Retro gaming", "VR gaming", "AR gaming",
    "Procedural generation in games", "AI in game design", "Open-world games",
    "Role-playing games (RPGs)", "Simulation games", "Strategy games", "Puzzle games",
    "Indie game development", "Mobile gaming trends", "Cloud gaming platforms",
    "Gaming hardware", "Graphics cards evolution", "CPU architecture", "Operating systems",
    "Open-source software", "Version control (Git)", "Continuous integration",
    "DevOps pipelines", "Containerization (Docker)", "Kubernetes orchestration",
    "Microservices architecture", "API design", "REST vs GraphQL"
]

#pick 3 random topics
random_topics = random.sample(topics, 3)

# Edge executable path
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Force Main profile (replace 'Default' with actual folder name once confirmed)
profile = "Default"

# Launch searches in new window under JERIN profile
for topic in random_topics:
    url = f"https://www.bing.com/search?q={topic}&form=ML2PCO"
    subprocess.Popen([edge_path, f"--profile-directory={profile}", url])
    time.sleep(2)  # wait 2 seconds before the next search