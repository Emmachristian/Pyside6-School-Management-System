from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PySide6 import QtCharts

class PieChartDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pie Chart Demo")
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.chart_view = QtCharts.QChartView()
        self.chart = QtCharts.QChart()

        self.label_boys = QLabel("Number of Boys:")
        self.label_girls = QLabel("Number of Girls:")
        self.edit_boys = QLineEdit()
        self.edit_girls = QLineEdit()

        self.button_update = QPushButton("Update Chart")
        self.button_update.clicked.connect(self.update_chart)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_boys)
        layout.addWidget(self.edit_boys)
        layout.addWidget(self.label_girls)
        layout.addWidget(self.edit_girls)
        layout.addWidget(self.button_update)
        layout.addWidget(self.chart_view)
        self.central_widget.setLayout(layout)

        # Initialize pie series
        self.pie_series = QtCharts.QPieSeries()
        self.pie_series.setLabelsVisible(True)
        self.pie_series.setLabelsPosition(QtCharts.QPieSlice.LabelOutside)

        # Add slices for boys and girls
        self.slice_boys = QtCharts.QPieSlice("Boys", 0)
        self.slice_girls = QtCharts.QPieSlice("Girls", 0)
        self.pie_series.append(self.slice_boys)
        self.pie_series.append(self.slice_girls)

        # Add pie series to chart
        self.chart.addSeries(self.pie_series)
        self.chart.setTitle("Gender Distribution")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view.setChart(self.chart)

    def update_chart(self):
        try:
            num_boys = int(self.edit_boys.text())
            num_girls = int(self.edit_girls.text())

            # Update slice values
            total_students = num_boys + num_girls
            if total_students > 0:
                self.slice_boys.setValue((num_boys / total_students) * 100)
                self.slice_girls.setValue((num_girls / total_students) * 100)

        except ValueError:
            # Handle non-integer inputs
            pass

if __name__ == "__main__":
    app = QApplication([])

    window = PieChartDemo()
    window.show()

    app.exec()