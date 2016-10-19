import random
import string
import sys

from stylesheet import set_stylesheet


from PyQt5 import QtCore, QtGui, QtWidgets


# Create main canvas
class Passwordy(QtWidgets.QMainWindow):
 

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)

        # Call function to create UI
        self.create_main_ui()


    def create_main_ui(self):

        # Set window stylesheet
        get_stylesheet = set_stylesheet()
        self.setStyleSheet(get_stylesheet)

        # Main window setting
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName('centralWidget')

        # Set main widget layout (centralWidget)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName('verticalLayout_10')

         # Create top frame
        self.top_frame = QtWidgets.QFrame(self.centralWidget)
        self.top_frame.setObjectName('top_frame')
        self.horizontallayout_10 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontallayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontallayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_10.setSpacing(0)
        self.horizontallayout_10.setObjectName('horizontallayout_10')

        # Add top frame to layout
        self.verticalLayout_10.addWidget(self.top_frame)
        
        # Create frame for menu button and title
        self.menu_frame = QtWidgets.QFrame(self.top_frame)

        # Set frame size
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_frame.sizePolicy().hasHeightForWidth())
        self.menu_frame.setSizePolicy(sizePolicy)
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName('menu_frame')

        # Set menu frames layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menu_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName('horizontalLayout')

        # Create menubutton
        self.menu_button = QtWidgets.QPushButton(self.menu_frame)
        self.menu_button.setObjectName('menu_button')
        self.menu_button.setText('☰')

        # Add menubutton widget to layout
        self.horizontalLayout.addWidget(self.menu_button)

        # Connect menu button to open_menu function
        self.menu_button.clicked.connect(self.open_menu)

        # Create title label
        self.title_label = QtWidgets.QLabel(self.menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setObjectName('title_label')
        self.title_label.setText('passwordy')

        # Add title label to layout
        self.horizontalLayout.addWidget(self.title_label)
        self.horizontallayout_10.addWidget(self.menu_frame)

        # Create frame for middle spacer
        self.spacer_frame = QtWidgets.QFrame(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spacer_frame.sizePolicy().hasHeightForWidth())     
        self.spacer_frame.setSizePolicy(sizePolicy)
        self.spacer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spacer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spacer_frame.setObjectName('spacer_frame')

        # Create layout for spacer frame
        self.verticalLayout = QtWidgets.QVBoxLayout(self.spacer_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName('verticalLayout')

        # Create horizontal spacer
        spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacer)

        # Add spacer to layout
        self.horizontallayout_10.addWidget(self.spacer_frame)
        
        # Create frame for generate button
        self.generate_frame = QtWidgets.QFrame(self.top_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_frame.sizePolicy().hasHeightForWidth())
        self.generate_frame.setSizePolicy(sizePolicy)
        self.generate_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generate_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generate_frame.setObjectName('generate_frame')

        # Create layout for generate button frame
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.generate_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        
        # Create generate button
        self.generate_button = QtWidgets.QPushButton(self.generate_frame)
        self.generate_button.setText('generate')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generate_button.sizePolicy().hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy)
        self.generate_button.setObjectName('generate_button')

        # Add generate button to layout
        self.verticalLayout_3.addWidget(self.generate_button)

        # Add generate frame to layout
        self.horizontallayout_10.addWidget(self.generate_frame)

        # Connect generate button to generate_passwords function
        self.generate_button.clicked.connect(self.open_password_ouput)
        
        # Set central widget
        self.setCentralWidget(self.centralWidget)

        # Hide OS' default window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Call menu ui to set options and immediately hide
        self.menu_ui()
        self.options_frame.hide()

        # Reset menu button icon
        self.menu_button.setText('☰')
        # Reset window size
        self.resize(500, 50)

        # Set password output open flag
        self.password_output_open = False
 

    def open_menu(self):
        self.menu_ui()


    def close_menu(self):
        
        # Hide menu
        self.options_frame.hide()

        # Reset window size
        self.resize(500, 50)

        # Reset menu button icon
        self.menu_button.setText('☰')
        

    def menu_ui(self):

        # Change menu button to 'open'
        self.menu_button.setText('☷')

        # Create options frame
        self.options_frame = QtWidgets.QFrame(self.centralWidget)
        self.options_frame.setObjectName('options_frame')
        self.horizontallayout_4 = QtWidgets.QHBoxLayout(self.options_frame)
        self.horizontallayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontallayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_4.setSpacing(0)
        self.horizontallayout_4.setObjectName('horizontallayout_4')

        # Add options frame to layout
        self.verticalLayout_10.addWidget(self.options_frame)
        
        # Add checkboxes frame        
        self.checks_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checks_frame.sizePolicy().hasHeightForWidth())
        self.checks_frame.setSizePolicy(sizePolicy)
        self.checks_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.checks_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.checks_frame.setObjectName('checks_frame')
        self.horizontallayout_3 = QtWidgets.QHBoxLayout(self.checks_frame)
        self.horizontallayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_3.setSpacing(0)
        self.horizontallayout_3.setObjectName('horizontallayout_3')
        self.characters_frame = QtWidgets.QFrame(self.checks_frame)
        self.characters_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.characters_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.characters_frame.setObjectName('characters_frame')
        self.verticallayout_6 = QtWidgets.QVBoxLayout(self.characters_frame)
        self.verticallayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticallayout_6.setSpacing(6)
        self.verticallayout_6.setObjectName('verticallayout_6')
        self.numbers_checkbox = QtWidgets.QCheckBox(self.characters_frame)
        self.numbers_checkbox.setChecked(True)
        self.numbers_checkbox.setObjectName('numbers_checkbox')
        self.verticallayout_6.addWidget(self.numbers_checkbox)
        self.special_characters_checkbox = QtWidgets.QCheckBox(self.characters_frame)
        self.special_characters_checkbox.setChecked(True)
        self.special_characters_checkbox.setObjectName('special_characters_checkbox')
        self.verticallayout_6.addWidget(self.special_characters_checkbox)
        self.horizontallayout_3.addWidget(self.characters_frame)
        self.case_frame = QtWidgets.QFrame(self.checks_frame)
        self.case_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.case_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_frame.setObjectName('case_frame')
        self.verticallayout_7 = QtWidgets.QVBoxLayout(self.case_frame)
        self.verticallayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticallayout_7.setSpacing(6)
        self.verticallayout_7.setObjectName('verticallayout_7')
        self.lowercase_checkbox = QtWidgets.QCheckBox(self.case_frame)
        self.lowercase_checkbox.setChecked(True)
        self.lowercase_checkbox.setObjectName('lowercase_checkbox')
        self.verticallayout_7.addWidget(self.lowercase_checkbox)
        self.uppercase_checkbox = QtWidgets.QCheckBox(self.case_frame)
        self.uppercase_checkbox.setChecked(True)
        self.uppercase_checkbox.setObjectName('uppercase_checkbox')
        self.verticallayout_7.addWidget(self.uppercase_checkbox)
        self.horizontallayout_3.addWidget(self.case_frame)
        self.horizontallayout_4.addWidget(self.checks_frame)
        self.spins_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spins_frame.sizePolicy().hasHeightForWidth())

        self.numbers_checkbox.setText('Numbers')
        self.special_characters_checkbox.setText('Specials')
        self.lowercase_checkbox.setText('Lowercase')
        self.uppercase_checkbox.setText('Uppercase')
        
        self.spins_frame.setSizePolicy(sizePolicy)
        self.spins_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spins_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spins_frame.setObjectName('spins_frame')
        self.verticallayout_3 = QtWidgets.QVBoxLayout(self.spins_frame)
        self.verticallayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticallayout_3.setSpacing(0)
        self.verticallayout_3.setObjectName('verticallayout_3')
        self.labels_frame = QtWidgets.QFrame(self.spins_frame)
        self.labels_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.labels_frame.setObjectName('labels_frame')
        self.horizontallayout_6 = QtWidgets.QHBoxLayout(self.labels_frame)
        self.horizontallayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_6.setSpacing(0)
        self.horizontallayout_6.setObjectName('horizontallayout_6')
        self.characters_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.characters_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.characters_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.characters_label_frame.setObjectName('characters_label_frame')
        self.verticallayout_5 = QtWidgets.QVBoxLayout(self.characters_label_frame)
        self.verticallayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticallayout_5.setSpacing(0)
        self.verticallayout_5.setObjectName('verticallayout_5')
        self.characters_label = QtWidgets.QLabel(self.characters_label_frame)
        self.characters_label.setObjectName('characters_label')
        self.verticallayout_5.addWidget(self.characters_label)
        self.horizontallayout_6.addWidget(self.characters_label_frame)
        self.passwords_label_frame = QtWidgets.QFrame(self.labels_frame)
        self.passwords_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.passwords_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.passwords_label_frame.setObjectName('passwords_label_frame')
        self.horizontallayout_7 = QtWidgets.QHBoxLayout(self.passwords_label_frame)
        self.horizontallayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_7.setSpacing(0)
        self.horizontallayout_7.setObjectName('horizontallayout_7')
        self.passwords_label = QtWidgets.QLabel(self.passwords_label_frame)
        self.passwords_label.setObjectName('passwords_label')
        self.horizontallayout_7.addWidget(self.passwords_label)
        self.horizontallayout_6.addWidget(self.passwords_label_frame)
        self.verticallayout_3.addWidget(self.labels_frame)
        self.spin_boxes_frame = QtWidgets.QFrame(self.spins_frame)
        self.spin_boxes_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spin_boxes_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spin_boxes_frame.setObjectName('spin_boxes_frame')
        self.horizontallayout_5 = QtWidgets.QHBoxLayout(self.spin_boxes_frame)
        self.horizontallayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_5.setSpacing(0)
        self.horizontallayout_5.setObjectName('horizontallayout_5')
        self.number_of_characters = QtWidgets.QSpinBox(self.spin_boxes_frame)
        self.number_of_characters.setMinimum(1)
        self.number_of_characters.setMaximum(64)
        self.number_of_characters.setObjectName('number_of_characters')
        self.horizontallayout_5.addWidget(self.number_of_characters)
        self.number_of_passwords = QtWidgets.QSpinBox(self.spin_boxes_frame)
        self.number_of_passwords.setMinimum(1)
        self.number_of_passwords.setObjectName('number_of_passwords')
        self.horizontallayout_5.addWidget(self.number_of_passwords)
        self.verticallayout_3.addWidget(self.spin_boxes_frame)
        self.horizontallayout_4.addWidget(self.spins_frame)

        self.characters_label.setText('Number of Characters')
        self.passwords_label.setText('Number of Passwords')
        
        self.close_button_frame = QtWidgets.QFrame(self.options_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button_frame.sizePolicy().hasHeightForWidth())
        
        self.close_button_frame.setSizePolicy(sizePolicy)
        self.close_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close_button_frame.setObjectName('close_button_frame')
        self.verticallayout_4 = QtWidgets.QVBoxLayout(self.close_button_frame)
        self.verticallayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticallayout_4.setSpacing(0)
        self.verticallayout_4.setObjectName('verticallayout_4')
        self.close_options_button = QtWidgets.QPushButton(self.close_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_options_button.sizePolicy().hasHeightForWidth())
        self.close_options_button.setSizePolicy(sizePolicy)
        self.close_options_button.setObjectName('close_options_button')
        self.verticallayout_4.addWidget(self.close_options_button)
        self.horizontallayout_4.addWidget(self.close_button_frame)
                
        self.close_options_button.setText('⇪')

        # Connect options close button to options_close function
        self.close_options_button.clicked.connect(self.close_menu)
    

    def open_password_ouput(self):
        if not self.password_output_open:
            self.password_ui()
            self.generate_passwords()
        else:
            self.generate_passwords()



    def close_password_ouput(self):
        self.create_main_ui()


    def password_ui(self):

        # Set open flag
        self.password_output_open = True

        # Change menu button to 'open'
        self.menu_button.setText('☷')

        # Create output frame
        self.output_frame = QtWidgets.QFrame(self.centralWidget)
        self.output_frame.setObjectName('output_frame')
        self.horizontallayout_14 = QtWidgets.QHBoxLayout(self.output_frame)
        self.horizontallayout_14.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontallayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontallayout_14.setSpacing(0)
        self.horizontallayout_14.setObjectName('horizontallayout_14')

        # Add output frame to layout
        self.verticalLayout_10.addWidget(self.output_frame)

        # Create output box
        self.password_output = QtWidgets.QTextEdit(self.output_frame)
        self.password_output.setReadOnly(True)
        self.password_output.setSizePolicy(QtWidgets.QSizePolicy.Preferred, 
                                           QtWidgets.QSizePolicy.Expanding)
        self.password_output.setStyleSheet('font: bold 12px;'
                                           'background: #FFFFFF; '
                                           'border: 1px solid #272727')

        self.horizontallayout_14.addWidget(self.password_output)




    def generate_passwords(self):

        # Increase window size
        self.resize(500, 250)

        # Clear the output box
        self.password_output.setText('')

        # Set strings to get characters from
        # Numbers
        numbers = string.digits
        # Letters
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        # Special Characters
        special_characters = '!@#$%^&*()\{\}[]?,.'

        # Init output character string
        output_characters = ''

        # Init empty password list
        final_password_list = []

        # Check user has used a lowercase_checkbox, add characters from strings relative to checkboxes, generate password
        if True in [self.numbers_checkbox.isChecked(), 
                    self.lowercase_checkbox.isChecked(), 
                    self.uppercase_checkbox.isChecked(),
                    self.special_characters_checkbox.isChecked()]:

            output_characters = (numbers * self.numbers_checkbox.isChecked() 
                                  + lowercase * self.lowercase_checkbox.isChecked() 
                                  + uppercase * self.uppercase_checkbox.isChecked() 
                                  + special_characters * self.special_characters_checkbox.isChecked())
            # Check how many passwords the user requires, generate for that amount
            for i in range(0, self.number_of_passwords.value()):

                password = ''.join(random.choice(output_characters) for i in range(self.number_of_characters.value()))

                final_password_list.append(password)

        # If user hasn't selected a lowercase_checkbox, inform them in a popup
        else:
            informer = QMessageBox()
            #informer.setWindowTitle('Passwordy - Error')
            informer.setStandardButtons(QMessageBox.Ok)
            informer.setDefaultButton(QMessageBox.Ok)
                # Warning text
            informer.setText('Error: ' + '\n' + 'You must make a selection using one of the checkboxes, please try again...')
            informer.exec_()

        # Add each password in the password list to the output box
        for i in final_password_list:
            self.password_output.append(i)


    def mousePressEvent(self, event):
        self.offset = event.pos()


    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)
    
 
# Run App
def main():
 
    app = QtWidgets.QApplication(sys.argv)
 
    main = Passwordy()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    
    main()
