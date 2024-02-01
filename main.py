import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MapWindow(QMainWindow):
    def __init__(self, lat, lon, scale):
        super().__init__()

        if response.status_code == 200:
            with open("map.png", "wb") as file:
                file.write(response.content)

            pixmap = QPixmap("map.png")
            label = QLabel(self)
            label.setPixmap(pixmap)
            self.setCentralWidget(label)

        else:
            label = QLabel(self)
            label.setText("Error")
            self.setCentralWidget(label)


if __name__ == "__main__":
    lat, lon, scale = 55, 37, 10
    url = f"https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z={scale}&l=map"
    response = requests.get(url)
    app = QApplication(sys.argv)
    window = MapWindow(lat, lon, scale)
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())
