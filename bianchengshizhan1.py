import wx
import wx.grid as wg
import openpyxl

class MyFrame1(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'主界面',pos=(230,120),size=(1000,700),style = wx.DEFAULT_FRAME_STYLE)
        self.SetMaxSize((1000, 700))
        self.panel = wx.Panel(self,size=(1000, 700))
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

        self.font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.LIGHT)
        self.bt_game = wx.Button(self.panel, label='最受欢迎的商圈', pos=(390,50),size=(200, 60), style=0)
        self.bt_game.SetBackgroundColour('DARK TURQUOISE')
        self.bt_game.SetForegroundColour('FIREBRICK')
        self.bt_game.SetFont(font=font)
        self.bt_game.Bind(wx.EVT_BUTTON, self.zshysq)
        self.bt_rank = wx.Button(self.panel, label='美食餐厅', pos=(390,200),size=(200, 60))
        self.bt_rank.Bind(wx.EVT_BUTTON, self.msct)
        self.bt_rank.SetBackgroundColour('LIGHT STEEL BLUE')
        self.bt_rank.SetForegroundColour('FIREBRICK')
        self.bt_rank.SetFont(font=font)
        self.bt_history = wx.Button(self.panel, label='最佳美食聚集地', pos=(390,350),size=(200, 60), style=0)
        self.bt_history.Bind(wx.EVT_BUTTON, self.zjmsjjd)
        self.bt_history.SetBackgroundColour('DARK TURQUOISE')
        self.bt_history.SetForegroundColour('FIREBRICK')
        self.bt_history.SetFont(font=font)
        self.bt_room = wx.Button(self.panel, label='服饰类最佳评分商圈', pos=(390,500),size=(200, 60))
        self.bt_room.Bind(wx.EVT_BUTTON,self.fslzjpfsq)
        self.bt_room.SetBackgroundColour('LIGHT STEEL BLUE')
        self.bt_room.SetForegroundColour('FIREBRICK')
        self.bt_room.SetFont(font=font)


        self.panel2 = wx.Panel(self, size=(1000, 700))
        self.panel2.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack1)
        self.bt_re2=wx.Button(self.panel2, label='返回',pos=(10, 10), size=(80, 40), style=0)
        self.bt_re2.SetBackgroundColour('white')
        self.bt_re2.SetFont(self.font)
        self.bt_re2.Bind(wx.EVT_BUTTON,self.re2)
        self.grid2 = wg.Grid(self.panel2, -1)
        self.grid2.CreateGrid(10, 4)
        self.grid2.SetSize((663, 290))
        self.grid2.SetPosition((150, 180))
        for i in range(3):
            self.grid2.SetColSize(i, 160)
        for i in range(10):
            self.grid2.SetRowSize(i, 40)
        for i in range(10):
            if not (i % 2):
                self.grid2.SetCellBackgroundColour(i, 0, 'TURQUOISE')
                self.grid2.SetCellBackgroundColour(i, 2, 'TURQUOISE')
                self.grid2.SetCellBackgroundColour(i, 1, 'TURQUOISE')
                self.grid2.SetCellBackgroundColour(i, 3, 'TURQUOISE')
        self.grid2.SetColLabelValue(0, "餐厅名")
        self.grid2.SetColLabelValue(1, "餐厅地址")
        self.grid2.SetColLabelValue(2, "消费均额")
        self.grid2.SetColLabelValue(3, "菜型")
        self.grid2.SetLabelBackgroundColour('white')
        self.grid2.SetCellValue(0,0,'华莱士（福兴店）')
        self.grid2.SetCellAlignment(0, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        
        self.panel2.Hide()

        self.panel3 = wx.Panel(self, size=(1000, 700))
        self.panel3.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack1)
        self.bt_re3 = wx.Button(self.panel3, label='返回',pos=(10, 10), size=(80, 40), style=0)
        self.bt_re3.SetBackgroundColour('white')
        self.bt_re3.SetFont(self.font)
        self.bt_re3.Bind(wx.EVT_BUTTON, self.re3)
        self.grid1 = wg.Grid(self.panel3, -1)
        self.grid1.CreateGrid(10, 4)
        self.grid1.SetSize((663, 290))
        self.grid1.SetPosition((150, 180))
        for i in range(3):
            self.grid1.SetColSize(i, 160)
        for i in range(10):
            self.grid1.SetRowSize(i,40)
        for i in range(10):
            if not (i % 2):
                self.grid1.SetCellBackgroundColour(i, 0, 'TURQUOISE')
                self.grid1.SetCellBackgroundColour(i, 2, 'TURQUOISE')
                self.grid1.SetCellBackgroundColour(i, 1, 'TURQUOISE')
                self.grid1.SetCellBackgroundColour(i, 3, 'TURQUOISE')
        self.grid1.SetColLabelValue(0, "餐厅名")
        self.grid1.SetColLabelValue(1, "餐厅地址")
        self.grid1.SetColLabelValue(2, "消费均额")
        self.grid1.SetColLabelValue(3, "评分")
        self.grid1.SetLabelBackgroundColour('white')
        self.panel3.Hide()

        self.panel4 = wx.Panel(self, size=(1000, 700))
        self.panel4.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack1)
        self.bt_re4 = wx.Button(self.panel4, label='返回', pos=(10, 10), size=(80, 40), style=0)
        self.bt_re4.SetBackgroundColour('white')
        self.bt_re4.SetFont(self.font)
        self.bt_re4.Bind(wx.EVT_BUTTON, self.re4)
        self.grid4 = wg.Grid(self.panel4, -1)
        self.grid4.CreateGrid(10, 4)
        self.grid4.SetSize((663, 290))
        self.grid4.SetPosition((150, 180))
        for i in range(3):
            self.grid4.SetColSize(i, 160)
        for i in range(10):
            self.grid4.SetRowSize(i, 40)
        for i in range(10):
            if not (i % 2):
                self.grid4.SetCellBackgroundColour(i, 0, 'TURQUOISE')
                self.grid4.SetCellBackgroundColour(i, 2, 'TURQUOISE')
                self.grid4.SetCellBackgroundColour(i, 1, 'TURQUOISE')
                self.grid4.SetCellBackgroundColour(i, 3, 'TURQUOISE')
        self.grid4.SetColLabelValue(0, "餐厅名")
        self.grid4.SetColLabelValue(1, "餐厅地址")
        self.grid4.SetColLabelValue(2, "消费均额")
        self.grid4.SetColLabelValue(3, "评分")
        self.grid4.SetLabelBackgroundColour('white')
        self.panel4.Hide()

        self.panel5 = wx.Panel(self, size=(1000, 700))
        self.panel5.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack1)
        self.bt_re5 = wx.Button(self.panel5, label='返回', pos=(10, 10), size=(80, 40), style=0)
        self.bt_re5.SetBackgroundColour('white')
        self.bt_re5.SetFont(self.font)
        self.bt_re5.Bind(wx.EVT_BUTTON, self.re5)
        self.grid5 = wg.Grid(self.panel5, -1)
        self.grid5.CreateGrid(10, 4)
        self.grid5.SetSize((663, 290))
        self.grid5.SetPosition((150, 180))
        for i in range(3):
            self.grid5.SetColSize(i, 160)
        for i in range(10):
            self.grid5.SetRowSize(i, 40)
        for i in range(10):
            if not (i % 2):
                self.grid5.SetCellBackgroundColour(i, 0, 'TURQUOISE')
                self.grid5.SetCellBackgroundColour(i, 2, 'TURQUOISE')
                self.grid5.SetCellBackgroundColour(i, 1, 'TURQUOISE')
                self.grid5.SetCellBackgroundColour(i, 3, 'TURQUOISE')
        self.grid5.SetColLabelValue(0, "餐厅名")
        self.grid5.SetColLabelValue(1, "餐厅地址")
        self.grid5.SetColLabelValue(2, "消费均额")
        self.grid5.SetColLabelValue(3, "评分")
        self.grid5.SetLabelBackgroundColour('white')
        self.panel5.Hide()

    def OnEraseBack1(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp1 = wx.Bitmap("90/zjm.png")
        dc.DrawBitmap(bmp1, 0, 150)

    def vvvvt(self):
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.bt_game, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        vsizer_all.Add(self.bt_rank, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        vsizer_all.Add(self.bt_history, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        vsizer_all.Add(self.bt_room, proportion=0, flag=wx.ALIGN_CENTER|wx.ALL, border=45)
        self.panel.SetSizer(vsizer_all)

    def OnEraseBack(self,event):
            dc = event.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                rect = self.GetUpdateRegion().GetBox()
                dc.SetClippingRect(rect)
            dc.Clear()
            bmp = wx.Bitmap("90/zjm.png")
            dc.DrawBitmap(bmp, 0, 200)

    def zshysq(self,event):
        '''self.bt_history.Hide()
        self.bt_rank.Hide()
        self.bt_room.Hide()
        self.bt_game.Hide()'''
        self.panel.Hide()
        self.panel2.Show()

    def msct(self,event):
        self.panel.Hide()
        self.panel3.Show()

    def zjmsjjd(self,event):
        self.panel.Hide()
        self.panel4.Show()

    def fslzjpfsq(self,event):
        self.panel.Hide()
        self.panel5.Show()

    def re2(self,event):
        self.panel2.Hide()
        self.panel.Show()

    def re3(self,event):
        self.panel3.Hide()
        self.panel.Show()

    def re4(self,event):
        self.panel4.Hide()
        self.panel.Show()

    def re5(self,event):
        self.panel5.Hide()
        self.panel.Show()


if __name__=='__main__':
    app=wx.App()
    frame=MyFrame1(None,-1)
    frame.Show()
    app.MainLoop()
