package HelloWorldJava;

public class HelloWorld {

    static {
        System.loadLibrary("HelloWorldNative");
    }

    public static void main(String[] args){
        new HelloWorld().sayHello();
    }

    private native void sayHello();
}