<<<<<<< HEAD
# AI_ResumeAnalyzer
=======
# Career Copilot AI: Multi-Industry Career Optimization and Analysis Engine

Career Copilot AI is an end-to-end career engineering platform designed to analyze professional resumes against diverse industry dynamics, execute data-driven scoring, and provide personalized growth roadmaps through Large Language Model (LLM) integration.

## Project Vision
Traditional Applicant Tracking Systems (ATS) often focus solely on keyword matching. Career Copilot AI transcends this by anonymizing candidate data, cross-referencing it with industry-specific taxonomies, and delivering qualitative enhancement suggestions powered by advanced generative AI.

## Core Functional Modules

### 1. Dynamic Role Taxonomy and Matching Engine
The system features an extensive library covering dozens of sub-roles across sectors such as Finance, Healthcare, Engineering, Management, and Technology. It utilizes a hybrid scoring algorithm based on pre-defined critical (Must-have) and complementary (Nice-to-have) skill sets.

### 2. Privacy and PII Redaction
To ensure user data security, all resume content undergoes PII (Personally Identifiable Information) redaction before being transmitted to AI models. Sensitive identifiers, including email addresses and phone numbers, are automatically masked.

### 3. AI-Driven Strategic Development Roadmap
Leveraging OpenAI's models, the system identifies specific "Skill Gaps" and constructs a 4-week, application-oriented development plan. This roadmap includes both theoretical milestones and tangible project suggestions suitable for portfolio platforms like GitHub.

### 4. Content Optimization via STAR Methodology
Existing candidate experiences are re-interpreted using the industry-standard STAR (Situation, Task, Action, Result) technique. This module enables candidates to transform static job descriptions into impact-oriented, metric-driven achievements.

## Technical Architecture



### Layered Infrastructure
- **Interface Layer:** Modernized UI developed with the Streamlit framework, utilizing custom CSS configurations for enhanced user experience.
- **Analysis Layer:** NLP engine based on SpaCy, coupled with a parsing layer capable of processing complex file formats including PDF and DOCX.
- **Intelligence Layer:** Contextual analysis and generation engine powered by OpenAI GPT API integration.
- **Data Layer:** JSON-based role cataloging and hierarchical skill mapping system.

## Installation and Configuration

1. Clone the repository:
   git clone https://github.com/Huseyinvk/AI_ResumeAnalyzer.git
   cd AI_ResumeAnalyzer

2. Install dependencies:
   pip install -r requirements.txt

3. Environment Setup:
   Create a .env file in the root directory and add your OpenAI API key:
   OPENAI_API_KEY=your_api_key_here

4. Launch the application:
   streamlit run app/Home.py

## License
This project is released under the MIT License. It is available for both commercial and personal use, provided that privacy protocols are maintained during development cycles.
>>>>>>> 242da00 (feat: complete professional AI career copilot architecture)
