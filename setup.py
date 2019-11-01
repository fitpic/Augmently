from distutils.core import setup
setup(
  name = 'Augmently',         # How you named your package folder (MyLib)
  packages = ['Augmently'],   # Chose the same as "name"
  version = '1.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library for Data Augmentation of images in computer vision.',   # Give a short description about your library
  author = 'Nicolas Carmont',                   # Type in your name
  author_email = 'nickcarmont8@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/fitpic/Augmently',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/fitpic/Augmently/archive/1.0.3.tar.gz',    # I explain this later on
  keywords = ['image', 'augmentation', 'machine learning', 'CNN', 'data augmentation','deep learning','data processing'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'opencv-python',
          'Pillow',
          'stat'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
