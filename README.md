
# PDF Q&A Chatbot 🤖

This is a PDF Q&A Chatbot built using Streamlit and Hugging Face's Transformers. The application allows users to upload a PDF document, extract text from it, and interact with a chatbot that can answer questions related to the content of the PDF using a BERT-based question-answering model.

## Features

- **PDF Upload**: Upload any PDF file to extract its text content.
- **Question Answering**: Ask questions about the PDF content and receive answers based on the BERT-based model.
- **Interactive Interface**: A user-friendly interface powered by Streamlit.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

2. **Upload a PDF File**

   - Use the file uploader in the sidebar to upload a PDF document.

3. **Ask Questions**

   - After uploading the PDF, type your questions in the text input box to receive answers based on the document's content.

## Dependencies

- `streamlit`: Used for creating the web application interface.
- `PyPDF2`: Used for extracting text from PDF files.
- `transformers`: Provides the pre-trained BERT model for question answering.
- `torch`: Required by the transformers library for model inference.

## Notes

- Make sure to set up your Hugging Face API key if you plan to use private models or access additional Hugging Face features. Update the `HF_HOME_API_KEY` environment variable with your API key in the code.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Acknowledgments

- Thanks to [Hugging Face](https://huggingface.co/) for providing the transformers library and pre-trained models.
- Built with [Streamlit](https://streamlit.io/) for a seamless web app experience.


Explanation of Sections:

- **Features**: Provides a summary of what the app does.
- **Installation**: Includes instructions for setting up the project locally, including cloning the repository and installing dependencies.
- **Usage**: Details how to run the app and interact with it.
- **Dependencies**: Lists the major libraries used in the project.
- **Notes**: Includes information about the API key and any specific configuration.
- **Contributing**: Invites others to contribute to the project.
- **License**: Mentions the project's license.
- **Acknowledgments**: Credits the tools and libraries that make the project possible.
