#!/usr/bin/env python

from includes.vars import CloudFoundry

def main():
  cloud_foundry = CloudFoundry()
  print('*******************')
  cloud_foundry.get_cf_variables()
  print('*******************')

if __name__ == '__main__':
  main()
