# AI Bonds Deployment Guide

## Overview
AI Bonds can be deployed using two different approaches:

### Option 1: Streamlit App (Recommended)
- **Platform**: Render.com, Heroku, or any Python hosting service
- **Configuration**: `render.yaml`
- **Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`

### Option 2: Node.js Express Server
- **Platform**: Render.com, Heroku, Vercel, or any Node.js hosting service  
- **Configuration**: `render-nodejs.yaml`
- **Command**: `npm start`

## Deployment Instructions

### Render.com (Streamlit - Primary Option)
1. Connect your GitHub repository to Render
2. Choose "Web Service"
3. Use the following settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`
4. Set environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `STRIPE_API_KEY`: Your Stripe secret key

### Render.com (Node.js - Alternative Option)
1. Connect your GitHub repository to Render
2. Choose "Web Service"
3. Use the following settings:
   - **Environment**: Node.js
   - **Build Command**: `npm install`
   - **Start Command**: `npm start`
4. Set environment variables:
   - `NODE_ENV`: production
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `STRIPE_API_KEY`: Your Stripe secret key

### Heroku
1. Install the Heroku CLI
2. Run the following commands:
   ```bash
   heroku create your-app-name
   heroku config:set OPENAI_API_KEY=your-key-here
   heroku config:set STRIPE_API_KEY=your-stripe-key-here
   git push heroku main
   ```

## Environment Variables Required
- `OPENAI_API_KEY`: For AI agent functionality
- `STRIPE_API_KEY`: For premium features and payments
- `PORT`: Set automatically by most hosting platforms

## Health Checks
Both deployment options include health check endpoints:
- **Streamlit**: `/?health=check`
- **Node.js**: `/health`

## Files Structure
- `app.py`: Main Streamlit application
- `index.js`: Node.js Express server
- `requirements.txt`: Python dependencies
- `package.json`: Node.js dependencies
- `render.yaml`: Render.com configuration (Streamlit)
- `render-nodejs.yaml`: Render.com configuration (Node.js)
- `Procfile`: Heroku configuration
- `.gitignore`: Excludes unnecessary files from deployment

## Troubleshooting
1. **Build fails**: Check that all dependencies are listed in `requirements.txt` or `package.json`
2. **App doesn't start**: Verify environment variables are set correctly
3. **Health check fails**: Ensure the health check endpoints are accessible
4. **Static files not served**: Check that file paths are correct in the server configuration