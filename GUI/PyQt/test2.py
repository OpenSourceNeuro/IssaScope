import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
import cv2

class VideoWriterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Writer App")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Press 'Start Recording' to begin recording video.")
        self.btn_start = QPushButton("Start Recording")
        self.btn_start.clicked.connect(self.start_recording)
        self.btn_stop = QPushButton("Stop Recording")
        self.btn_stop.clicked.connect(self.stop_recording)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_stop)

        self.setLayout(layout)

        self.video_writer = None
        self.recording = False

    def start_recording(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self, "Save Video", "", "Video Files (*.avi *.mp4)", options=options)
        if filename:
            fourcc = self.select_codec()
            if fourcc:
                self.video_writer = cv2.VideoWriter(filename, fourcc, 30.0, (640, 480))
                if self.video_writer.isOpened():
                    self.label.setText("Recording video. Press 'Stop Recording' to stop.")
                    self.recording = True
                else:
                    QMessageBox.warning(self, "Error", "Failed to open video writer.")
            else:
                QMessageBox.warning(self, "Error", "Failed to select codec.")
        else:
            QMessageBox.warning(self, "Error", "Please select a file to save.")

    def stop_recording(self):
        if self.recording:
            self.video_writer.release()
            self.label.setText("Recording stopped. Press 'Start Recording' to record again.")
            self.recording = False

    def select_codec(self):
        options = ["MJPG", "DIVX", "XVID", "H264", "HEVC"]
        codec, _ = QMessageBox().getItem(self, "Select Codec", "Select video codec:", options=options)
        codec_dict = {"MJPG": cv2.VideoWriter_fourcc(*'MJPG'),
                      "DIVX": cv2.VideoWriter_fourcc(*'DIVX'),
                      "XVID": cv2.VideoWriter_fourcc(*'XVID'),
                      "H264": cv2.VideoWriter_fourcc(*'H264'),
                      "HEVC": cv2.VideoWriter_fourcc(*'HEVC')}
        return codec_dict.get(codec, None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoWriterApp()
    window.show()
    sys.exit(app.exec_())