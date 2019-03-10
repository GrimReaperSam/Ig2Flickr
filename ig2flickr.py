import json
from dateutil.parser import parse
import argparse
import flickrapi


parser = argparse.ArgumentParser('Ig2Flickr')
parser.add_argument('api_key', type=str, help='API key obtained from Flickr')
parser.add_argument('api_secret', type=str, help='API secret obtained from Flickr')
parser.add_argument('ig_folder', type=str, help='Path where the Instagram data folder resides')
parser.add_argument('--geocode', default=False, action='store_true', help='Whether to add location info for the photos')
parser.add_argument('--verbose', default=False, action='store_true', help='Print out details about uploaded photos')

opt = parser.parse_args()
ig_folder = opt.ig_folder
if opt.geocode:
    import geocoder

api_key = opt.api_key
api_secret = opt.api_secret
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='xmlnode')
flickr.authenticate_via_browser(perms='delete')

with open('%s/media.json' % ig_folder) as f:
    data = json.load(f)

posts = data['photos']
for p in posts:
    title = p['location']
    description = p['caption']
    path = p['path']
    taken = p['taken_at']
    date_taken = parse(taken).strftime('%Y-%m-%d')

    z = flickr.upload('%s/%s' % (ig_folder, p['path']), title=p['location'], description=p['caption'])
    photoid = z.photoid[0].text
    flickr.photos.setDates(photo_id=photoid, date_taken=date_taken)

    if opt.geocode:
        g = geocoder.osm(title)
        lat, lon = g.latlng
        flickr.photos.geo.setLocation(photo_id=photoid, lat=lat, lon=lon)

    if opt.verbose:
        print(title, description, path, taken)
