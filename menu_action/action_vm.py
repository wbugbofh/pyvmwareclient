#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import sys
import os
import wx
import ssl
import OpenSSL
import webbrowser
import logging.config
from wxgladegen import dialogos
from pyVmomi import vim

__author__ = "Mario Ezquerro."


def on_info_vm(self, event, conexion, logger):
        fila = self.listadoVM
        print (self, event, conexion)
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
            
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        
        # List about vm detail in dialog box

        self.my_dialogo_texto = dialogos.Dialogo_texto(None, -1, 'Listados de datos VM')

        vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
        if logger != None: logger.info('informacion vm: '+ vm.summary.config.name)
        

        snaptexto ='\n Maquna vm = ' + fila[1] + '\n'

        snaptexto +="=====================\n"
        details = {'name': vm.summary.config.name,
                   'instance UUID': vm.summary.config.instanceUuid,
                   'bios UUID': vm.summary.config.uuid,
                   'path to VM': vm.summary.config.vmPathName,
                   'guest OS id': vm.summary.config.guestId,
                   'guest OS name': vm.summary.config.guestFullName,
                   'host name': vm.runtime.host.name,
                   'last booted timestamp': vm.runtime.bootTime}

        for name, value in details.items():
            snaptexto +=u"\n  {0:{width}{base}}: {1}".format(name, value, width=25, base='s')

        snaptexto += "\n------------------------------"
        snaptexto += "\nDevices:"
        snaptexto +="\n------------------------------\n"
        for device in vm.config.hardware.device:
            # diving into each device, we pull out a few interesting bits
            dev_details = {'key': device.key,
                           'summary': device.deviceInfo.summary,
                           'device type': type(device).__name__,
                           'backing type': type(device.backing).__name__}

            snaptexto +="\n------------------\n"
            snaptexto +=u"\n  label: {0}".format(device.deviceInfo.label)

            for name, value in dev_details.items():
                snaptexto +=u"\n    {0:{width}{base}}: {1}".format(name, value, width=15, base='s')

            if device.backing is None:
                continue

            # the following is a bit of a hack, but it lets us build a summary
            # without making many assumptions about the backing type, if the
            # backing type has a file name we *know* it's sitting on a datastore
            # and will have to have all of the following attributes.
            if hasattr(device.backing, 'fileName'):
                datastore = device.backing.datastore
                if datastore:
                    snaptexto +="    datastore\n"
                    snaptexto +="        name: {0}\n".format(datastore.name)
                    # there may be multiple hosts, the host property
                    # is a host mount info type not a host system type
                    # but we can navigate to the host system from there
                    for host_mount in datastore.host:
                        host_system = host_mount.key
                        snaptexto +=u"\n        host: {0}".format(host_system.name)
                    snaptexto +="        summary"
                    summary = {'capacity': datastore.summary.capacity,
                               'freeSpace': datastore.summary.freeSpace,
                               'file system': datastore.summary.type,
                               'url': datastore.summary.url}
                    for key, val in summary.items():
                        snaptexto +=(u"\n            {0}: {1}".format(key, val))
                snaptexto +=(u"\n    fileName: {0}".format(device.backing.fileName))
                snaptexto +=(u"\n    device ID: {0}".format(device.backing.backingObjectId))

            snaptexto +="\n--------------------------------------------\n"

        snaptexto += "====================="
        self.my_dialogo_texto.salida_texto.SetValue(snaptexto)
        result = self.my_dialogo_texto.ShowModal() # pintamos la ventana con la informcion
        self.my_dialogo_texto.Destroy()






