import org.python.core.*;
import org.python.util.PythonInterpreter;

public class Runer {

    public static void runsimple(){
        PythonInterpreter interp = new PythonInterpreter();

        System.out.println("Hello, brave new world");
        interp.exec("import sys");
        interp.exec("print sys");

        interp.set("a", new PyInteger(42));
        interp.exec("print a");
        interp.exec("x = 2+2");
        PyObject x = interp.get("x");

        System.out.println("x: " + x);

        interp.exec("from pymodule import square");
        interp.set("integer", new PyInteger(42));
        interp.exec("result = square(integer)");
        interp.exec("print(result)");
        PyInteger result = (PyInteger)interp.get("result");
    }

    public static void runClient(){
        PythonInterpreter interp = new PythonInterpreter();

        interp.exec("from client import *");

    }

    public static void main(String[] args) throws PyException {
        runClient();

        //System.out.println(“result: “+ result.asInt());
        //PyFunction pf = (PyFunction)pi.get(“square”);
        //System.out.println(pf.__call__(new PyInteger(5)));
    }


}
