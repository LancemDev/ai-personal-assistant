import os
import sys
import logging
from src.logger_config import setup_logger
from pathlib import Path

# Add the src directory to the module search path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from src import setup, pro, utils

"""
Main entry point for the AI llama3 pro voice assistant.

This script loads the necessary API credentials from environment variables,
initializes the pro assistant with the provided keys, and starts listening
for user input. The program will exit if any of the required API keys are
missing.

To run the application, execute this script in an environment where the
`.env` file is properly configured with the required API keys.
"""

if __name__ == "__main__":
    try:
        # Determine the current directory of the script
        project_root_folder_path = Path(os.path.dirname(os.path.abspath(__file__)))
        log_file_path = project_root_folder_path / "logs" / "main.log"
        
        # Setup logger
        setup_logger(log_file_path)
        logger = logging.getLogger(__name__)
        
        logger.info("Starting main.py")

        # Get log file for today
        chat_log_file_path = utils.get_log_file_for_today(
            project_root_folder_path=project_root_folder_path
        )
        logger.info(f"Chat log file path: {chat_log_file_path}")

        # Get API keys
        all_api_keys = setup.get_credentials()
        groq_api_key, google_gen_ai_api_key, openai_api_key = all_api_keys
        logger.info("API keys loaded successfully")

        # Initialize pro instance
        pro_instance = pro.Pro(
            log_file_path=chat_log_file_path,
            project_root_folder_path=project_root_folder_path,
            groq_api_key=groq_api_key,
            google_gen_ai_api_key=google_gen_ai_api_key,
            openai_api_key=openai_api_key,
        )
        logger.info("pro instance initialized")

        # Start listening
        pro_instance.listen()
        logger.info("pro is now listening")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)