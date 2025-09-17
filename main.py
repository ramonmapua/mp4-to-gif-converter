import os
import logging
import ffmpeg
import subprocess

logging.basicConfig(filename="mp4-to-gif-converter.log", encoding="utf-8", level=logging.DEBUG)
logging.debug("start")

scripts = os.path.dirname(os.path.realpath(__file__))
inputs = f"{scripts}/input"
outputs = f"{scripts}/output"

def convert(file_name: str, fps: int, lossy: int):
    input_path = os.path.join(inputs, file_name)
    if not os.path.isfile(input_path):
        print(f"File '{file_name}' not found in {inputs}")
        return

    file_name_final = os.path.splitext(file_name)[0]
    output_path = os.path.join(outputs, f"{file_name_final}.gif")

    try:
        (
            ffmpeg
            .input(input_path)
            .filter("fps", fps=fps, round="up")
            .output(output_path)
            .run(overwrite_output=True, quiet=True)
        )

        if lossy > 0:
            compressed_path = os.path.join(outputs, f"{file_name_final}_compressed.gif")
            subprocess.run(
                ["gifsicle", f"--lossy={lossy}", "-O3", output_path, "-o", compressed_path],
                check=True
            )
            os.replace(compressed_path, output_path)

        size_bytes = os.path.getsize(output_path)
        size_mb = size_bytes / (1024 * 1024)
        print(f"Conversion complete: {output_path} ({size_mb:.2f} MB)")

    except Exception as err:
        logging.debug(err)
        print(f"Error during conversion: {err}")

def main():
    file_name = input("Enter the MP4 file name (with extension): ").strip()
    fps = int(input("Enter the desired FPS: ").strip())
    lossy = int(input("Enter lossy compression level (0 = none, higher = more compression): ").strip())

    convert(file_name, fps, lossy)

if __name__ == "__main__":
    main()