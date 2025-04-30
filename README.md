# Resume Ranking AI  
Resume Ranking AI is a machine learning and NLP-based application that automates the process of screening and ranking resumes based on their relevance to a given job description. It is designed to help recruiters quickly identify the most suitable candidates by comparing text content extracted from resumes with a job posting using similarity scoring techniques.  

## Features  
- Parses resumes (PDF format) to extract relevant text using PDF processing libraries.  
- Converts both resumes and job descriptions into TF-IDF vectors for numerical analysis.  
- Calculates cosine similarity scores to determine how closely each resume matches the job description.  
- Ranks candidates based on similarity scores from highest to lowest.  
- Provides an interactive web-based interface using Streamlit for easy uploading and visualization.  
- Outputs ranked results in downloadable CSV format.  

## Tech Stack  
- **Language**: Python  
- **Frontend**: Streamlit (for user interaction)  
- **Backend**: Flask (for core processing logic)  
- **Libraries**: scikit-learn (TF-IDF and cosine similarity), pdfplumber or PyPDF2 (PDF parsing), pandas (data handling)  
- **Deployment**: Local with optional support for Docker or cloud deployment  

## Installation  
1. Clone the repository:  
   `git clone https://github.com/nvs0108/Resume_Ranking_AI.git && cd Resume_Ranking_AI`  
2. Install dependencies:  
   `pip install -r requirements.txt`  
3. Run the application:  
   - For backend (Flask): `python flask_app.py`  
   - For frontend (Streamlit): `streamlit run streamlit_app.py`  
4. Open your browser and navigate to `http://localhost:8501` to access the UI.  

## Usage  
1. Open the Streamlit interface in your browser.  
2. Upload multiple resumes in PDF format.  
3. Paste the job description into the provided input box.  
4. Click the "Rank Resumes" button.  
5. View the ranked list of resumes based on relevance to the job.  
6. Download the ranking results as a CSV file if needed.  

## Repository Structure  
- `flask_app.py`: Contains the logic for reading resumes, processing text, calculating similarity, and ranking.  
- `streamlit_app.py`: UI for uploading files, entering job descriptions, and displaying output.  
- `requirements.txt`: Lists Python dependencies for the project.  
- `setup.sh`: Optional script to configure and initialize the environment.  

## Potential Improvements  
- Integration of deep learning models like BERT for enhanced semantic understanding.  
- Support for additional file types (DOCX, TXT).  
- Compatibility with popular ATS (Applicant Tracking Systems).  
- Real-time analytics and feedback features for recruiters.  

## License  
This project is open-source and available under the MIT License.  

## Acknowledgments  
Thanks to the developers and maintainers of the libraries used, including scikit-learn, Streamlit, and PDF parsing tools.  
