# Career Copilot AI: Strategic Career Engineering Platform

Career Copilot AI is an intelligent framework designed to automate resume analysis and provide data-driven career growth strategies. By leveraging Large Language Models (LLMs) and industry-specific taxonomies, it bridges the gap between candidate profiles and high-level job requirements.

## Live Experience
The application is deployed and ready for live testing. You can access the professional dashboard and analyze your resume here:
**[Launch Career Copilot AI](https://airesumeanalyzer-jzqsghqfecqgvuaud3tnvf.streamlit.app/)**

---

## Key Features

### 1. Multi-Industry Skill Mapping
The engine features a sophisticated role catalog covering Finance, Technology, Healthcare, Engineering, and Management. It executes a hybrid scoring algorithm that evaluates both "Must-have" and "Nice-to-have" competencies.

### 2. Privacy-Centric Architecture
Data security is integrated at the core. The system utilizes a PII (Personally Identifiable Information) Redaction layer to mask sensitive identifiers like emails and phone numbers before any AI processing occurs.

### 3. AI-Driven Growth Roadmap
Using OpenAI's GPT models, the platform identifies specific skill gaps and constructs a personalized 4-week development plan. This includes technical milestones and hands-on project suggestions tailored to the candidate's target role.

### 4. Experience Optimization (STAR Method)
The platform features an AI assistant that re-interprets existing resume bullet points using the STAR (Situation, Task, Action, Result) methodology, transforming static job descriptions into impact-oriented achievements.

## Technical Implementation

### Tech Stack
- **Interface:** Streamlit with custom CSS and dark mode integration.
- **NLP Processing:** SpaCy and dedicated parsers for PDF/DOCX.
- **AI Integration:** OpenAI GPT API for contextual analysis and generation.
- **Data Layer:** JSON-based hierarchical role taxonomy.

### Setup for Developers
For those who wish to run the engine locally:
1. Clone the repository and install dependencies via `pip install -r requirements.txt`.
2. Configure your OpenAI API Key in a `.env` file.
3. Launch the dashboard using `streamlit run app/Home.py`.

---
*Created by Hüseyin to revolutionize career transitions through the power of Artificial Intelligence.*
