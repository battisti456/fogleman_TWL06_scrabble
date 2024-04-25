import setuptools
def setup(name = "fogleman-TWL06-scrabble",
          version='revision-4',
          description="A convenient, self-contained, 515 KB Scrabble dictionary module, ideal for use in word games.",
          url = 'https://github.com/fogleman/TWL06',
          author = 'Michael Fogleman',
          author_email = "",
          license = 'MIT',
          classifiers = [
              'Development Status :: 5 - As Is',
              'Intended Audience :: Developers',
              'Topic :: Software Development :: Build Tools',
              'Programming Language :: Python :: 3',
              'Private :: Do Not Upload'
          ],
          keywords = "",
          project_urls = {},
          packages = setuptools.find_packages(include=['base64','itertools','struct','zlib']),
          pymodules = [],
          install_requires = [],
          python_requires=">=3",
          package_data = {},
          data_files = [],
          entry_points = {},
          ):
    pass
def main():
    setuptools.setup(name = "fogleman-TWL06-scrabble",
          description="A convenient, self-contained, 515 KB Scrabble dictionary module, ideal for use in word games.",
          version = "1.0.0",
          url = 'https://github.com/fogleman/TWL06',
          author = 'Michael Fogleman',
          author_email = "",
          license = 'MIT')
if __name__ == "__main__":
    main()