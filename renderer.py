

from Style import Style

import cv2

import numpy as np



class Renderer:


    def process(
            self,
            frame: np.ndarray,
            ) -> np.ndarray:

        self.draw_horizontal(frame)
        self.draw_vertical(frame)

        return frame
    

    def draw_horizontal(self, frame):

        cv2.line(
            frame,
            (0, Style.cam_height//2),
            (Style.cam_width, Style.cam_height//2),
            Style.line_colour,
            Style.line_width
        )


    def draw_vertical(self,frame):
            
        cv2.line(
            frame,
            (Style.cam_width//2, 0),
            (Style.cam_width//2, Style.cam_height),
            Style.line_colour,
            Style.line_width
        )

