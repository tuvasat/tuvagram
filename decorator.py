import tuvagramm
from tuvagramm import Hyphenation, StrVSlova
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from db_methods import db_content
from db_methods import new_db_create
import noun
from noun import NounsInList


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tuvagramm.ui', self)
        self.soster = []
        self.btn1_1.clicked.connect(self.btn1_click)
        self.btn1_2.clicked.connect(self.btn2_click)
        self.btn1_3.clicked.connect(self.btn3_click)
        self.btn1_4.clicked.connect(self.btn4_click)

    def btn1_click(self):
        if self.checkBox1_1.isChecked():
            try:
                db = db_content()
                list = db.table_texts_content_read('WORDS')
                db.conn.close()
                words = []
                for num, word in list:
                    words.append(word)
                self.textEdit1_1.setText('\n'.join(sorted(words)))
            except:
                print('Ошибка чтения из базы данных')
        else:
            self.textEdit1_1.setText('\n'.join(self.soster))

    def btn2_click(self):
        if self.checkBox1_1.isChecked():
            try:
                db = db_content()
                words1 = db.table_texts_content_read('WORDS')
                db.conn.close()
                words_k = []
                for num, word in words1:
                    words_k.append(str(Hyphenation(word)))
                self.textEdit1_1.setText('\n'.join(sorted(words_k)))
            except:
                print('Ошибка чтения из базы данных')
        else:
            words1 = str(tuvagramm.StrVSlova(self.textEdit1_1.toPlainText().lower())).split()
            words_k = []
            for word in words1:
                words_k.append(str(Hyphenation(word)))
            self.textEdit1_1.setText('\n'.join(sorted(words_k)))

    def btn3_click(self):
        if self.checkBox1_1.isChecked():
            try:
                db = db_content()
                words1 = db.table_texts_content_read('WORDS')
                db.conn.close()
                words2 = []
                for num, word in words1:
                    words2.append(word)
                self.textEdit1_1.setText(str(NounsInList(words2)))
            except:
                print('Ошибка чтения из базы данных')
        else:
            words1 = str(tuvagramm.StrVSlova(self.textEdit1_1.toPlainText().lower())).split()
            words2 = []
            for word in words1:
                words2.append(word)
            self.textEdit1_1.setText(str(NounsInList(words2)))

    def btn4_click(self):
        # Считываем содержимое файла и выводим на поле
        if self.lineEdit1_1.text():
            filename = self.lineEdit1_1.text()
        else:
            filename = 'text/text.txt'
        try:
            f = open(f"{filename}", "r", encoding="utf-8")
            self.textEdit1_1.setText('\n'.join(f.readlines()))
            f.close()
            self.soster = str(tuvagramm.StrVSlova(self.textEdit1_1.toPlainText().lower())).split()
            try:
                db = db_content()
                db.table_texts_content_add(self.textEdit1_1.toPlainText())
                db.table_words_content_add(self.soster)
                db.conn.close()
            except:
                print('Ошибка загрузки текста в базу данных.')
        except :
            print('Ошибка')

    def btn5_click(self):
        soster = set(str(StrVSlova(self.textEdit1.toPlainText().lower())).split(' '))
        ad_p, ha_p, be_p, on_p, tu_p, ug_p, un_p = [], [], [], [], [], [], []
        for i in soster:
            if i[-3:] in tuvagramm.tuva_ha_p:
                ha_p.append(i)
            elif i[-2:] in tuvagramm.tuva_be_p:
                be_p.append(i)
            elif i[-2:] in tuvagramm.tuva_on_p:
                on_p.append(i)
            elif i[-2:] in tuvagramm.tuva_tu_p:
                tu_p.append(i)
            elif i[-3:] in tuvagramm.tuva_un_p:
                un_p.append(i)
            elif i[-2:] in tuvagramm.tuva_ug_p1 or i[-4:] in tuvagramm.tuva_ug_p2:
                ug_p.append(i)
            else:
                ad_p.append(i)

        res = ''
        #        res += '_____ Адаарының падежи _____\n'
        #        res += '\n'.join(sorted(ad_p))
        res += '\n_____ Хамаарыштырарының падежи _____\n'
        res += '\n'.join(sorted(ha_p))
        res += '\n_____ Бээриниң падежи _____\n'
        res += '\n'.join(sorted(be_p))
        res += '\n_____ Онаарының падежи _____\n'
        res += '\n'.join(sorted(on_p))
        res += '\n_____ Турарының падежи _____\n'
        res += '\n'.join(sorted(tu_p))
        res += '\n_____ Үнериниң падежи _____\n'
        res += '\n'.join(sorted(un_p))
        res += '\n_____ Углаарының падежи _____\n'
        res += '\n'.join(sorted(ug_p))
        self.textEdit2.setText(res)

    def btn6_click(self):
        soster = set(str(StrVSlova(self.textEdit1.toPlainText().lower())).split(' '))
        res = []
        for i in soster:
            res.append(str(noun.Padej(i, 1)) + '\n')
            res.append(str(noun.Padej(i, 2)) + '\n')
            res.append(str(noun.Padej(i, 3)) + '\n')
            res.append(str(noun.Padej(i, 4)) + '\n')
            res.append(str(noun.Padej(i, 5)) + '\n')
            res.append(str(noun.Padej(i, 6)) + '\n')
            res.append(str(noun.Padej(i, 7)) + '\n')
        self.textEdit2.setText(''.join(sorted(res)))

    def btn7_click(self):
        soster = set(str(StrVSlova(self.textEdit1.toPlainText().lower())).split(' '))
        self.textEdit2.setText(str(noun.NounsInList(soster)))

    def btn8_click(self):
        self.textEdit1.setText(self.textEdit2.toPlainText())
