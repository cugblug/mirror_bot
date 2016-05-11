from setuptools import setup, find_packages
import mirror_bot

entry_points = {
    "console_scripts": [
        "mirror_bot = mirror_bot.cli:main",
    ]
}

setup(
    name="mirror_bot",
    version=mirror_bot.version,
    url="https://xuanwo.org/",
    author="Xuanwo",
    author_email="xuanwo.cn@gmail.com",
    description="Mirror_bot is a tool for control mirror server",
    long_description="Mirror_bot is a tool for control mirror server",
    keywords="bot, mirror, script, docker",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
    install_requires=[
        'docopt',
        'pyyaml',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
