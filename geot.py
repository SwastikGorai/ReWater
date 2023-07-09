from PIL import Image
from PIL.ExifTags import TAGS

def get_geotag(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Extract the EXIF data
        exif_data = image._getexif()

        # Check if the image has EXIF data
        if exif_data is not None:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag)
                if tag_name == 'GPSInfo':
                    # Return the geotag information
                    
                    
                    return str(f'{int(value[2][0])}°{int(value[2][1])}\'{value[2][2]}\"{value[1]} {int(value[4][0])}°{int(value[4][1])}\'{value[4][2]}\"{value[3]}')

    except (IOError, AttributeError, KeyError, IndexError):
        pass

    # If no geotag information found, return None
    return None

# # Example usage
# image_path = '/content/Predict/DJI_0080.jpg'
# geotag = get_geotag(image_path)

# if geotag is not None:
#     ss =  f'{int(geotag[2][0])}°{int(geotag[2][1])}\'{geotag[2][2]}\"{geotag[1]} {int(geotag[4][0])}°{int(geotag[4][1])}\'{geotag[4][2]}\"{geotag[3]}'
# else:
#     print("No geotag information found.")
    

