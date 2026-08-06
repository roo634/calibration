from Style import Style

from gstpipeline import GstPipeline

from renderer import Renderer


def main():

    style = Style()

    pipeline = GstPipeline(style)
    renderer = Renderer()

    pipeline.start()

    running = True

    while running:
        try:

            frame = pipeline.get_frame()

            if frame is None:
                continue

            frame = renderer.process(frame)

            pipeline.push_frame(frame)


        except KeyboardInterrupt:
            running = False


    pipeline.stop()



if __name__ == "__main__":
    main()

