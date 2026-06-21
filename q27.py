import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.citylabel = QLabel("Enter city name: ",self)
        self.cityinput = QLineEdit(self)
        self.getweatherbut = QPushButton("Get Weather",self)
        self.templabel = QLabel(self)
        self.emojilabel = QLabel()
        self.desclabel = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.citylabel)
        vbox.addWidget(self.cityinput)
        vbox.addWidget(self.getweatherbut)
        vbox.addWidget(self.templabel)
        vbox.addWidget(self.emojilabel)
        vbox.addWidget(self.desclabel)

        self.setLayout(vbox)

        self.citylabel.setAlignment(Qt.AlignCenter)
        self.cityinput.setAlignment(Qt.AlignCenter)
        self.templabel.setAlignment(Qt.AlignCenter)
        self.emojilabel.setAlignment(Qt.AlignCenter)
        self.desclabel.setAlignment(Qt.AlignCenter)

        self.citylabel.setObjectName("citylabel")
        self.cityinput.setObjectName("cityinput")
        self.getweatherbut.setObjectName("getweatherbut")
        self.templabel.setObjectName("templabel")
        self.emojilabel.setObjectName("emojilabel")
        self.desclabel.setObjectName("desclabel")

        self.setStyleSheet("""
        QLabel,QPushButton{font-family:calibri;}
        QLabel#citylabel{font-size:45px;font-style:italic;}
        QLineEdit#cityinput{font-size:42px;}
        QPushButton#getweatherbut{font-size:35px;font-weight:bold}
        QLabel#templabel{font-size:70px;}
        QLabel#emojilabel{font-size:90px;font-family:Segoe UI emoji;}
        QLabel#desclabel{font-size:50px}
        """)

        self.getweatherbut.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "4caef5194b46c1c639c64e52f7faf9f7"
        city = self.cityinput.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.disp_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.error("Bad Request\nPlease enter a valid input")
                case 401:
                    self.error("Unauthorised\nInvalid API Key")
                case 403:
                    self.error("Forbidden\nAcces denied")
                case 404:
                    self.error("Not found\nCity not found")
                case 500:
                    self.error("Internal Server Error\nPlease try again later")
                case 502:
                    self.error("Bad Gateway\nInvalid response from server")
                case 503:
                    self.error("Service Unavailable\nServer Down")
                case 504:
                    self.error("Gateway Timeout\nNo response from server")
                case _:
                    self.error(f"HTTP Error occured\n{http_error}")
        
        except requests.exceptions.ConnectionError:
            self.error("Connection error\nCheck your internet")
        except requests.exceptions.Timeout:
            self.error("Timeout error\nThe request timed out")
        except requests.exceptions.ToomanyRedirects:
            self.error("Too many redirects\nCheck your url")
        except requests.exceptions.RequestException as req_error:
            self.error(f"Request Error\n{req_error}")

                
    def error(self,message):
        self.templabel.setStyleSheet("font-size:25px;")
        self.templabel.setText(message)
    def disp_weather(self,data):
        self.templabel.setStyleSheet("font-size:70px;")
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15  
        temp_f = (temp_k * 9/5) - 459.67  

        weather_desc = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.templabel.setText(f"{temp_c:.2f}°C")  
        self.emojilabel.setText(self.get_emoji(weather_id))
        self.desclabel.setText(weather_desc) 

    @staticmethod
    def get_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

