"""
Этот модуль представляет собой сборник классов и функций
для работы с существительными.
Нахождение существительных в тексте.
Преобразование существительных.
Преобразование других частей речи в существительные.
"""

import tuvagramm
from tuvagramm import WordEnd


# окончания множественного числа существительных
tuva_mn_f = ['лар', 'лер', 'дар', 'дер', 'нар', 'нер', 'тар', 'тер']

# Адаарының падежи Кым? Чүү? Кымнар? Чүлер?
tuva_ad_p = []
# Хамаарыштырарының падежи Кымның? Чүнүң? Кымнарның? Чүлерниң?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза	-тың -тиң -туң -түң	кадаттың эштиң остуң пөштүң
# -л болза	-дың -диң -дуң -дүң	талдың элдиң холдуң шөлдүң
# ажык азы -г, -й, -м, -н, -ң, -р болза	-ның -ниң -нуң -нүң	кажааның черниң номнуң шүүрнүң
tuva_ha_p = ['дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң', 'тың', 'тиң', 'туң', 'түң']
# Бээриниң падежи Кымга? Чүге? Кымнарга? Чүлерге?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза	-ка -ке	хатка эътке
# ажык болгаш аяар болза	-га -ге	тараага кежигге
tuva_be_p = ['ка', 'ке', 'га', 'ге']
# Онаарының падежи Кымны? Чүнү? Кымнарны? Чүлерни? Чүзүн? Чүлерин?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза   -ты -ти -ту -тү катты кишти отту уөтү
# -л болза  -ды -ди -ду -дү аалды челди оолду хөлдү
# ажык болгаш аяар болза    -ны -ни -ну -нү торлааны эртемни тонну хүннү
tuva_on_p = ['ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү', 'ты', 'ти', 'ту', 'тү']
# Турарының падежи Кымда? Чүде? Кымнарда? Чүлерде?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза	-та -те	дашта шетте
# ажык азы аяар болза	-да -де	шынаада хүнде
tuva_tu_p = ['та', 'те', 'да', 'де']
# Үнериниң падежи Кымдан? Чүден? Кымнардан? Чүлерден?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза	-тан -тен	хаштан эъттен
# ажык азы ыыткыр болза	-дан -ден	оваадан өгден
tuva_un_p = ['тан', 'тен', 'дан', 'ден']
# Углаарының падежи Кымче? Чүже? Кымнарже? Чүлерже?
# Падежтиң янзызы	Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# Углаарының 1-ги падежи	дүлей -м, -н, -ң, -л болза	-че	орукче хүнче
# ажык азы -г, -р, й болза	-же	кажааже хоорайже
# Углаарының 2-ги падежи	дүлей болза	-тыва -тиве -тува -түве	шаттыва эштиве хостува көштүве
# ажык азы аяар болза	-дыва -диве -дува -дүве	хадыдыва херимдиве ховудува бөрүдүве
tuva_ug_1p = ['же', 'че']
tuva_ug_2p = ['тыва', 'тиве', 'тува', 'түве', 'дыва', 'диве', 'дува', 'дүве']

# Наклонениелер
# Кылдыныгга чугаалап турар кижиниң хамаарылгазын илередир
# кылыг сөзүнүң хевирлерин наклонениелер дээр.
# Болуушкун наклонениези
# Шагда эрткен үе
tuva_nak_shert_chs = ['ган', 'ген', 'кан', 'кен']
tuva_nak_shert_hs = ['нар', 'нер']
tuva_nak_shert_bas = ['баан', 'бээн']


"""
Класс который на входе получает
строку и номер падежа
- возвращает строку с окончанием указанного
падежа
(В тувинском языке всего 7 падежей, 7-й падеж имеет 2 разных формы.
Эти формы пронумерованы как 7 и 8)
"""


class NounToCase(WordEnd):
    def __init__(self, word, case):
        super().__init__(word)
        self.word = word
        self.case = case

    def __str__(self):
        if self.case == 1:
            return self.ad_p()
        elif self.case == 2:
            return self.ha_p()
        elif self.case == 3:
            return self.be_p()
        elif self.case == 4:
            return self.on_p()
        elif self.case == 5:
            return self.tu_p()
        elif self.case == 6:
            return self.un_p()
        elif self.case == 7:
            return self.ug_1p()
        elif self.case == 8:
            return self.ug_2p()

    def ad_p(self):
        return self.word

    def be_p(self):
        return self.word + tuva_be_p[self.word_end1(self.word) - 1]

    def tu_p(self):
        return self.word + tuva_tu_p[self.word_end1(self.word) - 1]

    def un_p(self):
        return self.word + tuva_un_p[self.word_end1(self.word) - 1]

    def ha_p(self):
        return self.word + tuva_ha_p[self.word_end2(self.word) - 1]

    def on_p(self):
        return self.word + tuva_on_p[self.word_end2(self.word) - 1]

    def ug_1p(self):
        return self.word + tuva_ug_1p[self.word_end3(self.word) - 1]

    def ug_2p(self):
        return self.word + tuva_ug_2p[self.word_end4(self.word) - 1]


