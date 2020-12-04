"""Calls the datas form the config file if it is called in the CLI"""
import configparser

parser = configparser.ConfigParser()
parser.read('imagefilter.ini')
input = parser.get('general', 'input_dir')
output = parser.get('general', 'output_dir')
logfile = parser.get('general', 'log_file')
filters = parser.get('filter', 'content')
