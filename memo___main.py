from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from memo___app import app
from memo_data import *
from memo_main_layout import *
from memo___card_layout import *
from memo_edit_layout import txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3

main_width, main_height = 1000, 450
card_width, card_height = 600, 500 
time_unit = 1000

questions_listmodel = QuestionListModel()
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
frm_card = 0
timer = QTimer()
win_card = QWidget()
win_main = QWidget()

def testlist():
    frm = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
    questions_listmodel.form_list.append(frm)
    frm = Question('Будинок', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)
######################################     Функції для проведення тесту:    #############################################

def set_card():
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)

def sleep_card():
    win_card.hide()
    timer.setInterval(time_unit * box_Minutes.value() )
    timer.start()

def show_card():
    win_card.show()
    timer.stop()

def show_random():
    global frm_card
    frm_card = random_AnswerCheck(questions_listmodel, lb_Question, radio_list, lb_Correct, lb_Result)
    frm_card.show()
    show_question()

def click_OK():
    if btn_Ok.text() != "Наступне питання":
        frm_card.check()
        show_result()
    else:
        show_random()

def back_to_menu():
    win_card.hide()
    win_main.showNormal()
######################################     Функції для редагування питань:    ######################################

def set_main():
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle("Список питань")
    win_main.setLayout(layout_main)

def edit_question(index):
    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()

def add_form():
    questions_listmodel.insertRows()
    last = questions_listmodel.rowCount(0) - 1
    index = questions_listmodel.index(last)
    list_questions.setCurrentIndex(index)
    edit_question(index)
    txt_Question.setFocus(Qt.TabFocusReason)

def del_form():
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())

def start_test():
    show_random()
    win_card.show()
    win_main.showMinimized()
######################################      Встановлення потрібних з'єднань:    #############################################

def connects():
    list_questions.setModel(questions_listmodel) # зв'язати список на екрані зі списком запитань
    list_questions.clicked.connect(edit_question) # під час натискання на елемент списку буде відкриватися для редагування потрібне питання
    btn_add.clicked.connect(add_form) # з'єднали натискання кнопки "нове питання" з функцією додавання
    btn_delete.clicked.connect(del_form) # з'єднали натискання кнопки "видалити питання" з функцією видалення
    btn_start.clicked.connect(start_test) # натискання кнопки "почати тест" 
    btn_Ok.clicked.connect(click_OK) # натискання кнопки "OK" на формі тесту
    btn_Menu.clicked.connect(back_to_menu) # натискання кнопки "Меню" для повернення з форми тесту в редактор запитань
    timer.timeout.connect(show_card) # показуємо форму тесту після закінчення таймера
    btn_Sleep.clicked.connect(sleep_card) # натискання кнопки "спати" у картки-тесту

testlist()
set_card()
set_main()
connects()
win_card.show()
app.exec_()