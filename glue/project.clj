(defproject glue "0.4.1"
  :description "Clojure library to interoperate between Clojure-Java-Python"
  :dependencies [[org.clojure/clojure "1.4.0"]
                 [org.python/jython-standalone "2.5.3"]]

  :profiles {:dev {:dependencies [[midje "1.4.0"]]}}
  :plugins [[lein-midje "2.0.0"]]

  :source-paths      ["src/clj"]
  :java-source-paths ["src/java"]

  :main cljpy.example


)
