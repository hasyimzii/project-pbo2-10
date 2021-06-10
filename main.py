import mysql.connector
import wx
import wx.xrc
import wx.grid
import conn
import View

# connection & cursor database
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="pbo2_toko"
)
curs = conn.cursor()

class Login(View.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)
    def login(self, event):
        username = self.login_input1.GetValue()
        password = self.login_input2.GetValue()
        query = f'SELECT * FROM user WHERE username = "{username}" AND password = "{password}"'
        curs.execute(query)
        data = curs.fetchall()
        if data[0][3] == "pemilik":
            self.Hide()
            import pemilik
        elif data[0][3] == "manager":
            self.Hide()
            import manajer
        elif data[0][3] == "kasir":
            self.Hide()
            import kasir
        else:
            wx.MessageBox(f'Username dan Password Salah')



app = wx.App()
frame = Login(None)
frame.Show()
app.MainLoop()



