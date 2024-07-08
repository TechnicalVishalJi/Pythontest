from flask import Flask
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def home():
    # Setup Selenium and ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headless mode if you don't need to see the display output
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get("https://www.google.com")
    title = driver.title
    print(title)
    driver.quit()
    return f"Title of the page is: {title}"
