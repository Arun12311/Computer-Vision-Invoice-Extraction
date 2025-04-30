# Computer Vision Invoice Extraction

This project is a Streamlit-based web application that uses Google's Gemini AI model to analyze text input and an uploaded image. The application generates a response based on the provided input and image.

## Features

- Upload an image (JPG or PNG format).
- Input text to provide context for the image.
- Generate a response using Google's Gemini AI model.
- Display the uploaded image and the AI-generated response.

## Requirements

To run this project, you need the following dependencies:

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`):
  - `streamlit`
  - `google-generativeai`
  - `python-dotenv`

## Installation

1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd COMPUTER_VISION_INVOICE_EXTRACTION
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project directory and add your Google API key:
   ```plaintext
   GOOGLE_API_KEY="your_google_api_key_here"
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run invoice.py
   ```
2. Open the application in your web browser (usually at `http://localhost:8501`).
3. Enter text in the input field and upload an image.
4. Click the "Tell me about image" button to generate a response.

## File Structure

- `invoice.py`: The main application file containing the Streamlit app logic.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `.env`: Stores the Google API key (not included in the repository for security reasons).

## How It Works

1. The application uses the `dotenv` library to load the Google API key from the `.env` file.
2. The `google-generativeai` library is configured with the API key to interact with the Gemini AI model.
3. Users can input text and upload an image through the Streamlit interface.
4. The `get_gemini_response` function sends the input text and image to the Gemini AI model and processes the response.
5. The AI-generated response is displayed on the web interface.

## Notes

- Ensure that your Google API key has the necessary permissions to access the Gemini AI model.
- The application currently supports image formats JPG and PNG.

## License

This project is for educational purposes. Please ensure compliance with Google's API usage policies when using this application.
