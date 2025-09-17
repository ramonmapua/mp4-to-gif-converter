# MP4 to GIF Converter (Python + FFmpeg)

This is a simple Python script that converts `.mp4` video files into `.gif` images using [FFmpeg](https://ffmpeg.org/).
You can specify the file name and the frames per second (FPS) for the output GIF. The script also shows the final GIF size in MB.

## Features

* Convert any `.mp4` file to `.gif`
* User specifies:

  * File name (must exist in the `input/` folder)
  * FPS (controls smoothness vs file size)
* Displays the GIF’s size in megabytes
* Logs errors and activity to `mp4-to-gif-converter.log`

## Project Structure

```
mp4-to-gif-converter/
│── input/              # Place your MP4 files here
│── output/             # Converted GIFs will be saved here
│── mp4_to_gif.py       # Main Python script
│── mp4-to-gif-converter.log
│── README.md
```

## Requirements

* [Python 3.8+](https://www.python.org/)
* [FFmpeg](https://ffmpeg.org/download.html) installed and added to your PATH
* Python dependencies:

  ```bash
  pip install ffmpeg-python
  ```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mp4-to-gif-converter.git
   cd mp4-to-gif-converter
   ```

2. Place your `.mp4` file inside the `input/` folder.

3. Run the script:

   ```bash
   python mp4_to_gif.py
   ```

4. Enter the required information:

   ```
   Enter the MP4 file name (with extension): example.mp4
   Enter the desired FPS: 20
   ```

5. Your converted GIF will be saved in the `output/` folder:

   ```
   Conversion complete: output/example.gif (2.34 MB)
   ```

---

## Example

If you have `cat.mp4` in the `input/` folder and want a 15 FPS GIF:

```
Enter the MP4 file name (with extension): cat.mp4
Enter the desired FPS: 15
```

Output:

```
Conversion complete: output/cat.gif (3.21 MB)
```

---

## Troubleshooting

* Error: `[WinError 2] The system cannot find the file specified`
  * FFmpeg is not installed or not added to your PATH.
  Install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and make sure `ffmpeg -version` works in your terminal.

* GIF too large
  → Lower the FPS or resize the video before converting.
