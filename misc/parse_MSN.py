from dateutil.parser import parse
import os
import pytz
import xml.etree.ElementTree as ET

tw_tz = pytz.timezone('Asia/Taipei')

input_folder = '/Users/joannewolf/Desktop/gerji/MSN'
output_folder = '/Users/joannewolf/Desktop/MSN'

def parse_MSN(filename):
    output_filename = os.path.join(output_folder, filename)

    tree = ET.parse(os.path.join(input_folder, filename))
    root = tree.getroot()

    with open(output_filename, 'w') as f_out:
        for message in root:
            if message.tag == 'Message':
                datetime = parse(message.attrib['DateTime']).astimezone(tw_tz)
                datetime_str = datetime.strftime('%Y-%m-%d %H:%M:%S')
                from_name = message[0][0].attrib['FriendlyName']
                to_name = message[1][0].attrib['FriendlyName']
                text = message[2].text.replace('\n', ' ')
                f_out.write(f'{datetime_str} | {from_name} -> {to_name} : {text}\n')
            else:
                datetime = parse(message.attrib['DateTime']).astimezone(tw_tz)
                datetime_str = datetime.strftime('%Y-%m-%d %H:%M:%S')
                from_name = message[0][0].attrib['FriendlyName']
                text = message[2].text.replace('\n', ' ')
                f_out.write(f'{datetime_str} | {from_name} : {text}\n')

for filename in os.listdir(input_folder):
    if filename.endswith('.xml'):
        parse_MSN(filename)
