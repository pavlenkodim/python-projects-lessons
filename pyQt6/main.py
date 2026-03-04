import re
import sys
from PySide6 import QtCore, QtWidgets

from docx import Document
from collections import Counter

# work
class WordAnalysis():
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.text = ""

    def read_document(self):
        doc = Document(self.file_path)
        self.text = "\n".join([p.text for p in doc.paragraphs])

    def get_all_words(self):
        return re.findall(r"\b\w{2,}\b", str(self.text.lower())) if self.text else []

    def get_common_word(self):
        words = self.get_all_words()

        if not words:
            return None

        counter = Counter(words)
        most_common = counter.most_common(1)

        return most_common[0] if most_common else None


# ui
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.file_name = ''

        self.button = QtWidgets.QPushButton("Select file")
        self.text = QtWidgets.QLabel("I count most common word in Word file \n Please select file", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.open_file_dialog)

    @QtCore.Slot()
    def open_file_dialog(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(self,
                                                               "Select file",
                                                               "C:/Users/dmitry/OneDrive/Документы",
                                                               "Word Files (*.doc *.docx)")

        if self.file_name:
            analysis = WordAnalysis(self.file_name[0])
            analysis.read_document()
            result = analysis.get_common_word()

            self.text.setText(f"{result[0]} - {result[1]}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())