import dearpygui.dearpygui as dpg
from time import sleep
from src.Corelia.Program import Corely, _close_api
from src.auth.database import add_user, get_all_users


try:
    class AuthPage():
        def __init__(self) -> None:
            self.locked: int = []
            self.login_username: str = ""
            self.login_password_counter: int = 0
            self.password_show: bool = True  # Sign up Checker
            self.password_show2: bool = True  # Login Checker
            dpg.create_context()
            dpg.create_viewport(title='Authorization: SIGN UP ALOWE', width=390, height=100)

            with dpg.window(tag="main", no_collapse=True, no_title_bar=True, no_resize=True,
                            no_close=True, no_move=True, width=390, height=100):
                dpg.add_text("SIGN UP PAGE")
                dpg.add_spacing(count=5)
                dpg.add_input_text(tag="username", label="USERNAME")
                dpg.add_spacing(count=3)
                dpg.add_input_text(tag="passw", label="PASSWORD", password=True)
                dpg.add_spacing(count=2)
                dpg.add_input_text(tag="passw2", label="CONFIRM PASSWORD", password=True)
                dpg.add_spacing(count=2)
                dpg.add_button(label="Show / Hide Password", callback=self._shown_hide)
                dpg.add_spacing(count=2)
                dpg.add_button(tag="senda", label="SUBMIT", callback=self._submit)
                dpg.add_spacing(count=2)
                dpg.add_button(label="LOGIN INSTEAD", callback=self._login_page)

            with dpg.window(tag="logins", no_collapse=True, no_title_bar=True, no_resize=True,
                            no_close=True, no_move=True, width=390, height=100):
                dpg.add_text("LOGIN PAGE")
                dpg.add_spacing(count=5)
                dpg.add_input_text(tag="usernamed", label="USERNAME")
                dpg.add_spacing(count=3)
                dpg.add_input_text(tag="passwd", label="PASSWORD", password=True)
                dpg.add_spacing(count=2)
                dpg.add_button(label="Show / Hide Password", callback=self._shown_hide2)
                dpg.add_spacing(count=2)
                dpg.add_button(tag="sendad", label="SUBMIT", callback=self._submit2)
                dpg.add_spacing(count=2)
                dpg.add_button(label="SIGN UP INSTEAD", callback=self._sign_page)

            self._login_page() # Login page by default

        
        def _sign_page(self):
            dpg.hide_item("logins") 
            dpg.set_viewport_title("Authorization: SIGN UP ALOWE")
            dpg.show_item("main")      
            dpg.set_primary_window("main", True)


        def _submit2(self, sender, data):
            bar = get_all_users()
            username: str = dpg.get_value("usernamed")
            password: str = dpg.get_value("passwd")
            Corelian: Corely = Corely()
            dpg.configure_item("sendad", label="Checking...")
            password = Corelian.SentinelEn(unlocking=password, secret=password)
            password = Corelian.CryoSecureEncrypt(secret=password, shifting=14)
            
            
            for i in bar:
                if i[1] == username:
                    password: bool = Corelian.CryoSecureCrusherChecker(password, i[2])
                    if i[1] == self.login_username and self.login_password_counter >= 3 or username in self.locked:
                        self.locked.append(self.login_username)
                        dpg.configure_item("sendad", label="This user is locked.")
                        self.login_username: str = ""
                        self.login_password_counter: int = 0
                        sleep(1.2)
                        dpg.configure_item("sendad", label="SUBMIT")
                        break
                    
                    elif password:
                        # TODO ADD APP HERE
                        print("Password correct")

                    else:
                        self.login_username = username
                        self.login_password_counter += 1
                        dpg.configure_item("sendad", label="Username / Password Wrong.")
                        sleep(1.2)
                        dpg.configure_item("sendad", label="SUBMIT")

                else:
                    dpg.configure_item("sendad", label="Username / Password Wrong.")
                    sleep(1.2)
                    dpg.configure_item("sendad", label="SUBMIT")
            


        def _shown_hide2(self) -> None:
            if self.password_show2:
                dpg.configure_item("passwd", label="PASSWORD", password=False)
                self.password_show2 = False
            else:
                dpg.configure_item("passwd", label="PASSWORD", password=True)
                self.password_show2 = True


        def _login_page(self):
            dpg.hide_item("main")
            dpg.set_viewport_title("Authorization: LOGIN ALOWE")
            dpg.show_item("logins")
            dpg.set_primary_window("logins", True)


        def _submit(self, sender, data):
            username: str = dpg.get_value("username")
            password: str = dpg.get_value("passw")
            confirmed_password: str = dpg.get_value("passw2")

            if confirmed_password == password:
                if password == username:
                    dpg.configure_item("senda", label="Choose another password")
                    sleep(1.2)
                    dpg.configure_item("senda", label="SUBMIT")
                    
                else:
                    bar = get_all_users()
                    create: bool = True
                    for i in bar:
                        if i[1] == username:
                            dpg.configure_item("senda", label="Username already exists")
                            sleep(1.2)
                            dpg.configure_item("senda", label="SUBMIT")
                            create = False
                            break
                    l, d, p , ur = self.check_string(password)
                    if len(password) <= 7:
                        dpg.configure_item("senda", label="Not enough characters")
                        sleep(1.2)
                        create = False
                        dpg.configure_item("senda", label="SUBMIT")
                    elif l <= 3:
                        dpg.configure_item("senda", label="Not enough letters")
                        sleep(1.2)
                        create = False
                        dpg.configure_item("senda", label="SUBMIT")
                    elif d <= 2:
                        dpg.configure_item("senda", label="Not enough digits")
                        sleep(1.2)
                        create = False
                        dpg.configure_item("senda", label="SUBMIT")
                    elif p <= 1:
                        dpg.configure_item("senda", label="Not enough punctuations")
                        sleep(1.2)
                        create = False
                        dpg.configure_item("senda", label="SUBMIT")
                    elif create:
                        dpg.configure_item("senda", label="Creating account...", enabled=False)
                        Corelian: Corely = Corely()
                        password = Corelian.SentinelEn(unlocking=password, secret=password)
                        password = Corelian.CryoSecureEncrypt(secret=password, shifting=14)
                        password = Corelian.CryoSecureCrusher(secret=password, workfactor=15)
                        add_user(username, password)
                        dpg.configure_item("senda", label="Account created!")
                        sleep(1)
                        dpg.configure_item("senda", label="SUBMIT", enabled=True)
                        dpg.configure_item("username", value="")
                        dpg.configure_item("passw", value="")
                        dpg.configure_item("passw2", value="")

            else:
                dpg.configure_item("senda", label="Password does not match")
                sleep(1.2)
                dpg.configure_item("senda", label="SUBMIT")

            

        def _shown_hide(self) -> None:
            if self.password_show:
                dpg.configure_item("passw", label="PASSWORD", password=False)
                dpg.configure_item("passw2", label="CONFIRM PASSWORD", password=False)
                self.password_show = False
            else:
                dpg.configure_item("passw", label="PASSWORD", password=True)
                dpg.configure_item("passw2", label="CONFIRM PASSWORD", password=True)
                self.password_show = True


        def check_string(self, s):

            punctuation_count = 0
            digit_count = 0
            letter_count = 0
            not_recognised = 0
            PUNCT = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';',
                    '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

            for char in s:
                if char.isalpha():  
                    letter_count += 1
                elif char.isdigit():
                    digit_count += 1
                elif char in PUNCT:
                    punctuation_count += 1
                else:
                    not_recognised += 1

            return letter_count, digit_count, punctuation_count, not_recognised


        def run(self):
            dpg.setup_dearpygui()
            dpg.show_viewport()
            dpg.set_primary_window("logins", True)
            dpg.start_dearpygui()
            dpg.destroy_context()

except KeyboardInterrupt:
    pass
finally:
    try:
        _close_api()
    except:
        pass