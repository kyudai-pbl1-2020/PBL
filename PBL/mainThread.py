import threading
from PBL import application

class MainThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = application.Application()
        self.root.protocol("WM_DELETE_WINDOW",self.callback)



def main():
    app = MainThread()

if __name__ == "__main__":
    main()
