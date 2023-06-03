main.o: main.c
	cc -c -I%JAVA_HOME%\include -I%JAVA_HOME%\include\win32 main.c -o main.o

HelloWorldNative.dll: main.o
	ld -shared -o HelloWorldNative.dll main.o --add-stdcall-alias

