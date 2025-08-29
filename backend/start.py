#!/usr/bin/env python3
"""
Startup script for the AI Chatbot backend server
"""
import uvicorn
import os
import sys
from pathlib import Path

# Add the backend directory to Python path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

def main():
    """Main function to start the server"""
    # Set environment variables if .env file exists
    env_file = backend_dir.parent / ".env"
    if env_file.exists():
        from dotenv import load_dotenv
        load_dotenv(env_file)

    # Get port from environment variable (for Railway deployment)
    port = int(os.getenv("PORT", 8000))
    
    # Check if we're in production
    is_production = os.getenv("RAILWAY_ENVIRONMENT") or os.getenv("VERCEL") or os.getenv("NODE_ENV") == "production"

    # Start the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=not is_production,  # Only reload in development
        reload_dirs=[str(backend_dir)] if not is_production else None,
        log_level="info"
    )

if __name__ == "__main__":
    main()
