from setuptools import setup

setup(
    name='ecg_denoiser_laurenz'
    ,version='1.0.0'
    ,description='Thesis code'
    ,author='Laurenz Tolentino'
    ,author_email='laurenz@outlook.ph'
    ,packages=['src/ecg_denoiser_laurenz']
    ,install_requires=['numpy', 'torch', 'matplotlib', 'sys', 'cython']
)