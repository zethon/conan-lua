# conan-luadist

[Conan](https://bintray.com/zethon/owl/luadist%3Aowl) package for the [Lua CMake distribution](https://github.com/LuaDist/lua).

This is the Lua recipe used in my open source project [Owl](https://github.com/zethon/owl). 

## Usage

Add `luadist/x.y.z@owl/stable` in the list of requirements of your conanfile, where `x.y.z` is the desired version. See [how to use a conanfile.py](http://docs.conan.io/en/latest/mastering/conanfile_py.html) for more information.

## Packaging

See [Conan-Package-Tools](https://github.com/conan-io/conan-package-tools) Github page for more information on packaging.

<!--
conan install .
conan source .
conan build .
conan package . -sf=source -pf=package
conan export-pkg . luadist/5.2.3@owl/stable
conan upload luadist/5.2.3@owl/stable -r owl
-->