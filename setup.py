# SuperPrinter | SuperPrinter is pretty much like print(), but with superpowers
# Copyright (C) 2022 Oscar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import find_packages, setup

setup(
    name="SuperPrinter",
    packages=find_packages(include=["superPrinter"]),
    # The version should be the same as __version__ in globals
    version="0.3",
    description="SuperPrinter is pretty much like print(), but with superpowers",
    author="ItsTheGuy",
)
