

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
        self.draw_circle(frame)
        self.draw_dot(frame)

        return frame
    

    def draw_horizontal(self, frame):

        # Left segment            

        cv2.line(
            frame,
            (0, Style.cam_height//2),
            (Style.centre_x-Style.circle_rad, Style.cam_height//2),
            Style.line_colour,
            Style.line_width
        )
        # Right segment            

        cv2.line(
            frame,
            (Style.centre_x+Style.circle_rad, Style.cam_height//2),
            (Style.cam_width, Style.cam_height//2),
            Style.line_colour,
            Style.line_width
        )

    def draw_vertical(self,frame):
            
        # Top segment

        cv2.line(
            frame,
            (Style.cam_width//2, 0),
            (Style.cam_width//2, Style.centre_y-Style.circle_rad),
            Style.line_colour,
            Style.line_width
        )

        # Bottom segment

        cv2.line(
            frame,
            (Style.cam_width//2, Style.centre_y+Style.circle_rad),
            (Style.cam_width//2, Style.cam_height),
            Style.line_colour,
            Style.line_width
        )        

    def draw_circle(self,frame):

        cv2.circle(
            frame,
            (Style.cam_width//2, Style.cam_height//2),
            Style.circle_rad,
            Style.line_colour,
            Style.line_width
        )


    def draw_dot(self,frame):

        cv2.circle(
            frame,
            (Style.cam_width//2, Style.cam_height//2),
            Style.dot_rad,
            Style.line_colour,
            -1
        )

