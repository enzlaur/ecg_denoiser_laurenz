from setuptools import setup

setup(
    name='ecg_denoiser_laurenz'
    ,version='1.0.0'
    ,description='Thesis code'
    ,author='Laurenz Tolentino'
    ,author_email='laurenz@outlook.ph'
    ,packages=['src/ecg_denoiser_laurenz', "src/ecg_denoiser_laurenz/ecg_toolkit", "src/ecg_denoiser_laurenz/models"]
    ,install_requires=['numpy', 'torch', 'matplotlib', 'sys', 'cython']
)