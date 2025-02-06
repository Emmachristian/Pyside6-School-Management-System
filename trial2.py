from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PySide6 import QtCharts

class BarChartDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bar Chart Demo")
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.chart_view = QtCharts.QChartView()
        self.chart = QtCharts.QChart()

        # Create and set Y-axis
        self.y_axis = QtCharts.QValueAxis()
        self.chart.addAxis(self.y_axis, Qt.AlignLeft)

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

        # Initialize bar series
        self.bar_series = QtCharts.QBarSeries()

        # Add bars for boys and girls
        self.bar_set = QtCharts.QBarSet("Gender Distribution")
        self.bar_series.append(self.bar_set)

        # Add bar series to chart
        self.chart.addSeries(self.bar_series)
        self.chart.setTitle("Gender Distribution")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        # Attach Y-axis to the series
        self.bar_series.attachAxis(self.y_axis)

        self.chart_view.setChart(self.chart)

    def update_chart(self):
        try:
            num_boys = int(self.edit_boys.text())
            num_girls = int(self.edit_girls.text())

            # Update bar values
            self.bar_set.replace(0, num_boys)
            self.bar_set.replace(1, num_girls)

            # Adjust axis range
            max_value = max(num_boys, num_girls)
            self.y_axis.setRange(0, max_value + 5)  # Add some padding for better visualization

        except ValueError:
            # Handle non-integer inputs
            pass

if __name__ == "__main__":
    app = QApplication([])

    window = BarChartDemo()
    window.show()

    app.exec()