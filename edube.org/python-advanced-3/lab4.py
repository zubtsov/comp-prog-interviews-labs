# https://edube.org/learn/pcpp1-4-gui-programming/lab-traffic-lights

from tkinter import Tk, Button, Canvas


class TrafficLights:
    DISABLED_COLOR = 'gray'

    CANVAS_WIDTH = 200
    CANVAS_HEIGHT = 300

    HEIGHT_MARGIN = 30
    WIDTH_MARGIN = 20

    SPACE_BETWEEN_LIGHTS = 10

    _phases = ((True, False, False),
               (True, True, False),
               (False, False, True),
               (False, True, False))
    _colors = ('red', 'yellow', 'green')

    def __init__(self):
        self._main_window = Tk()
        self._current_phase = 0

        self._canvas = Canvas(self._main_window, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT)
        self._display_current_phase()
        self._canvas.pack()

        self._next_button = Button(self._main_window, text='Next', command=self._switch_to_next_phase)
        self._next_button.pack()
        self._quit_button = Button(self._main_window, text='Quit', command=self._main_window.destroy)
        self._quit_button.pack()

    def run(self):
        self._main_window.mainloop()

    def _switch_to_next_phase(self):
        self._current_phase = (self._current_phase + 1) % len(self._phases)
        self._display_current_phase()

    def _display_current_phase(self):

        number_of_lights = len(self._colors)
        estimated_height = (self.CANVAS_HEIGHT - self.HEIGHT_MARGIN - self.SPACE_BETWEEN_LIGHTS
                            * (number_of_lights - 1)) / number_of_lights
        estimated_width = self.CANVAS_WIDTH - self.WIDTH_MARGIN
        circle_diameter = min(estimated_height, estimated_width)

        x_offset = max((self.CANVAS_WIDTH - circle_diameter) / 2, 0)

        for ind, color, enabled in zip(range(number_of_lights), self._colors, self._phases[self._current_phase]):
            if not enabled:
                color = self.DISABLED_COLOR
            self._canvas.create_oval(x_offset,
                                     self.HEIGHT_MARGIN / 2 + ind * (circle_diameter + self.SPACE_BETWEEN_LIGHTS),
                                     x_offset + circle_diameter,
                                     (ind + 1) * (circle_diameter + self.SPACE_BETWEEN_LIGHTS),
                                     fill=color)


if __name__ == '__main__':
    TrafficLights().run()
