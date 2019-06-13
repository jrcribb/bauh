#!env/bin/python
import argparse
import sys

from PyQt5.QtWidgets import QApplication, QWidget

from core.controller import FlatpakController
from core.model import FlatpakManager
from view.qt.systray import TrayIcon
from core import __version__

parser = argparse.ArgumentParser(prog='fpakman', description="GUI for Flatpak applications management")
parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(__version__))
args = parser.parse_args()

app = QApplication(sys.argv)
manager = FlatpakManager()
manager.load_database_async()
controller = FlatpakController(manager)
hidden_widget = QWidget()
trayIcon = TrayIcon(parent=hidden_widget, controller=controller, check_interval=30)
trayIcon.show()

sys.exit(app.exec_())
