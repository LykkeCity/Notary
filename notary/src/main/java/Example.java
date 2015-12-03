

import org.python.core.PyInstance;
import org.python.util.PythonInterpreter;


public class Example {

    PythonInterpreter interpreter = null;


    public Example() {
        PythonInterpreter.initialize(System.getProperties(),
                System.getProperties(), new String[0]);

        this.interpreter = new PythonInterpreter();
    }

    void execfile(final String fileName) {
        this.interpreter.execfile(fileName);
    }

    PyInstance createClass(final String className, final String opts) {
        return (PyInstance) this.interpreter.eval(className + "(" + opts + ")");
    }

    public static void main(String gargs[]) {
        Example ie = new Example();

        //ie.execfile("hello.py");
        ie.execfile("client.py");

        //PyInstance hello = ie.createClass("Hello", "None");

        //hello.invoke("run");
    }
}