import logging
logger = logging.getLogger('[Aethernum]')

import ui
import net
import wndmgr
import snd
import settings
import ServerStateChecker
import random
import app
import systemsetting
import dbg

import database
import database_manager as dbMgr

class LoginWindow(ui.Image):
	def __init__(self):
		super().__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)
		self.set_image('root/images/background/background.png')

		self.image_logo = ui.Image()
		self.image_logo.set_parent(self)
		self.image_logo.set_image('root/images/logo.png')
		self.image_logo.set_horizontal_align(wndmgr.HORIZONTAL_ALIGN_CENTER)
		self.image_logo.set_pos(0, 113)

		self.image_bottom_bar = ui.Image()
		self.image_bottom_bar.set_parent(self)
		self.image_bottom_bar.set_image('root/images/bottom_bar.png')
		self.image_bottom_bar.set_vertical_align(wndmgr.VERTICAL_ALIGN_BOTTOM)

		self.editline_username = ui.EditLine()
		self.editline_username.set_parent(self)
		self.editline_username.set_image('root/images/input.png')
		self.editline_username.set_pos(0, 440)
		self.editline_username.set_horizontal_align(wndmgr.HORIZONTAL_ALIGN_CENTER)
		self.editline_username.set_text('Myth')

		self.editline_password = ui.EditLine()
		self.editline_password.set_parent(self)
		self.editline_password.set_image('root/images/input.png')
		self.editline_password.set_pos(0, 537.5)
		self.editline_password.set_horizontal_align(wndmgr.HORIZONTAL_ALIGN_CENTER)
		self.editline_password.set_text('1234')

		self.button_test = ui.Button()
		self.button_test.set_parent(self)
		self.button_test.set_horizontal_align(wndmgr.HORIZONTAL_ALIGN_CENTER)
		self.button_test.set_pos(0, 764)
		self.button_test.set_size(268, 75)
		self.button_test.add_callback("on_button_click", self.on_click)
		self.on_click(self.button_test)

	def on_open(self):
		self.show()

	def on_close(self):
		self.hide()

	def RequestServerStateChecker(self):
		ServerStateChecker.Initialize()
		for i in settings.SERVER_SETTINGS["channel_info"]:
			ServerStateChecker.AddChannel(
				i,
				settings.SERVER_SETTINGS["server_ip"],
				settings.SERVER_SETTINGS["channel_info"][i]
			)
		ServerStateChecker.Request()

	def on_click(self, caller):
		_engine = dbMgr.GetEngine()
		_phase_manager = dbMgr.GetPhaseManager()
		with database.SessionManager(_engine) as session:
			account = session.query(database.schema.Account).filter_by(name=self.editline_username.get_input()).first()
			if account is None:
				logger.info("Account does not exist")
				return
			if account.hash != self.editline_password.get_input():
				logger.info("Wrong password")
				return
			logger.info("Login successful")
			app.SetGuildMarkPath("10.tga")
			app.SetGuildSymbolPath("10")
			_phase_manager.SetSelectCharacterPhase()
# 
# 
# 
# 
# snd.SetSoundVolume(systemsetting.GetSoundVolume())
#
#		ServerStateChecker.Create(self)
#		ServerStateChecker.Update()
#
#		channel_id = 1
#
#		server_ip = settings.SERVER_SETTINGS["server_ip"]
#		channel_info = settings.SERVER_SETTINGS["channel_info"][channel_id]
#		auth_info = random.choice(settings.SERVER_SETTINGS["auth_info"])
#
#		net.SetMarkServer(
#			settings.SERVER_SETTINGS["server_ip"],
#			settings.SERVER_SETTINGS["channel_info"][channel_id],
#		)
#		net.SetServerInfo(
#			"{} - Channel {}".format(
#			settings.SERVER_SETTINGS["server_name"],
#			str(channel_id))
#		)
#		app.SetGuildMarkPath("10.tga")
#		app.SetGuildSymbolPath("10")
#
#		if app.ENABLE_CHANNEL_CHANGER:
#			net.ClearServerInfo()
#			channelMax = len(settings.SERVER_SETTINGS["channel_info"])
#			for i in range(1, channelMax+1):
#				_channelName = "Channel%d" % i
#				net.SetChannelName(i, _channelName.strip())
#				
#			net.SetChannelName(99, "localeinfo.MOVE_CHANNEL_99_REAL")
#			
#			net.SetChannelName(channel_id)
#			net.SetServerName(settings.SERVER_SETTINGS["server_name"])
#
#
#		net.SetPacketSequenceMode()
#
#		char_slot = 0
#
#		id = self.editline_username.get_input()
#		pwd = self.editline_password.get_input()
#		net.SetLoginInfo(id, pwd)
#
#		net.ConnectToAccountServer(server_ip, channel_info, server_ip, auth_info)
#
#		logger.error(f'Username {self.editline_username.get_input()} Password {self.editline_password.get_input()}')

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")
		#dbg.LogBox("Handshake")

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		dbg.LogBox("fail")
		#net.Disconnect()

	def OnLoginFailure(self, error):
		snd.PlaySound("sound/ui/loginfail.wav")

		dbg.LogBox(error)

		#net.Disconnect()

	def on_process(self, caller):
		pass
