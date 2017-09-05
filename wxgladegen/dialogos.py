#!/usr/bin/env python
# -*- coding: US-ASCII -*-
#
# generated by wxGlade 0.7.1 on Tue Sep  5 14:52:41 2017
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Dialog_snapshot(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dialog_snapshot.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "Nombre:")
        self.nombre_snap = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_2 = wx.StaticText(self, wx.ID_ANY, u"Descripci\u00f3n:")
        self.descripcion_snap = wx.TextCtrl(self, wx.ID_ANY, "")
        self.checkbox_memory = wx.CheckBox(self, wx.ID_ANY, "memory")
        self.checkbox_quiesce = wx.CheckBox(self, wx.ID_ANY, "quiesce")
        self.snap_ok = wx.Button(self, wx.ID_OK, "OK")
        self.snap_cancel = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dialog_snapshot.__set_properties
        self.SetTitle("dialogo_snapshot")
        self.nombre_snap.SetMinSize((300, 20))
        self.descripcion_snap.SetMinSize((300, 20))
        self.checkbox_memory.SetValue(1)
        self.snap_ok.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dialog_snapshot.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.FlexGridSizer(4, 2, 10, 10)
        grid_sizer_2.Add(self.label_1, 0, 0, 0)
        grid_sizer_2.Add(self.nombre_snap, 0, 0, 0)
        grid_sizer_2.Add(self.label_2, 0, 0, 0)
        grid_sizer_2.Add(self.descripcion_snap, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_memory, 0, 0, 0)
        grid_sizer_2.Add(self.checkbox_quiesce, 0, 0, 0)
        grid_sizer_2.Add(self.snap_ok, 0, wx.ALIGN_RIGHT | wx.RIGHT, 0)
        grid_sizer_2.Add(self.snap_cancel, 0, 0, 0)
        grid_sizer_2.AddGrowableCol(1)
        sizer_2.Add(grid_sizer_2, 1, wx.ALL | wx.EXPAND, 10)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Dialog_snapshot

class Dialogo_texto(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dialogo_texto.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.salida_texto = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.bnt_salida_ok = wx.Button(self, wx.ID_OK, "OK")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dialogo_texto.__set_properties
        self.SetTitle("dialogo_texto")
        self.SetSize((575, 303))
        self.salida_texto.SetMinSize((391, 200))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dialogo_texto.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.salida_texto, 0, wx.ADJUST_MINSIZE | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 4)
        sizer_1.Add(self.bnt_salida_ok, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.RIGHT, 5)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class Dialogo_texto

class Dialogo_user_pass(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dialogo_user_pass.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, "Usuario:")
        self.usuario = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_4 = wx.StaticText(self, wx.ID_ANY, "Password:")
        self.password = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.button_OK = wx.Button(self, wx.ID_OK, "OK")
        self.button_cancel = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dialogo_user_pass.__set_properties
        self.SetTitle("user_pass")
        self.usuario.SetMinSize((300, 20))
        self.label_4.Hide()
        self.password.SetMinSize((300, 20))
        self.password.Hide()
        self.button_OK.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dialogo_user_pass.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_4 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(2, 2, 5, 5)
        grid_sizer_1.Add(self.label_3, 0, 0, 0)
        grid_sizer_1.Add(self.usuario, 0, 0, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.password, 0, 0, 0)
        grid_sizer_1.AddGrowableCol(0)
        sizer_3.Add(grid_sizer_1, 1, wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 10)
        grid_sizer_4.Add(self.button_OK, 0, 0, 0)
        grid_sizer_4.Add(self.button_cancel, 0, wx.ALIGN_RIGHT, 0)
        sizer_3.Add(grid_sizer_4, 1, wx.ALIGN_RIGHT | wx.ALL, 4)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Dialogo_user_pass

