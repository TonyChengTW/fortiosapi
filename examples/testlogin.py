#!/root/fortinet/bin/python
import logging
import pprint

from fortiosapi import FortiOSAPI

formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger('fortiosapi')
hdlr = logging.FileHandler('testfortiosapi.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

fgt = FortiOSAPI()


def main():
    # Login to the FGT ip
    fgt.debug('on')
    fgthost = '172.16.100.253:10443'
    user = 'tony1'
    passwd = '1qaz@WSX'
    vdom = 'root'
    resp = fgt.login(fgthost, user, passwd, vdom)
    pp = pprint.PrettyPrinter(indent=4)
    resp = fgt.license()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(resp)

if __name__ == '__main__':
    main()