"""
Класс который на входе получает существительное в единственном числе
- возвращает существительное во множественном числе
"""


class NounToPlural(WordEnd):
    def __init__(self, word):
        super().__init__(word)
        self.word = word

    def __str__(self):
        return self.plural()

    def plural(self):
        return self.word + tuva_mn_f[self.word_end5(self.word) - 1]


"""
Класс который на входе получает существительное и номер притяжательной формы
- возвращает существительное притяжательной формы
"""


class NounToPossessive(WordEnd):
    def __init__(self, word, form):
        super().__init__(word)
        self.word = word
        self.form = form

    def __str__(self):
        if self.form == 1:
            return self.nountopossessive1()
        if self.form == 2:
            return self.nountopossessive2()
        if self.form == 3:
            return self.nountopossessive3()

    def nountopossessive(self, nounposs):
        if self.word[-1] in tuvagramm.tuvagl:
            return self.word + nounposs[self.word_end01(self.word, 1) - 1]
        elif self.word[-1] in tuvagramm.tuvasglb:
            return self.word + nounposs[self.word_end01(self.word, 2) + 3]
        elif self.word[-1] in tuvagramm.tuvasglp:
            if self.word[-1] in 'т':
                self.word = self.word[:-1] + 'д'
            elif self.word[-1] in 'п':
                self.word = self.word[:-1] + 'в'
            return self.word + nounposs[self.word_end01(self.word, 2) + 3]  # шын эвес

    def nountopossessive1(self):
        nounposs1 = ['м', 'м', 'м', 'м', 'ым', 'им', 'ум', 'үм']
        return self.nountopossessive(nounposs1)

    def nountopossessive2(self):
        nounposs2 = ['ң', 'ң', 'ң', 'ң', 'ың', 'иң', 'уң', 'үң']
        return self.nountopossessive(nounposs2)

    def nountopossessive3(self):
        nounposs3 = ['зы', 'зи', 'зу', 'зү', 'ы', 'и', 'у', 'ү']
        return self.nountopossessive(nounposs3)


"""
Класс который на входе получает
строку и номер
- возвращает строку с окончанием номера падежа
"""


class Padej:
    def __init__(self, slovo, padej):
        self.slovo = slovo
        self.padej = padej

    def __str__(self):
        if self.padej == 1:
            return self.ad_p()
        elif self.padej == 2:
            return self.ha_p()
        elif self.padej == 3:
            return self.be_p()
        elif self.padej == 4:
            return self.ha_p()
        elif self.padej == 5:
            return self.be_p()
        elif self.padej == 6:
            return self.be_p()
        elif self.padej == 7:
            return self.be_p()

    def ad_p(self):
        return self.slovo

    def ha_p(self):
        if self.slovo[-1:] in 'БбВвДдЖжЗзКкПпСсТтФфХхЦцЧчШшЩщ':
            if self.slovo[-2] in 'АаЫыЯя':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[0]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[0]
            if self.slovo[-2] in 'ИиЕеЭэ':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[1]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[1]
            if self.slovo[-2] in 'ОоУуЮюЁё':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[2]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[2]
            if self.slovo[-2] in 'ӨөҮү':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[3]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[3]
        elif len(self.slovo) > 2 and self.slovo[-1] == 'л':
            if self.slovo[-2] in 'АаЫыЯя':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[4]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[4]
            if self.slovo[-2] in 'ИиЕеЭэ':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[5]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[5]
            if self.slovo[-2] in 'ОоУуЮюЁё':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[6]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[6]
            if self.slovo[-2] in 'ӨөҮү':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[7]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[7]
        elif len(self.slovo) > 1 and self.slovo[-1] in 'ГгЙйМмНнҢңРрАаЕеЁёИиОоӨөУуYүЫыЭэЮюЯя':
            if self.slovo[-2] in 'АаЫыЯя' or self.slovo[-1] in 'АаЫыЯя':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[8]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[8]
            if self.slovo[-2] in 'ИиЕеЭэ' or self.slovo[-1] in 'ИиЕеЭэ':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[9]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[9]
            if self.slovo[-2] in 'ОоУуЮюЁё' or self.slovo[-1] in 'ОоУуЮюЁё':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[10]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[10]
            if self.slovo[-2] in 'ӨөҮү' or self.slovo[-1] in 'ӨөҮү':
                if self.padej == 2:
                    return self.slovo + tuva_ha_p[11]
                elif self.padej == 4:
                    return self.slovo + tuva_on_p[11]
        else:
            return ''

    def be_p(self):
        if len(self.slovo) > 1 and self.slovo[-1] in tuvagramm.tuvasgl and self.slovo[-1] != 'лй':
            if self.slovo[-2] in 'АаЫыЯяОоУуЮюЁё':
                if self.padej == 3:
                    return self.slovo + tuva_be_p[0]
                elif self.padej == 5:
                    return self.slovo + tuva_tu_p[0]
                elif self.padej == 6:
                    return self.slovo + tuva_un_p[0]
                elif self.padej == 7:
                    return self.slovo + tuva_ug_1p[0]
            if self.slovo[-2] in 'ИиЕеЭэӨөҮү':
                if self.padej == 3:
                    return self.slovo + tuva_be_p[1]
                elif self.padej == 5:
                    return self.slovo + tuva_tu_p[1]
                elif self.padej == 6:
                    return self.slovo + tuva_un_p[1]
                elif self.padej == 7:
                    return self.slovo + tuva_ug_1p[0]
        elif len(self.slovo) > 1 and self.slovo[-1] in tuvagramm.tuvagl or self.slovo[-1] == 'лй':
            if self.slovo[-2] in 'АаЫыЯяОоУуЮюЁё' or self.slovo[-1] in 'АаЫыЯяОоУуЮюЁё':
                if self.padej == 3:
                    return self.slovo + tuva_be_p[2]
                elif self.padej == 5:
                    return self.slovo + tuva_tu_p[2]
                elif self.padej == 6:
                    return self.slovo + tuva_un_p[2]
                elif self.padej == 7:
                    return self.slovo + tuva_ug_1p[1]
            if self.slovo[-2] in 'ИиЕеЭэӨөҮү' or self.slovo[-1] in 'ИиЕеЭэӨөҮү':
                if self.padej == 3:
                    return self.slovo + tuva_be_p[3]
                elif self.padej == 5:
                    return self.slovo + tuva_tu_p[3]
                elif self.padej == 6:
                    return self.slovo + tuva_un_p[3]
                elif self.padej == 7:
                    return self.slovo + tuva_ug_1p[1]
        else:
            return ''


