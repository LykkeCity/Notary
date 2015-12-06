(defproject glue "0.4.1"
  :description "Clojure library to interoperate between Clojure-Java-Python"
  :dependencies [[org.clojure/clojure "1.4.0"]
                 [org.python/jython-standalone "2.5.3"]]

  :profiles {:dev
            {:dependencies [
              [midje "1.4.0"]
              [org.bitcoinj/bitcoinj-core "0.13.3"]
              [buddy/buddy-core "0.7.0"]
              ]}}
  :plugins [[lein-midje "2.0.0"]]

  :source-paths      ["src/clj"]
  :java-source-paths ["src/java"]

  :main glue.example


)
