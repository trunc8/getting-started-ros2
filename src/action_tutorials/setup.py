from setuptools import setup

package_name = 'action_tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Siddharth Saha',
    maintainer_email='sahasiddharth611@outlook.com',
    description='Python action tutorial code',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [        
            'fibonacci_action_server = action_tutorials.fibonacci_action_server:main',
            'fibonacci_action_client = action_tutorials.fibonacci_action_client:main',
        ],
    },
)
