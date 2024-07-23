from model.db_config import config_connection 
from dotenv import load_dotenv
import os
import cx_Oracle


# Load environment variables from .env file
load_dotenv()

# Get directories from environment variables
dir = os.getenv('PDF_PATH')


class Database:
    def __init__(self, user, password, dsn):
        self.connection = cx_Oracle.connect(user, password, dsn)
        self.cursor = self.connection.cursor()

    def create(self, languages_abr, languages):
        self.cursor.execute("INSERT INTO IDIOMA.languages (languages_abr, languages) VALUES (:languages_abr, :languages)", [languages_abr, languages])
        self.connection.commit()

    def read(self):
        self.cursor.execute("SELECT * FROM IDIOMA.languages")
        return self.cursor.fetchall()

    def update(self, id_languages, languages_abr, languages):
        self.cursor.execute("UPDATE IDIOMA.languages SET languages_abr = :language_abr, languages = :languages WHERE id_languages = :id", [languages_abr, languages, id_languages])
        self.connection.commit()

    def delete(self, id_languages):
        self.cursor.execute("DELETE FROM IDIOMA.languages WHERE id_languages = :id", [id_languages])
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
