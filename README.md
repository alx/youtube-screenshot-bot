# YouTube Screenshot Bot

A Python automation tool that captures screenshots from YouTube videos. This bot uses Selenium with Firefox WebDriver to load YouTube videos, play them, and take high-resolution screenshots at configured intervals.

## Features

- Capture screenshots from multiple YouTube videos defined in configuration
- Headless browser automation with virtual display support
- Configurable browser settings and wait times
- Automatic screenshot naming with timestamps
- YAML-based configuration

## Installation

### Prerequisites

- Python 3.7+
- Firefox browser

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/alx/youtube-screenshot-bot.git
   cd youtube-screenshot-bot
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `config.yaml` file in the project root directory with the following structure:

```yaml
# Display settings
display:
  visible: 0  # 0 for headless, 1 to see the browser
  width: 3840
  height: 2160

# Browser options
browser_options:
  - '--headless'
  - '--no-sandbox'
  - '--disable-dev-shm-usage'

# Video IDs to process
video_ids:
  - 'vCEsE5oK6RM'  # Example video ID
  - 'dQw4w9WgXcQ'  # Another example video

# Wait times (seconds)
wait_before_click: 3  # Wait after loading before clicking play
wait_after_click: 3   # Wait after clicking play before screenshot

# Screenshot settings
screenshot_directory: 'screenshots'
```

### How to find a YouTube video ID

The video ID is the part after `v=` in a YouTube URL. For example, in `https://www.youtube.com/watch?v=vCEsE5oK6RM`, the video ID is `vCEsE5oK6RM`.

## Usage

Run the script with:

```bash
python screenshot_bot.py
```

Screenshots will be saved in the `screenshots` directory (or your configured directory) with filenames including the video ID and timestamp.

## Dependencies

- selenium - Web browser automation
- pyvirtualdisplay - Virtual display for headless environments
- webdriver_manager - Automatic management of WebDriver binaries
- pyyaml - YAML file parsing

## Project Structure

```
youtube-screenshot-bot/
├── screenshot_bot.py   # Main script
├── config.yaml         # Configuration file
├── requirements.txt    # Dependencies
├── screenshots/        # Output directory
└── README.md           # This file
```

## Troubleshooting

- **Browser doesn't launch**: Make sure Firefox is installed on your system.
- **WebDriver errors**: Try updating selenium and webdriver-manager.
- **Blank screenshots**: Increase the wait times in your configuration.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Created with ❤️ for automating YouTube screenshots

---
