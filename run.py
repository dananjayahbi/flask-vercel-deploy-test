# run.py

from app import create_app

app = create_app()

# Export the app for Vercel
app = app  # This is necessary for Vercel to pick up the app

if __name__ == "__main__":
    app.run(debug=True)
