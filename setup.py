from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10 ',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
    ]

setup(
    name='MLTSA',
    version='0.0.7',
    description='Machine Learning Transition State Analysis',
    long_description='',
    url='',
    author='Pedro Buigues',
    author_email='pedrojuanbj@gmail.com',
    license="MIT",
    classifiers=classifiers,
    keywords="MLTSA",
    packages=find_packages(),
    install_requires=["numpy", "scipy", "matplotlib", "tqdm", "scikit-learn", "tensorflow"]
)
