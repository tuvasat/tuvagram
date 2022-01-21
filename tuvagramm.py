tuvaabc = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнҢңОоӨөПпРрСсТтУуYүФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
tuvagl = 'АаЕеЁёИиОоӨөУуYүЫыЭэЮюЯя'
tuvasgl = 'БбВвГгДдЖжЗзЙйКкЛлМмНнҢңПпРрСсТтФфХхЦцЧчШшЩщ'
tuvasglb = 'БбВвГгДдЖжЗзЙйЛлМмНнҢңРр'
tuvasglp = 'КкПпСсТтФфХхЦцЧчШшЩщ'


tuva_chisl_af = ['кы', 'ки', 'ку', 'кү', 'гы', 'ги', 'гу', 'гү']
tuva_mn_f = ['нар', 'нер', 'лар', 'лер', 'тар', 'тер', 'дар', 'дер']

# Адаарының падежи Кым? Чүү? Кымнар? Чүлер?
tuva_ad_p = []
# Хамаарыштырарының падежи Кымның? Чүнүң? Кымнарның? Чүлерниң?
# дүлей болза	            -тың -тиң -туң -түң	        кадаттың эштиң остуң пөштүң
# -л болза	                -дың -диң -дуң -дүң	        талдың элдиң холдуң шөлдүң
# ажык азы -г, -й, -м, -н, -ң, -р болза	    -ның -ниң -нуң -нүң	кажааның черниң номнуң шүүрнүң
tuva_ha_p = ['тың', 'тиң', 'туң', 'түң', 'дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң']
# Бээриниң падежи Кымга? Чүге? Кымнарга? Чүлерге?
# дүлей болза	            -ка -ке	хатка эътке
# ажык болгаш аяар болза	-га -ге	тараага кежигге
tuva_be_p = ['ка', 'ке', 'га', 'ге']
# Онаарының падежи Кымны? Чүнү? Кымнарны? Чүлерни? Чүзүн? Чүлерин?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза   -ты -ти -ту -тү катты кишти отту уөтү
# -л болза  -ды -ди -ду -дү аалды челди оолду хөлдү
# ажык болгаш аяар болза    -ны -ни -ну -нү торлааны эртемни тонну хүннү
tuva_on_p = ['ты', 'ти', 'ту', 'тү', 'ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү']
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
tuva_ug_p1 = ['че', 'же']
tuva_ug_p2 = ['тыва', 'тиве', 'тува', 'түве', 'дыва', 'диве', 'дува', 'дүве']

# Наклонениелер
# Кылдыныгга чугаалап турар кижиниң хамаарылгазын илередир
# кылыг сөзүнүң хевирлерин наклонениелер дээр.
# Болуушкун наклонениези
# Шагда эрткен үе
tuva_nak_shert_chs = ['ган', 'ген', 'кан', 'кен']
tuva_nak_shert_hs = ['нар', 'нер']
tuva_nak_shert_bas = ['баан', 'бээн']


"""
Следующие функции находят на какие звуки
заканчивается слово, от этого зависит какое именно
окончание добавится к слову
"""


class WordEnd:
    def __init__(self, inword):
        self.inword = inword

    def word_end01(self, inword, number):
        if inword[-number] in 'аыя':  # ы
            return 1
        elif inword[-number] in 'еиэ':  # и
            return 2
        elif inword[-number] in 'ёоую':  # у
            return 3
        elif inword[-number] in 'өү':  # ү
            return 4
        elif inword[-number] in 'ъ':  # е
            return self.word_end02(inword, number + 1)

    def word_end02(self, inword, number):
        if inword[- number] in 'аёоуыюя':  # а
            return 1
        elif inword[- number] in 'еиөүэ':  # е
            return 2
        elif inword[- number] in 'ъ':
            return self.word_end02(inword, number + 1)

    """
    Проверка звуков на которые заканчивается слово
    для добавления окончания падежа
    tuva_un_p = ['тан', 'тен', 'дан', 'ден']
    tuva_tu_p = ['та', 'те', 'да', 'де']
    """
    def word_end1(self, inword):
        if len(inword) < 2:
            return None
        elif inword[-1] in tuvasglp:
            return self.word_end02(inword, 2)
        elif inword[-1] in tuvasglb:
            return self.word_end02(inword, 2) + 2
        elif inword[-1] in tuvagl:
            return self.word_end02(inword, 1) + 2
        else:
            return None

    """
    Проверка звуков на которые заканчивается слово
    для добавления окончания падежа
    tuva_ha_p = ['дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң', 'тың', 'тиң', 'туң', 'түң']
    tuva_on_p = ['ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү', 'ты', 'ти', 'ту', 'тү']
    """
    def word_end2(self, inword):
        if len(inword) < 2:
            return None
        elif inword[-1] == 'л':
            return self.word_end01(inword, 2)
        elif inword[-1] in 'гймнңр':
            return self.word_end01(inword, 2) + 4
        elif inword[-1] in tuvagl:
            return self.word_end01(inword, 1) + 4
        elif inword[-1] in tuvasgl:
            return self.word_end01(inword, 2) + 8
        else:
            return None

    """
    Проверка звуков на которые заканчивается слово
    для добавления окончания падежа 'же', 'че'
    """
    def word_end3(self, inword):
        if len(inword) < 2:
            return None
        elif inword[-1] in (tuvagl + 'грй'):
            return 1
        elif inword[-1] in tuvasgl:
            return 2
        else:
            return None

    """
    Проверка звуков на которые заканчивается слово
    для добавления окончания падежа 'тыва', 'тиве', 'тува', 'түве', 'дыва', 'диве', 'дува', 'дүве'
    """
    def word_end4(self, inword):
        if len(inword) < 2:
            return None
        elif inword[-1] in tuvasglp:
            return self.word_end01(inword, 2)
        elif inword[-1] in tuvasglb:
            return self.word_end01(inword, 2) + 4
        elif inword[-1] in tuvagl:
            return self.word_end01(inword, 1) + 4
        else:
            return None

    """
    Проверка звуков на которые заканчивается слово
    для добавления окончания множественной формы -лар, -лер, -дар, -дер, -нар, -нер, -тар,-тер
    """
    def word_end5(self, inword):
        if len(inword) < 2:
            return None
        elif inword[-1] in 'грй':
            return self.word_end02(inword, 2)
        elif inword[-1] in tuvagl:
            return self.word_end02(inword, 1)
        elif inword[-1] == 'л':
            return self.word_end02(inword, 2) + 2
        elif inword[-1] in 'мнц':
            return self.word_end02(inword, 2) + 4
        elif inword[-1] in tuvasgl:
            return self.word_end02(inword, 2) + 6
        else:
            return None