"""
Класс возвращающий падеж слова (кроме именительного) по его окончанию
"""


class NounFromCase:

    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        if self.nounfromcase() == other:
            return True
        return False

    def __str__(self):
        return self.nounfromcase()

    def nounfromcase(self):
        if self.word[-3:] in tuva_ha_p:
            return 'ha_p'
        elif self.word[-2:] in tuva_be_p:
            return 'be_p'
        elif self.word[-2:] in tuva_on_p:
            return 'on_p'
        elif self.word[-2:] in tuva_tu_p:
            return 'tu_p'
        elif self.word[-3:] in tuva_un_p:
            return 'un_p'
        elif self.word[-2:] in tuva_ug_1p or self.word[-4:] in tuva_ug_2p:
            return 'ug_p'


"""
Класс который в предложенном тексте находит слова с окончаниями характерными
для падежей существительных, собирает их вокруг начальной формы существительного
и предлагает начальную форму в качестве существительного
с точностью до указанного количества форм в других падежах.

В дальнейшем предлагается искать также по притяжательной форме и
по окончаниям формирования существительного из других частей речи.
"""


class NounsInList:

    def __init__(self, words):
        self.words = words
        self.res = dict()
        self.nouninlist()

    def __call__(self, words):
        self.__init__(words)
        return self.res

    def __str__(self):
        res = ''
        for i in self.res.keys():
            if len(i) > 1 and len(' '.join(self.res[i]).split()) > 4:
                res += i + ':' + ' ' + ', '.join(self.res[i]) + '\n'
        return res

    def kojar(self, sos0, sos, padej):
        if self.res.get(sos0) is None:
            self.res[sos0] = [''] * 9
            self.res[sos0][0] = sos0
        self.res[sos0][padej] = sos

    def nouninlist(self):
        try:
            for word in sorted(self.words):
                if len(word) < 3:
                    continue
                elif word[0] in 'вгжзңрфц ':
                    continue
                # ['дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң', 'тың', 'тиң', 'туң', 'түң']
                elif NounFromCase(word) == 'ha_p':
                    self.kojar(word[:-3], word, 2)
                # ['ка', 'ке', 'га', 'ге']
                elif NounFromCase(word) == 'be_p':
                    self.kojar(word[:-2], word, 3)
                # ['ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү', 'ты', 'ти', 'ту', 'тү']
                elif NounFromCase(word) == 'on_p':
                    self.kojar(word[:-2], word, 4)
                # ['та', 'те', 'да', 'де']
                elif NounFromCase(word) == 'tu_p':
                    self.kojar(word[:-2], word, 5)
                # ['тан', 'тен', 'дан', 'ден']
                elif NounFromCase(word) == 'un_p':
                    self.kojar(word[:-3], word, 6)
                elif NounFromCase(word) == 'ug_1p':
                    self.kojar(word[:-2], word, 7)
                elif NounFromCase(word) == 'ug_2p':
                    self.kojar(word[:-4], word, 8)
        except:
            print('Ошибка формирования словаря')
