import argparse
import os
import sys
from macaddress_lookup.macaddresslookup import LookupMacAddress as LMA


def parse_args():
    """
    Parse CLI
    """
    parser = argparse.ArgumentParser(description="create vip")
    parser.add_argument('-a', '--macaddress',
                        type=str,
                        required=True,
                        help="Mac Address such as aa:bb:c3:dd:e5:f6")
    parser.add_argument('--api-key',
                        type=str,
                        nargs='?',
                        help="API Key in https://macaddress.io. If this param "
                             "is NOT passed, it will lookup environment "
                             "variable MAL_APIKEY")
    return parser.parse_args()


def main():
    """ Main function """
    args = parse_args()
    if args.api_key:
        controller = LMA(args.api_key)
    elif os.environ['MAL_APIKEY']:
        controller = LMA(os.environ['MAL_APIKEY'])
    else:
        print "API Key in https://macaddress.io is required. Aborting!"
        sys.exit(1)
    # Lookup vendor information of a given mac address
    controller.lookup_vendor(args.macaddress)


if __name__ == "__main__":
    main()
