#!/usr/bin/env python

import sys 
import types 

from PyQt5.QtWidgets import QMainWindow, QApplication 
from ui_events import Ui_Events 

def fprint(*args): 
    """ print and flush the output buffer so text 
        shows up immediately 
    """ 
    print(*args)
    sys.stdout.flush() 

class EventsMain(QMainWindow): 
    FRUITS = dict(A='Apple', B='Banana', C='Cherry', D='Date') 

    def __init__(self): 
        QMainWindow.__init__(self) 

        self.ui = Ui_Events()
        self.ui.setupUi(self) 

        # set the File->Quit handler 
        self.ui.actionQuit.triggered.connect(self.close) # <1>

        # set the Edit->Clear Name Field handler 
        self.ui.actionClear_name_field.triggered.connect(self._clear_field)

        # use the same handler for all 4 buttons 
        self.ui.pb_A.clicked.connect(self._mkfunc('red',self.ui.pb_A))  # <2>
        self.ui.pb_B.clicked.connect(self._mkfunc('blue',self.ui.pb_B)) 
        self.ui.pb_C.clicked.connect(self._mkfunc('yellow',self.ui.pb_C)) 
        self.ui.pb_D.clicked.connect(self._mkfunc('purple',self.ui.pb_D)) 

        self.setup_mouse_move_event_handler() 

        self.ui.checkBox.toggled.connect(self._toggled) 
        self.ui.checkBox.clicked.connect(self._clicked) 
        
    def setup_mouse_move_event_handler(self): 
        def mme(self, mouse_ev): 
            self.ui.statusbar.showMessage("Motion: {0},{1}".format(   # <3>
                mouse_ev.x(), mouse_ev.y(), 0)  # 2nd param is timeout 
            ) 
        # add method instance to label dynamically 
        self.ui.label.mouseMoveEvent = types.MethodType(mme, self) 

    def keyPressEvent(self, key_ev): 
        """ Generated on keypresses """ 
        key_code = key_ev.key()   # <4>
        char = chr(key_code) if key_code < 128 else 'Special'  # <5>
        fprint("Key press: {0} ({1})".format(key_code, char)) 

    def mousePressEvent(self, mouse_ev):    # <6>
        """ generated when mouse button is pressed """ 
        fprint("Press:", mouse_ev.x(), mouse_ev.y()) 

    
    def mouseReleaseEvent(self, mouse_ev): 
        fprint("Release:", mouse_ev.x(), mouse_ev.y()) 

    def _toggled(self, mouse_ev):   # <7>
        fprint("Toggle") 

    def _clicked(self, mouse_ev): 
        fprint("Click")

    def _checked(self, mouse_ev): 
        fprint("Toggle") 

    def _pushed(self): 
        sender = self.sender() 
        button_text = str(sender.text()) 
        if button_text in EventsMain.FRUITS: 
            sender.setText(EventsMain.FRUITS[button_text])

    def _mkfunc(self, color, widget):  # <8>
        def pushed(stuff):
            button_text = str(widget.text()) 
            fprint("HI I AM BUTTON {0} and I AM {1}".format(button_text, color))
            if button_text in EventsMain.FRUITS: 
                widget.setText(EventsMain.FRUITS[button_text])
                
        return pushed  # <9>

    def _clear_field(self): 
        self.ui.leName.setText('')   # <10>

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    main = EventsMain() 
    main.show() 
    sys.exit(app.exec_())
