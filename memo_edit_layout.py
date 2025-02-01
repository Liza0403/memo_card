from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from memo___app import app

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('Неправильна відповідь №1:', txt_Wrong1)
layout_form.addRow('Неправильна відповідь №2:', txt_Wrong2)
layout_form.addRow('Неправильна відповідь №3:', txt_Wrong3)

