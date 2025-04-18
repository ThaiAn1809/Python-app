from PyQt6.QtWidgets import *  # Import specific widgets you need
from PyQt6.QtGui import *  # Import specific GUI elements you need
from PyQt6 import uic
import sys
import database
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *
from PyQt6.QtMultimediaWidgets import *

class Alert(QMessageBox):
    def error_message(self, message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle('Error')
        self.exec()
        
    def success_message(self, message):
        self.setIcon(QMessageBox.Icon.Information)
        self.setText(message)
        self.setWindowTitle('Success')
        self.exec()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/login.ui',self)
        
        self.email_input = self.findChild(QLineEdit, 'email_input')
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        self.btn_register = self.findChild(QPushButton, 'register_btn')
        self.btn_eye = self.findChild(QPushButton, 'eye_btn')
        
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_eye.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_eye))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
        
    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        
        if email == '':
            msg = Alert()
            self.email_input.setFocus()
            return
        
        if password == '':
            msg = Alert()
            self.password_input.setFocus()
            return
        
        user = database.find_user_by_email_and_password(email,password)
        if user:
            msg = Alert()
            self.show_main(user["id"])
            msg.success_message('Login successful')
            
        else:
            msg = Alert()
            msg.error_message('invalid email or password')
            
    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()
        
    def show_main(self, user_id):
        self.main = Main(user_id)
        self.main.show()
        self.close()
        
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/register.ui',self)
        
        self.email_input = self.findChild(QLineEdit, 'email_input')
        self.name_input = self.findChild(QLineEdit, 'name_input')
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.confirm_password_input = self.findChild(QLineEdit, 'confirm_password_input')
        
        self.btn_register = self.findChild(QPushButton, 'register_btn')
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        self.btn_eye1 = self.findChild(QPushButton, 'eye_btn1')
        self.btn_eye2 = self.findChild(QPushButton, 'eye_btn2')
        
        self.btn_eye1.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_eye1))
        self.btn_eye2.clicked.connect(lambda: self.hiddenOrShow(self.confirm_password_input, self.btn_eye2))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
        
    def register(self):
        email = self.email_input.text()
        name = self.name_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        
        if email == '':
            msg = Alert()
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        if name == '':
            msg = Alert()
            msg.error_message('Please enter name')
            self.name_input.setFocus()
            return
        
        if password == '':
            msg = Alert()
            msg.error_message('Please enter password')
            self.password_input.setFocus()
            return
        
        if password != confirm_password:
            msg = Alert()
            msg.error_message('Password and confirm password does not match')
            self.confirm_password_input.setFocus()
            return
        
        user = database.find_user_by_email(email)
        if user:
            msg = Alert()
            msg.error_message('Email already exists')
        else:
            database.create_user(email, email, password)
            msg = Alert()
            msg.success_message('Registration successful')
            self.close()
            
    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        
            