"""
Класс который на входе получает слово
которое состоит из строчных букв тувинского алфавита,
и делит его на слоги
"""


class Hyphenation:

    def __init__(self, slovo):
        self.__slovo = slovo

    def __call__(self, slovo):
        return self.perenos(slovo)

    def __str__(self):
        return self.perenos(self.__slovo)

    # Формирование шаблона слова по типам символов
    def sgsg(self, slovo):
        mtz = {'ъ', 'ь'}
        dfs = '-'

        istroka = ''
        for i in slovo:
            if i in tuvagl:
                istroka = istroka + 'g'
            elif i in tuvasgl:
                istroka = istroka + 's'
            elif i == dfs:
                istroka = istroka + '-'
            elif i in mtz:
                istroka = istroka + 'z'
            else:
                break
        return istroka

    # --------------------------------------------

    # расставляем символы мягкого переноса
    def slog(self, islog, iline):
        # Шаблоны слогов
        slog2 = {'gssg', 'sgsg', 'gssgg', 'sgszg'}
        slog3 = {'gzssgs', 'ggssg', 'sggsg', 'sgssg', 'sggsg', 'sgsgs', 'gsssg', 'gsgsg', 'ssgsg'}
        slog4 = {'ggsgsg', 'sggssg', 'gsgssg', 'gsggsg', 'ssgssg', 'sgsssg', 'ggsgsgs', 'sgszsg', 'sgszsg', 'ggszsg'}
        slog5 = {'ggsggsg', 'gsggssg', 'sggsssgs', 'sggsssgs', 'gsgsssg', 'sgssssg', 'ggsgssg', 'ssgsssg',
                 'gszgssg', 'sgsszsg'}
        slog6 = {'ggsggssg'}
        slog0 = {'sg-', 'gs-', 'gsg-', 'sgg-', 'sgs-', 'sggs-', 'gsgs-', 'gsggs-', 'ggsg-', 'ggs-',
                 'sgss-', 'ssg-', 'gsggs-', 'gzs-', 'gggs-'}
        # --------------------------------------------

        if (islog[:4] in slog2) or (islog[:5] in slog2) or (islog[:6] in slog2):
            iline = iline[:2] + '~' + iline[2:]
        elif (islog[:5] in slog3) or (islog[:6] in slog3) or (islog[:7] in slog3):
            iline = iline[0:3] + '~' + iline[3:]
        elif (islog[:5] in slog4) or (islog[:6] in slog4) or (islog[:7] in slog4) or (islog[:8] in slog4):
            iline = iline[0:4] + '~' + iline[4:]
        elif (islog[:7] in slog5) or (islog[:8] in slog5) or (islog[:9] in slog5) or (islog[:10] in slog5):
            iline = iline[0:5] + '~' + iline[5:]
        elif (islog[:8] in slog6) or (islog[:9] in slog6) or (islog[:10] in slog6):
            iline = iline[0:6] + '~' + iline[6:]
        elif (islog[:3] in slog0) or (islog[:4] in slog0) or (islog[:5] in slog0) \
                or (islog[:6] in slog0) or (islog[:6] in slog0):
            iline = iline[0:islog.index('-') + 1] + '~' + iline[islog.index('-') + 1:]
        else:
            iline = ''
        return iline

    # --------------------------------------------

    # Разбиваем слово на слоги
    def perenos(self, line):
        ege_sos = line
        # Вызываем функцию формирование шаблона слова по видам символов
        shablon = self.sgsg(ege_sos)
        slog1 = ege_sos
        ege_sos = ''
        while len(shablon) > 1:
            if (self.slog(shablon, slog1)) == '':
                break
            else:
                slog1 = (self.slog(shablon, slog1))
                ege_sos += '~~' + slog1.split('~')[0]
                slog1 = slog1.split('~')[1]
                shablon = self.sgsg(slog1)
        ege_sos = ege_sos[2:] + '~~' + slog1.split('~')[0]
        return ege_sos


# --------------------------------------------

"""
Класс который на входе получает строку
которое состоит из букв тувинского (кириллица) алфавита,
и возвращает множество состоящее
из отдельных слов (выражение которое состоит только из букв тувинского алфавита)
"""


class StrVSlova:
    def __init__(self, stroka):
        self.__stroka = stroka.lower()

    def __str__(self):
        s = ' '.join(self.str_v_slova(self.__stroka))
        return s

    def __call__(self, stroka):
        list1 = self.str_v_slova(self.__stroka)
        return list1

    def str_v_slova(self, stroka):
        # Открываем файл со списком с декодированием с юникод
        s = ''
        for i in stroka:
            if i in tuvaabc:
                s = s + i
            elif i in ' ,.?!@#$%^&*()1234567890_+=\n':
                s = s + ' '
        slova = []
        slova += s.split()
        slova = list(sorted(set(slova)))
        return slova
