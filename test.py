# Isolating functions and testing them out here

import os
import sys
from pathlib import Path

# Add the src directory to the module search path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from src import setup, siri, utils
from src.logger_config import setup_logger

if __name__ == "__main__":
    # Determine the current directory of the script
    project_root_folder_path = Path(os.path.dirname(os.path.abspath(__file__)))

    # Setup logger
    log_file_path = project_root_folder_path / "logs" / "test.log"
    setup_logger(log_file_path)

    # Get log file for today
    chat_log_file_path = utils.get_log_file_for_today(
        project_root_folder_path=project_root_folder_path
    )

    # Get API keys
    all_api_keys = setup.get_credentials()
    groq_api_key, google_gen_ai_api_key, openai_api_key = all_api_keys

    # Initialize Siri instance
    siri_instance = siri.Siri(
        log_file_path=chat_log_file_path,
        project_root_folder_path=project_root_folder_path,
        groq_api_key=groq_api_key,
        google_gen_ai_api_key=google_gen_ai_api_key,
        openai_api_key=openai_api_key,
    )

    # Test the transcribe_audio_to_text function
    audio_file_path = project_root_folder_path / "data" / "uploads" / "test.wav"
    if audio_file_path.exists():
        transcribed_text = siri_instance.transcribe_audio_to_text(audio_file_path)
        print(f"Transcribed Text: {transcribed_text}")
    else:
        print(f"Audio file {audio_file_path} does not exist.")

    # Test the extract_prompt function
    sample_transcribed_text = "siri, what is the weather today?"
    extracted_prompt = siri_instance.extract_prompt(sample_transcribed_text)
    print(f"Extracted Prompt: {extracted_prompt}")

    # Test the text to speech function
    siri_instance.text_to_speech("Hello world, this is a test of the text to speech function")

    # Test the generate_chat_response_with_groq function
    sample_prompt = "Tell me a joke."
    chat_response = siri_instance.generate_chat_response_with_groq(sample_prompt, None)
    print(f"Chat Response: {chat_response}")

    # Test the select_assistant_action function
    assistant_action = siri_instance.select_assistant_action(sample_prompt)
    print(f"Assistant Action: {assistant_action}")

    # Test the analyze_image_prompt function
    image_file_path = project_root_folder_path / "data" / "uploads" / "test_image.jpg"
    if image_file_path.exists():
        image_analysis_result = siri_instance.analyze_image_prompt(sample_prompt, image_file_path)
        print(f"Image Analysis Result: {image_analysis_result}")
    else:
        print(f"Image file {image_file_path} does not exist.")