def on_set_note(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
                if logger != None: logger.info(fila[i])
        # At tree elemente are the name and the nine at the UUID

        vm = conexion.searchIndex.FindByUuid(None,fila[8], True)

        self.my_dialogo_ssh = dialogos.Dialogo_user_pass(None, -1, 'New Note in: {0}' .format(vm.name))
        punteromaquina = vim.vm.ConfigSpec()

        # the actual file 8 is the Note

        self.my_dialogo_ssh.usuario.SetValue('{0}' .format(fila[7]) )


        result = self.my_dialogo_ssh.ShowModal() # pintamos la ventan con la informcion
        if result == wx.ID_OK:
                punteromaquina.annotation = str( self.my_dialogo_ssh.usuario.GetValue())
                task = vm.ReconfigVM_Task(punteromaquina)
                tasks.wait_for_tasks(conexion, [task])
        self.my_dialogo_ssh.Destroy()




def onSnap_list(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        
        #listado de snapshot en una ventana emergente

        self.my_dialogo_texto = dialogos.Dialogo_texto(None, -1, 'Listados de Snapshots')
        vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
        snap_info = vm.snapshot
        self.my_dialogo_texto.salida_texto.SetValue('Maquna vm = ' + fila[1]  )
        snaptexto = 'Listado de snapshot \n'
        if not snap_info:
            self.my_dialogo_texto.salida_texto.SetValue('No hay snapshot')
            if logger != None: logger.info ('No hay snapshot')
        else:
            tree = snap_info.rootSnapshotList
            while tree[0].childSnapshotList is not None:
                snaptexto = snaptexto +  ("Nombre Snap: {0} = description> {1}  \n".format(tree[0].name, tree[0].description))
                if logger != None: logger.info("Snap: {0} => {1}".format(tree[0].name, tree[0].description))
                if len(tree[0].childSnapshotList) < 1:
                    break
                tree = tree[0].childSnapshotList
            self.my_dialogo_texto.salida_texto.SetValue(snaptexto)

        result = self.my_dialogo_texto.ShowModal() # pintamos la ventana con la informcion
        self.my_dialogo_texto.Destroy()


def onSnap_create(self, event, conexion, logger):

        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        #Dialogo para pedir datos para el snapshop......

        self.my_dialogo_sanshot = dialogos.Dialog_snapshot(None, -1, 'Propiedades Snapshot')

        self.my_dialogo_sanshot.nombre_snap.SetValue(fila[1] + ' Razon del snapshot? ...' )
        result = self.my_dialogo_sanshot.ShowModal()

        nombre = str(self.my_dialogo_sanshot.nombre_snap.GetValue())
        descricion = str(self.my_dialogo_sanshot.descripcion_snap.GetValue())
        checkbox_memory=self.my_dialogo_sanshot.checkbox_memory.GetValue()
        checkbox_quiesce=self.my_dialogo_sanshot.checkbox_quiesce.GetValue()


        self.my_dialogo_sanshot.Destroy()
        #if logger != None: logger.info ('resultado = ' + str(result))
        #if logger != None: logger.info('wx.ID_OK = ' + str(wx.ID_OK))

        """dlg_reset = wx.MessageDialog(self,
                                     "¿Hacer snapshot de : ? \n " + fila[1] + " ",
                                     "Confirm Exit",
                                     wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg_reset.ShowModal()
        dlg_reset.Destroy()"""

        vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
        if result == wx.ID_OK:
            if  vm  is not None:
                if logger != None: logger.info ("The current powerState is: {0}".format(vm.runtime.powerState))
                TASK = task = vm.CreateSnapshot_Task(nombre, description = descricion, memory=checkbox_memory, quiesce=checkbox_quiesce)
                #contador de tareas
                count = 0
                #state_task= task.info.state
                while task.info.state != vim.TaskInfo.State.success:
                    if logger != None: logger.info('Running => {0}  state: {1} info.result = {2}'.format(count, task.info.state, task.info.result))
                    count += 1

                #tasks.wait_for_tasks(conexion, [TASK])
                if logger != None: logger.info("Snapshot Completed.")

        #listado de snapshot en una ventana emergente

        self.my_dialogo_texto = dialogos.Dialogo_texto(None, -1, 'Listados de Snapshots')

        del vm
        vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
        snap_info = vm.snapshot
        self.my_dialogo_texto.salida_texto.SetValue('Maquna vm = ' + fila[1]  )
        snaptexto = 'Listado de snapshot \n'
        if not snap_info:
            self.my_dialogo_texto.salida_texto.SetValue('No hay snapshot')
            if logger != None: logger.info ('No hay snapshot')
        else:
            tree = snap_info.rootSnapshotList
            while tree[0].childSnapshotList is not None:
                snaptexto = snaptexto +  ("Nombre Snap: {0} = description> {1}  \n".format(tree[0].name, tree[0].description))
                if logger != None: logger.info("Snap: {0} => {1}".format(tree[0].name, tree[0].description))
                if len(tree[0].childSnapshotList) < 1:
                    break
                tree = tree[0].childSnapshotList
            self.my_dialogo_texto.salida_texto.SetValue(snaptexto)

        result = self.my_dialogo_texto.ShowModal() # pintamos la ventana con la informcion
        self.my_dialogo_texto.Destroy()


def onSsh(self, event, conexion, logger):
        if sys.platform == 'darwin':
            fila = self.listadoVM
            for i in range(len(fila)):
                if logger != None: logger.info(fila[i])
            # El tercer elemento es la ip es decier la fila[2]
            self.my_dialogo_ssh = dialogos.Dialogo_user_pass(None, -1, 'Ususario y password')
            self.my_dialogo_ssh.usuario.SetValue('root' )
            result = self.my_dialogo_ssh.ShowModal() # pintamos la ventan con la informcion
            if result == wx.ID_OK:
                comando = 'ssh ' + fila[2] +'@'+ str(self.my_dialogo_ssh.usuario.GetValue()) + ' &'
                os.system(comando)
            self.my_dialogo_ssh.Destroy()

        if os.name == 'nt' or os.name == 'posix':
            fila = self.listadoVM
            for i in range(len(fila)):
                if logger != None: logger.info(fila[i])
            # El tercer elemento es la ip es decier la fila[2]
            self.my_dialogo_ssh = dialogos.Dialogo_user_pass(None, -1, 'Ususario y password')
            self.my_dialogo_ssh.usuario.SetValue('root')
            result = self.my_dialogo_ssh.ShowModal()  # pintamos la ventan con la informcion
            if result == wx.ID_OK:
                comando = 'putty ' + fila[2] + ' -l ' + str(self.my_dialogo_ssh.usuario.GetValue()) + ' &'
                os.system(comando)
            self.my_dialogo_ssh.Destroy()


def onHtml(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El tercer elemento es la ip y el 9 es el UUID
        vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
        vm_name = vm.summary.config.name
        vm_moid = vm._moId
        if logger != None: logger.info('void= '.format(vm_moid))
        vcenter_data = conexion.setting
        vcenter_settings = vcenter_data.setting
        console_port = '9443'
        puerto_vcenter= '443'

        for item in vcenter_settings:
            key = getattr(item, 'key')
            #print ('key: ' + key + ' =>'+ str(getattr(item, 'value')))
            if key == 'VirtualCenter.FQDN':
                vcenter_fqdn = getattr(item, 'value')
                #if key == 'WebService.Ports.https':
                #console_port = str(getattr(item, 'value'))

        host = vcenter_fqdn

        session_manager = conexion.sessionManager
        session = session_manager.AcquireCloneTicket()
        vc_cert = ssl.get_server_certificate((host, int(puerto_vcenter)))
        vc_pem = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,vc_cert)
        vc_fingerprint = vc_pem.digest('sha1')

        if logger != None: logger.info("Open the following URL in your browser to access the " \
                                       "Remote Console.\n" \
                                       "You have 60 seconds to open the URL, or the session" \
                                       "will be terminated.\n")
        print(str(vcenter_data))

        # Locate the version of vcenter the object .version for locate the version of vcenter
        object_about = conexion.about
        #For version vcenter 5.5
        if object_about.version == '5.5.0':
            console_portv5 = '7331'
            URL5 = "http://" + host + ":" + console_portv5 + "/console/?vmId=" \
                   + str(vm_moid) + "&vmName=" + vm_name + "&host=" + vcenter_fqdn \
                   + "&sessionTicket=" + session + "&thumbprint=" + vc_fingerprint.decode('utf8')
            webbrowser.open(URL5, new=1, autoraise=True)

        #For version vcenter 6.0 and 6.5
        if object_about.version == '6.0.0' or object_about.version == '6.5.0':
            URL = "https://" + host + ":" + console_port + "/vsphere-client/webconsole.html?vmId=" \
                  + str(vm_moid) + "&vmName=" + vm_name + "&host=" + vcenter_fqdn \
                  + "&sessionTicket=" + session + "&thumbprint.info=" + vc_fingerprint.decode('utf-8')
            if logger != None: logger.info(URL)
            webbrowser.open(URL, new=1, autoraise=True)
            if logger != None: logger.info ("Waiting for 60 seconds, then exit")




def onRdp(self, event, conexion, logger):
        if sys.platform == 'darwin':
            fila = self.listadoVM
            for i in range(len(fila)):
                if logger != None: logger.info(fila[i])
            # El tercer elemento es la ip es decier la fila[2]
            ruta_fichero_config = os.getcwd()
            archConfiguracion = open('conexion.rdp', 'w')
            archConfiguracion.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">' + '\n')
            archConfiguracion.write('<plist version="1.0">' + '\n')
            archConfiguracion.write('<dict>' + '\n')
            archConfiguracion.write('<key>AddToKeychain</key>' + '\n')
            archConfiguracion.write('<true/>' + '\n')
            archConfiguracion.write('<key>ApplicationPath</key>' + '\n')
            archConfiguracion.write('<string></string>' + '\n')
            archConfiguracion.write('<key>AudioRedirectionMode</key>' + '\n')
            archConfiguracion.write('<integer>0</integer>' + '\n')
            archConfiguracion.write('<key>AuthenticateLevel</key>' + '\n')
            archConfiguracion.write('<integer>0</integer>' + '\n')
            archConfiguracion.write('<key>AutoReconnect</key>' + '\n')
            archConfiguracion.write('<true/>' + '\n')
            archConfiguracion.write('<key>BitmapCaching</key>' + '\n')
            archConfiguracion.write('<true/>' + '\n')
            archConfiguracion.write('<key>ColorDepth</key>' + '\n')
            archConfiguracion.write('<integer>1</integer>' + '\n')
            archConfiguracion.write('<key>ConnectionString</key>' + '\n')
            archConfiguracion.write('<string>' + fila[2] + '</string>' + '\n')
            archConfiguracion.write('<key>DesktopSize</key>' + '\n')
            archConfiguracion.write('' + '\n')
            archConfiguracion.write('' + '\n')
            archConfiguracion.write('' + '\n')
            archConfiguracion.write('' + '\n')
            archConfiguracion.write('</dict>' + '\n')
            archConfiguracion.write('</plist>' + '\n')
            archConfiguracion.close
            comando = 'open -a \"Remote Desktop Connection.app\" ' + ruta_fichero_config +'/conexion.rdp' + ' &'
            os.system(comando)

        if os.name == 'nt':
            fila = self.listadoVM
            for i in range(len(fila)):
                if logger != None: logger.info(fila[i])
            # El tercer elemento es la ip es decier la fila[2]
            comando = 'mstsc ' +'/v:'+ fila[2]
            os.system(comando)

        if os.name == 'posix':
            fila = self.listadoVM
            for i in range(len(fila)):
                if logger != None: logger.info(fila[i])
            # El tercer elemento es la ip osea la fila 2
            ruta_fichero_config = os.getcwd()
            archConfiguracion = open('remminaconfig.remmina','w')
            archConfiguracion.write('[remmina]' + '\n')
            archConfiguracion.write('disableclipboard=0' + '\n')
            archConfiguracion.write('ssh_auth=0' + '\n')
            archConfiguracion.write('clientname=' + '\n')
            archConfiguracion.write('quality=0' + '\n')
            archConfiguracion.write('ssh_charset=' + '\n')
            archConfiguracion.write('ssh_privatekey=' + '\n')
            archConfiguracion.write('sharesmartcard=0' + '\n')
            archConfiguracion.write('resolution=' + '\n')
            archConfiguracion.write('group=' + '\n')
            archConfiguracion.write('password=' + '\n')
            archConfiguracion.write('name=' + fila[1] + '\n')
            archConfiguracion.write('ssh_loopback=0' + '\n')
            archConfiguracion.write('sharelogger.infoer=0' + '\n')
            archConfiguracion.write('ssh_username=' + '\n')
            archConfiguracion.write('ssh_server=' + '\n')
            archConfiguracion.write('security=' + '\n')
            archConfiguracion.write('protocol=RDP' + '\n')
            archConfiguracion.write('execpath=' + '\n')
            archConfiguracion.write('sound=off' + '\n')
            archConfiguracion.write('exec=' + '\n')
            archConfiguracion.write('ssh_enabled=0' + '\n')
            archConfiguracion.write('username=' + '\n')
            archConfiguracion.write('sharefolder=' + '\n')
            archConfiguracion.write('console=0' + '\n')
            archConfiguracion.write('domain=' + '\n')
            archConfiguracion.write('server=' +fila[2] + '\n')
            archConfiguracion.write('colordepth=24' + '\n')
            archConfiguracion.write('window_maximize=0' + '\n')
            archConfiguracion.write('window_height=' + '\n')
            archConfiguracion.write('window_width=' + '\n')
            archConfiguracion.write('viewmode=1' + '\n')
            archConfiguracion.write('scale=1' + '\n')
            archConfiguracion.close
            comando = 'remmina -c ' + ruta_fichero_config +'/remminaconfig.remmina' + ' &'
            os.system(comando)



# url del VMRC https://www.vmware.com/go/download-vmrc

def onsoftreboot(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        #Pedimos confirmacion del reset de la mv con ventana dialogo
        dlg_reset = wx.MessageDialog(self,
                                     "Estas a punto de reiniciar \n " + fila[1] + " ",
                                     "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg_reset.ShowModal()
        dlg_reset.Destroy()

        if result == wx.ID_OK:
            vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
            if  vm  is not None:

                if logger != None: logger.info ("The current powerState is: {0}".format(vm.runtime.powerState))
                TASK = vm.RebootGuest()
                #Este da error tasks.wait_for_tasks(conexion, [TASK])
                if logger != None: logger.info("Soft reboot its done.")


def onsoftPowerOff(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        #Pedimos confirmacion del reset de la mv con ventana dialogo
        dlg_reset = wx.MessageDialog(self,
                                     "Estas a punto de Soft Apagar \n " + fila[1] + " ",
                                     "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg_reset.ShowModal()
        dlg_reset.Destroy()

        if result == wx.ID_OK:
            vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
            if  vm  is not None:

                if logger != None: logger.info ("The current powerState is: {0}".format(vm.runtime.powerState))
                TASK = vm.ShutdownGuest()
                #Este da error tasks.wait_for_tasks(conexion, [TASK])
                if logger != None: logger.info("Soft poweroff its done.")


    # Reiniciamos el ordenador seleccionado en el menu contextual
def onreboot(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        #Pedimos confirmacion del reset de la mv con ventana dialogo
        dlg_reset = wx.MessageDialog(self,
                                     "Estas a punto de reiniciar \n " + fila[1] + " ",
                                     "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg_reset.ShowModal()
        dlg_reset.Destroy()

        if result == wx.ID_OK:
            vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
            if  vm  is not None:

                if logger != None: logger.info ("The current powerState is: {0}".format(vm.runtime.powerState))
                TASK = vm.ResetVM_Task()
                tasks.wait_for_tasks(conexion, [TASK])
                if logger != None: logger.info("reboot its done.")

def onpower_on(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        #Pedimos confirmacion del poweron de la mv con ventana dialogo
        dlg_reset = wx.MessageDialog(self,
                                     "Estas a punto de iniciar \n " + fila[1] + "\nAhora esta:  " + fila[3],
                                     "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg_reset.ShowModal()
        dlg_reset.Destroy()

        if result == wx.ID_OK:
            vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
            if  vm  is not None and not vm.runtime.powerState == 'poweredOn':
                if logger != None: logger.info ("The current powerState is: {0}".format(vm.runtime.powerState))
                TASK = vm.PowerOn()
                tasks.wait_for_tasks(conexion, [TASK])
                if logger != None: logger.info("Power ON  its done.")


def onpowerOff(self, event, conexion, logger):
        fila = self.listadoVM
        for i in range(len(fila)):
            if logger != None: logger.info(fila[i])
        # El 9 elemento es el UUID
        if logger != None: logger.info (fila[8])
        #Pedimos confirmacion del reset de la mv con ventana dialogo
        dlg_reset = wx.MessageDialog(self,
                                     "Estas a punto de Apagar \n " + fila[1] + " ",
                                     "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg_reset.ShowModal()
        dlg_reset.Destroy()

        if result == wx.ID_OK:
            vm = conexion.searchIndex.FindByUuid(None,fila[8], True)
            if  vm  is not None and not vm.runtime.powerState == 'poweredOff':
                if logger != None: logger.info ("The current powerState is: {0}".format(vm.runtime.powerState))
                TASK = vm.PowerOff()
                tasks.wait_for_tasks(conexion, [TASK])
                if logger != None: logger.info("Power OFF its done.")


