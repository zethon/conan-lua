# lua conan recipe 
# as used by https://github.com/zethon/Owl

from conans import ConanFile, CMake, tools

class LuadistConan(ConanFile):
    name = "luadist"
    version = "5.2.3"
    url = "https://github.com/LuaDist/lua"
    license = "GPL"
    description = "Lua is a powerful, efficient, lightweight, embeddable scripting language. It supports procedural programming, object-oriented programming, functional programming, data-driven programming, and data description."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="source")
        git.clone("https://github.com/LuaDist/lua.git", "master")
        git.checkout("96245accd1539c8bb0d8be310eaa9cf5fbab9fed")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="source")
        cmake.build()

    def package(self):
        for h in ["lauxlib.h", "lua.h", "lua.hpp", "lualib.h"]:
            self.copy(h, dst="include/lua", src="source/src")
        self.copy("luaconf.h", dst="include/lua", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lua"]

