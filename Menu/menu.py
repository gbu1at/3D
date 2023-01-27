from ROOT import FILE
from ROOT.FILE import *
from Menu.Map_menu import *
from Buttons.ButtonNewPolygon import *
from Game.POLYGON.CreateNewPolygon import *
from ROOT.setting_commands import *
from Menu.Instruction import *


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH_FOCUS, HEIGHT_FOCUS))
        self.maps = []
        self.create_maps()
        self.dy = 0
        self.speed_wheel = 30

        self.button_new_polygon = ButtonNewPolygon()
        self.button_instruction = ButtonInstruction(root_pos=(900, 200), text="инструкция", ID_PROCESS=0,
                                                    color_text=GREY)

        self.map_number = None

    def create_maps(self):
        self.dy = 0
        self.x_column_1 = 100
        self.x_column_2 = 500
        self.y_distance = 370
        self.y_coord = 30
        self.maps = []
        for number, polygon in enumerate(FILE.polygons):
            if number % 2 == 0:
                self.maps.append(MapMenu((self.x_column_1, self.y_coord), polygon))
            else:
                self.maps.append(MapMenu((self.x_column_2, self.y_coord), polygon))
                self.y_coord += self.y_distance

    def add_maps(self, new_polygon):
        size = len(self.maps)
        FILE.polygons.append(Polygon(new_polygon))
        if size % 2 == 0:
            self.maps.append(MapMenu((self.x_column_1, self.y_coord), Polygon(new_polygon)))
        else:
            self.maps.append(MapMenu((self.x_column_2, self.y_coord), Polygon(new_polygon)))
            self.y_coord += self.y_distance

    def start(self):
        map_selection = True
        self.map_number = None
        while map_selection:
            self.screen.fill(BLACK)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    return ID_EXIT
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button == 1:
                        self.map_number = self.click_on_map()

                        if self.map_number is not None:
                            map_selection = False

                        if self.button_new_polygon.click():
                            new_polygon = CreateNewPolygon(self.screen).start()
                            self.add_maps(new_polygon)
                        if self.button_instruction.is_click():
                            Instruction()(self.screen)
                if ev.type == pygame.MOUSEWHEEL:
                    if (self.dy + ev.y > -((len(self.maps) + 1) // 2 - 2) * 13) and (self.dy + ev.y < 1):
                        self.dy += ev.y

                self.click_keyboard()

            self.focusing_widgets(pygame.mouse.get_pos())

            self.draw()

            pygame.display.update()
        return polygons[self.map_number].polygon

    def draw(self):
        self.draw_maps(self.screen)
        self.button_new_polygon.draw(self.screen)
        self.button_instruction.draw(self.screen)

    def draw_maps(self, screen):
        for map in self.maps:
            map.draw(screen=screen, dy=self.dy * self.speed_wheel)

    def save(self):
        for map in self.maps:
            map.save()

    def focusing_widgets(self, mouse_pos):
        x, y = mouse_pos

        self.button_new_polygon.is_focus(mouse_pos)
        self.button_instruction.is_focus(mouse_pos)

        y -= self.dy * self.speed_wheel
        for map in self.maps:
            map.is_focus((x, y))

    def click_on_map(self):
        for n, map in enumerate(self.maps):
            if map.FOCUS:
                return n
        return None

    def click_keyboard(self):
        if pygame.key.get_pressed()[pygame.K_DELETE]:
            for map in self.maps:
                if map.FOCUS and not map.polygon.is_permanent:
                    self.maps.remove(map)
                    FILE.polygons.remove(map.polygon)
                    self.create_maps()
                    break
