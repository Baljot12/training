import threading
import time
#synchronisation in multithreading
lock = threading.Lock()
class printer:
    def PrintDocuments(self,docname,times):
        lock.acquire()#both the child classes can access printer obj ,first desktop
#start  it get the lock,when it finish ,the it release lock
        for i in range(1,times+1):
            print(">>printing {}copy".format(docname,i))
            time.sleep(1)
            lock.release()
class Desktop(threading.Thread):
    def attachPrinter(self,printer):
        self.printer= printer
    def run(self):
        self.printer.PrintDocuments("##learning java.pdf",10)

class Laptop(threading.Thread):
    def attachPrinter(self, printer):
        self.printer = printer

    def run(self):
        self.printer.PrintDocuments("##learning python.pdf", 10)
printer = printer()
desktop = Desktop()
desktop.attachPrinter(printer)
laptop = Laptop()
laptop.attachPrinter(printer)
desktop.start()
laptop.start()
