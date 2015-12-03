(ns cljpy.t-core
  (:require [midje.sweet :refer :all]
            [cljpy.core :as base])
  (:import Testing))

(def srcpy ["src/py/"])

(fact "append-paths adds the path to system path"
      (binding [base/*interp* (org.python.util.PythonInterpreter.)]
        (-> (#'base/append-paths srcpy)
            .getLocals
            (.__getitem__ "sys")
            .path
            set
            (get "src/py/")))
      =>
      "src/py/")

(fact "init sets *interp* root binding (but only once)"
      (do
        (base/init {:libpaths srcpy})
        (class base/*interp*))
      =>
      org.python.util.PythonInterpreter

      (do
        (base/init {:libpaths srcpy})
        (class base/*interp*))
      =>
      (do
        (base/init {:libpaths srcpy})
        (class base/*interp*)))


(defmacro with-test-interp [& body]
  `(base/with-interpreter
     {:libpaths srcpy}
     ~@body))

(fact "with-interpreter dynamically binds a new interpreter environment"
      (with-test-interp base/*interp*)
      =not=>
      (with-test-interp base/*interp*))

(fact "importing python modules works"
      (with-test-interp
        (base/py-import-lib example)
        (class example))
      =>
      org.python.core.PyStringMap)

(fact "importing python functions works"
      (with-test-interp
        (base/py-import-lib example)
        (base/import-fn example hello)
        (fn? hello))
      =>
      true)

(fact "calling python functions works"
      (with-test-interp
        (base/py-import-lib example)
        (base/import-fn example hello)
        (hello "world"))
      =>
      "hello, world how are you."

      (with-test-interp
        (base/py-import-lib example)
        ((base/py-fn example hello)
         "person"))
      =>
      "hello, person how are you.")

(fact "calling java works"
  (Testing/vier) => 4)
