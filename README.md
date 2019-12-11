# conan-lua

conan install .
conan source .
conan build . -bf=build
conan package . -sf=source -bf=build -pf=package
conan export-pkg . luadist/5.2.3@owl/stable
conan upload luadist/5.2.3@owl/stable -r owl