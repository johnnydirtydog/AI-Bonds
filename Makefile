# AI Bonds Makefile
# Provides common commands for development and deployment

.PHONY: help run install clean dev test

# Default target
help:
	@echo "Available commands:"
	@echo "  make run     - Start the Streamlit application"
	@echo "  make dev     - Start the application in development mode with auto-reload"
	@echo "  make install - Install Python dependencies"
	@echo "  make clean   - Clean up temporary files and cache"
	@echo "  make test    - Run any available tests"
	@echo "  make help    - Show this help message"

# Start the Streamlit application
run:
	@echo "Starting AI Bonds application..."
	streamlit run app.py

# Start in development mode
dev:
	@echo "Starting AI Bonds in development mode..."
	streamlit run app.py --server.runOnSave true

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt

# Clean up temporary files
clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

# Run tests (placeholder - add actual test commands if tests exist)
test:
	@echo "No tests configured yet. Add test commands here when available."
	@echo "To add tests, consider using pytest or unittest."