class Main(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/main.ui',self)
        self.user_id = user_id
        self.user = database.find_user_by_id(user_id)

        self.nav_home_btn = self.findChild(QPushButton,'nav_home_btn')
        self.nav_movie_btn = self.findChild(QPushButton,'nav_movie_btn')
        self.btn_mylist_btn = self.findChild(QPushButton,'btn_mylist_btn')
        self.stackedWidget = self.findChild(QStackedWidget,'stackedWidget')
        self.btn_avatar = self.findChild(QPushButton, 'btn_avatar')
        self.video_container = self.findChild(QWidget, 'video_container')
        self.favorite_container = self.findChild(QWidget, 'favorite_container')
        self.btn_play_video = self.findChild(QPushButton, 'btn_play_video')
        
        # Setup UI and load initial data
        self.setupUI()
        self.loadMovies()
        self.load_user_info()
        
        # Connect signals
        self.nav_home_btn.clicked.connect(lambda: self.navigateScreen(4))
        self.nav_movie_btn.clicked.connect(lambda: self.navigateScreen(0))
        self.btn_mylist_btn.clicked.connect(self.showFavorites)
        self.btn_avatar.clicked.connect(self.update_avatar)
        self.btn_play_video.clicked.connect(self.loadVideo)
        
    
    def load_user_info(self):
        self.btn_avatar = self.findChild(QPushButton,'btn_avatar')
        self.txt_name = self.findChild(QLineEdit,'txt_name')
        self.txt_email = self.findChild(QLineEdit,'txt_email')
        self.d_dob = self.findChild(QDateEdit,'d_dob')
        self.cb_gender = self.findChild(QComboBox,'cb_gender')
        self.btn_update_info = self.findChild(QPushButton,'btn_update_info')
        self.btn_update_info.clicked.connect(self.update_info)


        self.txt_name.setText(self.user["name"])
        self.txt_email.setText(self.user["email"])
        self.txt_email.setReadOnly(True)
        self.d_dob.setDate(QDate.fromString(self.user["birthday"], "dd/MM/yyyy"))
        self.cb_gender.setCurrentText(self.user["gender"])
        self.btn_avatar.setIcon(QIcon(self.user["avatar"]))
    
    def update_info(self):
        name = self.txt_name.text()
        dob = self.d_dob.date().toString("dd/MM/yyyy")
        gender = self.cb_gender.currentText()
        database.update_user(self.user_id, name, dob, gender)
        msg = Alert()
        msg.success_message("Update info success")
        self.load_user_info() 
    
    def update_avatar(self):
        file,_ = QFileDialog.getOpenFileName(self,"Select Image","","Image Files(*.png *.jpg *jpeg *.bmp)")
        if file:
            self.user["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            database.update_user_avatar(self.user_id, file)

    def setupUI(self):
        # Setup movie container
        self.movieList = QScrollArea()
        self.movieList.setStyleSheet("""
            QScrollArea {
                background-color: black;
                border: none;
            }
            QScrollBar:vertical {
                border: none;
                background: rgb(45, 45, 45);
                width: 10px;
                margin: 0;
            }
            QScrollBar::handle:vertical {
                background: rgb(80, 80, 80);
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        
        self.movieItem = QWidget()
        self.gridLayout = QGridLayout(self.movieItem)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)

        self.movieItem.setLayout(self.gridLayout)
        self.movieList.setWidget(self.movieItem)
        self.movieList.setWidgetResizable(True)
        
        # Add movie list to video container
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.movieList)
        self.video_container.setLayout(containerLayout)
        
        # Setup favorite container with scroll area
        self.favoriteList = QScrollArea()
        self.favoriteList.setStyleSheet("""
            QScrollArea {
                background-color: black;
                border: none;
            }
            QScrollBar:vertical {
                border: none;
                background: rgb(45, 45, 45);
                width: 10px;
                margin: 0;
            }
            QScrollBar::handle:vertical {
                background: rgb(80, 80, 80);
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        
        self.favoriteItem = QWidget()
        self.favoriteLayout = QGridLayout(self.favoriteItem)
        self.favoriteLayout.setContentsMargins(10, 10, 10, 10)
        self.favoriteLayout.setSpacing(10)
        
        self.favoriteItem.setLayout(self.favoriteLayout)
        self.favoriteList.setWidget(self.favoriteItem)
        self.favoriteList.setWidgetResizable(True)
        
        # Add favorite list to favorite container
        favoriteContainerLayout = QVBoxLayout()
        favoriteContainerLayout.addWidget(self.favoriteList)
        self.favorite_container.setLayout(favoriteContainerLayout)
        
        self.txt_search = self.findChild(QLineEdit, 'txt_search')
        self.btn_search = self.findChild(QPushButton, 'btn_search')
        self.btn_search.clicked.connect(self.search_movie)
        
        # Setup media player components
        self.setupMediaPlayer()
    
    def setupMediaPlayer(self):
        # Setup media player
        self.lbl_title = self.findChild(QLabel, 'videoName')
        self.volumeBtn = self.findChild(QPushButton, 'volumeBtn')
        self.timeLabel = self.findChild(QLabel, 'timeLabel')
        self.durationBar = self.findChild(QSlider, 'durationBar')
        self.volumeBar = self.findChild(QSlider, 'volumeBar')
        self.videoName = self.findChild(QLabel, 'videoName')
        self.playBtn = self.findChild(QPushButton, 'playBtn')
        
        # Load icons
        self.playIcon = QIcon("img/play-solid.svg")
        self.pauseIcon = QIcon("img/pause-solid.svg")
        self.volumeHighIcon = QIcon("img/volume-high-solid.svg")
        self.volumeLowIcon = QIcon("img/volume-low-solid.svg")
        self.volumeOffIcon = QIcon("img/volume-off-solid.svg")
        
        # Setup video player buttons
        self.playBtn.setIcon(self.playIcon)
        self.volumeBtn.setIcon(self.volumeHighIcon)
        
        # Setup volume control
        self.current_volume = 50
        self.volumeBar.setValue(self.current_volume)
        self.volumeBar.setRange(0, 100)
        self.volumeBar.setValue(50)
        
        # Connect signals
        self.playBtn.clicked.connect(self.play)
        self.volumeBtn.clicked.connect(self.toggleMute)
        
        # Setup video widget
        placeholder = self.findChild(QWidget, 'videoWidget')
        self.videoWidget = QVideoWidget()
        self.videoWidget.setGeometry(placeholder.geometry())
        self.videoWidget.setParent(placeholder.parentWidget())
        placeholder.hide()
        
        # Setup media player
        self.mediaPlayer = QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.audioOutput = QAudioOutput(self)
        self.mediaPlayer.setAudioOutput(self.audioOutput)

    def loadMovies(self):
        # Get all movies from database
        movies = database.get_all_videos()
        if movies:
            self.renderMovieList(movies)
        
    def renderMovieList(self, movie_list: list):
        # Clear previous search results
        for i in reversed(range(self.gridLayout.count())):
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            if widgetToRemove:
                self.gridLayout.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)
            
        row = 0
        column = 0
        for movie in movie_list:
            itemWidget = MovieItemWidget(
                movie["id"], 
                movie["title"], 
                movie["banner"],  
                movie["video_path"],  
                movie.get("description", "")
            )
            itemWidget.set_user_id(self.user_id)  # Set user_id for the widget
            itemWidget.signal_detail_movie.connect(self.catch_detail_movie)
            itemWidget.signal_play_movie.connect(self.catch_play_movie)
            itemWidget.signal_favorite_changed.connect(self.on_favorite_changed)  # Connect new signal
            self.gridLayout.addWidget(itemWidget, row, column)
            column += 1
            if column == 3:
                row += 1
                column = 0
    
    def search_movie(self):
        name = self.txt_search.text()
        movie_list = database.get_video_by_name(name)
        self.renderMovieList(movie_list)

    def detail_movie(self, movie_id):
        movie = database.get_video_by_id(movie_id)
        if not movie:
            return
            
        # Find all the label widgets
        self.lbl_name = self.findChild(QLabel, "lbl_detail_name")
        self.lbl_director = self.findChild(QLabel, "lbl_detail_director")
        self.lbl_release_date = self.findChild(QLabel, "lbl_detail_release_date")
        self.lbl_genre = self.findChild(QLabel, "lbl_detail_genre")
        self.lbl_description = self.findChild(QLabel, "lbl_detail_description")
        self.lbl_rating = self.findChild(QLabel, "lbl_detail_rating")
        self.lbl_duration = self.findChild(QLabel, "lbl_detail_duration")
        self.lbl_age_rating = self.findChild(QLabel, "lbl_detail_age_rating")
        self.lbl_main_actor = self.findChild(QLabel, "lbl_detail_main_actor")
        self.lbl_image = self.findChild(QLabel, "lbl_detail_image")
        
        # Set the text for each label
        self.lbl_name.setText(movie["title"])
        self.lbl_director.setText(f"Director: {movie.get('director', 'N/A')}")
        self.lbl_release_date.setText(f"Release Date: {movie.get('release_date', 'N/A')}")
        self.lbl_genre.setText(f"Genre: {movie.get('genre', 'N/A')}")
        self.lbl_rating.setText(f"Rating: {movie.get('rating', 'N/A')}")
        self.lbl_duration.setText(f"Duration: {movie.get('duration', 'N/A')}")
        self.lbl_age_rating.setText(f"Age Rating: {movie.get('age_rating', 'N/A')}")
        self.lbl_main_actor.setText(f"Main Actor: {movie.get('main_actor', 'N/A')}")
        
        # Set the banner image
        if movie.get('banner'):
            self.lbl_image.setPixmap(QPixmap(movie["banner"]))
        
        # Format and set the description with word wrapping
        description = movie.get("description", "No description available")
        split_description = description.split(" ")
        description = "\n".join([" ".join(split_description[i:i+10]) for i in range(0, len(split_description), 10)])
        self.lbl_description.setText(f"Description: {description}")
        
        # Find and setup favorite button
        self.btn_favorite = self.findChild(QPushButton, "btn_favorite")
        if self.btn_favorite:
            is_fav = database.is_favorite(self.user_id, movie_id)
            icon = QIcon("img/heart-solid.svg" if is_fav else "img/heart-regular.svg")
            self.btn_favorite.setIcon(icon)
            self.btn_favorite.clicked.connect(lambda: self.toggle_favorite(movie_id))
        
        # Switch to detail page
        self.stackedWidget.setCurrentIndex(1)
        
    def toggle_favorite(self, movie_id):
        is_fav = database.is_favorite(self.user_id, movie_id)
        if is_fav:
            database.remove_from_favorites(self.user_id, movie_id)
            self.btn_favorite.setIcon(QIcon("img/heart-regular.svg"))
        else:
            database.add_to_favorites(self.user_id, movie_id)
            self.btn_favorite.setIcon(QIcon("img/heart-solid.svg"))
        
    def loadVideo(self):
        if self.movie_id is None:
            return
        try:
            movie = database.get_video_by_id(self.movie_id)
            self.mediaPlayer.setSource(QUrl.fromLocalFile(movie["video_path"]))
            self.mediaPlayer.play()
            self.lbl_title.setText(movie["title"])
            self.durationBar.sliderMoved.connect(self.setPosition)
            self.volumeBar.sliderMoved.connect(self.setVolume)
            self.mediaPlayer.playbackStateChanged.connect(self.mediaStateChanged)
            self.mediaPlayer.positionChanged.connect(self.positionChanged)
            self.mediaPlayer.durationChanged.connect(self.durationChanged)
            self.mediaPlayer.errorOccurred.connect(self.handleError)
            self.stackedWidget.setCurrentIndex(3)
        except Exception as e:
            print(f"Error loading video: {e}")
        
    def mediaStateChanged(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.playBtn.setIcon(self.pauseIcon)
        else:
            self.playBtn.setIcon(self.playIcon)

    def positionChanged(self, position):
        self.durationBar.setValue(position)
        current_time = self.formatTime(position)
        total_time = self.formatTime(self.mediaPlayer.duration())
        self.timeLabel.setText(f"{current_time}/{total_time}")
        
    def durationChanged(self):
        self.durationBar.setRange(0, self.mediaPlayer.duration())
    
    def handleError(self):
        self.playBtn.setEnabled(False)
        error_message = self.mediaPlayer.errorString()
        self.playBtn.setText(f"Error: {error_message}")
        print(f"Media Player Error: {error_message}")
        
    def play(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
        
    def setVolume(self, volume):
        volume = volume / 100.0
        self.audioOutput.setVolume(volume)
        if volume == 0.0:
            self.volumeBtn.setIcon(self.volumeOffIcon)
        elif volume < 0.5:
            self.audioOutput.setMuted(False)
            self.volumeBtn.setIcon(self.volumeLowIcon)
        else:
            self.volumeBtn.setIcon(self.volumeHighIcon)
            self.audioOutput.setMuted(False)
    
    def toggleMute(self):
        if self.audioOutput.isMuted():
            self.audioOutput.setMuted(False)
            if self.current_volume >= 50:
                self.volumeBtn.setIcon(self.volumeHighIcon)
            elif self.current_volume < 50:
                self.volumeBtn.setIcon(self.volumeLowIcon)
            else:
                self.volumeBtn.setIcon(self.volumeOffIcon)
            self.volumeBar.setValue(self.current_volume)
        else:
            self.audioOutput.setMuted(True)
            self.volumeBtn.setIcon(self.volumeOffIcon)
            self.current_volume = self.volumeBar.value()
            self.volumeBar.setValue(0)
    
    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def formatTime(self, milliseconds):
        total_seconds = milliseconds // 1000
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def catch_play_movie(self, movie_id):
        self.movie_id = movie_id
        self.loadVideo()

    def catch_detail_movie(self, movie_id):
        self.movie_id = movie_id
        self.detail_movie(self.movie_id)
        self.stackedWidget.setCurrentIndex(1)
                
    def navigateScreen(self, page:int):
        self.stackedWidget.setCurrentIndex(page)

    def showFavorites(self):
        # Get favorite movies
        favorite_movies = database.get_user_favorites(self.user_id)
        
        # Clear previous items
        for i in reversed(range(self.favoriteLayout.count())):
            widgetToRemove = self.favoriteLayout.itemAt(i).widget()
            if widgetToRemove:
                self.favoriteLayout.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)
                
        if not favorite_movies:
            # Show empty message
            label = QLabel("You haven't added any titles to your list yet.")
            label.setStyleSheet("color: white; font-family: Geist; font-size: 16px;")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.favoriteLayout.addWidget(label)
        else:
            # Add movies to grid
            row = 0
            column = 0
            for movie in favorite_movies:
                itemWidget = MovieItemWidget(
                    movie["id"], 
                    movie["title"], 
                    movie["banner"],  
                    movie["video_path"],  
                    movie.get("description", "")
                )
                itemWidget.set_user_id(self.user_id)  # Set user_id for the widget
                itemWidget.signal_detail_movie.connect(self.catch_detail_movie)
                itemWidget.signal_play_movie.connect(self.catch_play_movie)
                itemWidget.signal_favorite_changed.connect(self.on_favorite_changed)  # Connect new signal
                self.favoriteLayout.addWidget(itemWidget, row, column)
                column += 1
                if column == 3:
                    row += 1
                    column = 0
        
        # Switch to favorites page
        self.stackedWidget.setCurrentIndex(2)
        
    def on_favorite_changed(self):
        # If we're on the favorites page, refresh it
        if self.stackedWidget.currentIndex() == 2:
            self.showFavorites()

class MovieItemWidget(QWidget):
    signal_detail_movie = pyqtSignal(int)
    signal_play_movie = pyqtSignal(int)
    signal_favorite_changed = pyqtSignal()  # New signal for favorite changes
    
    def __init__(self, movie_id, title, banner_path, video_path, description):
        super().__init__()
        self.movie_id = movie_id
        self.user_id = 1  # We'll get this from Main class
        
        # Load UI
        uic.loadUi('ui/movie_item.ui', self)
        
        # Set data
        self.titleLabel.setText(title)
        
        # Set banner
        pixmap = QPixmap(banner_path)
        self.bannerLabel.setPixmap(pixmap)
        
        # Connect signals
        self.infoButton.clicked.connect(self.show_detail)
        self.playButton.clicked.connect(self.play_movie)
        self.btn_favorite.clicked.connect(self.toggle_favorite)
        
        # Set favorite icon
        self.update_favorite_icon()
        
    def set_user_id(self, user_id):
        self.user_id = user_id
        self.update_favorite_icon()
        
    def update_favorite_icon(self):
        is_fav = database.is_favorite(self.user_id, self.movie_id)
        icon = QIcon("img/heart-solid.svg" if is_fav else "img/heart-regular.svg")
        self.btn_favorite.setIcon(icon)
        
    def show_detail(self):
        self.signal_detail_movie.emit(self.movie_id)
        
    def play_movie(self):
        self.signal_play_movie.emit(self.movie_id)
        
    def toggle_favorite(self):
        is_fav = database.is_favorite(self.user_id, self.movie_id)
        if is_fav:
            database.remove_from_favorites(self.user_id, self.movie_id)
        else:
            database.add_to_favorites(self.user_id, self.movie_id)
        self.update_favorite_icon()
        self.signal_favorite_changed.emit()  # Emit signal when favorite status changes

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # login = Login()
    # login.show()
    
    login = Main(1)
    login.show()
    sys.exit(app.exec())    
