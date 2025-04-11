import yaml
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pyvirtualdisplay import Display
from selenium.common.exceptions import WebDriverException

def load_config(config_path='config.yaml'):
    """Load configuration from YAML file."""
    with open(config_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML configuration: {e}")
            raise

def setup_display(config):
    """Set up virtual display based on configuration."""
    display_config = config.get('display', {})
    visible = display_config.get('visible', 0)
    width = display_config.get('width', 3840)
    height = display_config.get('height', 2160)

    display = Display(visible=visible, size=(width, height))
    display.start()
    return display

def setup_browser(config):
    """Initialize browser with configuration options."""
    options = webdriver.FirefoxOptions()

    for option in config.get('browser_options', []):
        options.add_argument(option)

    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=options
    )
    return browser

def process_video(browser, video_id, config):
    """Process a YouTube video by ID."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    wait_before = config.get('wait_before_click', 3)
    wait_after = config.get('wait_after_click', 3)
    screenshot_dir = config.get('screenshot_directory', 'screenshots')

    # Create screenshots directory if it doesn't exist
    os.makedirs(screenshot_dir, exist_ok=True)

    try:
        browser.get(url)
        time.sleep(wait_before)

        # Click play button
        browser.find_element(By.CLASS_NAME, "ytp-play-button").click()
        time.sleep(wait_after)

        # Generate timestamp for filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{video_id}.png"
        filepath = os.path.join(screenshot_dir, filename)

        # Take screenshot
        browser.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")

    except WebDriverException as e:
        print(f"Error processing video {video_id}: {e}")

def main():
    # Load configuration
    config = load_config()

    # Setup display
    display = setup_display(config)

    try:
        # Setup browser
        browser = setup_browser(config)

        # Process each video in the config
        for video_id in config.get('video_ids', []):
            process_video(browser, video_id, config)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up
        if 'browser' in locals():
            browser.quit()
        display.stop()

if __name__ == "__main__":
    main()
