from conans import ConanFile, CMake, tools


class Gainput(ConanFile):
    name = "gainput"
    version = "0.1"
    license = "GPL3"
    author = "Johannes Kuhlmann"
    url = "https://github.com/jkuhlmann/gainput"
    description = "Cross-platform C++ input library"
    topics = ("input", "keyboard", "mouse", "touch", "cross-platform" )
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def source(self):
        self.run("git clone https://github.com/jkuhlmann/gainput .")
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("*.h", src="lib/include", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gainput", "gainputstatic"]
