#!/usr/bin/env python3

from os import environ
from json import dumps

class CloudFoundry:
  def __init__(self, **kwargs):
    self.__CF_VARIABLES__ = {'CF_INSTANCE_ADDR': '',
                             'CF_INSTANCE_GUID': '',
                             'CF_INSTANCE_INDEX': '',
                             'CF_INSTANCE_INTERNAL_IP': '',
                             'CF_INSTANCE_IP': '',
                             'CF_INSTANCE_PORT': '',
                             'CF_INSTANCE_PORTS': [{}],
                             'CF_STACK': '',
                             'DATABASE_URL': '',
                             'HOME': '',
                             'INSTANCE_GUID': '',
                             'INSTANCE_INDEX': '',
                             'LANG': '',
                             'MEMORY_LIMIT': '',
                             'PATH': '',
                             'PORT': '',
                             'PWD': '',
                             'TMPDIR': '',
                             'USER': '',
                             'VCAP_APP_HOST': '',
                             'VCAP_APP_PORT': '',
                             'VCAP_APPLICATION': {},
                             'VCAP_SERVICES': {}}

    if kwargs.get('testing'):
      self.load_testing_data(**kwargs)
    else:
      self.set_cf_variables(**kwargs)


  def load_testing_data(self, **kwargs):
    pass

  def set_cf_variables(self, **kwargs):
    variables = kwargs.get('variables', None)
    if isinstance(variables, str):
      cf_variables = [variable.upper() for variable in variables.split(',')]
    elif isinstance(variables, list):
      cf_variables = [variable.upper() for variable in variables]
    else:
      cf_variables = self.__CF_VARIABLES__
    for cf_variable in cf_variables:
      # found in env
      if cf_variable in environ:
        setattr(self,str(cf_variable).lower(),environ[cf_variable])
      # not in env, but a known cf var
      elif cf_variable in self.__CF_VARIABLES__:
        setattr(self, str(cf_variable).lower(), self.__CF_VARIABLES__[cf_variable])
      # not in env and not defaulted
      else:
        setattr(self, str(cf_variable).lower(), '')
  def get_cf_variables(self, **kwargs):
    variables = {}
    for variable in sorted(self.__CF_VARIABLES__):
      variable = variable.lower()
      if hasattr(self, variable):
        variables[variable] = getattr(self,variable)
    print(dumps(variables, indent=4))
    return(variables)



