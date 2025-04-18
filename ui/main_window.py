from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt
from .ui_main import Ui_MainWindow
from .movie_list import MovieListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupMovieList()
        self.connectSignals()
        
    def setupMovieList(self):
        self.movie_list = MovieListWidget()
        self.ui.video_container.layout().addWidget(self.movie_list)
        
    def connectSignals(self):
        # Connect navigation buttons
        self.ui.nav_movie_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Movies))
        self.ui.btn_mylist_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.watch))
        
    def renderMovieList(self, movies):
        """Render the list of movies in the grid layout"""
        self.movie_list.renderMovieList(movies) 