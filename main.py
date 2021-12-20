"""
Main function for training and evaluating MARL algorithms in TSC problems
@author: Janayt
"""
import argparse
import os


def parse_args():
    default_base_dir = '/'
    default_config_dir = './config/config_ql_signel_intersection.ini'
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-dir', type=str, required=False, default=default_base_dir, help="experiment base dir")
    subparsers = parser.add_argument(dest='option', help="train or evaluate")


