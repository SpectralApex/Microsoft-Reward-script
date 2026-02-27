# Microsoft Rewards Script

A powerful Python script designed to automate and optimize your Microsoft Rewards experience. This tool helps you earn rewards efficiently by automating daily tasks, point collection, and account management.

## Features
- 🎯 **Automated Daily Rewards**: Automatically complete daily tasks to earn points
- 💰 **Point Collection**: Maximize your reward points through intelligent automation
- 📊 **Account Management**: Manage multiple accounts seamlessly
- ⚙️ **Customizable Settings**: Fine-tune the script to match your preferences
- 📈 **Progress Tracking**: Monitor your rewards and progress over time
- 🔐 **Secure**: Handles credentials safely with encryption support
- ✅ **Easy Setup**: Simple configuration and installation process

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A Microsoft account with Microsoft Rewards enabled
- Internet connection

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/SpectralApex/Microsoft-Reward-script.git
cd Microsoft-Reward-script
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration

Create a `config.json` file in the root directory with your settings:

```json
{
  "accounts": [
    {
      "email": "your-email@outlook.com",
      "password": "your-password",
      "enabled": true
    }
  ],
  "settings": {
    "auto_complete_tasks": true,
    "daily_limit": 1000,
    "timeout": 30
  }
}
```

**⚠️ Important**: Never commit `config.json` to version control. Use environment variables or `.env` file for sensitive data.

## Usage

### Basic Usage
```bash
python main.py
```

### With Custom Config
```bash
python main.py --config path/to/config.json
```

### View Help
```bash
python main.py --help
```

## Important Notes

⚠️ **Disclaimer**: 
- This script is for educational purposes only
- Use at your own risk and responsibility
- The authors are not responsible for any account bans or issues
- Always comply with Microsoft's Terms of Service
- Microsoft may change their platform at any time, potentially breaking this script
- Test with a secondary account before using with your main account

## Troubleshooting

### Script Won't Run
- Ensure Python 3.8+ is installed: `python --version`
- Check dependencies: `pip list`
- Verify config.json is correctly formatted

### Authentication Fails
- Verify email and password in config.json
- Check internet connection
- Try logging in manually to verify credentials work

### Missing Modules
```bash
pip install --upgrade -r requirements.txt
```

## Contributing
We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Support
For issues, questions, or suggestions, please open an [Issue](https://github.com/SpectralApex/Microsoft-Reward-script/issues) on GitHub.

---

**Last Updated**: February 2026
**Version**: 1.0.0