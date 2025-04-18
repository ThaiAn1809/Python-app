from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QPixmap

class MovieItemWidget(QWidget):
    signal_detail_movie = pyqtSignal(int)
    
    def __init__(self, movie_id, name, image_path):
        super().__init__()
        self.movie_id = movie_id
        self.setupUi(name, image_path)
        
    def setupUi(self, name, image_path):
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        
        # Image label
        self.imageLabel = QLabel()
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(170, 221, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.imageLabel.setPixmap(scaled_pixmap)
        self.imageLabel.setStyleSheet("""
            QLabel {
                border: 1px solid rgba(255, 255, 255, 0.8);
                border-radius: 15px;
                background-color: rgb(0, 0, 0);
            }
        """)
        layout.addWidget(self.imageLabel)
        
        # Buttons layout
        buttonLayout = QHBoxLayout()
        buttonLayout.setSpacing(5)
        
        # Play button
        self.playButton = QPushButton("Play")
        self.playButton.setStyleSheet("""
            QPushButton {
                border: 1px solid rgba(255, 255, 255, 0.8);
                border-radius: 5px;
                background-color: rgb(0, 0, 0);
                color: white;
                font-family: Geist;
                font-weight: bold;
                padding: 5px;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        
        # Info button
        self.infoButton = QPushButton("Info")
        self.infoButton.setStyleSheet("""
            QPushButton {
                border: 1px solid rgba(255, 255, 255, 0.8);
                border-radius: 5px;
                background-color: rgb(0, 0, 0);
                color: white;
                font-family: Geist;
                font-weight: bold;
                padding: 5px;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        
        # Add button
        self.addButton = QPushButton("Add")
        self.addButton.setStyleSheet("""
            QPushButton {
                border: 1px solid rgba(255, 255, 255, 0.8);
                border-radius: 5px;
                background-color: rgb(0, 0, 0);
                color: white;
                font-family: Geist;
                font-weight: bold;
                padding: 5px;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        
        # Add buttons to layout
        buttonLayout.addWidget(self.playButton)
        buttonLayout.addWidget(self.infoButton)
        buttonLayout.addWidget(self.addButton)
        
        # Add button layout to main layout
        layout.addLayout(buttonLayout)
        
        # Set the main layout
        self.setLayout(layout)
        
        # Connect signals
        self.infoButton.clicked.connect(self.show_detail)
        
    def show_detail(self):
        self.signal_detail_movie.emit(self.movie_id) 