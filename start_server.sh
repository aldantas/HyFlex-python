path_to_py4j=<path to py4j jar file>
classpath="hyflex/*:$path_to_py4j"

mkdir -p "class"
javac -cp $classpath *.java -d "class"
java -cp "$classpath:class" HyFlexServer
