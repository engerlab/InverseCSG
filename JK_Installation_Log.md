# Installation log for installing InverseCSG

# System parameters
- Ubuntu 24.04.2 LTS
- python 3.11.6

## Attempt #1
- `mkdir build`
- `python3 install.py -d ./build/`

Got a bunch of errors compiling sketch:

`core/Solver.cpp:2140:54: error: ‘chrono’ has not been declared
 2140 |     auto elapsed_since_start = chrono::duration_cast<chrono::microseconds>(at_time - prev_time).count();`

## Attempt #2
- Fixed compile errors for sketch-frontend by adding in proper includes (chrono, limits, etc.)
- Finally got it to compile with a slight modification of the install.py script

## Attempt #3
- Then had some issues with java maven for the frontend. 
- In `/build/sketch/sketch-frontend/pom.xml` I had to update

```<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>2.0.2</version>
    <configuration>
        <source>7</source>
        <target>7</target>
    </configuration>
</plugin>
``` 
to
```
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.1</version>  <!-- Updated version -->
    <configuration>
        <source>1.8</source>  <!-- Updated to Java 8 -->
        <target>1.8</target>
    </configuration>
</plugin>
```
(thanks ChatGPT!)

## Attempt #4

- Now that that's compiled, I need to make sure the `csg_cpp_command` executable compiles. 
- I found an `if False` in install.py that I removed.
- It doesn't compile due to missing Eigen, also had to uncomment out `InstallEigen()` function call in `install.py`
- I also had to go manually into `/InverseCSG/cpp/lib/eigen-3.3.4/`, make a `build` folder, then run 
```
cmake ..
sudo make install
```
since I don't think eigen is ever compiled by install.py
- Now issues in line `#include "CGAL/Shape_detection_3.h"`

## Attempt #5
- I had previously installed CGAL using apt-get, had to make sure to uninstall that and instead go with the source version
- Compilation now worked! Awesome!
