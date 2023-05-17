import pygame as pg
import numpy as np


FPS = 144
GRAVITY = 98 * 5
COLOR_STROKE = (255, 255, 255)
COLOR_BALL = (102, 12, 176)
BACKGROUND_COLOR = (20, 20, 20)


class Pendulum:
    def __init__(self, cable_origin: pg.Vector2, cable_lenght: int, angle: int, radius: int = 20):
        self.angle = np.deg2rad(angle)
        self.cable_lenght = cable_lenght
        self.cable_origin = cable_origin
        self.ball_radius = radius

        self.ang_acc = 0
        self.ang_vel = 0


    def update(self, dt):
        self.ang_acc = -GRAVITY * np.sin(self.angle) / self.cable_lenght
        self.ang_vel += self.ang_acc * dt
        self.angle += self.ang_vel * dt



    def show(self, screen: pg.Surface):
        x = self.cable_lenght * np.sin(self.angle)
        y = self.cable_lenght * np.cos(self.angle)
        ball_pos = pg.Vector2(x, y) + self.cable_origin

        pg.draw.line(screen, COLOR_STROKE, self.cable_origin, ball_pos, 2)
        pg.draw.circle(screen, COLOR_BALL, ball_pos, self.ball_radius)






def main():
    pg.init()
    screen = pg.display.set_mode((1000, 600))
    clock = pg.time.Clock()
    
    pend = Pendulum(
        cable_origin=pg.Vector2(500, 50),
        cable_lenght=300,
        angle=60,
    )
    pend2 = Pendulum(
        cable_origin=pg.Vector2(500, 50),
        cable_lenght=150,
        angle=60,
    )
    pend3 = Pendulum(
        cable_origin=pg.Vector2(500, 50),
        cable_lenght=100,
        angle=60,
    )
    pend4 = Pendulum(
        cable_origin=pg.Vector2(500, 50),
        cable_lenght=150,
        angle=0,
    )
    pendulums = [pend, pend2, pend3, pend4]


    # main loop
    running = True
    while running:
        clock.tick(FPS)
        dt = clock.get_time() / 1000  # millisec to sec

        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                return pg.quit()

        screen.fill(BACKGROUND_COLOR)
        
        for pend in pendulums:
            pend.update(dt) 
            pend.show(screen)
     

        pg.display.set_caption(f"fps: {round(clock.get_fps(), 2)}")
        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()
