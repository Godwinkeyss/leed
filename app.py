import os
from myapp import app


DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

if __name__ == '__main__':
   app.run(debug=True)