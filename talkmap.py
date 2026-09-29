# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Set the default timeout, in seconds
TIMEOUT = 5

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description. Online talks can set `map_location` (e.g. the
    # host city) to be pinned there, labelled "(virtual)"; online talks without
    # it are left off the map rather than geocoded to an arbitrary place.
    title = data['title'].strip()
    venue = data['venue'].strip()
    shown = data['location'].strip()
    is_virtual = 'virtual' in shown.lower()
    location = str(data.get('map_location', '')).strip() or shown
    if is_virtual and not data.get('map_location'):
        print(f"Skipping virtual talk without map_location: {title}")
        continue
    label = f"{location} (virtual)" if is_virtual else location
    description = f"{title}<br />{venue}; {label}"

    # Geocode the location and report the status
    try:
        point = geocoder.geocode(location, timeout=TIMEOUT)
        if point is None:
            print(f"Error: no geocode result for {location}")
            continue
        location_dict[description] = point
        print(description, location_dict[description])
    except ValueError as ex:
        print(f"Error: geocode failed on input {location} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {location} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {location} with message {ex}")

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
