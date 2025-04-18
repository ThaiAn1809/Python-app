from PyQt6.QtWidgets import QWidget, QGridLayout, QScrollArea, QFrame
from PyQt6.QtCore import Qt
from .movie_item import MovieItemWidget

class MovieListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        # Create a scroll area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        # Create a container widget for the grid
        self.container = QWidget()
        self.grid_layout = QGridLayout(self.container)
        self.grid_layout.setSpacing(20)
        self.grid_layout.setContentsMargins(20, 20, 20, 20)
        
        # Set the container as the scroll area widget
        self.scroll.setWidget(self.container)
        
        # Create main layout
        self.main_layout = QGridLayout(self)
        self.main_layout.addWidget(self.scroll)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
    def layout(self):
        return self.main_layout
        
    def renderMovieList(self, movies):
        # Clear existing items
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add new items
        row = 0
        col = 0
        max_cols = 4  # Number of items per row
        
        for movie in movies:
            movie_item = MovieItemWidget(
                movie_id=movie.get('id'),
                movie_name=movie.get('name'),
                image_path=movie.get('image')
            )
            self.grid_layout.addWidget(movie_item, row, col)
            
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
            
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Re-render the grid when the widget is resized
        if hasattr(self, '_current_movies'):
            self.renderMovieList(self._current_movies) 