class Dialogo_ejecutando(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dialogo_ejecutando.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.titulo = wx.StaticText(self, wx.ID_ANY, "Accediendo al sistema: ", style=wx.ALIGN_CENTER)
        self.elementos = wx.StaticText(self, wx.ID_ANY, "000000", style=wx.ALIGN_CENTER)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dialogo_ejecutando.__set_properties
        self.SetTitle("Ejecutando...")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dialogo_ejecutando.__do_layout
        grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3.Add(self.titulo, 0, wx.ALIGN_CENTER | wx.ALL, 4)
        grid_sizer_3.Add(self.elementos, 0, wx.ALIGN_CENTER | wx.ALL, 4)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Dialogo_ejecutando

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        wx.Frame.__init__(self, *args, **kwds)
        self.label_5 = wx.StaticText(self, wx.ID_ANY, "Cadena Busqueda:")
        self.text_ctrl_bucar = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_buscar = wx.Button(self, wx.ID_ANY, "Buscar")
        self.label_6 = wx.StaticText(self, wx.ID_ANY, "total VM: 333")
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("/Users/wbug/Documents/pyvmwareclient/wxglade/recicla.png", wx.BITMAP_TYPE_ANY))
        self.list_ctrl_1 = wx.ListCtrl(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.text_ctrl_bucar.SetMinSize((200, 20))
        self.button_buscar.SetMinSize((85, 40))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(self.label_5, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.text_ctrl_bucar, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 7)
        sizer_5.Add(self.button_buscar, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        sizer_5.Add(self.bitmap_button_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(sizer_5, 1, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 6)
        sizer_4.Add(self.list_ctrl_1, 1, 0, 0)
        self.SetSizer(sizer_4)
        sizer_4.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class Dialogo_acceso_vcenter(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dialogo_acceso_vcenter.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.label_7 = wx.StaticText(self, wx.ID_ANY, "Vcenter / esxi:")
        self.nombre_vcenter = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_9 = wx.StaticText(self, wx.ID_ANY, "Login:")
        self.login_vcenter = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_10 = wx.StaticText(self, wx.ID_ANY, "Password:")
        self.passwor_vcenter = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.label_8 = wx.StaticText(self, wx.ID_ANY, "Puerto:")
        self.puert_vcenter = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_Exit = wx.Button(self, wx.ID_CANCEL, "Exit")
        self.button_Connect = wx.Button(self, wx.ID_OK, "Conectar")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dialogo_acceso_vcenter.__set_properties
        self.SetTitle("dialog_acces_vcenter_esxi")
        self.SetSize((428, 222))
        self.nombre_vcenter.SetMinSize((300, 20))
        self.login_vcenter.SetMinSize((300, 20))
        self.passwor_vcenter.SetMinSize((300, 20))
        self.puert_vcenter.SetMinSize((84, 21))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dialogo_acceso_vcenter.__do_layout
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_6 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_5 = wx.FlexGridSizer(4, 2, 5, 5)
        grid_sizer_5.Add(self.label_7, 0, 0, 0)
        grid_sizer_5.Add(self.nombre_vcenter, 0, 0, 0)
        grid_sizer_5.Add(self.label_9, 0, 0, 0)
        grid_sizer_5.Add(self.login_vcenter, 0, 0, 0)
        grid_sizer_5.Add(self.label_10, 0, 0, 0)
        grid_sizer_5.Add(self.passwor_vcenter, 0, 0, 0)
        grid_sizer_5.Add(self.label_8, 0, 0, 0)
        grid_sizer_5.Add(self.puert_vcenter, 0, 0, 0)
        sizer_6.Add(grid_sizer_5, 1, wx.ALIGN_CENTER | wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 10)
        grid_sizer_6.Add(self.button_Exit, 0, 0, 0)
        grid_sizer_6.Add(self.button_Connect, 0, 0, 0)
        sizer_6.Add(grid_sizer_6, 1, wx.ALIGN_RIGHT | wx.ALL, 4)
        self.SetSizer(sizer_6)
        self.Layout()
        # end wxGlade

# end of class Dialogo_acceso_vcenter
