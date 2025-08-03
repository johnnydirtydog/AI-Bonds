# 💖 AI Bonds: The Ultimate AI Dating Sim

An interactive AI-powered dating simulation application that allows users to create, customize, and match AI agents with unique personalities.

## 🚀 Quick Deploy

### Deploy to Render.com (Recommended)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

Use the `render.yaml` configuration file for automatic deployment.

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## 🛠️ Local Development

### Prerequisites
- Python 3.12+
- Node.js 20+
- npm or yarn

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnnydirtydog/AI-Bonds.git
   cd AI-Bonds
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Running the Application

**Option 1: Streamlit App (Recommended)**
```bash
streamlit run app.py
```

**Option 2: Node.js Server**
```bash
npm start
```

## 📋 Features

- 🤖 **AI Agent Creation**: Design custom AI personalities
- 💕 **Smart Matching**: Advanced compatibility algorithms  
- 💎 **Premium Features**: Enhanced AI capabilities with Stripe integration
- 🎨 **Modern UI**: Responsive design with dark mode support
- 🔧 **Easy Deploy**: Ready for Render.com, Heroku, and other platforms

## 🌐 Deployment Options

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions including:
- Render.com (Streamlit & Node.js)
- Heroku
- Environment variable setup
- Health check configuration

## 🔧 Configuration

### Required Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key for AI functionality
- `STRIPE_API_KEY`: Stripe secret key for premium features

### Optional Environment Variables
- `PORT`: Server port (auto-set by hosting platforms)
- `NODE_ENV`: Node.js environment (production/development)

## 📁 Project Structure

```
AI-Bonds/
├── app.py                 # Streamlit application
├── index.js              # Node.js Express server
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
├── render.yaml          # Render.com config (Streamlit)
├── render-nodejs.yaml   # Render.com config (Node.js)
├── Procfile             # Heroku configuration
├── DEPLOYMENT.md        # Detailed deployment guide
└── .github/workflows/   # CI/CD configuration
```

## 🧪 Testing

The project includes automated testing via GitHub Actions:
- Python/Streamlit application testing
- Node.js server testing
- Health check validation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if needed
5. Submit a pull request

---

**Ready to deploy?** Check out our [deployment guide](DEPLOYMENT.md) for step-by-step instructions! 🚀