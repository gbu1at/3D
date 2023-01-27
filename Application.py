from Game.game import *
from Menu.menu import *
from ROOT import setting, setting_commands


class Application:
    def __init__(self):
        self.menu = Menu()

    def start(self, polygon=None):
        try:
            if polygon is None:
                polygon = self.show_menu()
            setting.GAME = True
            game = Game(polygon)
            command = game.start()
            if setting.WIN_PLAYER:
                self.menu.maps[self.menu.map_number].map_passed()
                FILE.polygons[self.menu.map_number].is_passed = True
            if command == setting_commands.ID_SHOW_MENU:
                self.start()
            elif command == setting_commands.ID_RESTART:
                self.start(polygon)
            elif command == setting_commands.ID_EXIT:
                self.menu.save()
                exit()
        except KeyboardInterrupt:
            self.menu.save()
            exit()

    def show_menu(self):
        polygon = self.menu.start()
        if polygon == ID_EXIT:
            self.menu.save()
            exit()
        return polygon
