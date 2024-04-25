from PIL import Image

def convert_webp_to_gif(webp_file, gif_file):
  """
  Attempts to convert a WEBP image to a GIF image.

  **Note:** This function cannot directly repair corrupted GIFs.

  Args:
    webp_file: Path to the WEBP image file.
    gif_file: Path to save the converted GIF image file.
  """
  try:
    # Open the WEBP image
    image = Image.open(webp_file)

    # Handle potential transparency issue (same as before)
    if Image.transparency.has_alpha(image):
      image = image.convert('RGBA')

    # Save as GIF
    image.save(gif_file, format='GIF', save_all=True)
    print(f"Converted WEBP image '{webp_file}' to GIF '{gif_file}'.")
  except FileNotFoundError:
    print(f"Error: WEBP file '{webp_file}' not found.")
  except Exception as e:
    print(f"An error occurred during conversion: {e}")
    print("**Warning:** The GIF might be corrupt. Consider using a repair tool.")


if __name__=="__main__":
    
#    input_directory = 'C:/Users/sasyn/Downloads/shitt/25450399.webp'
    input_directory ="C:\\Users\\sasyn\\Documents\\streamlit_test\\200.webp"
    output_gif = 'C:\\Users\\sasyn\\Documents\\streamlit_test\\output.gif'
    duration_per_frame = 100  # in milliseconds

    convert_webp_to_gif(input_directory, output_gif, )
