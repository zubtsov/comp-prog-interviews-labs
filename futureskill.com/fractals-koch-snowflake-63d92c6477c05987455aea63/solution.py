class Solution:
    def __init__(self, api):
        self.api = api

    def level_1_calculate_p2(self, x0, y0, x1, y1):
        x_diff = x1 - x0
        y_diff = y1 - y0
        x2 = x0 + x_diff / 3
        y2 = y0 + y_diff / 3
        return [x2, y2]

    def level_2_calculate_p4(self, x0, y0, x1, y1):
        x_diff = x1 - x0
        y_diff = y1 - y0
        x2 = x0 + x_diff * 2 / 3
        y2 = y0 + y_diff * 2 / 3
        return [x2, y2]

    def level_3_calculate_p3(self, x0, y0, x1, y1):
        import math

        x2, y2 = self.level_1_calculate_p2(x0, y0, x1, y1)
        x4, y4 = self.level_2_calculate_p4(x0, y0, x1, y1)

        xdiff = x4 - x2
        ydiff = y4 - y2
        length = math.sqrt(math.pow(xdiff, 2) + math.pow(ydiff, 2))

        p2p4_to_x_angle = math.atan2(ydiff, xdiff)
        p2p3_to_y_angle = math.pi / 6 - p2p4_to_x_angle

        return [x2 + math.sin(p2p3_to_y_angle) * length, y2 + math.cos(p2p3_to_y_angle) * length]
