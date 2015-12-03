(ns cljpy.example
  (:require [midje.sweet :refer :all]
            [cljpy.core :as base])
  (:import Testing))

(defmacro with-test-interp [& body]
  `(base/with-interpreter
     {:libpaths ["src/py/"]}
     ~@body))

(defn demo-interop
  "demontsrate interop"
  []
  (println "main")
  (with-test-interp
    (base/py-import-lib example)
    (base/import-fn example hello)
    (base/import-fn example calc)
    (println (hello "world"))
    (println (calc 2)))
  (Testing/ja)
  (println "main end"))

(defn -main []
  (demo-interop))
