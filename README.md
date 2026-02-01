# AI Web Search ChatBot

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-green?style=flat)](https://langchain.com)

A powerful web-based AI chatbot that analyzes website content and provides intelligent answers using the Gemma:2b model with RAG (Retrieval-Augmented Generation) capabilities.

## 🚀 Features

- **Web Content Analysis**: Automatically scrapes and processes website content
- **AI-Powered Q&A**: Uses Gemma:2b model for intelligent responses
- **Vector Search**: ChromaDB integration for semantic document retrieval
- **Real-time Processing**: Dynamic content loading and analysis
- **User-Friendly Interface**: Clean Streamlit web interface
- **LangSmith Integration**: Built-in tracking and monitoring

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Ollama Gemma:2b
- **Vector Database**: ChromaDB
- **Framework**: LangChain
- **Web Scraping**: BeautifulSoup4
- **Deployment**: Streamlit Cloud, Heroku

## 📋 Prerequisites

- Python 3.8 or higher
- Ollama installed with Gemma:2b model
- Git (for deployment)

## 🔧 Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd streamlit-project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Ollama**
   ```bash
   # Install Ollama (visit https://ollama.ai)
   ollama pull gemma:2b
   ```

5. **Configure environment variables**
   Create a `.env` file in the project root:
   ```env
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_project_name
   LANGCHAIN_TRACING_V2=true
   ```

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🎯 Usage

1. **Start the application** and navigate to `http://localhost:8501`
2. **Enter a website URL** in the sidebar
3. **Click "Process URL"** to analyze the content
4. **Ask questions** about the website content in the main interface
5. **Get AI-powered answers** based on the processed content

## 🚀 Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add environment variables in the Streamlit Cloud dashboard
5. Deploy with one click

### Heroku

1. **Install Heroku CLI**
2. **Login to Heroku**
   ```bash
   heroku login
   ```
3. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```
4. **Set environment variables**
   ```bash
   heroku config:set LANGCHAIN_API_KEY=your_key
   heroku config:set LANGCHAIN_PROJECT=your_project
   ```
5. **Deploy**
   ```bash
   git push heroku main
   ```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `LANGCHAIN_API_KEY` | Your LangChain API key for tracking | Yes |
| `LANGCHAIN_PROJECT` | Project name for LangSmith | Yes |
| `LANGCHAIN_TRACING_V2` | Enable LangSmith tracing | Optional |

### Model Configuration

- **Model**: Gemma:2b (via Ollama)
- **Chunk Size**: 1000 characters
- **Chunk Overlap**: 200 characters
- **Embedding Model**: Gemma:2b embeddings

## 📁 Project Structure

```
streamlit-project/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment config
├── setup.sh           # Streamlit configuration script
├── .env               # Environment variables (local)
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

- **Ollama not found**: Ensure Ollama is installed and Gemma:2b model is pulled
- **Port conflicts**: Change the port in the Streamlit command
- **Memory issues**: Reduce chunk size or use a smaller model

### Support

For issues and questions, please open an issue on GitHub or contact the maintainers.

---

**Built with ❤️ using Streamlit and LangChain**