import sys
import decorator
import noun

def list_to_case(inlist=None):
    res = dict()
    if not inlist:
        inlist = ['кижи', 'хой', 'тараа', 'тавак', 'курут']
    for sos in inlist:
        res[sos] = []
        for i in range(1, 9):
            a = noun.NounToCase(sos, i)
            res[sos].append(str(a))
    print(res)

# Запуск интерфейса пользователя
def app_run():
    app = decorator.QApplication(sys.argv)
    ex = decorator.MyWidget()
    ex.show()
    sys.exit(app.exec_())

# Запуск программы
if __name__ == '__main__':
    app_run()
