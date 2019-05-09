from distutils.core import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='cf-vcap-vars',
  version='0.0.1',
  packages=[''],
  url="https://github.com/jerseyshawn/cf-vcap-vars",
  license='MIT',
  author='shawn mulford',
  author_email='shawn.mulford@philips.com',
  description='Wrapper to simplify reading cf runtime environmental variables.',
  long_description=long_description,
  long_description_content_type="text/markdown"
)
